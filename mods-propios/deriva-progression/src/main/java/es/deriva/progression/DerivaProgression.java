package es.deriva.progression;

import es.deriva.core.config.CampaignConfig;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;

public final class DerivaProgression implements ModInitializer {
    @Override
    public void onInitialize() {
        // La carga diferida de CampaignConfig también cubre inicializadores
        // si el Loader invoca este entrypoint antes del del núcleo.
        CampaignConfig.get();
        CampaignProgression.registerCommands();
    }
}
