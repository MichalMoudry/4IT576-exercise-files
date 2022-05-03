"""
Modul reprezentující uložiště, do nějž hráči ukládají
objekty sebrané v jednotlivých prostorech.
"""

from .abstract.aitemcontainer import AItemContainer
from .item import Item

BAG_MAX_CAPACITY = 10
BAG_INITAL_CAPACITY = 2

class Bag(AItemContainer):
    """Instance představuje úložiště,
    do nějž hráči ukládají objekty sebrané v jednotlivých prostorech,
    aby je mohli přenést do jiných prostorů a/nebo použít.
    Úložiště má konečnou kapacitu definující maximální povolený
    součet vah objektů vyskytujících se v úložišti.
    """

    def __init__(self, initial_item_names:tuple[str]):
        """Definuje batoh jako kontejner h-objektů s omezenou kapacitou.
        """
        super().__init__(initial_item_names=initial_item_names)
        self._capacity = BAG_INITAL_CAPACITY


    def initialize(self) -> None:
        """Inicializuje batoh na počátku hry. Vedle inicializace obsahu
        inicializuje i informaci o zbývající kapacitě.
        """
        super().initialize()


    @property
    def capacity(self) -> int:
        """Vrátí kapacitu batohu.
        """
        return self._capacity
    

    def add_item(self, item:Item) -> bool:
        """Přidá zadaný objekt do kontejneru a vrátí informaci o tom,
        jestli se to podařilo.
        """
        if item.weight >= BAG_MAX_CAPACITY:
            return False
        self._items.append(item)
        self._capacity += item.weight
        return True

# Jediná instance batohu
# V této hře neobsahuje žádnou výchozí sadu h-objektů
BAG:Bag = Bag(("Pistole", "generátor_štítu"))