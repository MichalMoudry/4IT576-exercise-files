"""
Modul obsahující definici třídy Place.
"""

from .anamed import ANamed
from .aitemcontainer import AItemContainer
from .bag import BAG
from .item_constants import *

class Place(ANamed, AItemContainer):
    """Instance představují prostory, mezi nimiž hráč přechází.
    Prostory jsou definovány jako pojmenované kontejnery objektů.
    Prostory mohou obsahovat různé objekty,
    které mohou hráči pomoci v dosažení cíle hry.
    Každý prostor zná své aktuální bezprostřední sousedy
    a ví, jaké objekty se v něm v daném okamžiku nacházejí.
    Sousedé daného prostoru i v něm se nacházející objekty
    se mohou v průběhu hry měnit.
    """

    def __init__(self, name:str, description:str,
                 initial_neighbor_names:tuple[str],
                 initial_item_names    :tuple[str],
                 is_locked:bool = False
        ):
        super().__init__(name=name, initial_item_names=initial_item_names)
        self._description = description
        self.initial_neighbor_names = tuple(name.lower() for name
                                    in initial_neighbor_names)
        self._is_locked = is_locked


    def initialize(self) -> None:
        """Inicializuje prostor na počátku hry,
        tj. nastaví počáteční sadu sousedů a objektů v prostoru.
        """
        super().initialize()
        BAG.initialize()
        _NAME_2_PLACE[LIBRARY].is_locked = True
        self.name2neighbor = { name: _NAME_2_PLACE[name]
                            for name in self.initial_neighbor_names }


    @property
    def description(self) -> str:
        """Vrátí stručný popis daného prostoru.
        """
        return self._description


    @property
    def neighbors(self) -> tuple['IPlace']:
        """Vrátí n-tici aktuálních sousedů daného prostoru,
        tj. prostorů, do nichž je možno se z tohoto prostoru přesunout
        příkazem typu TypeOfStep.GOTO.
        """
        return tuple(self.name2neighbor.values())
    

    @property
    def is_locked(self) -> bool:
        """Vrátí informaci, jestli je prostor zamčený."""
        return self._is_locked
    
    @is_locked.setter
    def is_locked(self, value) -> None:
        """
        Setter pro atribut is_locked.
        """
        self._is_locked = value


# Slovník všech dostupných prostorů
_NAME_2_PLACE = {
    THE_PILLAR_OF_AUTUMN : Place(THE_PILLAR_OF_AUTUMN,
        "UNSC loď.",
        (HALO,),
        (AR, JACOB_KEYES)
    ),
    "halo" : Place(HALO,
        "Vesmírná stanice ve tvaru prstence.",
        (CONTROL_ROOM, KARTOGRAF,
        THE_PILLAR_OF_AUTUMN),
        (NEEDLER, PLASMA_PISTOL, GRUNT)
    ),
    CONTROL_ROOM : Place(CONTROL_ROOM,
        "Kontrolní místnost prstence.",
        (HALO, LAB),
        (NEEDLER, FLOOD)
    ),
    LAB : Place(LAB,
        "Laboratoř umístěná pod kontrolní místností prstence.",
        (CONTROL_ROOM,),
        (PLASMA_PISTOL, LIBRARY_KEY, ELITE)
    ),
    KARTOGRAF : Place(KARTOGRAF,
        "Místnost s mapu prstence.",
        (LIBRARY, HALO),
        (CARBINE, FORERUNNER)
    ),
    LIBRARY : Place(LIBRARY,
        "Knihovna na prstenci Halo, která obsahuje Index.",
        (TRC, KARTOGRAF),
        (PISTOL, INDEX),
        True
    ),
    TRC : Place(TRC,
        "Vesmírná loď kovenantu.",
        (THE_MAW, LIBRARY),
        (GRUNT, COVENANT)
    ),
    THE_MAW : Place(THE_MAW,
        "Trosky vesmírné UNSC lodi.",
        (TRC,),
        (ARBITER,)
    ),
}

# SLovník místností a jejich klíčů
ROOM_KEY_PAIRING = {
    LIBRARY : LIBRARY_KEY_2
}