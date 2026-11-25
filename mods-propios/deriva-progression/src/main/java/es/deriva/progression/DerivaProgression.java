package es.deriva.progression;

import es.deriva.core.api.CampaignState;
import net.fabricmc.api.ModInitializer;

import java.util.UUID;

public final class DerivaProgression implements ModInitializer {
    @Override
    public void onInitialize() {
        // Este módulo publica lógica invocable por otros módulos.
        // No asigna XP automáticamente ni introduce reglas narrativas nuevas.
    }

    public static int awardExperience(CampaignState state, UUID playerId, int amount) {
        return CampaignProgression.awardExperience(state, playerId, amount);
    }
}