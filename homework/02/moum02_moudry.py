#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_00a_module_template.py
"""
Co se týče hlavního zdroje o doposud probíraných tématech,
tak se jedno o materiály, jež jsem využíval při tom, kdy
jsem se učil programovat v jiných jazycích.

Co se týče pasáží, které mi dělaly problém, tak zatím jsem
s žádným tématem neměl problém.
"""
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
    return k

def put_left(k:Karel) -> Karel:
    """Funkce, která realizuje se zadaným robotem
položení značky na políčko vlevo od zadaného robota
a vrátí odkaz na svůj argument."""
    return k

def my_function_2(k:Karel) -> Karel:
    """Funkce, která se zadaným robotem provede vámi
navrženou činnost a vrátí odkaz na svůj argument."""
    return k

print(author_name(), author_id())

###########################################################################q
dbg.stop_mod(1, __name__)
