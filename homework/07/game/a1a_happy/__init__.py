#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Balíček s modulem scenarios definujícím šťastný scénář.
"""
import dbg
dbg.start_pkg(0, __name__, __doc__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'A1A'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
AUTHOR_NAME = 'HAPPY Křestní'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
# zapsané v jeho/jejím rodném jazyce
AUTHOR_ORIG_NAME = 'ŠŤASTNÝ Scénář'


# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
???
"""

# Problémy, které se vyskytly při zpracování probrané látky a řešení DU
PROBLEMS = """\
???
"""

# Poznámky a připomínky k výkladu
COMMENTS = """\
???
"""



############################################################################

def all_scenarios() -> tuple['Scenario']:
    """Vrátí n-tici definovaných scénářů.
    """
    from   .  import scenarios
    result = scenarios.SCENARIOS
    return result


def game() -> 'IGame':
    """Vrátí odkaz na objekt reprezentující hru.
    Tímto objektem je modul definující komunikační funkce hry
    """
    raise Exception(f'Funkce ještě není plně implementována')



############################################################################

def test_yourself():
    """Otestuje aktuální stav projektu.
    """
    from importlib import import_module
    me = import_module(__package__)
    from ..tests   import test
    from ..tests   import Level
    test(me, Level.HAPPY)   # Testuje definici šťastného scénáře

# Test spustíte zadáním příkazů
# import game.a1a_happy as at; at.test_yourself()



############################################################################
dbg.stop_pkg(0, __name__)
