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
AUTHOR_NAME = 'Moudrý Michal'

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
    ScenarioStep(tsSTART, '',                       # Zadaný příkaz
        'Uvítací zpráva popisující základní informace o cíli hry,\n'
        'způsobu, jak jej dosáhnout, a příkazu k získání nápovědy.',
        'Výchozí_prostor',                          # Aktuální prostor
        ('Aktuální', 'sousedé',),                   # Aktuální sousedé
        ('Objekty', 'v', 'prostoru', ),             # H-objekty v prostoru
        ('Objekty', 'v', 'batohu', ),               # H-Objekty v batohu
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
