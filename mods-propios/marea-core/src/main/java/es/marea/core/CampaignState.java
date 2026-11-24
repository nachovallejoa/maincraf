package es.marea.core;

import net.minecraft.nbt.NbtCompound;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

/**
 * Estado de campaña serializable y versionado.
 *
 * Las claves de hechos y los IDs de recompensa son identificadores persistentes.
 * Los IDs de recompensa completados quedan registrados para impedir su repetición.
 */
public final class CampaignState {
    public static final int CURRENT_SCHEMA_VERSION = 1;

    private int schemaVersion = CURRENT_SCHEMA_VERSION;
    private int level = 1;
    private long experience;
    private int attributePointsSpent;
    private int skillPointsSpent;
    private String classId = "";
    private final Map<String, Integer> reputation = new HashMap<>();
    private final Map<String, Boolean> facts = new HashMap<>();
    private final Map<String, String> choices = new HashMap<>();
    private final Map<String, Long> claimedRewards = new HashMap<>();
    private final Map<UUID, PlayerProgress> players = new HashMap<>();

    public int getSchemaVersion() {
        return schemaVersion;
    }

    public int getLevel() {
        return level;
    }

    public long getExperience() {
        return experience;
    }

    public int getAttributePointsSpent() {
        return attributePointsSpent;
    }

    public int getSkillPointsSpent() {
        return skillPointsSpent;
    }

    public String getClassId() {
        return classId;
    }

    public Map<String, Integer> getReputation() {
        return Collections.unmodifiableMap(reputation);
    }

    public Map<String, Boolean> getFacts() {
        return Collections.unmodifiableMap(facts);
    }

    public Map<String, String> getChoices() {
        return Collections.unmodifiableMap(choices);
    }

    public Map<String, Long> getClaimedRewards() {
        return Collections.unmodifiableMap(claimedRewards);
    }

    public PlayerProgress getPlayer(UUID playerId) {
        return players.getOrDefault(playerId, PlayerProgress.empty());
    }

    public boolean hasFact(String factId) {
        return facts.getOrDefault(factId, false);
    }

    public boolean hasClaimedReward(String rewardId) {
        return claimedRewards.containsKey(rewardId);
    }

    public void setClassId(String classId) {
        this.classId = classId == null ? "" : classId;
    }

    public void setExperience(long experience) {
        this.experience = Math.max(0L, experience);
        recalculateLevel();
    }

    public void addExperience(long amount) {
        if (amount <= 0L) {
            return;
        }
        setExperience(saturatedAdd(experience, amount));
    }

    public boolean spendAttributePoints(int amount) {
        if (amount <= 0 || getUnspentAttributePoints() < amount) {
            return false;
        }
        attributePointsSpent += amount;
        return true;
    }

    public boolean spendSkillPoints(int amount) {
        if (amount <= 0 || getUnspentSkillPoints() < amount) {
            return false;
        }
        skillPointsSpent += amount;
        return true;
    }

    public int getEarnedAttributePoints() {
        return Math.max(0, (level - 1) / CampaignConfig.get().attributePointsEveryLevels);
    }

    public int getUnspentAttributePoints() {
        return Math.max(0, getEarnedAttributePoints() - attributePointsSpent);
    }

    public int getEarnedSkillPoints() {
        return Math.max(0, (level - 1) * CampaignConfig.get().skillPointsAfterLevelOne);
    }

    public int getUnspentSkillPoints() {
        return Math.max(0, getEarnedSkillPoints() - skillPointsSpent);
    }

    public void setFact(String factId, boolean value) {
        requireId(factId);
        facts.put(factId, value);
    }

    public void setChoice(String choiceId, String value) {
        requireId(choiceId);
        requireId(value);
        choices.put(choiceId, value);
    }

    public int getReputation(String factionId) {
        return reputation.getOrDefault(factionId, 0);
    }

    public int adjustReputation(String factionId, int delta) {
        requireId(factionId);
        CampaignConfig config = CampaignConfig.get();
        int updated = clamp(getReputation(factionId) + delta,
                config.minimumReputation,
                config.maximumReputation);
        reputation.put(factionId, updated);
        return updated;
    }

    /**
     * Registra una recompensa una sola vez y devuelve si se aceptó el registro.
     * El llamador puede entregar el objeto únicamente cuando este método devuelve true.
     */
    public boolean claimReward(String rewardId, long claimedAtEpochMillis) {
        requireId(rewardId);
        if (claimedRewards.containsKey(rewardId)) {
            return false;
        }
        claimedRewards.put(rewardId, claimedAtEpochMillis);
        return true;
    }

    public void setPlayerProgress(UUID playerId, PlayerProgress progress) {
        if (playerId == null || progress == null) {
            throw new IllegalArgumentException("playerId y progress no pueden ser nulos");
        }
        players.put(playerId, progress);
    }

    NbtCompound writeNbt() {
        NbtCompound nbt = new NbtCompound();
        nbt.putInt("schema_version", schemaVersion);
        nbt.putInt("level", level);
        nbt.putLong("experience", experience);
        nbt.putInt("attribute_points_spent", attributePointsSpent);
        nbt.putInt("skill_points_spent", skillPointsSpent);
        nbt.putString("class_id", classId);
        nbt.put("reputation", writeIntMap(reputation));
        nbt.put("facts", writeBooleanMap(facts));
        nbt.put("choices", writeStringMap(choices));
        nbt.put("claimed_rewards", writeLongMap(claimedRewards));

        NbtCompound playerNbt = new NbtCompound();
        players.forEach((uuid, progress) -> playerNbt.put(uuid.toString(), progress.writeNbt()));
        nbt.put("players", playerNbt);
        return nbt;
    }

    static CampaignState readNbt(NbtCompound nbt) {
        int storedVersion = nbt.getInt("schema_version");
        NbtCompound migrated = migrate(nbt, storedVersion);

        CampaignState state = new CampaignState();
        state.schemaVersion = CURRENT_SCHEMA_VERSION;
        state.level = clamp(migrated.getInt("level"), 1, CampaignConfig.get().maximumLevel);
        state.experience = Math.max(0L, migrated.getLong("experience"));
        state.attributePointsSpent = Math.max(0, migrated.getInt("attribute_points_spent"));
        state.skillPointsSpent = Math.max(0, migrated.getInt("skill_points_spent"));
        state.classId = migrated.getString("class_id");

        readIntMap(migrated.getCompound("reputation"), state.reputation);
        readBooleanMap(migrated.getCompound("facts"), state.facts);
        readStringMap(migrated.getCompound("choices"), state.choices);
        readLongMap(migrated.getCompound("claimed_rewards"), state.claimedRewards);

        NbtCompound playerNbt = migrated.getCompound("players");
        for (String key : playerNbt.getKeys()) {
            try {
                UUID uuid = UUID.fromString(key);
                state.players.put(uuid, PlayerProgress.readNbt(playerNbt.getCompound(key)));
            } catch (IllegalArgumentException ignored) {
                // Ignora solamente las entradas de jugador con UUID inválido.
            }
        }

        state.recalculateLevel();
        return state;
    }

    private void recalculateLevel() {
        int maxLevel = CampaignConfig.get().maximumLevel;
        int result = 1;
        while (result < maxLevel && experience >= experienceRequiredForLevel(result + 1)) {
            result++;
        }
        level = result;
    }

    /**
     * XP acumulada necesaria para alcanzar el nivel indicado:
     * suma de la curva aprobada 100 + 25 × (L − 1).
     */
    public static long experienceRequiredForLevel(int targetLevel) {
        if (targetLevel <= 1) {
            return 0L;
        }
        long n = targetLevel - 1L;
        return 100L * n + 25L * n * (n - 1L) / 2L;
    }

    private static NbtCompound migrate(NbtCompound original, int version) {
        if (version > CURRENT_SCHEMA_VERSION) {
            throw new IllegalStateException("El guardado de campaña usa un esquema más nuevo: " + version);
        }

        NbtCompound nbt = original.copy();
        if (version <= 0) {
            // Migración inicial: los campos ausentes reciben defaults; los datos compatibles se conservan.
            if (!nbt.contains("experience")) {
                nbt.putLong("experience", 0L);
            }
            if (!nbt.contains("level")) {
                nbt.putInt("level", 1);
            }
            if (!nbt.contains("attribute_points_spent")) {
                nbt.putInt("attribute_points_spent", 0);
            }
            if (!nbt.contains("skill_points_spent")) {
                nbt.putInt("skill_points_spent", 0);
            }
            if (!nbt.contains("class_id")) {
                nbt.putString("class_id", "");
            }
            if (!nbt.contains("reputation")) {
                nbt.put("reputation", new NbtCompound());
            }
            if (!nbt.contains("facts")) {
                nbt.put("facts", new NbtCompound());
            }
            if (!nbt.contains("choices")) {
                nbt.put("choices", new NbtCompound());
            }
            if (!nbt.contains("claimed_rewards")) {
                nbt.put("claimed_rewards", new NbtCompound());
            }
            if (!nbt.contains("players")) {
                nbt.put("players", new NbtCompound());
            }
        }

        nbt.putInt("schema_version", CURRENT_SCHEMA_VERSION);
        return nbt;
    }

    private static NbtCompound writeIntMap(Map<String, Integer> values) {
        NbtCompound nbt = new NbtCompound();
        values.forEach(nbt::putInt);
        return nbt;
    }

    private static NbtCompound writeLongMap(Map<String, Long> values) {
        NbtCompound nbt = new NbtCompound();
        values.forEach(nbt::putLong);
        return nbt;
    }

    private static NbtCompound writeBooleanMap(Map<String, Boolean> values) {
        NbtCompound nbt = new NbtCompound();
        values.forEach(nbt::putBoolean);
        return nbt;
    }

    private static NbtCompound writeStringMap(Map<String, String> values) {
        NbtCompound nbt = new NbtCompound();
        values.forEach(nbt::putString);
        return nbt;
    }

    private static void readIntMap(NbtCompound nbt, Map<String, Integer> target) {
        for (String key : nbt.getKeys()) {
            target.put(key, nbt.getInt(key));
        }
    }

    private static void readLongMap(NbtCompound nbt, Map<String, Long> target) {
        for (String key : nbt.getKeys()) {
            target.put(key, nbt.getLong(key));
        }
    }

    private static void readBooleanMap(NbtCompound nbt, Map<String, Boolean> target) {
        for (String key : nbt.getKeys()) {
            target.put(key, nbt.getBoolean(key));
        }
    }

    private static void readStringMap(NbtCompound nbt, Map<String, String> target) {
        for (String key : nbt.getKeys()) {
            target.put(key, nbt.getString(key));
        }
    }

    private static void requireId(String id) {
        if (id == null || id.isBlank()) {
            throw new IllegalArgumentException("El identificador no puede ser nulo ni vacío");
        }
    }

    private static int clamp(int value, int min, int max) {
        return Math.max(min, Math.min(max, value));
    }

    private static long saturatedAdd(long left, long right) {
        if (right > 0L && left > Long.MAX_VALUE - right) {
            return Long.MAX_VALUE;
        }
        return left + right;
    }
}
