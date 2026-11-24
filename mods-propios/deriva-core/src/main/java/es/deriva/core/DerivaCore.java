package es.deriva.core;

import es.deriva.core.config.CampaignConfig;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;

public final class DerivaCore implements ModInitializer {
    public static final String MOD_ID = "deriva_core";

    @Override
    public void onInitialize() {
        CampaignConfig.load();
        ServerLifecycleEvents.SERVER_STARTED.register(CampaignState::get);
    }
}
