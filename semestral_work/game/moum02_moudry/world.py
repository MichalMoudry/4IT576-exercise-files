#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul vystupuje v roli správce světa hry a jeho prostorů.
Má na starosti vzájemné propojení jednotlivých prostorů
a udržuje informaci o tom, ve kterém z nich se hráč právě nachází.
Vzájemné uspořádání prostorů se může v průběhu hry měnit –
prostory mohou v průběhu hry získávat a ztrácet sousedy.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################



############################################################################

class ANamed():
    """Instance představují objekty v prostorech či batohu.
    """

    def __init__(self, name:str, **args):
        """Inicializuje objekt zadaným názvem.
        """
        super().__init__(**args)
        self._name = name

    @property
    def name(self) -> str:
        """Vrátí název daného objektu.
        """
        return self._name


    def __str__(self) -> str:
        """Vrátí uživatelský textový podpis jako název dané instance.
        """
        return self._name



############################################################################

class Item(ANamed):
    """Instance představují h-objekty v prostorech či batohu.
    """

    def __init__(self, name:str, **args):
        """Vytvoří h-objekt se zadaným názvem.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def weight(self) -> int:
        """Vrátí váhu daného objektu.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class AItemContainer():
    """Instance představují kontejnery objektů - prostory či batoh.
    V kontejneru může být několik objektů se shodným názvem.
    """

    def __init__(self, initial_item_names:tuple[str], **args):
        """Zapamatuje si názvy výchozí sady objektů na počátku hry.
        """
        self.initial_item_names = initial_item_names


    def initialize(self) -> None:
        """Inicializuje kontejner na počátku hry.
        Po inicializace bude obsahovat příslušnou výchozí sadu objektů.
        Protože se názvy objektů mohou opakovat, nemůže použít slovník.
        Pamatuje si proto seznam objektů a seznam jejích názvů malými písmeny.
        Musí se jen dbát na to, aby se v obou seznamech vyskytoval objekt
        a jeho název na pozicích se stejným indexem.
        """
        self._items = [Item(name) for name in self.initial_item_names]
        self.item_names = [item.name.lower() for item in self._items]


    @property
    def items(self) -> list[Item]:
        """Vrátí n-tici objektů v daném kontejneru.
        """
        return self._items


    def item(self, name:str) -> Item:
        """Je-li v kontejneru objekt se zadaným názvem, vrátí jej,
        jinak vrátí None.
        """
        if name.lower() in self.item_names:
            index = self.item_names.index(name.lower())
            return self.items[index]
        else:
            return None


    def add_item(self, item:Item) -> bool:
        """Přidá zadaný objekt do kontejneru a vrátí informaci o tom,
        jestli se to podařilo.
        """
        raise Exception(f'Ještě není plně implementováno')


    def remove_item(self, item_name:str) -> Item:
        """Pokusí se odebrat objekt se zadaným názvem z kontejneru.
        Vrátí odkaz na zadaný objekt nebo None.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

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
        raise Exception(f'Ještě není plně implementováno')


    def initialize(self) -> None:
        """Inicializuje batoh na počátku hry. Vedle inicializace obsahu
        inicializuje i informaci o zbývající kapacitě.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def capacity(self) -> int:
        """Vrátí kapacitu batohu.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

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
                 initial_item_names    :tuple[str]
        ):
        super().__init__(name=name, initial_item_names=initial_item_names)
        self._description = description
        self.initial_neighbor_names = initial_neighbor_names


    def initialize(self) -> None:
        """Inicializuje prostor na počátku hry,
        tj. nastaví počáteční sadu sousedů a objektů v prostoru.
        """
        super().initialize()
        self.name2neighbor = { name: _NAME_2_PLACE[name]
                            for name in self.initial_neighbor_name }


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
        raise Exception(f'Ještě není plně implementováno')



############################################################################

def initialize() -> None:
    """Inicializuje svět hry, tj. nastavuje vzájemné počáteční
    propojení jednotlivých prostorů a jejich výchozí obsah,
    nastaví výchozí aktuální prostor a inicializuje batoh.
    """
    for place in _NAME_2_PLACE.values():
        place.initialize()
    global _current_place
    _current_place = _NAME_2_PLACE["The_Pillar_of_Autumn"]
    


def current_place() -> Place:
    """Vrátí odkaz na aktuální prostor,
    tj. na prostor, v němž se hráč pravé nachází.
    """
    return _current_place


def places() -> tuple[Place]:
    """Vrátí n-tici odkazů na všechny prostory ve hře
    včetně těch aktuálně nedosažitelných či neaktivních.
    """
    raise Exception(f'Ještě není plně implementováno')


def place(name:str) -> Place:
    """Vrátí prostor se zadaným názvem.
    Pokud ve hře takový není, vrátí None.
    """
    raise Exception(f'Ještě není plně implementováno')



############################################################################

# Jediná instance batohu
# V této hře neobsahuje žádnou výchozí sadu h-objektů
BAG:Bag

# Slovník všech dostupných prostorů
_NAME_2_PLACE = {
    "The_Pillar_of_Autumn" : Place("The_Pillar_of_Autumn",
        "Popis místa",
        ("Halo",),
        ("Assault_Rifle", "Jacob_Keyes", )
    ),
    "Halo" : Place("Halo",
        "Popis místa",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]")
    ),
    "kontrolní_místnost_prstence" : Place("kontrolní_místnost_prstence",
        "Popis místa",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]")
    ),
    "Laboratoř" : Place("Laboratoř",
        "Popis místa",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]")
    ),
    "Kartograf" : Place("Kartograf",
        "Popis místa",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]")
    ),
    "Knihovna" : Place("Knihovna",
        "Popis místa",
        ("TRC", "Kartograf"),
        ("Pistole", "Index")
    ),
    "TRC" : Place("TRC",
        "Popis místa",
        ("the_maw", "Knihovna"),
        ("[Grunt]", "[Covenant]")
    ),
    "the_maw" : Place("the_maw",
        "Popis místa",
        ("TRC", "Kartograf"),
        ("[Arbiter]",)
    ),
}

# Aktuální prostor = prostor, v němž se hráč právě nachází
_current_place:Place



############################################################################
dbg.stop_mod(0, __name__)
