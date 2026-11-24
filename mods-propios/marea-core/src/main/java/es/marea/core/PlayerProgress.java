package es.marea.core;

import net.minecraft.nbt.NbtCompound;

/**
 * Progreso independiente por jugador; la campaña global permanece compartida.
 */
public final class PlayerProgress {
    private final int attributePointsSpent;
    private final int skillPointsSpent;

    public PlayerProgress(int attributePointsSpent, int skillPointsSpent) {
        this.attributePointsSpent = Math.max(0, attributePointsSpent);
        this.skillPointsSpent = Math.max(0, skillPointsSpent);
    }

    public static PlayerProgress empty() {
        return new PlayerProgress(0, 0);
    }

    public int getAttributePointsSpent() {
        return attributePointsSpent;
    }

    public int getSkillPointsSpent() {
        return skillPointsSpent;
    }

    NbtCompound writeNbt() {
        NbtCompound nbt = new NbtCompound();
        nbt.putInt("attribute_points_spent", attributePointsSpent);
        nbt.putInt("skill_points_spent", skillPointsSpent);
        return nbt;
    }

    static PlayerProgress readNbt(NbtCompound nbt) {
        return new PlayerProgress(
                nbt.getInt("attribute_points_spent"),
                nbt.getInt("skill_points_spent")
        );
    }
}
