#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul deklaruje metody požadované od modulů odevzdávaných jako
realizace konkrétní hry. Tyto metody mají za úkol identifikovat autora
a zprostředkovat komunikaci s klíčovými objekty dané aplikace.
"""
import dbg
dbg.start_mod(0, __name__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'Ještě není plně implementováno'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
# tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
# u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
# Má-li autor programu více křestních jmen, může je uvést všechna.
AUTHOR_NAME = 'Ještě není plně implementováno'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
# zapsané v jeho/jejím rodném jazyce
AUTHOR_ORIG_NAME = 'Ještě není plně implementováno'

# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
Zadání z předmětu 4IT111
"""

# Problémy, které se vyskytly při zpracování probrané látky a řešení DU
PROBLEMS = """\
Vyjmutí z balíčku
"""

# Poznámky a připomínky k výkladu
COMMENTS = """\
Žádné
"""



###########################################################################q

def all_scenarios() -> tuple['Scenario']:
    """Vrací n-tici všech definovaných scénářů v určeném pořadí.
    """
    raise Exception(f'Ještě není plně implementováno')


def game() -> 'IGame':
    """Vrátí odkaz na objekt reprezentující hru.
    Tento objekt musí implementovat protokol game.api.interfaces.IGame.
    """
    raise Exception(f'Ještě není plně implementováno')



###########################################################################q
dbg.stop_mod(0, __name__)
