package com.mardenuves.decisiones;

import com.mardenuves.nucleo.CampaignState;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;

/**
 * Inicializa el registro del prólogo sin adelantar ni revelar información
 * narrativa posterior.
 */
public final class DecisionsMod implements ModInitializer {
    @Override
    public void onInitialize() {
        ServerLifecycleEvents.SERVER_STARTED.register(CampaignState::get);
    }
}
