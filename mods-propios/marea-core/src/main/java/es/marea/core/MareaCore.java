package es.marea.core;

import net.fabricmc.api.ModInitializer;
import net.minecraft.util.Identifier;

public final class MareaCore implements ModInitializer {
    public static final String MOD_ID = "marea_core";

    @Override
    public void onInitialize() {
        CampaignConfig.load();
    }

    public static Identifier id(String path) {
        return new Identifier(MOD_ID, path);
    }
}
