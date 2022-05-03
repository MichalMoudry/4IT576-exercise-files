#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Základní čtveřice scénářů pro hru inspirovanou pohádkou o Červené Karkulce.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api.scenario   import ScenarioStep, Scenario
from ..api.scen_types import *  # Především typu kroků
from .constants.actions_constants import *
from .constants.text_constants import *
from .constants.item_constants import *

############################################################################

############################################################################
# Základní úspěšný scénář demonstrující průběh hry, při němž hráč
# nezadává žádné chybné příkazy a dosáhne zadaného cíle.
HAPPY = Scenario('', stHAPPY, (
    START_STEP := ScenarioStep(tsSTART, '', # Zadaný příkaz
        WELCOME_MESSAGE,
        THE_PILLAR_OF_AUTUMN, # Aktuální prostor
        ('Halo',), # Aktuální sousedé
        (AR[1:], JACOB_KEYES[1:], ), # H-objekty v prostoru
        (PISTOL, SHIELD_GENERATOR, ), # H-Objekty v batohu
    ),
    ScenarioStep(tsNS_1, f"{TALK} jacob_keyes",
        "Pokoušíte se zeptat objektu Jacob_Keyes. Jaký je váš dotaz?",
        THE_PILLAR_OF_AUTUMN,
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('pistole', 'generátor_štítu',),
    ),
    ScenarioStep(tsNS_0, END_TALK, END_TALK_TEXT,
        THE_PILLAR_OF_AUTUMN,
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('pistole', 'generátor_štítu',),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"(kontrolní_místnost_prstence, kartograf, {THE_PILLAR_OF_AUTUMN})",
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("needler", "plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "laboratoř"),
        ("needler", "[flood]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} laboratoř",
        f"{ROOM_MOVE} laboratoř\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence,)",
        "laboratoř",
        ("kontrolní_místnost_prstence",),
        ("plasma_pistole", "klíč_ke_knihovně", "[elite]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} klíč_ke_knihovně",
        ITEM_TAKE_TEXT,
        "laboratoř",
        ("kontrolní_místnost_prstence",),
        ("plasma_pistole", "[elite]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "laboratoř"),
        ("needler", "[flood]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE}: Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"(kontrolní_místnost_prstence, kartograf, {THE_PILLAR_OF_AUTUMN})",
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("needler", "plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_0, OVERVIEW,
        "---------- Přehled ----------\n"
        "- Obsah batohu: ('pistole', 'klíč_ke_knihovně')\n"
        "- Počet životů: 100\n"
        "- Velikost štítu: 150\n\n"
        "----- Postup -----\n"
        "- Máte klíč ke knihovně? Ano\n"
        "- Odemkli jste knihovnu? Ne\n",
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("needler", "plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kartograf",
        f"{ROOM_MOVE} kartograf\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Knihovna, Halo)",
        "kartograf",
        ("Knihovna", "Halo"),
        ("carbine", "[forerunner]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_1, f"{OPEN} knihovna",
        "Místnost (knihovna) byla otevřena",
        "kartograf",
        ("Knihovna", "Halo"),
        ("carbine", "[forerunner]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsPUT_DOWN, f"{PUT_DOWN} klíč_ke_knihovně",
        "Věc (klíč_ke_knihovně) byla položena",
        "kartograf",
        ("Knihovna", "Halo"),
        ("carbine", "[forerunner]", "klíč_ke_knihovně"),
        ("pistole", "generátor_štítu")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Knihovna",
        f"{ROOM_MOVE} Knihovna\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(trc, kartograf)",
        "Knihovna",
        ("trc", "kartograf"),
        ("pistole", "Index"),
        ("pistole", "generátor_štítu")
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Index",
        "Předmět (Index) byl zvednut",
        "Knihovna",
        ("trc", "kartograf"),
        ("pistole",),
        ("pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} trc",
        f"{ROOM_MOVE} trc\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(the_maw, Knihovna)",
        "trc",
        ("the_maw", "Knihovna"),
        ("[grunt]", "[Covenant]"),
        ("pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} the_maw",
        f"{ROOM_MOVE} the_maw\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(trc,)",
        "the_maw",
        ("trc",),
        ("[Arbiter]",),
        ("pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsNS_2, f"{USE} Index [Arbiter]",
        "Předmět (Index) byl použit na [Arbiter]",
        "the_maw",
        ("trc", "kartograf"),
        (),
        ("pistole", "generátor_štítu")
    ),
))



############################################################################
# Základní chybový scénář demonstrující průběh hry, při němž hráč
# zadává chybně příkazy k provedení základních akcí
# a současně vyzkouší vyvolání nápovědy a nestandardní ukončení.

ScenarioStep.next_index = -1  # Index kroku před korektním startem

WRONG_START = ScenarioStep(tsNOT_START, 'start', # Zadaný příkaz
    WRONG_START_TEXT,
    '',                                         # Aktuální prostor
    (),                                         # Aktuální sousedé
    (),                                         # H-objekty v prostoru
    (),                                         # H-Objekty v batohu
)

ScenarioStep.next_index = +1  # Index prvního kroku za startem

MISTAKE = Scenario('', stMISTAKES, (
    WRONG_START,
    START_STEP,
    ScenarioStep(tsHELP, HELP,
        f"{WELCOME_MESSAGE}\n\n{AVAILABLE_COMMANDS}",
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsEMPTY, "", EMPTY_COMMAND,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsUNKNOWN, "přines", UNKNOWN_COMMAND,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsBAD_ITEM, f"{PICK_UP} Index",
        OBJECT_NOT_PRESENT,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsBAD_NEIGHBOR, f"{MOVE} trc", WRONG_NEIGHBOUR,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsUNMOVABLE, f"{PICK_UP} Jacob_Keyes",
        "Předmět nelze zvednout",
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsMOVE_WA, MOVE, COMMAND_MISSING_PARAMS,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsPUT_DOWN_WA, PUT_DOWN,
        COMMAND_MISSING_PARAMS,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsTAKE_WA, PICK_UP, COMMAND_MISSING_PARAMS,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsNOT_IN_BAG, f"{PUT_DOWN} Index", ITEM_NOT_IN_BAG,
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"(kontrolní_místnost_prstence, kartograf, {THE_PILLAR_OF_AUTUMN})",
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("needler", "plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} needler", ITEM_TAKE_TEXT,
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu", "needler")
    ),
    ScenarioStep(tsBAG_FULL, f"{PICK_UP} plasma_pistole", BAG_FULL,
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu", "needler")
    ),
    ScenarioStep(tsEND, END, GAME_END,
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("plasma_pistolee", "[grunt]"),
        ("pistole", "generátor_štítu", "needler")
    )
),)



############################################################################
# Základní chybový scénář demonstrující průběh hry, při němž hráč
# # zadává chybně příkazy k provedení rozšiřujících akcí.
ScenarioStep.next_index = 8 # Index prvního nestandardního kroku
MISTAKE_NS = Scenario('', stMISTAKES_NS, (
        HAPPY.steps[0],
        HAPPY.steps[1],
        HAPPY.steps[2],
        HAPPY.steps[3],
        HAPPY.steps[4],
        HAPPY.steps[5],
        HAPPY.steps[6],
        HAPPY.steps[7],
        ScenarioStep(tsNS1_WRONG_ARG, f"{OPEN} R39OWTJR",
            "Špatný argument parametru", "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS0_WrongCond, OVERVIEW,
            "V tuto chvíli nelze zobrazit přehled",
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS0_WrongCond, END_TALK,
            "V tuto chvíli neprobíhá rozhovor",
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_WRONG_ARG, f"{TALK} R39OWTJR",
            WRONG_ARGUMENT, "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_WrongCond, f"{TALK} [flood]",
            "Tuto věc/postavu nelze oslovit",
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_0Args, TALK, MISSING_ARGUMENT,
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_WrongCond, f"{OPEN} Halo",
            "kontrolní_místnost_prstence", OPEN_WRONG_COND,
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_0Args, OPEN, MISSING_ARGUMENT,
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_WrongCond, f"{USE} generátor_štítu needler",
            WRONG_ITEM_TARGET, "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_1Args, f"{USE} generátor_štítu",
            MISSING_ARGUMENT,
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_WRONG_2ndARG, f"{USE} generátor_štítu [flood]",
            "Na tuto věc/osobu nelze věc použít",
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_WRONG_1stARG, f"{USE} [flood] já",
            UNUSEABLE_ITEM,
            "kontrolní_místnost_prstence",
            ("Halo", "laboratoř"),
            ("needler", "[flood]"),
            ("pistole", "generátor_štítu", "klíč_ke_knihovně")
        ),
    ),
)



############################################################################

ScenarioStep.next_index = +1  # Index prvního kroku za startem

REQUIRED = Scenario('REQUIRED', stREQUIRED, (
    START_STEP,
    ScenarioStep(tsHELP, HELP,
        f"{WELCOME_MESSAGE}\n\n{AVAILABLE_COMMANDS}",
        THE_PILLAR_OF_AUTUMN,
        ("Halo",),
        (AR[1:], JACOB_KEYES[1:], ),
        (PISTOL[1:], SHIELD_GENERATOR[1:], ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"(kontrolní_místnost_prstence, kartograf, {THE_PILLAR_OF_AUTUMN})",
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("needler", "plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "laboratoř"),
        ("needler", "[flood]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} laboratoř",
        f"{ROOM_MOVE} laboratoř\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence,)",
        "laboratoř",
        ("kontrolní_místnost_prstence",),
        ("plasma_pistole", "klíč_ke_knihovně", "[elite]"),
        ("pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} klíč_ke_knihovně",
        ITEM_TAKE_TEXT,
        "laboratoř",
        ("kontrolní_místnost_prstence",),
        ("plasma_pistole", "[elite]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "laboratoř"),
        ("needler", "[flood]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"(kontrolní_místnost_prstence, kartograf, {THE_PILLAR_OF_AUTUMN})",
        "Halo",
        ("kontrolní_místnost_prstence", "kartograf",
        THE_PILLAR_OF_AUTUMN),
        ("needler", "plasma_pistole", "[grunt]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kartograf",
        f"{ROOM_MOVE} kartograf\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Knihovna, Halo)",
        "kartograf",
        ("Knihovna", "Halo"),
        ("carbine", "[forerunner]"),
        ("pistole", "generátor_štítu", "klíč_ke_knihovně")
    ),
    ScenarioStep(tsEND, END, GAME_END,
        "kartograf",
        ("Knihovna", "Halo"),
        (),
        ("pistole", "generátor_štítu", "carbine", "klíč_ke_knihovně")
    )
))



############################################################################

SCENARIOS = ( HAPPY,
              MISTAKE,
              MISTAKE_NS,
              REQUIRED,
            )



############################################################################
dbg.stop_mod(0, __name__)
