package es.deriva.progression;

import es.deriva.core.api.CampaignIds;
import es.deriva.core.api.CampaignState;
import es.deriva.core.config.CampaignConfig;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;

import java.util.UUID;

/**
 * API de progresión disponible para los módulos propios futuros.
 *
 * No elige una fuente de XP: ninguna fuente está aprobada en la
 * documentación de mecánicas.
 */
public final class CampaignProgression {
    private CampaignProgression() {
    }

    public static int grantExperience(
            MinecraftServer server,
            UUID playerId,
            int amount
    ) {
        CampaignConfig config = CampaignConfig.get();
        return CampaignState.get(server).awardExperience(
                playerId,
                amount,
                config.getMaxLevel(),
                config.getXpBase(),
                config.getXpStep(),
                config.getAttributePointsEveryLevels(),
                config.getSkillPointsPerLevel()
        );
    }

    public static void registerCommands() {
        CommandRegistrationCallback.EVENT.register((dispatcher, registryAccess, environment) ->
                dispatcher.register(
                        CommandManager.literal("deriva")
                                .then(CommandManager.literal("estado")
                                        .executes(context -> showStatus(context.getSource())))
                                .then(CommandManager.literal("clase")
                                        .then(CommandManager.literal(CampaignIds.CLASS_GUARDACORRIENTE)
                                                .executes(context -> chooseClass(
                                                        context.getSource(),
                                                        CampaignIds.CLASS_GUARDACORRIENTE
                                                )))
                                        .then(CommandManager.literal(CampaignIds.CLASS_VIGIA_DEL_PRISMA)
                                                .executes(context -> chooseClass(
                                                        context.getSource(),
                                                        CampaignIds.CLASS_VIGIA_DEL_PRISMA
                                                )))
                                        .then(CommandManager.literal(CampaignIds.CLASS_ROMPEANCLAS)
                                                .executes(context -> chooseClass(
                                                        context.getSource(),
                                                        CampaignIds.CLASS_ROMPEANCLAS
                                                ))))
                )
        );
    }

    private static int showStatus(ServerCommandSource source)
            throws com.mojang.brigadier.exceptions.CommandSyntaxException {
        ServerPlayerEntity player = source.getPlayerOrThrow();
        CampaignState state = CampaignState.get(source.getServer());
        CampaignState.PlayerSnapshot snapshot = state.getPlayerSnapshot(player.getUuid());

        Text className = snapshot.classId().isEmpty()
                ? Text.translatable("deriva_progression.class.none")
                : Text.translatable("deriva_progression.class." + snapshot.classId() + ".name");

        int requiredXp = CampaignConfig.get().xpRequiredForLevel(snapshot.level());

        source.sendFeedback(
                () -> Text.translatable(
                        "deriva_progression.status",
                        className,
                        snapshot.level(),
                        snapshot.experienceInLevel(),
                        requiredXp,
                        snapshot.attributePoints(),
                        snapshot.skillPoints()
                ),
                false
        );

        return 1;
    }

    private static int chooseClass(ServerCommandSource source, String classId)
            throws com.mojang.brigadier.exceptions.CommandSyntaxException {
        ServerPlayerEntity player = source.getPlayerOrThrow();
        CampaignConfig config = CampaignConfig.get();

        if (!config.isClassSelectionEnabled()) {
            source.sendFeedback(
                    () -> Text.translatable("deriva_progression.class.selection_disabled"),
                    false
            );
            return 0;
        }

        CampaignState state = CampaignState.get(source.getServer());
        if (!state.setClass(player.getUuid(), classId, true)) {
            return 0;
        }

        Text className = Text.translatable(
                "deriva_progression.class." + classId + ".name"
        );

        source.sendFeedback(
                () -> Text.translatable("deriva_progression.class.selected", className),
                false
        );

        return 1;
    }
}
