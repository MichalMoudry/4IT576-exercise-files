#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Základní čtveřice scénářů pro hru inspirovanou hrou Halo.
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
        (HALO,), # Aktuální sousedé
        (AR_2, JACOB_KEYES_2, ), # H-objekty v prostoru
        (PISTOL_2, SHIELD_GENERATOR_2, ), # H-Objekty v batohu
    ),
    ScenarioStep(tsNS_1, f"{TALK} {JACOB_KEYES_2}",
        f"Pokoušíte se zeptat objektu {JACOB_KEYES_2}."
        " Jaký je váš dotaz?",
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2,),
        (PISTOL_2, SHIELD_GENERATOR_2,),
    ),
    ScenarioStep(tsNS_0, END_TALK, END_TALK_TEXT,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2,),
        (PISTOL_2, SHIELD_GENERATOR_2,),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {HALO}",
        f"{ROOM_MOVE} {HALO}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM}, {KARTOGRAF}, {THE_PILLAR_OF_AUTUMN})",
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (NEEDLER_2, PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {CONTROL_ROOM}",
        f"{ROOM_MOVE} {CONTROL_ROOM}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({HALO}, {LAB})",
        CONTROL_ROOM,
        (HALO, LAB),
        (NEEDLER_2, FLOOD_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {LAB}",
        f"{ROOM_MOVE} {LAB}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM},)",
        LAB,
        (CONTROL_ROOM,),
        (PLASMA_PISTOL_2, LIBRARY_KEY_2, ELITE_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} {LIBRARY_KEY_2}",
        ITEM_TAKE_TEXT,
        LAB,
        (CONTROL_ROOM,),
        (PLASMA_PISTOL_2, ELITE_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {CONTROL_ROOM}",
        f"{ROOM_MOVE} {CONTROL_ROOM}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({HALO}, {LAB})",
        CONTROL_ROOM,
        (HALO, LAB),
        (NEEDLER_2, FLOOD_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {HALO}",
        f"{ROOM_MOVE}: {HALO}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM}, {KARTOGRAF}, {THE_PILLAR_OF_AUTUMN})",
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (NEEDLER_2, PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsNS_0, OVERVIEW,
        f"---------- {OVERVIEW} ----------\n"
        f"- Obsah batohu: ('{PISTOL_2}', '{LIBRARY_KEY_2}')\n"
        "- Počet životů: 100\n"
        "- Velikost štítu: 150\n\n"
        "----- Postup -----\n"
        "- Máte klíč ke knihovně? Ano\n"
        "- Odemkli jste knihovnu? Ne\n",
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (NEEDLER_2, PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {KARTOGRAF}",
        f"{ROOM_MOVE} {KARTOGRAF}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({LIBRARY}, {HALO})",
        KARTOGRAF,
        (LIBRARY, HALO),
        (CARBINE_2, FORERUNNER_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsNS_1, f"{OPEN} {LIBRARY}",
        f"Místnost ({LIBRARY}) byla otevřena",
        KARTOGRAF,
        (LIBRARY, HALO),
        (CARBINE_2, FORERUNNER_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsPUT_DOWN, f"{PUT_DOWN} {LIBRARY_KEY_2}",
        f"Věc ({LIBRARY_KEY_2}) byla položena",
        KARTOGRAF,
        (LIBRARY, HALO),
        (CARBINE_2, FORERUNNER_2, LIBRARY_KEY_2),
        (PISTOL_2, SHIELD_GENERATOR_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {LIBRARY}",
        f"{ROOM_MOVE} {LIBRARY}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({TRC}, {KARTOGRAF})",
        LIBRARY,
        (TRC, KARTOGRAF),
        (PISTOL_2, INDEX_2),
        (PISTOL_2, SHIELD_GENERATOR_2)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} {INDEX_2}",
        f"Předmět ({INDEX_2}) byl zvednut",
        LIBRARY,
        (TRC, KARTOGRAF),
        (PISTOL_2,),
        (PISTOL_2, SHIELD_GENERATOR_2, INDEX_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {TRC}",
        f"{ROOM_MOVE} {TRC}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({THE_MAW}, {LIBRARY})",
        TRC,
        (THE_MAW, LIBRARY),
        (GRUNT_2, COVENANT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, INDEX_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {THE_MAW}",
        f"{ROOM_MOVE} {THE_MAW}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({TRC},)",
        THE_MAW,
        (TRC,),
        (ARBITER_2,),
        (PISTOL_2, SHIELD_GENERATOR_2, INDEX_2)
    ),
    ScenarioStep(tsNS_2, f"{USE} {INDEX_2} {ARBITER_2}",
        f"Předmět ({INDEX_2}) byl použit na {ARBITER_2}",
        THE_MAW,
        (TRC, KARTOGRAF),
        (),
        (PISTOL_2, SHIELD_GENERATOR_2)
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
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsEMPTY, "", EMPTY_COMMAND,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsUNKNOWN, "přines", UNKNOWN_COMMAND,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsBAD_ITEM, f"{PICK_UP} {INDEX_2}",
        OBJECT_NOT_PRESENT,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsBAD_NEIGHBOR, f"{MOVE} {TRC}", WRONG_NEIGHBOUR,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsUNMOVABLE, f"{PICK_UP} {JACOB_KEYES_2}",
        UNMOVABLE_ITEM,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsMOVE_WA, MOVE, COMMAND_MISSING_PARAMS,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsPUT_DOWN_WA, PUT_DOWN,
        COMMAND_MISSING_PARAMS,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsTAKE_WA, PICK_UP, COMMAND_MISSING_PARAMS,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsNOT_IN_BAG, f"{PUT_DOWN} {INDEX_2}", ITEM_NOT_IN_BAG,
        THE_PILLAR_OF_AUTUMN,
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {HALO}",
        f"{ROOM_MOVE} {HALO}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM}, {KARTOGRAF}, {THE_PILLAR_OF_AUTUMN})",
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (NEEDLER_2, PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} {NEEDLER_2}", ITEM_TAKE_TEXT,
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, NEEDLER_2)
    ),
    ScenarioStep(tsBAG_FULL, f"{PICK_UP} {PLASMA_PISTOL_2}", BAG_FULL,
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, NEEDLER_2)
    ),
    ScenarioStep(tsEND, END, GAME_END,
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, NEEDLER_2)
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
            WRONG_ARGUMENT,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS0_WrongCond, OVERVIEW,
            "V tuto chvíli nelze zobrazit přehled",
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS0_WrongCond, END_TALK,
            END_TALK_WRONG_COND,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS1_WRONG_ARG, f"{TALK} R39OWTJR",
            WRONG_ARGUMENT,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS1_WrongCond, f"{TALK} {FLOOD_2}",
            "Tuto věc/postavu nelze oslovit",
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS1_0Args, TALK, MISSING_ARGUMENT,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS1_WrongCond, f"{OPEN} {HALO}",
            OPEN_WRONG_COND,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS1_0Args, OPEN, MISSING_ARGUMENT,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS2_WrongCond,
            f"{USE} {SHIELD_GENERATOR_2} {NEEDLER_2}", WRONG_ITEM_TARGET,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS2_1Args, f"{USE} {SHIELD_GENERATOR_2}",
            MISSING_ARGUMENT,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS2_WRONG_2ndARG,
            f"{USE} {SHIELD_GENERATOR_2} {FLOOD_2}", WRONG_ITEM_TARGET,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
        ),
        ScenarioStep(tsNS2_WRONG_1stARG, f"{USE} {FLOOD_2} já",
            UNUSEABLE_ITEM,
            CONTROL_ROOM,
            (HALO, LAB),
            (NEEDLER_2, FLOOD_2),
            (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
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
        (HALO,),
        (AR_2, JACOB_KEYES_2, ),
        (PISTOL_2, SHIELD_GENERATOR_2, ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {HALO}",
        f"{ROOM_MOVE} {HALO}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM}, {KARTOGRAF}, {THE_PILLAR_OF_AUTUMN})",
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (NEEDLER_2, PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {CONTROL_ROOM}",
        f"{ROOM_MOVE} {CONTROL_ROOM}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({HALO}, {LAB})",
        CONTROL_ROOM,
        (HALO, LAB),
        (NEEDLER_2, FLOOD_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {LAB}",
        f"{ROOM_MOVE} {LAB}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM},)",
        LAB,
        (CONTROL_ROOM,),
        (PLASMA_PISTOL_2, LIBRARY_KEY_2, ELITE_2),
        (PISTOL_2, SHIELD_GENERATOR_2,)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} {LIBRARY_KEY_2}",
        ITEM_TAKE_TEXT,
        LAB,
        (CONTROL_ROOM,),
        (PLASMA_PISTOL_2, ELITE_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {CONTROL_ROOM}",
        f"{ROOM_MOVE} {CONTROL_ROOM}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({HALO}, {LAB})",
        CONTROL_ROOM,
        (HALO, LAB),
        (NEEDLER_2, FLOOD_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {HALO}",
        f"{ROOM_MOVE} {HALO}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({CONTROL_ROOM}, {KARTOGRAF}, {THE_PILLAR_OF_AUTUMN})",
        HALO,
        (CONTROL_ROOM, KARTOGRAF, THE_PILLAR_OF_AUTUMN),
        (NEEDLER_2, PLASMA_PISTOL_2, GRUNT_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} {KARTOGRAF}",
        f"{ROOM_MOVE} {KARTOGRAF}\n\n"
        f"{NEIGHBOURING_ROOMS_TEXT}\n"
        f"({LIBRARY}, {HALO})",
        KARTOGRAF,
        (LIBRARY, HALO),
        (CARBINE_2, FORERUNNER_2),
        (PISTOL_2, SHIELD_GENERATOR_2, LIBRARY_KEY_2)
    ),
    ScenarioStep(tsEND, END, GAME_END,
        KARTOGRAF,
        (LIBRARY, HALO),
        (),
        (PISTOL_2, SHIELD_GENERATOR_2, CARBINE_2, LIBRARY_KEY_2)
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
