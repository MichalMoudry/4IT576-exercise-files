#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Protokoly deklarující povinné atributy klíčových objektů
v odevzdaných semestrálních pracech.
Nebude-li některý z nich definován jako instance běžné třídy,
ale jako modul, odebere se ze seznamu parametrů parametr self.

Definované protokoly:
    INamed(Protocol)
    IItem(INamed)
    IItemContainer(Protocol)
    IBag(IItemContainer)
    IPlace(IItemContainer, INamed)
    IWorld(Protocol)
    IAction(Protocol)
    IGame(Protocol)

Definované třídy
    BasicActions

"""
import dbg; dbg.start_mod(1, __name__)
############################################################################

from abc      import abstractmethod
from typing   import Protocol
from ..api    import BasicActions


############################################################################

class INamed(Protocol):
    """Instance představují objekty v prostorech či batohu.
    """

    def __init__(self, name:str, **args):
        """Inicializuje objekt zadaným názvem.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def name(self) -> str:
        """Vrátí název daného objektu.
        """
        raise Exception(f'Ještě není plně implementováno')


    def __str__(self) -> str:
        """Vrátí uživatelský textový podpis jako název dané instance.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IItem(INamed):
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

class IItemContainer(Protocol):
    """Instance představují kontejnery objektů - prostory či batoh.
    V kontejneru může být několik objektů se shodným názvem.
    """

    def __init__(self, initial_item_names:tuple[str], **args):
        """Zapamatuje si názvy výchozí sady objektů na počátku hry.
        """
        raise Exception(f'Ještě není plně implementováno')


    def initialize(self) -> None:
        """Inicializuje kontejner na počátku hry.
        Po inicializace bude obsahovat příslušnou výchozí sadu objektů.
        Protože se názvy objektů mohou opakovat, nemůže použít slovník.
        Pamatuje si proto seznam objektů a seznam jejích názvů malými písmeny.
        Musí se jen dbát na to, aby se v obou seznamech vyskytoval objekt
        a jeho název na pozicích se stejným indexem.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def items(self) -> list[IItem]:
        """Vrátí n-tici objektů v daném kontejneru.
        """
        raise Exception(f'Ještě není plně implementováno')


    def item(self, name:str) -> IItem:
        """Je-li v kontejneru objekt se zadaným názvem, vrátí jej,
        jinak vrátí None.
        """
        raise Exception(f'Ještě není plně implementováno')


    def add_item(self, item:IItem) -> bool:
        """Přidá zadaný objekt do kontejneru a vrátí informaci o tom,
        jestli se to podařilo.
        """
        raise Exception(f'Ještě není plně implementováno')


    def remove_item(self, item_name:str) -> IItem:
        """Pokusí se odebrat objekt se zadaným názvem z kontejneru.
        Vrátí odkaz na zadaný objekt nebo None.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IBag(IItemContainer):
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

class IPlace(INamed, IItemContainer):
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
        raise Exception(f'Ještě není plně implementováno')


    def initialize(self) -> None:
        """Inicializuje prostor na počátku hry,
        tj. nastaví počáteční sadu sousedů a objektů v prostoru.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def description(self) -> str:
        """Vrátí stručný popis daného prostoru.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def neighbors(self) -> tuple['IPlace']:
        """Vrátí n-tici aktuálních sousedů daného prostoru,
        tj. prostorů, do nichž je možno se z tohoto prostoru přesunout
        příkazem typu TypeOfStep.GOTO.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IWorld(Protocol):
    """Instance vystupuje v roli správce světa hry a jeho prostorů.
    V dané hře musí být definována jako jedináček (např. modul).
    Má na starosti vzájemné propojení jednotlivých prostorů
    a udržuje informaci o tom, ve kterém z nich se hráč právě nachází.
    Vzájemné uspořádání prostorů se může v průběhu hry měnit –
    prostory mohou v průběhu hry získávat a ztrácet sousedy.
    """

    def initialize(self) -> None:
        """Inicializuje svět hry, tj. nastavuje vzájemné počáteční
        propojení jednotlivých prostorů a jejich výchozí obsah,
        nastaví výchozí aktuální prostor a inicializuje batoh.
        """
        raise Exception(f'Ještě není plně implementováno')


    def current_place(self) -> IPlace:
        """Vrátí odkaz na aktuální prostor,
        tj. na prostor, v němž se hráč pravé nachází.
        """
        raise Exception(f'Ještě není plně implementováno')


    def places(self) -> tuple[IPlace]:
        """Vrátí n-tici odkazů na všechny prostory ve hře
        včetně těch aktuálně nedosažitelných či neaktivních.
        """
        raise Exception(f'Ještě není plně implementováno')


    def place(self, name:str) -> IPlace:
        """Vrátí prostor se zadaným názvem.
        Pokud ve hře takový není, vrátí None.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IActionManager(Protocol):
    """Reprezentuje správce akcí, který rozhoduje,
    která akce dostane na starost zpracování aktuálního příkazu
    a řídí celkové chování v závislosti na tom, je-li hra právě aktivní.
    Správce akcí bývá definován jako modul definující třídy akcí.
    """

    def execute_command(self, command:str) -> str:
        """Zpracuje zadaný příkaz a vrátí odpověď hry.
        Zadaný příkaz zanalyzuje a v závislosti na aktuální aktivitě hry
        rozhodne, která akce dostane na starost jeho zpracování.
        Vrátí odpověď hry na zadaný příkaz.
       """
        raise Exception(f'Ještě není plně implementováno')


    def is_alive(self) -> bool:
        """Vrátí informaci o tom, je-li hra živá = aktuálně spuštěná.
        Spuštěnou hru není možno pustit znovu.
        Chceme-li hru spustit znovu, musíme ji nejprve ukončit.
        """
        raise Exception(f'Ještě není plně implementováno')


    def _initialize(self):
        """V rámci startu hry inicializuje všechny potřebné objekty.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IAAction(INamed):
    """Společná rodičovská třída všech akcí.
    """

    def __init__(self, name:str, description:str):
        """Vytvoří rodičovský podobjekt dané akce, který si zapamatuje
        název dané akce a její popis.
        """
        raise Exception(f'Ještě není plně implementováno')


    @property
    def description(self) -> str:
        """Vrátí popis příkazu s vysvětlením jeho funkce,
        významu jednotlivých parametrů a možností (resp. účelu) použití
        daného příkazu. Tento popis tak může sloužit jako nápověda
        k použití daného příkazu.
        """
        raise Exception(f'Ještě není plně implementováno')


    @abstractmethod
    def execute(self, arguments:tuple[str]) -> str:
        """Metoda realizující reakci hry na zadání daného příkazu.
        Předávané pole je vždy neprázdné, protože jeho nultý prvek
        je zadaný název vyvolaného příkazu. Počet argumentů je závislý
        na konkrétním akci, ale pro každou akci je konstantní.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IAction(IAAction):
    """Instance mají na starosti interpretaci příkazů zadávaných uživatelem
    hrajícím hru. Název spouštěné akce je první slovo zadávaného příkazu;
    další slova pak jsou interpretována jako argumenty.

    Lze ale definovat i akci, která odstartuje konverzaci
    (např. s osobou přítomnou v místnosti) a tím systém přepne do režimu,
    v němž se zadávané texty neinterpretují jako příkazy,
    ale předávají se definovanému objektu až do chvíle, kdy bude rozhovor
    ukončen a hra se přepne zpět do režimu klasických příkazů.
    """

    def __init__(self, name:str, description:str):
        """Vytvoří objekt reprezentující danou akci,
        a zpracovávající odpovídající příkazy..
        """
        raise Exception(f'Ještě není plně implementováno')


    def execute(self, arguments:tuple[str]) -> str:
        """Metoda realizující reakci hry na zadání daného příkazu.
        Předávané pole je vždy neprázdné, protože jeho nultý prvek
        je zadaný název vyvolaného příkazu. Počet argumentů je závislý
        na konkrétním akci, ale pro každou akci je konstantní.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IGame(Protocol):
    """Instance má na starosti řízení hry a komunikaci s uživatelem.
    Je schopna akceptovat zadávané příkazy a poskytovat informace
    o průběžném stavu hry a jejích součástí.
    Hra musí být definována jako jedináček (singleton),
    a bývá proto definována jako modul
    """

    def is_alive(self) -> bool:
        """Vrátí informaci o tom, je-li hra aktuálně spuštěná.
        Spuštěnou hru není možno pustit znovu.
        Chceme-li hru spustit znovu, musíme ji nejprve ukončit.
        """
        raise Exception(f'Ještě není plně implementováno')


    def execute_command(self, command:str) -> str:
        """Zpracuje zadaný příkaz a vrátí text zprávy pro uživatele.
        """
        raise Exception(f'Ještě není plně implementováno')


    def stop(self) -> None:
        """Ukončí hru a uvolní alokované prostředky.
        Zadáním prázdného příkazu lze následně spustit hru znovu.
        """
        raise Exception(f'Ještě není plně implementováno')


    def all_actions(self) -> tuple[IAction]:
        """Vrátí n-tici všech akcí použitelných ve hře.
        """
        raise Exception(f'Ještě není plně implementováno')


    def basic_actions(self) -> BasicActions:
        """Vrátí přepravku s názvy povinných akcí.
        """
        raise Exception(f'Ještě není plně implementováno')


    def bag(self) -> IBag:
        """Vrátí odkaz na batoh, do nějž bude hráč ukládat sebrané objekty.
        """
        raise Exception(f'Ještě není plně implementováno')


    def world(self) -> IWorld:
        """Vrátí odkaz na svět hry.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################

class IInterface(Protocol):
    """Objekty tohoto typu představují tovární objekty, které na požádání
    dodají ID a jméno autora/autorky programu a instance klíčových
    objektů aplikace, konkrétně definovaných scénářů,
    objektu aktuální hry a případného objektu uživatelského rozhraní.
    Protože tento protokol má být importován odevzdaným balíčkem,
    nejsou funkce deklarovány jako instanční metody s parametrem self,
    ale jako funkce daného modulu.
    """

    # Login autora/autorky programu zadaný VELKÝMI PÍSMENY
    AUTHOR_ID = 'Ještě není plně implementováno'

    # Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
    # tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
    # u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
    # Má-li autor programu více křestních jmen, může je uvést všechna.
    AUTHOR_NAME = 'Ještě není plně implementováno'

    # Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
    # zapsané v jeho/jejím rodném jazyce
    AUTHOR_ORIG_NAME = 'Ještě není plně implementováno'


    # Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
    SOURCES = """\
    ???
    """

    # Problémy, které se vyskytly při zpracování probrané látky a řešení DU
    PROBLEMS = """\
    ???
    """

    # Poznámky a připomínky k výkladu
    COMMENTS = """\
    ???
    """



    #######################################################################q

    def all_scenarios(self) -> tuple['Scenario']:
        """Vrátí n-tici definovaných scénářů.
        """
        raise Exception(f'Ještě není plně implementováno')


    def game(self) -> IGame:
        """Vrátí odkaz na objekt reprezentující hru.
        """
        raise Exception(f'Ještě není plně implementováno')



############################################################################
dbg.stop_mod(0, __name__)
