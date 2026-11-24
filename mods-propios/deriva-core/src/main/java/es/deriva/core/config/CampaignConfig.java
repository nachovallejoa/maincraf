package es.deriva.core.config;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Properties;

/**
 * Configuración externa del núcleo.
 *
 * Los valores iniciales corresponden a las cifras documentadas de la
 * propuesta de progresión. No definen fuentes de XP ni habilidades.
 */
public final class CampaignConfig {
    private static final Path CONFIG_PATH = Path.of("config", "deriva.properties");

    private static volatile CampaignConfig instance;

    private final boolean classSelectionEnabled;
    private final int maxLevel;
    private final int xpBase;
    private final int xpStep;
    private final int attributePointsEveryLevels;
    private final int skillPointsPerLevel;
    private final int skillNodeCost;

    private CampaignConfig(
            boolean classSelectionEnabled,
            int maxLevel,
            int xpBase,
            int xpStep,
            int attributePointsEveryLevels,
            int skillPointsPerLevel,
            int skillNodeCost
    ) {
        this.classSelectionEnabled = classSelectionEnabled;
        this.maxLevel = maxLevel;
        this.xpBase = xpBase;
        this.xpStep = xpStep;
        this.attributePointsEveryLevels = attributePointsEveryLevels;
        this.skillPointsPerLevel = skillPointsPerLevel;
        this.skillNodeCost = skillNodeCost;
    }

    public static CampaignConfig get() {
        CampaignConfig current = instance;
        if (current != null) {
            return current;
        }

        synchronized (CampaignConfig.class) {
            if (instance == null) {
                instance = loadFromDisk();
            }
            return instance;
        }
    }

    /**
     * Carga o crea el archivo de configuración. Puede volver a llamarse
     * desde el hilo del servidor si un módulo futuro incorpora recarga.
     */
    public static synchronized CampaignConfig load() {
        instance = loadFromDisk();
        return instance;
    }

    private static CampaignConfig loadFromDisk() {
        Properties properties = defaults();

        try {
            if (Files.exists(CONFIG_PATH)) {
                try (Reader reader = Files.newBufferedReader(CONFIG_PATH, StandardCharsets.UTF_8)) {
                    properties.load(reader);
                }
            } else {
                Path parent = CONFIG_PATH.getParent();
                if (parent != null) {
                    Files.createDirectories(parent);
                }

                try (Writer writer = Files.newBufferedWriter(CONFIG_PATH, StandardCharsets.UTF_8)) {
                    properties.store(writer, "Deriva campaign configuration");
                }
            }
        } catch (IOException exception) {
            throw new IllegalStateException(
                    "No se pudo leer o crear " + CONFIG_PATH,
                    exception
            );
        }

        return new CampaignConfig(
                readBoolean(properties, "class_selection_enabled", true),
                readInteger(properties, "max_level", 30, 1, 30),
                readInteger(properties, "xp_base", 100, 1, 1_000_000),
                readInteger(properties, "xp_step", 25, 0, 1_000_000),
                readInteger(properties, "attribute_points_every_levels", 2, 1, 30),
                readInteger(properties, "skill_points_per_level", 1, 0, 100),
                readInteger(properties, "skill_node_cost", 3, 1, 100)
        );
    }

    private static Properties defaults() {
        Properties properties = new Properties();
        properties.setProperty("class_selection_enabled", "true");
        properties.setProperty("max_level", "30");
        properties.setProperty("xp_base", "100");
        properties.setProperty("xp_step", "25");
        properties.setProperty("attribute_points_every_levels", "2");
        properties.setProperty("skill_points_per_level", "1");
        properties.setProperty("skill_node_cost", "3");
        return properties;
    }

    private static int readInteger(
            Properties properties,
            String key,
            int defaultValue,
            int minimum,
            int maximum
    ) {
        String raw = properties.getProperty(key);
        if (raw == null) {
            return defaultValue;
        }

        try {
            int value = Integer.parseInt(raw.trim());
            return value >= minimum && value <= maximum ? value : defaultValue;
        } catch (NumberFormatException exception) {
            return defaultValue;
        }
    }

    private static boolean readBoolean(Properties properties, String key, boolean defaultValue) {
        String raw = properties.getProperty(key);
        if (raw == null) {
            return defaultValue;
        }

        if ("true".equalsIgnoreCase(raw.trim())) {
            return true;
        }
        if ("false".equalsIgnoreCase(raw.trim())) {
            return false;
        }
        return defaultValue;
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
        if (level < 1 || level >= maxLevel) {
            return 0;
        }

        return xpBase + xpStep * (level - 1);
    }
}
