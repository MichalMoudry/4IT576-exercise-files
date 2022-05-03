from .abstract.anamed import ANamed
from .abstract.aitemcontainer import AItemContainer
from .bag import BAG

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
    "the_pillar_of_autumn" : Place("The_Pillar_of_Autumn",
        "Popis místa",
        ("Halo",),
        ("_assault_Rifle", "#jacob_keyes")
    ),
    "halo" : Place("Halo",
        "Popis místa",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("_needler", "_plasma_Pistol", "#[Grunt]")
    ),
    "kontrolní_místnost_prstence" : Place("kontrolní_místnost_prstence",
        "Popis místa",
        ("Halo", "Laboratoř"),
        ("_needler", "#[flood]")
    ),
    "laboratoř" : Place("Laboratoř",
        "Popis místa",
        ("kontrolní_místnost_prstence",),
        ("_plasma_pistol", "_klíč_ke_knihovně", "#[elite]")
    ),
    "kartograf" : Place("Kartograf",
        "Popis místa",
        ("Knihovna", "Halo"),
        ("_carbine", "#[forerunner]")
    ),
    "knihovna" : Place("Knihovna",
        "Popis místa",
        ("TRC", "Kartograf"),
        ("_pistole", "_index"),
        True
    ),
    "trc" : Place("TRC",
        "Popis místa",
        ("the_maw", "Knihovna"),
        ("#[grunt]", "#[covenant]")
    ),
    "the_maw" : Place("the_maw",
        "Popis místa",
        ("TRC",),
        ("#[arbiter]",)
    ),
}