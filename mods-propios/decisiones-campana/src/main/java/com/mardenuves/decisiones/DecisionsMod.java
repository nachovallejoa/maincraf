package com.mardenuves.decisiones;

import com.mardenuves.nucleo.CampaignState;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerWorldEvents;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.world.ServerWorld;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class DecisionsMod implements ModInitializer {
    public static final String MOD_ID = "mardenuves_decisiones";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    @Override
    public void onInitialize() {
        ServerWorldEvents.LOAD.register(DecisionsMod::initializeNarrativeState);
        LOGGER.info("Registro narrativo de Mar de Nubes inicializado.");
    }

    private static void initializeNarrativeState(MinecraftServer server, ServerWorld world) {
        if (world != server.getOverworld()) {
            return;
        }

        CampaignState state = CampaignState.get(world);
        putDefaultIfMissing(state, "narrative.schema", "1");
        putDefaultIfMissing(state, "faction.liga_del_lastre.reputation", "0");
        putDefaultIfMissing(state, "faction.cartografos_del_prisma.reputation", "0");
        putDefaultIfMissing(state, "faction.hermandad_del_vaiven.reputation", "0");
        putDefaultIfMissing(state, "faction.flota_sumergida.reputation", "0");
    }

    private static void putDefaultIfMissing(CampaignState state, String key, String value) {
        if (!state.hasValue(key)) {
            state.putValue(key, value);
        }
    }
}
