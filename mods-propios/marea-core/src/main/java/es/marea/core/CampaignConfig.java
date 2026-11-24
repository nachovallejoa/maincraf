package es.marea.core;

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
 * Configuración externa global del mod, ubicada en config/marea-campaign.json.
 * La configuración no modifica progreso guardado en mundos.
 */
public final class CampaignConfig {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final Path FILE = FabricLoader.getInstance()
            .getConfigDir()
            .resolve("marea-campaign.json");

    private static CampaignConfig current = defaults();

    public boolean campaignEnabled = true;
    public int maximumLevel = 30;
    public int attributePointsEveryLevels = 2;
    public int skillPointsAfterLevelOne = 1;
    public int skillPointsPerNode = 3;
    public int minimumReputation = -2;
    public int maximumReputation = 2;
    public boolean announceCampaignMilestones = true;

    public CampaignConfig() {
    }

    public static CampaignConfig defaults() {
        return new CampaignConfig();
    }

    public static CampaignConfig get() {
        return current;
    }

    public static synchronized void load() {
        if (!Files.exists(FILE)) {
            current = defaults();
            save();
            return;
        }

        try (Reader reader = Files.newBufferedReader(FILE)) {
            CampaignConfig loaded = GSON.fromJson(reader, CampaignConfig.class);
            current = validate(loaded == null ? defaults() : loaded);
        } catch (IOException | JsonParseException exception) {
            // [SIN VERIFICAR] MareaCore.LOGGER no está declarado en el MareaCore recibido.
            MareaCore.LOGGER.warn("No se pudo leer {}; se conservan los valores predeterminados.", FILE, exception);
            current = defaults();
        }
    }

    public static synchronized void save() {
        try {
            Files.createDirectories(FILE.getParent());
            try (Writer writer = Files.newBufferedWriter(FILE)) {
                GSON.toJson(current, writer);
            }
        } catch (IOException exception) {
            // [SIN VERIFICAR] MareaCore.LOGGER no está declarado en el MareaCore recibido.
            MareaCore.LOGGER.error("No se pudo guardar la configuración de campaña en {}.", FILE, exception);
        }
    }

    private static CampaignConfig validate(CampaignConfig config) {
        config.maximumLevel = clamp(config.maximumLevel, 1, 30);
        config.attributePointsEveryLevels = clamp(config.attributePointsEveryLevels, 1, 30);
        config.skillPointsAfterLevelOne = clamp(config.skillPointsAfterLevelOne, 0, 10);
        config.skillPointsPerNode = clamp(config.skillPointsPerNode, 1, 100);
        config.minimumReputation = clamp(config.minimumReputation, -100, 0);
        config.maximumReputation = clamp(config.maximumReputation, 0, 100);

        if (config.minimumReputation >= config.maximumReputation) {
            config.minimumReputation = -2;
            config.maximumReputation = 2;
        }
        return config;
    }

    private static int clamp(int value, int min, int max) {
        return Math.max(min, Math.min(max, value));
    }
}
