package es.deriva.progression;

import es.deriva.core.api.CampaignState;
import es.deriva.core.config.CampaignConfig;
import net.fabricmc.api.ModInitializer;

/**
 * Fachada de progresión para que otros módulos no dupliquen la configuración
 * ni las reglas de concesión de XP.
 */
public final class DerivaProgression implements ModInitializer {
    @Override
    public void onInitialize() {
        // Inicializa/carga la configuración compartida del núcleo.
        CampaignConfig.load();
    }

    public static int awardExperience(CampaignState state, java.util.UUID playerId, int amount) {
        CampaignConfig config = CampaignConfig.get();
        return state.awardExperience(
                playerId,
                amount,
                config.getMaxLevel(),
                config.getXpBase(),
                config.getXpStep(),
                config.getAttributePointsEveryLevels(),
                config.getSkillPointsPerLevel()
        );
    }
}
