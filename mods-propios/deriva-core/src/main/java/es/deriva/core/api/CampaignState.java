package es.deriva.core.api;

import net.minecraft.nbt.NbtCompound;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.world.PersistentState;
import net.minecraft.world.PersistentStateManager;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.UUID;

/**
 * Datos de campaña guardados en el almacenamiento persistente del Overworld.
 *
 * Las mutaciones deben hacerse en el hilo del servidor. Se mantienen UUID
 * de jugador e IDs de finalización en vez de nombres o IDs efímeros.
 */
public final class CampaignState extends PersistentState {
    private static final String DATA_ID = "deriva_campaign";
    private static final int CURRENT_SCHEMA = 1;

    private final Map<UUID, PlayerData> players = new HashMap<>();

    public static CampaignState get(MinecraftServer server) {
        ServerWorld overworld = server.getOverworld();
        PersistentStateManager manager = overworld.getPersistentStateManager();

        return manager.getOrCreate(
                CampaignState::readNbt,
                CampaignState::new,
                DATA_ID
        );
    }

    private static CampaignState readNbt(NbtCompound originalTag) {
        NbtCompound tag = originalTag.copy();
        int schema = tag.contains("schema_version")
                ? tag.getInt("schema_version")
                : 0;

        if (schema < 0 || schema > CURRENT_SCHEMA) {
            throw new IllegalStateException(
                    "Esquema de campaña no compatible: " + schema
            );
        }

        boolean migrated = false;

        while (schema < CURRENT_SCHEMA) {
            if (schema == 0) {
                // El esquema inicial no tenía versión y podía omitir el mapa
                // de jugadores. Se conserva lo que exista y se añade el
                // contenedor faltante antes de fijar el esquema actual.
                if (!tag.contains("players")) {
                    tag.put("players", new NbtCompound());
                }
                schema = 1;
                tag.putInt("schema_version", schema);
                migrated = true;
            } else {
                throw new IllegalStateException(
                        "No hay migración de campaña para el esquema " + schema
                );
            }
        }

        CampaignState state = new CampaignState();
        NbtCompound playersTag = tag.getCompound("players");

        for (String key : playersTag.getKeys()) {
            try {
                UUID playerId = UUID.fromString(key);
                PlayerDataReadResult result = PlayerData.readNbt(playersTag.getCompound(key));
                state.players.put(playerId, result.data());
                migrated |= result.normalized();
            } catch (IllegalArgumentException ignored) {
                // Ignora una entrada con clave UUID inválida, sin abortar
                // la carga de las demás campañas.
                migrated = true;
            }
        }

        if (migrated) {
            state.markDirty();
        }

        return state;
    }

    @Override
    public NbtCompound writeNbt(NbtCompound tag) {
        tag.putInt("schema_version", CURRENT_SCHEMA);

        NbtCompound playersTag = new NbtCompound();
        for (Map.Entry<UUID, PlayerData> entry : players.entrySet()) {
            playersTag.put(entry.getKey().toString(), entry.getValue().writeNbt());
        }

        tag.put("players", playersTag);
        return tag;
    }

    public synchronized PlayerSnapshot getPlayerSnapshot(UUID playerId) {
        PlayerData data = players.get(playerId);
        if (data == null) {
            data = new PlayerData();
        }
        return data.snapshot();
    }

    /**
     * Selecciona una de las tres clases aprobadas. La selección repetida o
     * cambiada no borra XP, puntos ni datos guardados.
     */
    public synchronized boolean setClass(UUID playerId, String classId, boolean selectionEnabled) {
        if (!selectionEnabled || !CampaignIds.isClassId(classId)) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (classId.equals(data.classId)) {
            return true;
        }

        data.classId = classId;
        markDirty();
        return true;
    }

    /**
     * Añade XP y aplica la curva configurada. El exceso no se conserva al
     * alcanzar el nivel máximo documentado/configurado.
     *
     * @return número de niveles ganados
     */
    public synchronized int awardExperience(
            UUID playerId,
            int amount,
            int maxLevel,
            int xpBase,
            int xpStep,
            int attributePointsEveryLevels,
            int skillPointsPerLevel
    ) {
        if (amount <= 0 || maxLevel < 1 || maxLevel > 30
                || xpBase < 1 || xpStep < 0
                || attributePointsEveryLevels < 1
                || skillPointsPerLevel < 0) {
            return 0;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (data.level >= maxLevel) {
            return 0;
        }

        long remaining = amount;
        int levelsGained = 0;

        while (remaining > 0 && data.level < maxLevel) {
            long required = (long) xpBase + (long) xpStep * (data.level - 1);
            long combined = (long) data.experienceInLevel + remaining;

            if (combined < required) {
                data.experienceInLevel = (int) combined;
                remaining = 0;
            } else {
                remaining = combined - required;
                data.level++;
                levelsGained++;

                data.skillPoints += skillPointsPerLevel;
                if (data.level % attributePointsEveryLevels == 0) {
                    data.attributePoints++;
                }

                data.experienceInLevel = 0;
            }
        }

        if (levelsGained > 0 || amount > 0) {
            markDirty();
        }

        return levelsGained;
    }

    /**
     * Gasta un punto de atributo. Los IDs concretos de atributos y sus
     * efectos quedan para el módulo de builds; el núcleo solo persiste la
     * asignación solicitada.
     */
    public synchronized boolean allocateAttribute(UUID playerId, String attributeId) {
        if (!isValidKey(attributeId)) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (data.attributePoints <= 0) {
            return false;
        }

        int current = data.attributes.getOrDefault(attributeId, 0);
        if (current == Integer.MAX_VALUE) {
            return false;
        }

        data.attributePoints--;
        data.attributes.put(attributeId, current + 1);
        markDirty();
        return true;
    }

    /**
     * Ajusta la reputación de una facción ya documentada.
     */
    public synchronized boolean adjustFactionReputation(
            UUID playerId,
            String factionId,
            int delta
    ) {
        if (!CampaignIds.isFactionId(factionId) || delta == 0) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        int current = data.factionReputation.getOrDefault(factionId, 0);

        final int updated;
        try {
            updated = Math.addExact(current, delta);
        } catch (ArithmeticException exception) {
            return false;
        }

        data.factionReputation.put(factionId, updated);
        markDirty();
        return true;
    }

    /**
     * Registra un hito por jugador una sola vez.
     */
    public synchronized boolean completeOnce(UUID playerId, String completionId) {
        if (!isValidKey(completionId)) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (!data.completedIds.add(completionId)) {
            return false;
        }

        markDirty();
        return true;
    }

    private static boolean isValidKey(String value) {
        if (value == null || value.isEmpty() || value.length() > 128) {
            return false;
        }

        for (int index = 0; index < value.length(); index++) {
            char character = value.charAt(index);
            boolean valid = (character >= 'a' && character <= 'z')
                    || (character >= '0' && character <= '9')
                    || character == '_'
                    || character == '-'
                    || character == '.'
                    || character == ':';

            if (!valid) {
                return false;
            }
        }

        return true;
    }

    public record PlayerSnapshot(
            String classId,
            int level,
            int experienceInLevel,
            int attributePoints,
            int skillPoints,
            Map<String, Integer> attributes,
            Map<String, Integer> factionReputation,
            Set<String> completedIds,
            Set<String> learnedSkillNodeIds
    ) {
        public PlayerSnapshot {
            attributes = Map.copyOf(attributes);
            factionReputation = Map.copyOf(factionReputation);
            completedIds = Set.copyOf(completedIds);
            learnedSkillNodeIds = Set.copyOf(learnedSkillNodeIds);
        }
    }

    private record PlayerDataReadResult(PlayerData data, boolean normalized) {
    }

    private static final class PlayerData {
        private String classId = "";
        private int level = 1;
        private int experienceInLevel;
        private int attributePoints;
        private int skillPoints;
        private final Map<String, Integer> attributes = new HashMap<>();
        private final Map<String, Integer> factionReputation = new HashMap<>();
        private final Set<String> completedIds = new HashSet<>();

        // Reservado para el árbol de habilidades. No se ofrecen compras
        // de nodos hasta que sus habilidades y efectos estén definidos.
        private final Set<String> learnedSkillNodeIds = new HashSet<>();

        private static PlayerDataReadResult readNbt(NbtCompound tag) {
            PlayerData data = new PlayerData();
            boolean normalized = false;

            String storedClassId = tag.getString("class_id");
            if (CampaignIds.isClassId(storedClassId)) {
                data.classId = storedClassId;
            } else if (!storedClassId.isEmpty()) {
                normalized = true;
            }

            int storedLevel = tag.getInt("level");
            data.level = clamp(storedLevel, 1, 30);
            normalized |= storedLevel != data.level;

            int storedExperience = tag.getInt("experience_in_level");
            data.experienceInLevel = Math.max(0, storedExperience);
            normalized |= storedExperience != data.experienceInLevel;

            int storedAttributePoints = tag.getInt("attribute_points");
            data.attributePoints = Math.max(0, storedAttributePoints);
            normalized |= storedAttributePoints != data.attributePoints;

            int storedSkillPoints = tag.getInt("skill_points");
            data.skillPoints = Math.max(0, storedSkillPoints);
            normalized |= storedSkillPoints != data.skillPoints;

            NbtCompound attributesTag = tag.getCompound("attributes");
            for (String key : attributesTag.getKeys()) {
                if (isValidKey(key)) {
                    int value = attributesTag.getInt(key);
                    if (value > 0) {
                        data.attributes.put(key, value);
                    } else {
                        normalized = true;
                    }
                } else {
                    normalized = true;
                }
            }

            NbtCompound reputationTag = tag.getCompound("faction_reputation");
            for (String key : reputationTag.getKeys()) {
                if (CampaignIds.isFactionId(key)) {
                    data.factionReputation.put(key, reputationTag.getInt(key));
                } else {
                    normalized = true;
                }
            }

            normalized |= readStringSet(tag.getCompound("completed_ids"), data.completedIds);
            normalized |= readStringSet(
                    tag.getCompound("learned_skill_nodes"),
                    data.learnedSkillNodeIds
            );

            if (data.level >= 30 && data.experienceInLevel != 0) {
                data.experienceInLevel = 0;
                normalized = true;
            }

            return new PlayerDataReadResult(data, normalized);
        }

        private static boolean readStringSet(NbtCompound tag, Set<String> target) {
            boolean normalized = false;
            for (String key : tag.getKeys()) {
                if (isValidKey(key) && tag.getBoolean(key)) {
                    target.add(key);
                } else {
                    normalized = true;
                }
            }
            return normalized;
        }

        private NbtCompound writeNbt() {
            NbtCompound tag = new NbtCompound();
            tag.putString("class_id", classId);
            tag.putInt("level", level);
            tag.putInt("experience_in_level", experienceInLevel);
            tag.putInt("attribute_points", attributePoints);
            tag.putInt("skill_points", skillPoints);

            NbtCompound attributesTag = new NbtCompound();
            attributes.forEach(attributesTag::putInt);
            tag.put("attributes", attributesTag);

            NbtCompound reputationTag = new NbtCompound();
            factionReputation.forEach(reputationTag::putInt);
            tag.put("faction_reputation", reputationTag);

            tag.put("completed_ids", writeStringSet(completedIds));
            tag.put("learned_skill_nodes", writeStringSet(learnedSkillNodeIds));
            return tag;
        }

        private static NbtCompound writeStringSet(Set<String> values) {
            NbtCompound tag = new NbtCompound();
            for (String value : values) {
                tag.putBoolean(value, true);
            }
            return tag;
        }

        private PlayerSnapshot snapshot() {
            return new PlayerSnapshot(
                    classId,
                    level,
                    experienceInLevel,
                    attributePoints,
                    skillPoints,
                    attributes,
                    factionReputation,
                    completedIds,
                    learnedSkillNodeIds
            );
        }

        private static int clamp(int value, int minimum, int maximum) {
            return Math.max(minimum, Math.min(maximum, value));
        }
    }
}
