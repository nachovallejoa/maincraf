package es.marea.core;

import net.minecraft.nbt.NbtCompound;
import net.minecraft.server.MinecraftServer;
import net.minecraft.world.PersistentState;
import net.minecraft.world.PersistentStateManager;

/**
 * Persistencia global de campaña en el Overworld.
 * La estructura NBT incluye schema_version y se migra al cargar.
 */
public final class CampaignSavedData extends PersistentState {
    private static final String DATA_NAME = "marea_core_campaign";

    private CampaignState state;

    private CampaignSavedData(CampaignState state) {
        this.state = state;
    }

    public static CampaignSavedData get(MinecraftServer server) {
        PersistentStateManager manager = server.getOverworld().getPersistentStateManager();
        return manager.getOrCreate(CampaignSavedData::fromNbt, CampaignSavedData::new, DATA_NAME);
    }

    public CampaignState state() {
        return state;
    }

    public void markChanged() {
        markDirty();
    }

    @Override
    public NbtCompound writeNbt(NbtCompound nbt) {
        nbt.put("campaign", state.writeNbt());
        return nbt;
    }

    private static CampaignSavedData fromNbt(NbtCompound nbt) {
        return new CampaignSavedData(CampaignState.readNbt(nbt.getCompound("campaign")));
    }
}
