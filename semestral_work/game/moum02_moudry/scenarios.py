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
        'The_Pillar_of_Autumn', # Aktuální prostor
        ('Halo',), # Aktuální sousedé
        (AR, JACOB_KEYES, ), # H-objekty v prostoru
        (PISTOL, 'generátor_štítu', ), # H-Objekty v batohu
    ),
    ScenarioStep(tsNS_1, f"{TALK} jacob_keyes",
        "Pokoušíte se zeptat objektu Jacob_Keyes. Jaký je váš dotaz?",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole', 'generátor_štítu',),
    ),
    ScenarioStep(tsNS_0, END_TALK, END_TALK_TEXT,
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole', 'generátor_štítu',),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence, Kartograf, The_Pillar_of_Autumn)",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, Laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Laboratoř",
        f"{ROOM_MOVE} Laboratoř\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence,)",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Klíč_ke_knihovně",
        ITEM_TAKE_TEXT,
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "[Elite]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, Laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE}: Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence, Kartograf, The_Pillar_of_Autumn)",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_0, OVERVIEW,
        "---------- Přehled ----------\n"
        "- Obsah batohu: ('Pistole', 'Klíč_ke_knihovně')\n"
        "- Počet životů: 100\n"
        "- Velikost štítu: 150\n\n"
        "----- Postup -----\n"
        "- Máte klíč ke knihovně? Ano\n"
        "- Odemkli jste knihovnu? Ne\n",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Kartograf",
        f"{ROOM_MOVE} Kartograf\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Knihovna, Halo)",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_1, f"{OPEN} knihovna",
        "Místnost (knihovna) byla otevřena",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsPUT_DOWN, f"{PUT_DOWN} Klíč_ke_knihovně",
        "Věc (Klíč_ke_knihovně) byla položena",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]", "Klíč_ke_knihovně"),
        ("Pistole", "generátor_štítu")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Knihovna",
        f"{ROOM_MOVE} Knihovna\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(TRC, Kartograf)",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole", "Index"),
        ("Pistole", "generátor_štítu")
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Index",
        "Předmět (Index) byl zvednut",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole",),
        ("Pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} TRC",
        f"{ROOM_MOVE} TRC\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(the_maw, Knihovna)",
        "TRC",
        ("the_maw", "Knihovna"),
        ("[Grunt]", "[Covenant]"),
        ("Pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} the_maw",
        f"{ROOM_MOVE} The Maw\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(TRC,)",
        "the_maw",
        ("TRC",),
        ("[Arbiter]",),
        ("Pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsNS_2, f"{USE} Index [Arbiter]",
        "Předmět (Index) byl použit na [Arbiter]",
        "the_maw",
        ("TRC", "Kartograf"),
        (),
        ("Pistole", "generátor_štítu")
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
    ScenarioStep(tsHELP, HELP, AVAILABLE_COMMANDS,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsEMPTY, "", EMPTY_COMMAND,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsUNKNOWN, "přines", UNKNOWN_COMMAND,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsBAD_ITEM, f"{PICK_UP} Index",
        OBJECT_NOT_PRESENT,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsBAD_NEIGHBOR, f"{MOVE} TRC", WRONG_NEIGHBOUR,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsUNMOVABLE, f"{PICK_UP} Jacob_Keyes",
        "Předmět nelze zvednout",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsMOVE_WA, MOVE, COMMAND_MISSING_PARAMS,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsPUT_DOWN_WA, PUT_DOWN,
        COMMAND_MISSING_PARAMS,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsTAKE_WA, PICK_UP, COMMAND_MISSING_PARAMS,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsNOT_IN_BAG, f"{PUT_DOWN} Index", ITEM_NOT_IN_BAG,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence, Kartograf, The_Pillar_of_Autumn)",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Needler", ITEM_TAKE_TEXT,
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Needler")
    ),
    ScenarioStep(tsBAG_FULL, f"{PICK_UP} Plasma_Pistol", BAG_FULL,
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Needler")
    ),
    ScenarioStep(tsEND, END, GAME_END,
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Needler")
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
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS0_WrongCond, OVERVIEW,
            "V tuto chvíli nelze zobrazit přehled",
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS0_WrongCond, END_TALK,
            "V tuto chvíli neprobíhá rozhovor",
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_WRONG_ARG, f"{TALK} R39OWTJR",
            WRONG_ARGUMENT, "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_WrongCond, f"{TALK} [Flood]",
            "Tuto věc/postavu nelze oslovit",
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_0Args, TALK, MISSING_ARGUMENT,
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_WrongCond, f"{OPEN} Halo",
            "kontrolní_místnost_prstence", OPEN_WRONG_COND,
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS1_0Args, OPEN, MISSING_ARGUMENT,
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_WrongCond, f"{USE} generátor_štítu Needler",
            WRONG_ITEM_TARGET, "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_1Args, f"{USE} generátor_štítu",
            MISSING_ARGUMENT,
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_WRONG_2ndARG, f"{USE} generátor_štítu [Flood]",
            "Na tuto věc/osobu nelze věc použít",
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
        ScenarioStep(tsNS2_WRONG_1stARG, f"{USE} [Flood] já",
            UNUSEABLE_ITEM,
            "kontrolní_místnost_prstence",
            ("Halo", "Laboratoř"),
            ("Needler", "[Flood]"),
            ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ),
)



############################################################################

ScenarioStep.next_index = +1  # Index prvního kroku za startem

REQUIRED = Scenario('REQUIRED', stREQUIRED, (
    START_STEP,
    ScenarioStep(tsHELP, HELP, AVAILABLE_COMMANDS,
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence, Kartograf, The_Pillar_of_Autumn)",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, Laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Laboratoř",
        f"{ROOM_MOVE} Laboratoř\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence,)",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Klíč_ke_knihovně",
        ITEM_TAKE_TEXT,
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "[Elite]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        f"{ROOM_MOVE} kontrolní_místnost_prstence\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Halo, Laboratoř)",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        f"{ROOM_MOVE} Halo\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(kontrolní_místnost_prstence, Kartograf, The_Pillar_of_Autumn)",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Kartograf",
        f"{ROOM_MOVE} Kartograf\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(Knihovna, Halo)",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_1, f"{OPEN} knihovna",
        "Místnost (knihovna) byla otevřena",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Knihovna",
        f"{ROOM_MOVE} Knihovna\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(TRC, Kartograf)",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole", "Index"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Index",
        f"{ITEM_TAKE_TEXT} (Index)",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole",),
        ("Pistole", "generátor_štítu", "Index", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} TRC",
        f"{ROOM_MOVE} TRC\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(the_maw, Knihovna)",
        "TRC",
        ("the_maw", "Knihovna"),
        ("[Grunt]", "[Covenant]"),
        ("Pistole", "generátor_štítu", "Index", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} the_maw",
        f"{ROOM_MOVE} The Maw\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        "(TRC,)",
        "the_maw",
        ("TRC",),
        ("[Arbiter]",),
        ("Pistole", "generátor_štítu", "Index", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_2, f"{USE} Index [Arbiter]",
        "Předmět (Index) byl použit na [Arbiter]",
        "the_maw",
        ("TRC",),
        (),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
))



############################################################################

SCENARIOS = ( HAPPY,
              MISTAKE,
              MISTAKE_NS,
              REQUIRED,
            )



############################################################################
dbg.stop_mod(0, __name__)
