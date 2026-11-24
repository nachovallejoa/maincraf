package com.mardenuves.nucleo;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerWorldEvents;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.world.ServerWorld;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class CampaignCoreMod implements ModInitializer {
    public static final String MOD_ID = "mardenuves_nucleo";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    @Override
    public void onInitialize() {
        ServerWorldEvents.LOAD.register(CampaignCoreMod::onWorldLoad);
        LOGGER.info("Núcleo de campaña de Mar de Nubes inicializado.");
    }

    private static void onWorldLoad(MinecraftServer server, ServerWorld world) {
        if (world == server.getOverworld()) {
            CampaignState.get(world);
        }
    }
}
