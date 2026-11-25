package es.deriva.progression;

import es.deriva.core.api.CampaignState;
import es.deriva.core.config.CampaignConfig;

import java.util.UUID;

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
        if (!CampaignConfig.get().isClassSelectionEnabled()) {
            return false;
        }
        return state.setClass(playerId, classId, false);
    }

    public static boolean learnSkillNode(CampaignState state, UUID playerId, String nodeId) {
        return state.learnSkillNode(
                playerId,
                nodeId,
                CampaignConfig.get().getSkillNodeCost()
        );
    }
}