"""
Modul obsahující definici třídy Item.
"""

from .anamed import ANamed
from .item_constants import *

HEAVY_PREFIX = '#'

UNMOVABLE_ITEM_WEIGHT = 3000

class Item(ANamed):
    """Instance představují h-objekty v prostorech či batohu.
    """

    def __init__(self, name:str, **args):
        """Vytvoří h-objekt se zadaným názvem.
        """
        if not name:
            raise Exception("Nepovolená hodnota názvu objektu")
        super().__init__(name[1:], **args)
        self._weight = (
            UNMOVABLE_ITEM_WEIGHT if name[0] == HEAVY_PREFIX else 1
        )


    @property
    def weight(self) -> int:
        """Vrátí váhu daného objektu.
        """
        return self._weight

TALKABLE:tuple[str] = (JACOB_KEYES_2, )
USEABLE:tuple[str] = (SHIELD_GENERATOR_2, INDEX_2,)
TARGETABLE:tuple[str] = (GRUNT_2, FLOOD_2, ELITE_2, FORERUNNER_2,
COVENANT_2, ARBITER_2)