package es.deriva.core.config;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import net.fabricmc.loader.api.FabricLoader;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Configuración externa del sistema de campaña.
 *
 * Los valores iniciales corresponden a parámetros aprobados para pruebas,
 * no a un balance final.
 */
public final class CampaignConfig {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final Path CONFIG_PATH =
            FabricLoader.getInstance().getConfigDir().resolve("deriva-campaign.json");

    private static CampaignConfig instance = defaults();

    private boolean classSelectionEnabled = true;
    private int maxLevel = 30;
    private int xpBase = 100;
    private int xpStep = 25;
    private int attributePointsEveryLevels = 2;
    private int skillPointsPerLevel = 1;
    private int skillNodeCost = 1;

    private CampaignConfig() {
    }

    private static CampaignConfig defaults() {
        return new CampaignConfig();
    }

    public static CampaignConfig get() {
        return instance;
    }

    public static void load() {
        CampaignConfig loaded = defaults();

        if (Files.exists(CONFIG_PATH)) {
            try (Reader reader = Files.newBufferedReader(CONFIG_PATH)) {
                JsonObject json = GSON.fromJson(reader, JsonObject.class);
                if (json != null) {
                    loaded.classSelectionEnabled = readBoolean(
                            json, "classSelectionEnabled", loaded.classSelectionEnabled);
                    loaded.maxLevel = readInt(json, "maxLevel", loaded.maxLevel);
                    loaded.xpBase = readInt(json, "xpBase", loaded.xpBase);
                    loaded.xpStep = readInt(json, "xpStep", loaded.xpStep);
                    loaded.attributePointsEveryLevels = readInt(
                            json, "attributePointsEveryLevels",
                            loaded.attributePointsEveryLevels);
                    loaded.skillPointsPerLevel = readInt(
                            json, "skillPointsPerLevel", loaded.skillPointsPerLevel);
                    loaded.skillNodeCost = readInt(
                            json, "skillNodeCost", loaded.skillNodeCost);
                }
            } catch (IOException | RuntimeException exception) {
                System.err.println("[deriva_core] No se pudo leer la configuración; se usarán defaults: "
                        + exception.getMessage());
            }
        }

        loaded.sanitize();
        instance = loaded;
        instance.save();
    }

    public void save() {
        try {
            Path parent = CONFIG_PATH.getParent();
            if (parent != null) {
                Files.createDirectories(parent);
            }

            JsonObject json = new JsonObject();
            json.addProperty("classSelectionEnabled", classSelectionEnabled);
            json.addProperty("maxLevel", maxLevel);
            json.addProperty("xpBase", xpBase);
            json.addProperty("xpStep", xpStep);
            json.addProperty("attributePointsEveryLevels", attributePointsEveryLevels);
            json.addProperty("skillPointsPerLevel", skillPointsPerLevel);
            json.addProperty("skillNodeCost", skillNodeCost);

            try (Writer writer = Files.newBufferedWriter(CONFIG_PATH)) {
                GSON.toJson(json, writer);
            }
        } catch (IOException exception) {
            System.err.println("[deriva_core] No se pudo guardar la configuración: "
                    + exception.getMessage());
        }
    }

    public boolean isClassSelectionEnabled() {
        return classSelectionEnabled;
    }

    public int getMaxLevel() {
        return maxLevel;
    }

    public int getXpBase() {
        return xpBase;
    }

    public int getXpStep() {
        return xpStep;
    }

    public int getAttributePointsEveryLevels() {
        return attributePointsEveryLevels;
    }

    public int getSkillPointsPerLevel() {
        return skillPointsPerLevel;
    }

    public int getSkillNodeCost() {
        return skillNodeCost;
    }

    public int xpRequiredForLevel(int level) {
        int safeLevel = Math.max(1, Math.min(level, maxLevel));
        return xpBase + xpStep * (safeLevel - 1);
    }

    private void sanitize() {
        maxLevel = Math.max(1, maxLevel);
        xpBase = Math.max(1, xpBase);
        xpStep = Math.max(0, xpStep);
        attributePointsEveryLevels = Math.max(1, attributePointsEveryLevels);
        skillPointsPerLevel = Math.max(0, skillPointsPerLevel);
        skillNodeCost = Math.max(1, skillNodeCost);
    }

    private static int readInt(JsonObject json, String key, int fallback) {
        return json.has(key) && json.get(key).isJsonPrimitive()
                ? json.get(key).getAsInt()
                : fallback;
    }

    private static boolean readBoolean(JsonObject json, String key, boolean fallback) {
        return json.has(key) && json.get(key).isJsonPrimitive()
                ? json.get(key).getAsBoolean()
                : fallback;
    }
}