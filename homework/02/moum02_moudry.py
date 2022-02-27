#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_00a_module_template.py
"""
Zdroje: prezentace z hodiny

Problémy: žádné

Připomínky: žádné
"""
import dbg; dbg.start_mod(1, __name__)
from robotcz import *
###########################################################################q

# Tělo modulu
def author_name() -> str:
    """
    Funkce, která vrátí jméno autora.
    """
    return "MOUDRÝ Michal"

def author_id() -> str:
    """
    Funkce, která vrátí identifikační řetězec autora.
    """
    return "MOUM02"

def step_back(k:Karel) -> Karel:
    """
    Funkce, která realizuje se zadaným robotem
    krok vzad a vrátí odkaz na svůj argument.

    Pokud je za robotem zeď či jiný robot, tak
    je ohlášena chyba.
    """
    turn_left(k)
    turn_left(k)
    step(k)
    return k

def put_left(k:Karel) -> Karel:
    """
    Funkce, která realizuje se zadaným robotem
    položení značky na políčko vlevo od zadaného robota
    a vrátí odkaz na svůj argument.

    Pokud je vlevo od robota zeď nebo jiný robot, tak je
    ohlášena chyba.
    
    Dále pokud celkový počet značek na daném políčku přesáhne
    maximální povolený počet, tak je ohlášena chyba.
    """
    turn_left(k)
    step(k)
    put(k)
    step_back(k)
    turn_left(k)
    return k

def my_function_2(k:Karel) -> Karel:
    """
    Funkce, která realizuje se zadaným robotem otočení
    doleva, následný posun o jedno políčko, zvednutí značky,
    vrácení zpět na původní pozici a položení značky na pozici.

    Ve výsledku jde o vyjmutí značky, která je vlevo od robota a
    její vložení na původní pozici.

    Pokud je vlevo od robota zeď nebo jiný robot, tak je
    ohlášena chyba.

    Dále pokud na políčku vlevo od robota není žádná značka, tak
    je ohlášena chyba.

    Také pokud je na původním políčku maximální počet značek, tak
    je ohlášena chyba.
    """
    turn_left(k)
    step(k)
    pick(k)
    step_back(k)
    put(k)
    return k

###########################################################################q
dbg.stop_mod(1, __name__)
