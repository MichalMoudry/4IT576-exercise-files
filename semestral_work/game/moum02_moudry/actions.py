#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul reprezentuje správce akcí, který řídí celkové chování
v závislosti na tom, je-li hra právě aktivní a rozhoduje,
která akce dostane na starost zpracování aktuálního příkazu.
Současně obsahuje definice všech akcí.
"""

import dbg
dbg.start_mod(0, __name__)
############################################################################

#from abc import ABC, abstractmethod

from .world import current_place
from .classes.bag import BAG
from .classes.action import Action

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
            return WELCOME_MESSAGE

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

def goto(arguments:tuple[str]) -> str:
    """Přesune hráče do zadaného sousedního prostoru.
    """
    from . import world as w
    dest_name = arguments[1].lower()
    dest_place = w._current_place.name2neighbor.get(dest_name.lower())
    if dest_place:
        w._current_place = dest_place
        return (
            f"{ROOM_MOVE} {dest_place}\n\n"
            f"{NEIGHBOURING_ROOMS_TEXT}\n{w._current_place.neighbors}"
        )
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
        return f"{ITEM_TAKE_TEXT} ({item_name})"
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
    result = "Příkazy, které lze zadat:\n"
    for action in _NAME_2_ACTION:
        result += f"- {action}{_ACTION_ARGUMENTS[action]}\n"
    result = result.strip()
    return result

def end(arguments:tuple[str]) -> str:
    """Ukončí hru a poděkuje hráči za htu.
    """
    raise Exception(f'Ještě není plně implementováno')


############################################################################

def ns0(arguments:tuple[str]) -> str:
    """
    Nestandardní akce č. 0.
    """
    raise Exception(f'Ještě není plně implementováno')

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
    OVERVIEW : Action(OVERVIEW, "", ns0),
    OPEN : Action(OPEN, "", ns1),
    PUT_DOWN : Action(PUT_DOWN, "", put),
    USE : Action(USE, "", ns2),
    HELP : Action(HELP, "", help),
    TALK : Action(TALK, "", ns3),
    END_TALK : Action(END_TALK, "", ns4),
    END : Action(END, "", end),
}

_ACTION_ARGUMENTS = {
    MOVE : " [místo]",
    PICK_UP : " [věc]",
    OVERVIEW : "",
    OPEN : " [místnost]",
    PUT_DOWN : " [věc]",
    USE : " [věc] [cíl]",
    HELP : "",
    TALK : " [osoba]",
    END_TALK : "",
    END : "",
}


############################################################################
dbg.stop_mod(0, __name__)
