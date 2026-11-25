package es.deriva.core.api;

import java.util.Set;

public final class CampaignIds {
    public static final String CLASS_GUARDACORRIENTE = "guardacorriente";
    public static final String CLASS_VIGIA_DEL_PRISMA = "vigia_del_prisma";
    public static final String CLASS_ROMPEANCLAS = "rompeanclas";

    public static final String FACTION_LIGA_DEL_LASTRE = "liga_del_lastre";
    public static final String FACTION_CARTOGRAFOS_DEL_PRISMA = "cartografos_del_prisma";
    public static final String FACTION_HERMANDAD_DEL_VAIVEN = "hermandad_del_vaiven";
    public static final String FACTION_FLOTA_SUMERGIDA = "flota_sumergida";

    private static final Set<String> CLASS_IDS = Set.of(
            CLASS_GUARDACORRIENTE,
            CLASS_VIGIA_DEL_PRISMA,
            CLASS_ROMPEANCLAS
    );

    private static final Set<String> FACTION_IDS = Set.of(
            FACTION_LIGA_DEL_LASTRE,
            FACTION_CARTOGRAFOS_DEL_PRISMA,
            FACTION_HERMANDAD_DEL_VAIVEN,
            FACTION_FLOTA_SUMERGIDA
    );

    private CampaignIds() {
    }

    public static boolean isClassId(String id) {
        return id != null && CLASS_IDS.contains(id);
    }

    public static boolean isFactionId(String id) {
        return id != null && FACTION_IDS.contains(id);
    }
}