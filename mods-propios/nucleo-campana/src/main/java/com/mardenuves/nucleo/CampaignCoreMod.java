package com.mardenuves.nucleo;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;

public final class CampaignCoreMod implements ModInitializer {
    public static final String MOD_ID = "mardenuves_nucleo";

    @Override
    public void onInitialize() {
        ServerLifecycleEvents.SERVER_STARTED.register(CampaignState::get);
    }
}
