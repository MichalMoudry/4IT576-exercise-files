"""
Modul obsahující definici třídy Action.
"""

from .anamed import ANamed
from typing import Callable

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