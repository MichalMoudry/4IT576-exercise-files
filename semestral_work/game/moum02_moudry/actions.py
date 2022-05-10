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
from .bag import BAG, BAG_MAX_CAPACITY
from . import world
from .action import Action

from .actions_constants import *
from .text_constants import *

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
    if len(arguments) < 2:
        return COMMAND_MISSING_PARAMS
    dest_name = arguments[1].lower()
    dest_place = world._current_place.name2neighbor.get(dest_name.lower())
    if dest_place:
        if dest_place.is_locked:
            return ROOM_IS_LOCKED
        world._current_place = dest_place
        return (
            f"{ROOM_MOVE} {dest_place}\n\n"
            f"{NEIGHBOURING_ROOMS_TEXT}\n{world._current_place.neighbors}"
        )
    else:
        return WRONG_NEIGHBOUR


def take(arguments:tuple[str]) -> str:
    """Přesune zadaný objekt z aktuálního prostoru do batohu.
    """
    if len(arguments) < 2:
        return COMMAND_MISSING_PARAMS
    curr_place = current_place()
    item_name = arguments[1]
    item = curr_place.item(item_name)
    if item:
        if item.weight >= BAG_MAX_CAPACITY:
            return UNMOVABLE_ITEM
        curr_place.remove_item(item_name)
        if BAG.add_item(item):
            return f"{ITEM_TAKE_TEXT} ({item_name})"
        else:
            return BAG_FULL
    else:
        return OBJECT_NOT_PRESENT


def put(arguments:tuple[str]) -> str:
    """Přesune zadaný objekt z batohu do aktuálního prostoru.
    """
    if len(arguments) != 2:
        return COMMAND_MISSING_PARAMS
    item_name = arguments[1]
    item = BAG.item(item_name)
    if item:
        BAG.remove_item(item.name)
        current_place().add_item(item)
        return f"Věc ({item.name}) byla položena"
    else:
        return ITEM_NOT_IN_BAG


def help(arguments:tuple[str]) -> str:
    """Vrátí text jednoduché nápovědy popisující
    všechny dostupné příkazy.
    """
    res = [WELCOME_MESSAGE, "\n\n"]
    res.append("Příkazy, které lze zadat:\n")
    for action in _NAME_2_ACTION.values():
        res.append(f"- {action.name}{_ACTION_ARGUMENTS[action.name]}\n")
        res.append(f"    • {action.description}\n")
    return "".join(res)

def end(arguments:tuple[str]) -> str:
    """Ukončí hru a poděkuje hráči za hru.
    """
    global _is_alive
    _is_alive = False
    return GAME_END


############################################################################

def ns0(arguments:tuple[str]) -> str:
    """
    Nestandardní akce č. 0.
    """
    raise Exception(f'Ještě není plně implementováno')

def ns1(arguments:tuple[str]) -> str:
    """Nestandardní akce číslo 1.
    """
    # Chyba, když uživ nezadal druhý parametr
    if len(arguments) != 2:
        return COMMAND_MISSING_PARAMS
    place_name = arguments[1]
    place_name = place_name.lower()
    # Kontrola, jestli je potřebný klíč v batohu
    required_key_name = _ROOM_KEY_PAIRING[place_name]
    required_key = BAG.item(required_key_name)
    if required_key == None:
        return MISSING_KEY
    # Získání prostoru a pokus o jeho otevření
    place = world.place(place_name)
    if place == None:
        return OPEN_WRONG_COND
    if place.is_locked:
        place.is_locked = False
        return f"Místnost ({place_name}) byla otevřena"
    else:
        return OPEN_WRONG_COND


def ns2(arguments:tuple[str]) -> str:
    """Nestandardní akce číslo 1.
    """
    # TODO: Dokončit akci
    if len(arguments) != 3:
        return COMMAND_MISSING_PARAMS
    item_name = arguments[1]
    target = arguments[2]
    return f"Předmět ({item_name}) byl použit na {target}"


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
    MOVE : Action(MOVE, "Přesune hráče do specifikovaného prostoru", goto),
    PICK_UP : Action(PICK_UP, "Přidá určený předmět do batohu", take),
    OVERVIEW : Action(
        OVERVIEW, "Zobrazí přehled hráče a jeho průběhu", ns0
    ),
    OPEN : Action(
        OPEN,
        "Tento příkaz se pokusí o otevření předmětu nebo místnosti",
        ns1
    ),
    PUT_DOWN : Action(PUT_DOWN, "Položí předmět", put),
    USE : Action(USE, "Použije zadanou věc na určený cíl", ns2),
    HELP : Action(HELP, "Příkaz pro vyvolání nápovědy", help),
    TALK : Action(TALK, "Pokusí se o oslovení objektu v místnosti", ns3),
    END_TALK : Action(
        END_TALK, "Příkaz pro ukončení rozhovoru, pokud nějaký probíhá", ns4
    ),
    END : Action(END, "Tento příkaz ukončí hru", end),
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

_ROOM_KEY_PAIRING = {
    "knihovna" : "klíč_ke_knihovně"
}


############################################################################
dbg.stop_mod(0, __name__)
