#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Definice šťastného scénáře vlastní hry vyhovující
požadavkům zadaným na stránce předmětu.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'MOUM02'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
AUTHOR_NAME = 'MOUDRÝ Michal'

# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
Prezentace
"""

# Problémy, které se vyskytly při zpracování probrané látky a řešení DU
PROBLEMS = """\
Žádné
"""

# Poznámky a připomínky k výkladu
COMMENTS = """\
Žádné
"""

def all_scenarios() -> tuple['Scenario']:
    """Vrací n-tici všech definovaných scénářů v určeném pořadí.
    """
    return SCENARIOS


###########################################################################q
# Importy

from game.api.scenario   import ScenarioStep, Scenario
from game.api.scen_types import *  # Především typu kroků

############################################################################
# Základní úspěšný scénář demonstrující průběh hry, při němž hráč
# nezadává žádné chybné příkazy a dosáhne zadaného cíle.
HAPPY = Scenario('', stHAPPY, (
    START_STEP :=
    ScenarioStep(tsSTART, '', # Zadaný příkaz
        'Vítejte ve hře Halo, kdy vaším cílem je se dostat do místnosti'
        ' "The Maw",\npřičemž pro úspěšné dokončení hry je třeba donést'
        ' tzv. Index, který se\nnachází v zamčené knihovně, tedy je třeba'
        ' knihovnu odemknout\na sebrat Index do batohu.\n\nPro zobrazení'
        ' nápovědy je třeba zadat příkaz: ?.',
        'The_Pillar_of_Autumn', # Aktuální prostor
        ('Halo',), # Aktuální sousedé
        ('Assault_Rifle', 'Jacob_Keyes', ), # H-objekty v prostoru
        ('Pistole', ), # H-Objekty v batohu
        ),
    ScenarioStep(tsNS_1, "oslov jacob_keyes",
        "Pokoušíte se zeptat objektu Jacob_Keyes. Jaký je váš dotaz?",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole',),
        ),
    ScenarioStep(tsNS_0, "ukončit_rozhovor",
        "Rozhovor byl úspěšně ukončen.",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole',),
        ),
    ScenarioStep(tsGOTO, "jdi Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("Kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole",)
    ),
    ScenarioStep(tsGOTO, "jdi kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole",)
    ),
    ScenarioStep(tsGOTO, "jdi Laboratoř",
        "Proběhl přesun na: Laboratoř\n"
        "Sousedící místnosti: kontrolní_místnost_prstence",
        "Laboratoř",
        ("kontrolní_místnost_prstence"),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]"),
        ("Pistole",)
    ),
    ScenarioStep(tsTAKE, "zvedni Klíč_ke_knihovně",
        "Předmět byl zvednut",
        "Laboratoř",
        ("kontrolní_místnost_prstence"),
        ("Plasma_pistol", "[Elite]"),
        ("Pistole", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, "jdi kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsGOTO, "jdi Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("Kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "Klíč_ke_knihovně")
    ),
    ScenarioStep(tsNS_0, "přehled",
        "---------- Přehled ----------\n"
        "- Obsah batohu: ('Pistole', 'Klíč_ke_knihovně')\n"
        "- Počet životů: 100\n"
        "- Velikost štítu: 150\n\n"
        "----- Postup -----\n"
        "- Máte klíč ke knihovně? Ano\n"
        "- Odemkli jste knihovnu? Ne\n",
        "Halo",
        ("Kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "Klíč_ke_knihovně")
        ),
    )
)



############################################################################

SCENARIOS = ( HAPPY,
            # MISTAKE,
            # MISTAKE_NS,
            # START,
            )



###########################################################################q
# Testy

def self_test():
    """Metoda testující právě definovanou sadu scénářů.
    """
    from importlib import import_module as im
    mod = im(__name__)

    from game.tests import test_scenario as ts
    ts.test_scenarios_from(mod)



###########################################################################q
dbg.stop_mod(1, __name__)
