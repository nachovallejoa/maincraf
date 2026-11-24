package es.deriva.core.api;

import net.minecraft.nbt.NbtCompound;
import net.minecraft.nbt.NbtElement;
import net.minecraft.nbt.NbtList;
import net.minecraft.server.MinecraftServer;
import net.minecraft.world.PersistentState;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.UUID;

/**
 * Estado de campaña compartido por los módulos.
 *
 * El archivo NBT guarda un número de esquema. Las lecturas de esquemas
 * anteriores se migran de forma tolerante y se vuelven a guardar en el
 * esquema actual.
 */
public final class CampaignState extends PersistentState {
    public static final String STORAGE_ID = "deriva_core_campaign";
    public static final int SCHEMA_VERSION = 1;

    private static final String KEY_SCHEMA = "schema";
    private static final String KEY_PLAYERS = "players";

    private final Map<UUID, PlayerData> players = new HashMap<>();

    public static CampaignState get(MinecraftServer server) {
        return server.getOverworld()
                .getPersistentStateManager()
                .getOrCreate(CampaignState::fromNbt, CampaignState::new, STORAGE_ID);
    }

    public synchronized PlayerSnapshot getPlayerSnapshot(UUID playerId) {
        PlayerData data = players.get(playerId);
        if (data == null) {
            return PlayerData.createDefault().snapshot();
        }
        return data.snapshot();
    }

    public synchronized boolean setClass(UUID playerId, String classId, boolean selectionEnabled) {
        if (!selectionEnabled || !CampaignIds.isClassId(classId)) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (classId.equals(data.classId)) {
            return false;
        }

        data.classId = classId;
        markDirty();
        return true;
    }

    /**
     * Añade XP de campaña y procesa todos los cambios de nivel.
     *
     * @return número de niveles obtenidos
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
        if (amount <= 0) {
            return 0;
        }

        int safeMaxLevel = Math.max(1, maxLevel);
        int safeXpBase = Math.max(1, xpBase);
        int safeXpStep = Math.max(0, xpStep);
        int safeAttributeInterval = Math.max(0, attributePointsEveryLevels);
        int safeSkillPoints = Math.max(0, skillPointsPerLevel);

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (data.level >= safeMaxLevel) {
            return 0;
        }

        long combinedXp = (long) data.experienceInLevel + amount;
        data.experienceInLevel = (int) Math.min(Integer.MAX_VALUE, combinedXp);

        int levelsGained = 0;
        while (data.level < safeMaxLevel) {
            int required = requiredXp(data.level, safeXpBase, safeXpStep);
            if (data.experienceInLevel < required) {
                break;
            }

            data.experienceInLevel -= required;
            data.level++;
            levelsGained++;

            if (safeAttributeInterval > 0 && data.level % safeAttributeInterval == 0) {
                data.attributePoints++;
            }
            data.skillPoints += safeSkillPoints;
        }

        if (data.level >= safeMaxLevel) {
            data.experienceInLevel = 0;
        }

        markDirty();
        return levelsGained;
    }

    public synchronized boolean allocateAttribute(UUID playerId, String attributeId) {
        if (attributeId == null || attributeId.isBlank()) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (data.attributePoints <= 0) {
            return false;
        }

        data.attributePoints--;
        data.attributes.merge(attributeId, 1, Integer::sum);
        markDirty();
        return true;
    }

    public synchronized boolean adjustFactionReputation(UUID playerId, String factionId, int delta) {
        if (!CampaignIds.isFactionId(factionId) || delta == 0) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        int oldValue = data.factionReputation.getOrDefault(factionId, 0);
        int newValue = Math.max(-2, Math.min(2, oldValue + delta));
        if (oldValue == newValue) {
            return false;
        }

        data.factionReputation.put(factionId, newValue);
        markDirty();
        return true;
    }

    public synchronized boolean completeOnce(UUID playerId, String completionId) {
        if (completionId == null || completionId.isBlank()) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (!data.completedIds.add(completionId)) {
            return false;
        }

        markDirty();
        return true;
    }

    public synchronized boolean learnSkillNode(UUID playerId, String nodeId, int cost) {
        if (nodeId == null || nodeId.isBlank() || cost <= 0) {
            return false;
        }

        PlayerData data = players.computeIfAbsent(playerId, ignored -> new PlayerData());
        if (data.learnedSkillNodeIds.contains(nodeId) || data.skillPoints < cost) {
            return false;
        }

        data.skillPoints -= cost;
        data.learnedSkillNodeIds.add(nodeId);
        markDirty();
        return true;
    }

    public synchronized int getSkillPoints(UUID playerId) {
        PlayerData data = players.get(playerId);
        return data == null ? 0 : data.skillPoints;
    }

    @Override
    public synchronized NbtCompound writeNbt(NbtCompound nbt) {
        nbt.putInt(KEY_SCHEMA, SCHEMA_VERSION);

        NbtList playerList = new NbtList();
        for (Map.Entry<UUID, PlayerData> entry : players.entrySet()) {
            NbtCompound playerNbt = new NbtCompound();
            playerNbt.putString("uuid", entry.getKey().toString());
            entry.getValue().writeNbt(playerNbt);
            playerList.add(playerNbt);
        }
        nbt.put(KEY_PLAYERS, playerList);
        return nbt;
    }

    public static CampaignState fromNbt(NbtCompound nbt) {
        CampaignState state = new CampaignState();
        int storedSchema = nbt.contains(KEY_SCHEMA, NbtElement.NUMBER_TYPE)
                ? nbt.getInt(KEY_SCHEMA)
                : 0;

        NbtList playerList = nbt.getList(KEY_PLAYERS, NbtElement.COMPOUND_TYPE);
        for (int i = 0; i < playerList.size(); i++) {
            NbtCompound playerNbt = playerList.getCompound(i);
            try {
                UUID uuid = UUID.fromString(playerNbt.getString("uuid"));
                state.players.put(uuid, PlayerData.fromNbt(playerNbt, storedSchema));
            } catch (IllegalArgumentException ignored) {
                // Entrada corrupta/antigua: se omite sin descartar el resto.
            }
        }

        // Siempre se escribe con la versión vigente en el siguiente guardado.
        if (storedSchema != SCHEMA_VERSION) {
            state.markDirty();
        }
        return state;
    }

    private static int requiredXp(int currentLevel, int base, int step) {
        long required = (long) base + (long) step * Math.max(0, currentLevel - 1);
        return (int) Math.min(Integer.MAX_VALUE, required);
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

    private static final class PlayerData {
        private String classId = "";
        private int level = 1;
        private int experienceInLevel;
        private int attributePoints;
        private int skillPoints;
        private final Map<String, Integer> attributes = new HashMap<>();
        private final Map<String, Integer> factionReputation = new HashMap<>();
        private final Set<String> completedIds = new HashSet<>();
        private final Set<String> learnedSkillNodeIds = new HashSet<>();

        private static PlayerData createDefault() {
            return new PlayerData();
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

        private void writeNbt(NbtCompound nbt) {
            nbt.putString("class", classId);
            nbt.putInt("level", level);
            nbt.putInt("xp", experienceInLevel);
            nbt.putInt("attribute_points", attributePoints);
            nbt.putInt("skill_points", skillPoints);

            NbtCompound attributeNbt = new NbtCompound();
            attributes.forEach(attributeNbt::putInt);
            nbt.put("attributes", attributeNbt);

            NbtCompound reputationNbt = new NbtCompound();
            factionReputation.forEach(reputationNbt::putInt);
            nbt.put("reputation", reputationNbt);

            nbt.put("completed", stringList(completedIds));
            nbt.put("learned_nodes", stringList(learnedSkillNodeIds));
        }

        private static PlayerData fromNbt(NbtCompound nbt, int storedSchema) {
            PlayerData data = new PlayerData();

            String storedClass = nbt.getString("class");
            if (CampaignIds.isClassId(storedClass)) {
                data.classId = storedClass;
            }

            data.level = Math.max(1, nbt.contains("level", NbtElement.NUMBER_TYPE)
                    ? nbt.getInt("level")
                    : 1);
            data.experienceInLevel = Math.max(0, nbt.getInt("xp"));
            data.attributePoints = Math.max(0, nbt.getInt("attribute_points"));
            data.skillPoints = Math.max(0, nbt.getInt("skill_points"));

            NbtCompound attributeNbt = nbt.getCompound("attributes");
            for (String key : attributeNbt.getKeys()) {
                int value = attributeNbt.getInt(key);
                if (!key.isBlank() && value > 0) {
                    data.attributes.put(key, value);
                }
            }

            NbtCompound reputationNbt = nbt.getCompound("reputation");
            for (String key : reputationNbt.getKeys()) {
                if (CampaignIds.isFactionId(key)) {
                    data.factionReputation.put(key, Math.max(-2, Math.min(2, reputationNbt.getInt(key))));
                }
            }

            readStringList(nbt, "completed", data.completedIds);
            readStringList(nbt, "learned_nodes", data.learnedSkillNodeIds);

            // Migración de esquema 0: los campos ya existentes se preservan;
            // los campos inexistentes reciben los valores base seguros.
            if (storedSchema <= 0) {
                data.level = Math.max(1, data.level);
            }
            return data;
        }

        private static NbtList stringList(Set<String> values) {
            NbtList list = new NbtList();
            for (String value : values) {
                if (value != null && !value.isBlank()) {
                    list.add(net.minecraft.nbt.NbtString.of(value));
                }
            }
            return list;
        }

        private static void readStringList(NbtCompound source, String key, Set<String> destination) {
            NbtList list = source.getList(key, NbtElement.STRING_TYPE);
            for (int i = 0; i < list.size(); i++) {
                String value = list.getString(i);
                if (!value.isBlank()) {
                    destination.add(value);
                }
            }
        }
    }
}
