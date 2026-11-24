package es.deriva.progression;

import es.deriva.core.api.CampaignState;
import es.deriva.core.config.CampaignConfig;

import java.util.UUID;

/**
 * API pública del servicio de progresión.
 *
 * Esta capa no define fuentes de XP por actividad: esa decisión sigue siendo
 * externa y los módulos llamadores deben conceder XP solo tras eventos
 * narrativos o de juego aprobados.
 */
public final class CampaignProgression {
    private CampaignProgression() {
    }

    public static int awardExperience(CampaignState state, UUID playerId, int amount) {
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

    public static boolean selectClass(CampaignState state, UUID playerId, String classId) {
        CampaignConfig config = CampaignConfig.get();
        return state.setClass(playerId, classId, config.isClassSelectionEnabled());
    }

    public static boolean learnSkillNode(CampaignState state, UUID playerId, String nodeId) {
        CampaignConfig config = CampaignConfig.get();
        return state.learnSkillNode(playerId, nodeId, config.getSkillNodeCost());
    }
}
