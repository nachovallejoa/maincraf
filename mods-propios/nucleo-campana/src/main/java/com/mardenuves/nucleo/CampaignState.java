package com.mardenuves.nucleo;

import net.minecraft.nbt.NbtCompound;
import net.minecraft.server.MinecraftServer;
import net.minecraft.world.PersistentState;

/**
 * Núcleo narrativo mínimo ya existente en el árbol del proyecto.
 * Se conserva separado de deriva-core para no mezclar IDs ni formatos de
 * almacenamiento que la documentación identifica como núcleos distintos.
 */
public final class CampaignState extends PersistentState {
    private static final String STORAGE_ID = "mardenuves_campaign";
    private static final int SCHEMA_VERSION = 1;

    private int schema = SCHEMA_VERSION;
    private boolean prologueStarted;
    private boolean lighthouseEvacuationRecorded;

    public static CampaignState get(MinecraftServer server) {
        return server.getOverworld()
                .getPersistentStateManager()
                .getOrCreate(CampaignState::fromNbt, CampaignState::new, STORAGE_ID);
    }

    public synchronized boolean startPrologue() {
        if (prologueStarted) {
            return false;
        }
        prologueStarted = true;
        markDirty();
        return true;
    }

    public synchronized boolean recordLighthouseEvacuation() {
        if (lighthouseEvacuationRecorded) {
            return false;
        }
        prologueStarted = true;
        lighthouseEvacuationRecorded = true;
        markDirty();
        return true;
    }

    public synchronized boolean isPrologueStarted() {
        return prologueStarted;
    }

    public synchronized boolean isLighthouseEvacuationRecorded() {
        return lighthouseEvacuationRecorded;
    }

    @Override
    public synchronized NbtCompound writeNbt(NbtCompound nbt) {
        nbt.putInt("schema", SCHEMA_VERSION);
        nbt.putBoolean("prologue_started", prologueStarted);
        nbt.putBoolean("lighthouse_evacuation_recorded", lighthouseEvacuationRecorded);
        return nbt;
    }

    public static CampaignState fromNbt(NbtCompound nbt) {
        CampaignState state = new CampaignState();
        int storedSchema = nbt.contains("schema") ? nbt.getInt("schema") : 0;

        // La versión 0 no tenía marcador de esquema; se conserva la información
        // disponible y se normaliza al esquema vigente en el siguiente guardado.
        state.prologueStarted = nbt.getBoolean("prologue_started");
        state.lighthouseEvacuationRecorded = nbt.getBoolean("lighthouse_evacuation_recorded");
        if (state.lighthouseEvacuationRecorded) {
            state.prologueStarted = true;
        }
        state.schema = SCHEMA_VERSION;
        if (storedSchema != SCHEMA_VERSION) {
            state.markDirty();
        }
        return state;
    }
}
