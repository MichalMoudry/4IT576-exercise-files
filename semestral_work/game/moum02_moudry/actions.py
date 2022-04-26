#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul reprezentuje správce akcí, který řídí celkové chování
v závislosti na tom, je-li hra právě aktivní a rozhoduje,
která akce dostane na starost zpracování aktuálního příkazu.
Současně obsahuje definice všech akcí.
"""
from typing import Callable

import dbg
dbg.start_mod(0, __name__)
############################################################################

from abc import ABC, abstractmethod

from .world import ANamed, current_place, BAG

from .constants.actions_constants import *
from .constants.text_constants import *

############################################################################

def execute_command(command:str) -> str:
    """Zpracuje zadaný příkaz a vrátí odpověď hry.
    Zadaný příkaz zanalyzuje a v závislosti na aktuální aktivitě hry
    rozhodne, která akce dostane na starost jeho zpracování.
    Vrátí odpověď hry na zadaný příkaz.
   """
    command = command.strip()
    if command:
        if is_alive():
            command_parts = command.split()
            action_name = command_parts[0].lower()
            if action_name in _NAME_2_ACTION:
                return _NAME_2_ACTION[action_name]._execute(command_parts)
            else:
                return UNKNOWN_COMMAND
        else:
            # Hra neběží
            return ("Prvním příkazem není startovací příkaz.\n" 
                    "Hru, která neběží, lze spustit pouze "
                    "startovacím příkazem.\n")
    else:
        if is_alive():
            return EMPTY_COMMAND
        else:
            _start_game()
            return (
            'Vítejte ve hře Halo, kdy vaším cílem je se dostat do místnosti'
            ' "The Maw",\npřičemž pro úspěšné dokončení hry je třeba donést'
            ' tzv. Index a použít ho\n na postavu Arbiter, který se nachází'
            ' v zamčené knihovně, tedy je třeba\nknihovnu odemknouta sebrat'
            ' Index do batohu.\n\nPro zobrazení'
            ' nápovědy je třeba zadat příkaz: ?.'
            )

def _start_game() -> None:
    """
    Funkce pro odstartování hry.
    """
    from . import world
    world.initialize()

    global _is_alive
    _is_alive = True
    

def is_alive() -> bool:
    """Vrátí informaci o tom, je-li hra živá = aktuálně spuštěná.
    Spuštěnou hru není možno pustit znovu.
    Chceme-li hru spustit znovu, musíme ji nejprve ukončit.
    """
    return _is_alive


def _initialize():
    """V rámci startu hry inicializuje všechny potřebné objekty.
    """
    raise Exception(f'Ještě není plně implementováno')



############################################################################

class Action(ANamed):
    """Společná rodičovská třída všech akcí.
    """

    def __init__(self, name:str, description:str,
                       execute:Callable[[list[str]], str]):
        """Vytvoří rodičovský podobjekt dané akce, který si zapamatuje
        název dané akce a její popis.
        """
        super().__init__(name)
        self._description = description
        self._execute = execute


    @property
    def description(self) -> str:
        """Vrátí popis příkazu s vysvětlením jeho funkce,
        významu jednotlivých parametrů a možností (resp. účelu) použití
        daného příkazu. Tento popis tak může sloužit jako nápověda
        k použití daného příkazu.
        """
        return self._description


    @property
    def execute(self, arguments:tuple[str]) -> str:
        """Metoda realizující reakci hry na zadání daného příkazu.
        Předávané pole je vždy neprázdné, protože jeho nultý prvek
        je zadaný název vyvolaného příkazu. Počet argumentů je závislý
        na konkrétním akci, ale pro každou akci je konstantní.
        """
        return self._execute(arguments)



############################################################################

def goto(arguments:tuple[str]) -> str:
    """Přesune hráče do zadaného sousedního prostoru.
    """
    from . import world as w
    dest_name = arguments[1].lower()
    dest_place = w._current_place.name2neighbor.get(dest_name.lower())
    if dest_place:
        w._current_place = dest_place
        return ""
    else:
        return WRONG_NEIGHBOUR


def take(arguments:tuple[str]) -> str:
    """Přesune zadaný objekt z aktuálního prostoru do batohu.
    """
    curr_place = current_place()
    item_name = arguments[1]
    item = curr_place.item(item_name)
    if item:
        curr_place.remove_item(item_name)
        BAG.add_item(item)
        return ""
    else:
        return OBJECT_NOT_PRESENT


def put(self, arguments:tuple[str]) -> str:
    """Přesune zadaný objekt z batohu do aktuálního prostoru.
    """
    raise Exception(f'Ještě není plně implementováno')


def help(arguments:tuple[str]) -> str:
    """Vrátí text jednoduché nápovědy popisující
    všechny dostupné příkazy.
    """
    result = ""
    for action in _NAME_2_ACTION:
        ...

def end(arguments:tuple[str]) -> str:
    """Ukončí hru a poděkuje hráči za htu.
    """
    raise Exception(f'Ještě není plně implementováno')


############################################################################

def ns1(arguments:tuple[str]) -> str:
    """Nestandardní akce číslo 1.
    """
    raise Exception(f'Ještě není plně implementováno')


def ns2(arguments:tuple[str]) -> str:
    """Nestandardní akce číslo 1.
    """
    raise Exception(f'Ještě není plně implementováno')


def ns3(arguments:tuple[str]) -> str:
    """Nestandardní akce číslo 1.
    """
    raise Exception(f'Ještě není plně implementováno')


def ns4(arguments:tuple[str]) -> str:
    """Nestandardní akce číslo 1.
    """
    raise Exception(f'Ještě není plně implementováno')



############################################################################
_is_alive = False
_NAME_2_ACTION = {
    MOVE : Action(MOVE, "", goto),
    PICK_UP : Action(PICK_UP, "", take),
    OVERVIEW : Action(OVERVIEW, "", put),
    OPEN : Action(OPEN, "", None),
    PUT_DOWN : Action(PUT_DOWN, "", None),
    USE : Action(USE, "", None),
    HELP : Action(HELP, "", help),
    TALK : Action(TALK, "", None),
    END_TALK : Action(END_TALK, "", None),
    END : Action(END, "", end),
}


############################################################################
dbg.stop_mod(0, __name__)
