#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul má na starosti řízení hry a komunikaci s uživatelem.
Je schopen akceptovat zadávané příkazy a poskytovat informace
o průběžném stavu hry a jejích součástí.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api import BasicActions

from .classes.bag import Bag
from .actions import Action

from . import world, actions

############################################################################

def is_alive() -> bool:
    """Vrátí informaci o tom, je-li hra aktuálně spuštěná.
    Spuštěnou hru není možno pustit znovu.
    Chceme-li hru spustit znovu, musíme ji nejprve ukončit.
    """
    raise Exception(f'Ještě není plně implementováno')


def execute_command(command:str) -> str:
    """Zpracuje zadaný příkaz a vrátí text zprávy pro uživatele.
    """
    return actions.execute_command(command)


def stop() -> None:
    """Ukončí hru a uvolní alokované prostředky.
    Zadáním prázdného příkazu lze následně spustit hru znovu.
    """
    raise Exception(f'Ještě není plně implementováno')


def all_actions() -> tuple[Action]:
    """Vrátí n-tici všech akcí použitelných ve hře.
    """
    result = tuple(actions._NAME_2_ACTION.values())
    return result


def basic_actions() -> BasicActions:
    """Vrátí přepravku s názvy povinných akcí.
    """
    raise Exception(f'Ještě není plně implementováno')


def bag() -> Bag:
    """Vrátí odkaz na batoh, do nějž bude hráč ukládat sebrané objekty.
    """
    from . import world as w
    return w.BAG


def world() -> 'IWorld':
    """Vrátí odkaz na svět hry.
    """
    from . import world as w
    return w



############################################################################
dbg.stop_mod(0, __name__)
