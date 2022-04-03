#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul deklaruje metody požadované od modulů odevzdávaných jako
realizace konkrétní hry. Tyto metody mají za úkol identifikovat autora
a zprostředkovat komunikaci s klíčovými objekty dané aplikace.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

def authorID() -> str:
    """Vrátí identifikační řetězec autora/autorky programu
    zapsaný VELKÝMI PÍSMENY.
    Tímto řetězcem bývá login do informačního systému školy.
    """
    raise Exception(f'Ještě není plně implementováno')


def authorName() -> str:
    """Vrátí jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
    tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
    u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
    Má-li autor programu více křestních jmen, může je uvést všechna.
    """
    raise Exception(f'Ještě není plně implementováno')


def authorOrigName() -> str:
    """Vrátí jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
    zapsané v jeho/jejím rodném jazyce.
    """
    raise Exception(f'Ještě není plně implementováno')


def all_scenarios() -> tuple['Scenario']:
    """Vrátí n-tici definovaných scénářů.
    """
    raise Exception(f'Ještě není plně implementováno')


def game() -> 'IGame':
    """Vrátí odkaz na objekt reprezentující hru.
    Tímto objektem je modul definující komunikační funkce hry
    """
    raise Exception(f'Ještě není plně implementováno')



############################################################################
dbg.stop_mod(0, __name__)
