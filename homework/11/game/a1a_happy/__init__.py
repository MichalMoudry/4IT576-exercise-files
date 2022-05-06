#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/game/a1a_happy/__init__.py
"""
Balíček s modulem scenarios definujícím šťastný scénář.
"""
import dbg; dbg.start_pkg(1, __name__, __doc__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'A1A'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
# tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
# u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
# Má-li autor programu více křestních jmen, může je uvést všechna.
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



###########################################################################q

def all_scenarios() -> tuple['Scenario']:
    """Vrátí n-tici definovaných scénářů.
    """
    from   .  import scenarios
    result = scenarios.SCENARIOS
    return result


def game() -> 'IGame':
    """Vrátí odkaz na objekt reprezentující hru.
    """
    raise Exception(f'Ještě není plně implementováno')



###########################################################################q

def self_test():
    """Otestuje aktuální stav projektu.
    """
    from importlib import import_module
    me = import_module(__package__)   # Importuje modul svého balíčku

    from game.tests import Level, test
    test(me, Level.HAPPY)   # Testuje definici šťastného scénáře

# Test spustíte zadáním příkazů
# import game.a1a_happy as at; at.self_test()



###########################################################################q
dbg.stop_pkg(0, __name__)
