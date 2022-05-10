#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul vystupuje v roli správce světa hry a jeho prostorů.
Má na starosti vzájemné propojení jednotlivých prostorů
a udržuje informaci o tom, ve kterém z nich se hráč právě nachází.
Vzájemné uspořádání prostorů se může v průběhu hry měnit –
prostory mohou v průběhu hry získávat a ztrácet sousedy.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

# Nemazat import BAG
from .place import Place, _NAME_2_PLACE, BAG

############################################################################

def initialize() -> None:
    """Inicializuje svět hry, tj. nastavuje vzájemné počáteční
    propojení jednotlivých prostorů a jejich výchozí obsah,
    nastaví výchozí aktuální prostor a inicializuje batoh.
    """
    for place in _NAME_2_PLACE.values():
        place.initialize()
    global _current_place
    _current_place = _NAME_2_PLACE["the_pillar_of_autumn"]
    


def current_place() -> Place:
    """Vrátí odkaz na aktuální prostor,
    tj. na prostor, v němž se hráč pravé nachází.
    """
    return _current_place


def places() -> tuple[Place]:
    """Vrátí n-tici odkazů na všechny prostory ve hře
    včetně těch aktuálně nedosažitelných či neaktivních.
    """
    raise Exception(f'Ještě není plně implementováno')


def place(name:str) -> Place:
    """Vrátí prostor se zadaným názvem.
    Pokud ve hře takový není, vrátí None.
    """
    return _NAME_2_PLACE.get(name)



############################################################################
# Aktuální prostor = prostor, v němž se hráč právě nachází
_current_place:Place



############################################################################
dbg.stop_mod(0, __name__)
