package es.deriva.core;

import es.deriva.core.config.CampaignConfig;
import net.fabricmc.api.ModInitializer;

public final class DerivaCore implements ModInitializer {
    public static final String MOD_ID = "deriva_core";

    @Override
    public void onInitialize() {
        CampaignConfig.load();
    }
}