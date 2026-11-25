package es.deriva.core.api;

import net.minecraft.nbt.NbtCompound;
import net.minecraft.nbt.NbtElement;
import net.minecraft.nbt.NbtList;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.world.PersistentState;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.UUID;

public final class CampaignState extends PersistentState {
    private static final String STORAGE_ID = "deriva_campaign";
    private static final int CURRENT_SCHEMA = 1;

    private final Map<UUID, PlayerData> players = new HashMap<>();

    public static CampaignState get(MinecraftServer server) {
        ServerWorld overworld = server.getOverworld();
        return overworld.getPersistentStateManager().getOrCreate(
                CampaignState::fromNbt,
                CampaignState::new,
                STORAGE_ID
        );
    }

    public PlayerSnapshot getPlayerSnapshot(UUID playerId) {
        return dataFor(playerId).snapshot();
    }

    public boolean setClass(UUID playerId, String classId, boolean allowReplacement) {
        if (classId != null && !CampaignIds.isClassId(classId)) {
            return false;
        }

        PlayerData data = dataFor(playerId);
        if (data.classId != null && !allowReplacement) {
            return false;
        }

        if (classId == null && data.classId == null) {
            return true;
        }

        data.classId = classId;
        markDirty();
        return true;
    }

    /**
     * Añade XP y actualiza nivel y puntos según los parámetros externos.
     * El cálculo acumulativo usa la curva aprobada como base de prueba:
     * XP requerida para el siguiente nivel = base + paso * (nivel - 1).
     */
    public int awardExperience(
            UUID playerId,
            int amount,
            int maxLevel,
            int xpBase,
            int xpStep,
            int attributePointsEveryLevels,
            int skillPointsPerLevel
    ) {
        if (amount <= 0 || maxLevel < 1 || xpBase < 1) {
            return 0;
        }

        PlayerData data = dataFor(playerId);
        int oldLevel = data.level;
        long added = Math.min((long) amount, Integer.MAX_VALUE - (long) data.experience);
        data.experience += (int) added;

        while (data.level < maxLevel) {
            long required = Math.max(
                    1L,
                    (long) xpBase + (long) Math.max(0, xpStep) * (data.level - 1L)
            );
            if (data.experience < required) {
                break;
            }

            data.experience -= (int) required;
            data.level++;
            data.skillPoints += Math.max(0, skillPointsPerLevel);

            if (attributePointsEveryLevels > 0
                    && data.level % attributePointsEveryLevels == 0) {
                data.attributePoints++;
            }
        }

        if (data.level >= maxLevel) {
            data.experience = 0;
        }

        markDirty();
        return data.level - oldLevel;
    }

    public boolean allocateAttribute(UUID playerId, String attributeId) {
        if (attributeId == null || attributeId.isBlank()) {
            return false;
        }

        PlayerData data = dataFor(playerId);
        if (data.attributePoints <= 0) {
            return false;
        }

        data.attributes.merge(attributeId, 1, Integer::sum);
        data.attributePoints--;
        markDirty();
        return true;
    }

    public boolean adjustFactionReputation(UUID playerId, String factionId, int amount) {
        if (!CampaignIds.isFactionId(factionId) || amount == 0) {
            return false;
        }

        PlayerData data = dataFor(playerId);
        int current = data.reputation.getOrDefault(factionId, 0);
        int updated = (int) Math.max(-2L, Math.min(2L, (long) current + amount));
        if (updated == current) {
            return false;
        }

        data.reputation.put(factionId, updated);
        markDirty();
        return true;
    }

    public boolean completeOnce(UUID playerId, String completionId) {
        if (completionId == null || completionId.isBlank()) {
            return false;
        }

        PlayerData data = dataFor(playerId);
        if (!data.completions.add(completionId)) {
            return false;
        }

        markDirty();
        return true;
    }

    public boolean learnSkillNode(UUID playerId, String nodeId, int nodeCost) {
        if (nodeId == null || nodeId.isBlank() || nodeCost < 1) {
            return false;
        }

        PlayerData data = dataFor(playerId);
        if (data.learnedNodes.contains(nodeId) || data.skillPoints < nodeCost) {
            return false;
        }

        data.learnedNodes.add(nodeId);
        data.skillPoints -= nodeCost;
        markDirty();
        return true;
    }

    public int getSkillPoints(UUID playerId) {
        return dataFor(playerId).skillPoints;
    }

    @Override
    public NbtCompound writeNbt(NbtCompound nbt) {
        nbt.putInt("schemaVersion", CURRENT_SCHEMA);
        NbtList playerList = new NbtList();

        for (Map.Entry<UUID, PlayerData> entry : players.entrySet()) {
            NbtCompound playerNbt = new NbtCompound();
            playerNbt.putUuid("uuid", entry.getKey());
            writePlayer(playerNbt, entry.getValue());
            playerList.add(playerNbt);
        }

        nbt.put("players", playerList);
        return nbt;
    }

    private static CampaignState fromNbt(NbtCompound nbt) {
        CampaignState state = new CampaignState();

        int schema = nbt.contains("schemaVersion", NbtElement.INT_TYPE)
                ? nbt.getInt("schemaVersion")
                : 0;

        // No se reinterpretan datos de un esquema futuro desconocido.
        if (schema > CURRENT_SCHEMA) {
            return state;
        }

        // Migración del esquema 0: conserva los registros previos con sus claves
        // conocidas y añade los nuevos campos ausentes con defaults seguros.
        NbtList playerList = nbt.getList("players", NbtElement.COMPOUND_TYPE);
        for (int i = 0; i < playerList.size(); i++) {
            NbtCompound playerNbt = playerList.getCompound(i);
            if (!playerNbt.containsUuid("uuid")) {
                continue;
            }

            UUID uuid = playerNbt.getUuid("uuid");
            PlayerData data = readPlayer(playerNbt, schema);
            state.players.put(uuid, data);
        }

        return state;
    }

    private static void writePlayer(NbtCompound nbt, PlayerData data) {
        if (data.classId != null) {
            nbt.putString("classId", data.classId);
        }
        nbt.putInt("level", data.level);
        nbt.putInt("experience", data.experience);
        nbt.putInt("attributePoints", data.attributePoints);
        nbt.putInt("skillPoints", data.skillPoints);

        NbtCompound attributes = new NbtCompound();
        data.attributes.forEach(attributes::putInt);
        nbt.put("attributes", attributes);

        NbtCompound reputation = new NbtCompound();
        data.reputation.forEach(reputation::putInt);
        nbt.put("reputation", reputation);

        nbt.put("completions", writeStringSet(data.completions));
        nbt.put("learnedNodes", writeStringSet(data.learnedNodes));
    }

    private static PlayerData readPlayer(NbtCompound nbt, int schema) {
        PlayerData data = new PlayerData();

        if (nbt.contains("classId", NbtElement.STRING_TYPE)) {
            String classId = nbt.getString("classId");
            data.classId = CampaignIds.isClassId(classId) ? classId : null;
        }

        data.level = Math.max(1, nbt.contains("level", NbtElement.INT_TYPE)
                ? nbt.getInt("level") : 1);
        data.experience = Math.max(0, nbt.contains("experience", NbtElement.INT_TYPE)
                ? nbt.getInt("experience") : 0);
        data.attributePoints = Math.max(0,
                nbt.contains("attributePoints", NbtElement.INT_TYPE)
                        ? nbt.getInt("attributePoints") : 0);
        data.skillPoints = Math.max(0,
                nbt.contains("skillPoints", NbtElement.INT_TYPE)
                        ? nbt.getInt("skillPoints") : 0);

        if (nbt.contains("attributes", NbtElement.COMPOUND_TYPE)) {
            NbtCompound attributes = nbt.getCompound("attributes");
            for (String key : attributes.getKeys()) {
                data.attributes.put(key, Math.max(0, attributes.getInt(key)));
            }
        }

        if (nbt.contains("reputation", NbtElement.COMPOUND_TYPE)) {
            NbtCompound reputation = nbt.getCompound("reputation");
            for (String key : reputation.getKeys()) {
                if (CampaignIds.isFactionId(key)) {
                    data.reputation.put(key, Math.max(-2, Math.min(2, reputation.getInt(key))));
                }
            }
        }

        readStringSet(nbt, "completions", data.completions);
        readStringSet(nbt, "learnedNodes", data.learnedNodes);
        return data;
    }

    private static NbtList writeStringSet(Set<String> values) {
        NbtList list = new NbtList();
        for (String value : values) {
            NbtCompound entry = new NbtCompound();
            entry.putString("value", value);
            list.add(entry);
        }
        return list;
    }

    private static void readStringSet(NbtCompound nbt, String key, Set<String> destination) {
        if (!nbt.contains(key, NbtElement.LIST_TYPE)) {
            return;
        }

        NbtList list = nbt.getList(key, NbtElement.COMPOUND_TYPE);
        for (int i = 0; i < list.size(); i++) {
            NbtCompound entry = list.getCompound(i);
            if (entry.contains("value", NbtElement.STRING_TYPE)) {
                destination.add(entry.getString("value"));
            }
        }
    }

    private PlayerData dataFor(UUID playerId) {
        return players.computeIfAbsent(playerId, ignored -> new PlayerData());
    }

    public record PlayerSnapshot(
            String classId,
            int level,
            int experience,
            int attributePoints,
            int skillPoints,
            Map<String, Integer> attributes,
            Map<String, Integer> reputation,
            Set<String> completions,
            Set<String> learnedNodes
    ) {
        public PlayerSnapshot {
            attributes = Map.copyOf(attributes);
            reputation = Map.copyOf(reputation);
            completions = Set.copyOf(completions);
            learnedNodes = Set.copyOf(learnedNodes);
        }
    }

    private static final class PlayerData {
        private String classId;
        private int level = 1;
        private int experience;
        private int attributePoints;
        private int skillPoints;
        private final Map<String, Integer> attributes = new HashMap<>();
        private final Map<String, Integer> reputation = new HashMap<>();
        private final Set<String> completions = new HashSet<>();
        private final Set<String> learnedNodes = new HashSet<>();

        private PlayerSnapshot snapshot() {
            return new PlayerSnapshot(
                    classId,
                    level,
                    experience,
                    attributePoints,
                    skillPoints,
                    attributes,
                    reputation,
                    completions,
                    learnedNodes
            );
        }
    }
}