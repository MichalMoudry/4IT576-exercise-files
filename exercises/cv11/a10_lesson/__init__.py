#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Balíček s poloprázdnými moduly tvořícími zárodek aplikace¤
a definujícími její základní architekturu a API.
Moduly obsahují všechny atributy definované v odpovídajících protokolech.

Oproti minulé verzi přibylo:
- Poloprázdné moduly definující základní architekturu a API.
"""
import dbg; dbg.start_pkg(0, __name__, __doc__)
############################################################################

# Následující moduly je třeba importovat až při spuštění kontroly typů
# from ..api.scenario import Scenario
# from ..api.game_types import IGame


############################################################################

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'A0C'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
# tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
# u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
# Má-li autor programu více křestních jmen, může je uvést všechna.
AUTHOR_NAME = 'LESSON Current'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
# zapsané v jeho/jejím rodném jazyce
AUTHOR_ORIG_NAME = 'LEKCE Průběžné'


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
    """Vrátí správně seřazenou n-tici definovaných scénářů.
    """
    from   .  import scenarios
    result = scenarios.SCENARIOS
    return result


def game() -> 'IGame':
    """Vrátí odkaz na objekt reprezentující hru.
    Tímto objektem je modul definující komunikační funkce hry
    """
    from . import main
    return main



############################################################################

def self_test():
    """Otestuje aktuální stav projektu.
    """
    from importlib  import import_module
    me = import_module(__package__)
    from ..tests    import test
    from ..tests    import Level
    test(me, Level.START)    # Testuje korespondenci s návrhem
        # architektury, tj. deklaraci navržených modulů a jejich atributů

# Test spustíte zadáním příkazů
# import game.a1c_architecture as at; at.self_test()



###########################################################################q
dbg.stop_mod(0, __name__)
