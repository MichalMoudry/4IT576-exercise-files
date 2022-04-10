#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Balíček s modulem scenarios definujícím všechny čtyři povinné scénáře.¤

Oproti minulé verzi jsou definovány všechny čtyři povinné scénáře.
"""
import dbg; dbg.start_pkg(1, __name__, __doc__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'MOUM02'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
# tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
# u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
# Má-li autor programu více křestních jmen, může je uvést všechna.
AUTHOR_NAME = 'MOUDRÝ Michal'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
# zapsané v jeho/jejím rodném jazyce
AUTHOR_ORIG_NAME = 'MOUDRÝ Michal'


# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
Prezentace
"""

# Problémy, které se vyskytly při zpracování probrané látky a řešení DU
PROBLEMS = """\
Není mi kompletně zřejmé, jak funguje importovací systém Pythonu. 
Respektive nevím, jak fungují relativní importy.
"""

# Poznámky a připomínky k výkladu
COMMENTS = """\
Žádné
"""



###########################################################################q

def all_scenarios() -> tuple['Scenario']:
    """Vrátí správně seřazenou n-tici definovaných scénářů.
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
    test(me, Level.SCENARIOS)   # Testuje základní čtveřici scénářů

# Test spustíte zadáním příkazů
# import game.a1b_all as at; at.self_test()


############################################################################
dbg.stop_pkg(0, __name__)
