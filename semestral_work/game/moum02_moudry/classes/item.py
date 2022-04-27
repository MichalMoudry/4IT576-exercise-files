"""
Modul obsahující definici třídy Item.
"""

from .abstract.anamed import ANamed

class Item(ANamed):
    """Instance představují h-objekty v prostorech či batohu.
    """

    def __init__(self, name:str, is_heavy:bool = False, **args):
        """Vytvoří h-objekt se zadaným názvem.
        """
        if not name:
            raise Exception("Nepovolená hodnota názvu objektu")
        super().__init__(name, **args)
        self._is_heavy = is_heavy


    @property
    def weight(self) -> int:
        """Vrátí váhu daného objektu.
        """
        return self._weight
    
    @property
    def is_heavy(self) -> bool:
        """
        Vrátí informaci, zda je předmět těžký.
        """
        return self._is_heavy