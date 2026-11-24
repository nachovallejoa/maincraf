package com.mardenuves.nucleo;

import net.minecraft.nbt.NbtCompound;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.world.PersistentState;
import net.minecraft.world.PersistentStateManager;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;
import java.util.regex.Pattern;

/**
 * Estado persistente único de campaña. Se almacena en el PersistentStateManager
 * del mundo principal para que dimensiones distintas no creen campañas paralelas.
 */
public final class CampaignState extends PersistentState {
    public static final String STORAGE_ID = "mardenuves_campaign";
    public static final int CURRENT_SCHEMA_VERSION = 1;

    private static final String KEY_SCHEMA = "schema_version";
    private static final String KEY_CAMPAIGN_ID = "campaign_id";
    private static final String KEY_STARTED = "started";
    private static final String KEY_LEVEL = "level";
    private static final String KEY_XP = "xp";
    private static final String KEY_ATTRIBUTES = "attribute_points";
    private static final String KEY_SKILLS = "skill_points";
    private static final String KEY_VALUES = "values";
    private static final Pattern SAFE_KEY = Pattern.compile("[a-z0-9_.-]{1,128}");

    private String campaignId;
    private boolean started;
    private int level;
    private long xp;
    private int attributePoints;
    private int skillPoints;
    private final Map<String, String> values;

    private CampaignState() {
        this(UUID.randomUUID().toString(), false, 1, 0L, 0, 0, new LinkedHashMap<>());
        markDirty();
    }

    private CampaignState(
            String campaignId,
            boolean started,
            int level,
            long xp,
            int attributePoints,
            int skillPoints,
            Map<String, String> values
    ) {
        this.campaignId = campaignId;
        this.started = started;
        this.level = clamp(level, 1, 30);
        this.xp = Math.max(0L, xp);
        this.attributePoints = Math.max(0, attributePoints);
        this.skillPoints = Math.max(0, skillPoints);
        this.values = new LinkedHashMap<>(values);
    }

    public static CampaignState get(ServerWorld world) {
        Objects.requireNonNull(world, "world");
        PersistentStateManager manager = world.getPersistentStateManager();
        return manager.getOrCreate(CampaignState::fromNbt, CampaignState::new, STORAGE_ID);
    }

    /**
     * Marca una campaña como iniciada una sola vez y devuelve false si ya lo estaba.
     */
    public boolean beginCampaign() {
        if (started) {
            return false;
        }
        started = true;
        markDirty();
        return true;
    }

    public String getCampaignId() {
        return campaignId;
    }

    public boolean isStarted() {
        return started;
    }

    public int getLevel() {
        return level;
    }

    public long getXp() {
        return xp;
    }

    public int getAttributePoints() {
        return attributePoints;
    }

    public int getSkillPoints() {
        return skillPoints;
    }

    public Map<String, String> getValues() {
        return Collections.unmodifiableMap(values);
    }

    /**
     * Guarda un valor pequeño de estado narrativo mediante una clave estable.
     * Devuelve false cuando la clave o el valor exceden los límites admitidos.
     */
    public boolean putValue(String key, String value) {
        if (key == null || value == null || !SAFE_KEY.matcher(key).matches() || value.length() > 4096) {
            return false;
        }
        String previous = values.put(key, value);
        if (!Objects.equals(previous, value)) {
            markDirty();
        }
        return true;
    }

    public boolean hasValue(String key) {
        return values.containsKey(key);
    }

    public String getValue(String key, String fallback) {
        return values.getOrDefault(key, fallback);
    }

    /**
     * Añade XP y aplica la curva aprobada: 100 + 25 × (nivel actual - 1)
     * para avanzar cada nivel, hasta nivel 30.
     */
    public long addXp(long amount) {
        if (amount <= 0L || level >= 30) {
            return 0L;
        }

        long remaining = amount;
        long maxAwardable = 0L;
        for (int currentLevel = level; currentLevel < 30; currentLevel++) {
            maxAwardable += xpToNextLevel(currentLevel);
        }
        maxAwardable -= xp;
        long accepted = Math.min(amount, Math.max(0L, maxAwardable));
        if (accepted == 0L) {
            return 0L;
        }

        long remainingToApply = accepted;
        long awarded = 0L;

        while (remainingToApply > 0L && level < 30) {
            long needed = xpToNextLevel(level) - xp;
            if (needed <= 0L) {
                levelUp();
                continue;
            }

            long applied = Math.min(remainingToApply, needed);
            xp += applied;
            remainingToApply -= applied;
            awarded += applied;

            if (xp >= xpToNextLevel(level)) {
                xp -= xpToNextLevel(level);
                levelUp();
            }
        }

        if (awarded > 0L) {
            markDirty();
        }
        return awarded;
    }

    public static long xpToNextLevel(int currentLevel) {
        int boundedLevel = clamp(currentLevel, 1, 30);
        return 100L + 25L * (boundedLevel - 1L);
    }

    private void levelUp() {
        if (level >= 30) {
            xp = 0L;
            return;
        }
        level++;
        skillPoints++;
        if (level % 2 == 0) {
            attributePoints++;
        }
        markDirty();
    }

    /**
     * Consume puntos de atributo de forma atómica.
     */
    public boolean spendAttributePoints(int amount) {
        if (amount <= 0 || amount > attributePoints) {
            return false;
        }
        attributePoints -= amount;
        markDirty();
        return true;
    }

    /**
     * Consume puntos de habilidad de forma atómica.
     */
    public boolean spendSkillPoints(int amount) {
        if (amount <= 0 || amount > skillPoints) {
            return false;
        }
        skillPoints -= amount;
        markDirty();
        return true;
    }

    @Override
    public NbtCompound writeNbt(NbtCompound nbt) {
        nbt.putInt(KEY_SCHEMA, CURRENT_SCHEMA_VERSION);
        nbt.putString(KEY_CAMPAIGN_ID, campaignId);
        nbt.putBoolean(KEY_STARTED, started);
        nbt.putInt(KEY_LEVEL, level);
        nbt.putLong(KEY_XP, xp);
        nbt.putInt(KEY_ATTRIBUTES, attributePoints);
        nbt.putInt(KEY_SKILLS, skillPoints);

        NbtCompound serializedValues = new NbtCompound();
        for (Map.Entry<String, String> entry : values.entrySet()) {
            if (SAFE_KEY.matcher(entry.getKey()).matches() && entry.getValue().length() <= 4096) {
                serializedValues.putString(entry.getKey(), entry.getValue());
            }
        }
        nbt.put(KEY_VALUES, serializedValues);
        return nbt;
    }

    public static CampaignState fromNbt(NbtCompound nbt) {
        int schema = nbt.contains(KEY_SCHEMA) ? nbt.getInt(KEY_SCHEMA) : 0;

        // Migración 0 -> 1: conserva los campos antiguos conocidos y añade
        // identificador, inicio y contenedor de valores con defaults seguros.
        if (schema < 1) {
            return migrateSchemaZero(nbt);
        }

        String campaignId = nbt.getString(KEY_CAMPAIGN_ID);
        if (campaignId.isEmpty()) {
            campaignId = UUID.randomUUID().toString();
        }

        Map<String, String> migratedValues = new LinkedHashMap<>();
        NbtCompound valuesNbt = nbt.getCompound(KEY_VALUES);
        for (String key : valuesNbt.getKeys()) {
            if (SAFE_KEY.matcher(key).matches()) {
                String value = valuesNbt.getString(key);
                if (value.length() <= 4096) {
                    migratedValues.put(key, value);
                }
            }
        }

        return new CampaignState(
                campaignId,
                nbt.getBoolean(KEY_STARTED),
                nbt.getInt(KEY_LEVEL),
                nbt.getLong(KEY_XP),
                nbt.getInt(KEY_ATTRIBUTES),
                nbt.getInt(KEY_SKILLS),
                migratedValues
        );
    }

    private static CampaignState migrateSchemaZero(NbtCompound nbt) {
        String oldId = nbt.getString(KEY_CAMPAIGN_ID);
        if (oldId.isEmpty()) {
            oldId = UUID.randomUUID().toString();
        }

        Map<String, String> values = new LinkedHashMap<>();
        if (nbt.contains(KEY_VALUES)) {
            NbtCompound oldValues = nbt.getCompound(KEY_VALUES);
            for (String key : oldValues.getKeys()) {
                if (SAFE_KEY.matcher(key).matches()) {
                    String value = oldValues.getString(key);
                    if (value.length() <= 4096) {
                        values.put(key, value);
                    }
                }
            }
        }

        CampaignState migrated = new CampaignState(
                oldId,
                nbt.getBoolean(KEY_STARTED),
                nbt.contains(KEY_LEVEL) ? nbt.getInt(KEY_LEVEL) : 1,
                nbt.getLong(KEY_XP),
                nbt.getInt(KEY_ATTRIBUTES),
                nbt.getInt(KEY_SKILLS),
                values
        );
        migrated.markDirty();
        return migrated;
    }

    private static int clamp(int value, int min, int max) {
        return Math.max(min, Math.min(max, value));
    }
}
