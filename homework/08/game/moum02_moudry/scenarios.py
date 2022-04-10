#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Základní čtveřice scénářů pro hru inspirovanou pohádkou o Červené Karkulce.
"""
import dbg;dbg.start_mod(0, __name__)
############################################################################

from ..api.scenario   import ScenarioStep, Scenario
from ..api.scen_types import *  # Především typu kroků

############################################################################
# Pomocné konstanty
MOVE = "jdi"
PICK_UP = "zvedni"
OVERVIEW = "přehled"
OPEN = "otevři"
PUT_DOWN = "polož"
USE = "použij"
HELP = "?"
TALK = "oslov"
END_TALK = "ukončit_rozhovor"

############################################################################

############################################################################
# Základní úspěšný scénář demonstrující průběh hry, při němž hráč
# nezadává žádné chybné příkazy a dosáhne zadaného cíle.
HAPPY = Scenario('', stHAPPY, (
    START_STEP := ScenarioStep(tsSTART, '', # Zadaný příkaz
        'Vítejte ve hře Halo, kdy vaším cílem je se dostat do místnosti'
        ' "The Maw",\npřičemž pro úspěšné dokončení hry je třeba donést'
        ' tzv. Index a použít ho\n na postavu Arbiter, který se nachází'
        ' v zamčené knihovně, tedy je třeba\nknihovnu odemknouta sebrat'
        ' Index do batohu.\n\nPro zobrazení'
        ' nápovědy je třeba zadat příkaz: ?.',
        'The_Pillar_of_Autumn', # Aktuální prostor
        ('Halo',), # Aktuální sousedé
        ('Assault_Rifle', 'Jacob_Keyes', ), # H-objekty v prostoru
        ('Pistole', 'generátor_štítu', ), # H-Objekty v batohu
    ),
    ScenarioStep(tsNS_1, f"{TALK} jacob_keyes",
        "Pokoušíte se zeptat objektu Jacob_Keyes. Jaký je váš dotaz?",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole', 'generátor_štítu',),
    ),
    ScenarioStep(tsNS_0, END_TALK,
        "Rozhovor byl úspěšně ukončen.",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole', 'generátor_štítu',),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Laboratoř",
        "Proběhl přesun na: Laboratoř\n"
        "Sousedící místnosti: kontrolní_místnost_prstence",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Klíč_ke_knihovně",
        "Předmět byl zvednut",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "[Elite]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
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
        "Proběhl přesun na: Kartograf\nSousedící místnosti:\n"
        "Knihovna; Halo",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_1, f"{OPEN} knihovnu",
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
        "Proběhl přesun na: Knihovna\nSousedící místnosti:\n"
        "TRC; Kartograf",
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
        "Proběhl přesun na: TRC\nSousedící místnosti:\n"
        "The_Maw; Knihovna",
        "TRC",
        ("the_maw", "Knihovna"),
        ("[Grunt]", "[Covenant]"),
        ("Pistole", "generátor_štítu", "Index")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} the_maw",
        "Proběhl přesun na: The Maw\nSousedící místnosti:\nTRC",
        "the_maw",
        ("TRC", "Kartograf"),
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
    'Prvním příkazem není startovací příkaz.\n' 
    'Hru, která neběží, lze spustit pouze startovacím příkazem.\n',
    '',                                         # Aktuální prostor
    (),                                         # Aktuální sousedé
    (),                                         # H-objekty v prostoru
    (),                                         # H-Objekty v batohu
)

ScenarioStep.next_index = +1  # Index prvního kroku za startem

MISTAKE = Scenario('', stMISTAKES, (
    WRONG_START,
    START_STEP,
    ScenarioStep(tsHELP, HELP, "Příkazy, které lze zadat:\n"
        "- jdi [místo]\n- zvedni [věc]\n- polož [věc]\n- oslov [osoba]\n"
        "-ukončit_rozhovor\n- přehled\n- otevři [místnost]\n"
        "- použij [věc] [cíl]\n",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsEMPTY, "", "Prázdný příkaz",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsUNKNOWN, "přines", "Neznámý příkaz",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsBAD_ITEM, f"{PICK_UP} Index",
        "Objekt není v této místnosti",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsBAD_NEIGHBOR, f"{MOVE} TRC", "Místo není sousedem",
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
    ScenarioStep(tsMOVE_WA, MOVE, "Příkazu chybí požadované parametry",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsPUT_DOWN_WA, PUT_DOWN, "Příkazu chybí požadované parametry",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
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
    ),
)



############################################################################

ScenarioStep.next_index = +1  # Index prvního kroku za startem

REQUIRED = Scenario('REQUIRED', stREQUIRED, (
    START_STEP,
    ScenarioStep(tsHELP, HELP, "Příkazy, které lze zadat:\n"
        "- jdi [místo]\n- zvedni [věc]\n- polož [věc]\n- oslov [osoba]\n"
        "-ukončit_rozhovor\n- přehled\n- otevři [místnost]\n"
        "- použij [věc] [cíl]\n",
        "The_Pillar_of_Autumn",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", ),
        ("Pistole", "generátor_štítu", ),
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Laboratoř",
        "Proběhl přesun na: Laboratoř\n"
        "Sousedící místnosti: kontrolní_místnost_prstence",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]"),
        ("Pistole", "generátor_štítu",)
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Klíč_ke_knihovně",
        "Předmět byl zvednut",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "[Elite]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, f"{MOVE} Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, f"{MOVE} Kartograf",
        "Proběhl přesun na: Kartograf\nSousedící místnosti:\n"
        "Knihovna; Halo",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_1, f"{OPEN} knihovnu",
        "Místnost (knihovna) byla otevřena",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} Knihovna",
        "Proběhl přesun na: Knihovna\nSousedící místnosti:\n"
        "TRC; Kartograf",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole", "Index"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsTAKE, f"{PICK_UP} Index",
        "Předmět (Index) byl zvednut",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole",),
        ("Pistole", "generátor_štítu", "Index", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} TRC",
        "Proběhl přesun na: TRC\nSousedící místnosti:\n"
        "The_Maw; Knihovna",
        "TRC",
        ("the_maw", "Knihovna"),
        ("[Grunt]", "[Covenant]"),
        ("Pistole", "generátor_štítu", "Index", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, f"{MOVE} the_maw",
        "Proběhl přesun na: The Maw\nSousedící místnosti:\nTRC",
        "the_maw",
        ("TRC", "Kartograf"),
        ("[Arbiter]",),
        ("Pistole", "generátor_štítu", "Index", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_2, f"{USE} Index [Arbiter]",
        "Předmět (Index) byl použit na [Arbiter]",
        "the_maw",
        ("TRC", "Kartograf"),
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
