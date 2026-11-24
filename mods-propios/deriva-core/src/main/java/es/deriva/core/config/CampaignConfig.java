package es.deriva.core.config;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import net.fabricmc.loader.api.FabricLoader;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Configuración externa en config/deriva_core.json.
 * Se crean defaults si el archivo aún no existe.
 */
public final class CampaignConfig {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final Path CONFIG_PATH =
            FabricLoader.getInstance().getConfigDir().resolve("deriva_core.json");

    private static volatile CampaignConfig instance;

    private boolean classSelectionEnabled = true;
    private int maxLevel = 30;
    private int xpBase = 100;
    private int xpStep = 25;
    private int attributePointsEveryLevels = 2;
    private int skillPointsPerLevel = 1;
    private int skillNodeCost = 1;

    public static CampaignConfig get() {
        CampaignConfig result = instance;
        return result == null ? load() : result;
    }

    public static synchronized CampaignConfig load() {
        if (Files.exists(CONFIG_PATH)) {
            try (Reader reader = Files.newBufferedReader(CONFIG_PATH)) {
                CampaignConfig loaded = GSON.fromJson(reader, CampaignConfig.class);
                instance = sanitize(loaded == null ? new CampaignConfig() : loaded);
                return instance;
            } catch (IOException | JsonParseException exception) {
                System.err.println("[deriva_core] No se pudo leer deriva_core.json; se usan valores predeterminados: "
                        + exception.getMessage());
            }
        }

        instance = new CampaignConfig();
        saveDefaults(instance);
        return instance;
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

    /**
     * Recibe el nivel actual; el nivel 1 requiere xpBase para alcanzar nivel 2.
     */
    public int xpRequiredForLevel(int currentLevel) {
        long required = (long) xpBase + (long) xpStep * Math.max(0, currentLevel - 1);
        return (int) Math.min(Integer.MAX_VALUE, required);
    }

    private static CampaignConfig sanitize(CampaignConfig config) {
        config.maxLevel = Math.max(1, config.maxLevel);
        config.xpBase = Math.max(1, config.xpBase);
        config.xpStep = Math.max(0, config.xpStep);
        config.attributePointsEveryLevels = Math.max(0, config.attributePointsEveryLevels);
        config.skillPointsPerLevel = Math.max(0, config.skillPointsPerLevel);
        config.skillNodeCost = Math.max(1, config.skillNodeCost);
        return config;
    }

    private static void saveDefaults(CampaignConfig config) {
        try {
            Files.createDirectories(CONFIG_PATH.getParent());
            try (Writer writer = Files.newBufferedWriter(CONFIG_PATH)) {
                GSON.toJson(config, writer);
            }
        } catch (IOException exception) {
            System.err.println("[deriva_core] No se pudo crear deriva_core.json: " + exception.getMessage());
        }
    }
}
