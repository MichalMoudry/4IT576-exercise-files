"""
Modul reprezentující uložiště, do nějž hráči ukládají
objekty sebrané v jednotlivých prostorech.
"""

from .aitemcontainer import AItemContainer
from .item import Item

BAG_MAX_CAPACITY = 3
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


    def initialize(self) -> None:
        """Inicializuje batoh na počátku hry. Vedle inicializace obsahu
        inicializuje i informaci o zbývající kapacitě.
        """
        super().initialize()
        self._content = BAG_INITAL_CAPACITY


    @property
    def capacity(self) -> int:
        """Vrátí kapacitu batohu.
        """
        return BAG_MAX_CAPACITY

    
    @property
    def content(self):
        """
        Vrátí momentální váhu batohu.
        """
        return self._content
    

    def add_item(self, item:Item) -> bool:
        """Přidá zadaný objekt do kontejneru a vrátí informaci o tom,
        jestli se to podařilo.
        """
        if (new_content := item.weight + self._content) > BAG_MAX_CAPACITY:
            return False
        self._content = new_content
        return super().add_item(item)
    
    def remove_item(self, item_name:str) -> Item:
        """Pokusí se odebrat objekt se zadaným názvem z kontejneru.
        Vrátí odkaz na zadaný objekt nebo None.
        """
        name = item_name.lower()
        if name in self.item_names:
            item = self.item(item_name)
            self.item_names.remove(name)
            self._items.remove(item)
            self._content -= item.weight
            return item
        else:
            return None

# Jediná instance batohu
# V této hře neobsahuje žádnou výchozí sadu h-objektů
BAG:Bag = Bag(("_pistole", "_generátor_štítu"))