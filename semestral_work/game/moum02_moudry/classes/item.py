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
        self._weight = 3000 if is_heavy else 1


    @property
    def weight(self) -> int:
        """Vrátí váhu daného objektu.
        """
        return self._weight