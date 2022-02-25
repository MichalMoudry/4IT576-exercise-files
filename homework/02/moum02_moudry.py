#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_00a_module_template.py
"""
Co se týče hlavního zdroje o doposud probíraných tématech,
tak se jedno o materiály, jež jsem využíval při tom, kdy
jsem se učil programovat v jiných jazycích.

Co se týče pasáží, které mi dělaly problém, tak zatím jsem
s žádným tématem neměl problém.
"""
from cmath import pi
import dbg; dbg.start_mod(1, __name__)
from robotcz import *
###########################################################################q

# Tělo modulu
def author_name() -> str:
    """Funkce, která vrátí jméno autora."""
    return "MOUDRÝ Michal"

def author_id() -> str:
    """Funkce, která vrátí identifikační řetězec autora."""
    return "MOUM02"

def step_back(k:Karel) -> Karel:
    """Funkce, která realizuje se zadaným robotem
krok vzad a vrátí odkaz na svůj argument."""
    turn_left(k)
    turn_left(k)
    step(k)
    return k

def put_left(k:Karel) -> Karel:
    """Funkce, která realizuje se zadaným robotem
položení značky na políčko vlevo od zadaného robota
a vrátí odkaz na svůj argument."""
    turn_left(k)
    step(k)
    put(k)
    step_back(k)
    return k

def my_function_2(k:Karel) -> Karel:
    """Funkce, která realizuje se zadaným robotem otočení
    doleva, následný posun o jedno políčko, zvednutí značky,
    vrácení zpět na původní pozici a položení značky na pozici.
    Ve výsledku jde o vyjmutí značky, která je vlevo od robota."""
    turn_left(k)
    step(k)
    pick(k)
    step_back(k)
    put(k)
    return k

"""
new_world("0123456789", " .:…∷…:. #")
k = Karel()
step(k)
my_function_2(k)
input("Press Enter to exit...")
"""

###########################################################################q
dbg.stop_mod(1, __name__)
