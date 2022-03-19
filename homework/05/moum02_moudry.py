#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Zadání domácího úkolu, v němž má student(ka) demonstrovat zvládnutí
doposud probrané látky prostřednictvím realizace hry Prší.
"""
import dbg; dbg.start_mod(1, __name__)
import random
###########################################################################q
# Identifikační a informační konstanty

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'MOUM02'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
AUTHOR_NAME = 'MOUDRÝ Michal'

# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
Prezentace
"""

# Problémy, které se vyskytly při zpracování probrané látky a řešení DU
PROBLEMS = """\
Žádné
"""

# Poznámky a připomínky k výkladu
COMMENTS = """\
Některé požadavky na funkce nedávají smysl (např. požadavek č. 4 u funkce
prepare(), kdy nemá smysl pracovat s nějakým "mezibalíkem", když můžu od
začátku pracovat se zamýchaným TALON, kdy v realitě potom co rozdám karty
a jednu dám na vršek (do té FACE_UP), a pak jednou kartou za druhou
nebudu plnit lízací balík na stole, ale prostě ho tam položím, tedy
metoda prepare() vyžaduje práci s balíčkem, který v reálném světě
neexistuje).
"""


###########################################################################q
# Konstanty

# Barvy karet
COLOR  = ('♠', '♣', '♥', '♦')
COLORS = len(COLOR)     # Pro testování lze hodnotu nastavit od 2 do 4

# Velikosti karet
VALUE  = ('7', '8', '9', 'X', 'J', 'Q', 'K', 'A')
VALUES = len(VALUE)     # Pro testování lze hodnotu nastavit od 2 do 8

# Počet rozdávaných karel
TO_DEAL = 4             # Pro testování lze hodnotu nastavit

# Balíček karet určených k "lízání" seřazených tak, že karta,
# která se má lízat, je vždy uvedena jako poslední (tj. je na konci seznamu).
TALON:list[str] = []

# Balíček odložených karet seřazených tak, že naposledy odložená karta
# je vždy uvedena jako poslední (tj. je na konci seznamu).
FACE_UP:list[str] = []

# Karty, které má v ruce hráč
USER:list[str] = []

# Karty, které má v ruce počítač
COMP:list[str] = []



###########################################################################q
# Abecedně seřazené pomocné funkce

def draw_card(card: str, orig: list[str], destination: list[str]) -> None:
    """
    Funkce pro přesunutí karty z balíčku do libovolné destinace.
    """
    orig.remove(card)
    destination.append(card)

def get_random_card_from_deck(deck: list[str]) -> str:
    """
    Funkce, která vrátí náhodnou kartu z talónu.
    """
    card = deck[random.randint(0, len(deck) - 1)]
    return card

def initial_hand_fill(deck: list[str], to: list[str]) -> None:
    """
    Funkce pro rozdání karet určité straně.
    """
    card = ""
    deck_length = len(deck)
    for i in range(TO_DEAL):
        card = deck[deck_length - (i + 1)]
        draw_card(card, deck, to)

def initial_deck_fill(deck: list[str]) -> list[str]:
    """
    Funkce pro prvotní naplnění losovacího balíčku
    """
    for color in COLOR:
        for number in VALUE:
            deck.append(f"{number}{color}")
    deck = shuffle_deck(deck)
    return deck

def shuffle_deck(deck: list[str]) -> list[str]:
    """
    Funkce pro zamýchání balíčku.
    """
    new_deck:list[str] = []
    while len(deck) > 0:
        random_card = get_random_card_from_deck(deck)
        draw_card(random_card, deck, new_deck)
    return new_deck

def print_state(prolog:str='nezadáno', level:int=1) -> None:
    """Pomocná funkce pro ladění, která vytiskne zadanou úvodní hlášku
    s prologem charakterizujícím místo, odkud byla zavolána,
    a za ní vytiskne přehled o stavu hry, tj. jednotlivé sady karet.
    """
    dbg.prDB(level,
       f'===== Stav hry {prolog}\n'
       f'   Uživatel {USER}\n'
       f'   Počítač  {COMP}\n'
       f'   Balík    {FACE_UP}\n'
       f'   Talón    {TALON}\n'
       f'{60*"-"}' )


###########################################################################q
# Požadované funkce

def prepare() -> None:
    """Připraví karty pro další hru, tj.
    1. Připraví zamíchanou sadu (seznam) karet se zadaným počtem barev
       a zadaným počtem hodnot. Karty budou reprezentovány dvouznakovými
       stringy, v nichž bude prvním znakem některá z hodnot v konstantě
       VALUE a druhým znakem některý z obrazců v konstantě COLOR.
       Počet barev, počet hodnot a počet rozdávaných karet je zadán
       v konstantách COLORS, VALUES a TO_DEAL.
       Pro účely testování můžete jejich hodnoty snížit.
       Je-li požadovaných barev (COLORS) nebo hodnot (VALUES) méně,
       než je dálka příslušné n-tice, tak se přebírají od počátku
       seznamů COLOR a VALUE.
    2. Z konce tohoto seznamu rozdá počet karet zadaný konstantou TO_DEAL
       nejprve hráči a pak počítači.
    2. Přesune ze seznamu poslední kartu jako základ odkládacího balíku
       FACE_UP.
    4. Zbytkem seznamu naplní seznam TALON.
    """
    deck:list[str] = []
    deck = initial_deck_fill(deck)
    initial_hand_fill(deck, USER)
    initial_hand_fill(deck, COMP)
    face_up_card = deck[len(deck) - 1]
    draw_card(face_up_card, deck, FACE_UP)
    for card in deck:
        TALON.append(card)


def comp_turn() -> int:
    """Realizuje další tah počítače.
    Má-li počítač "v ruce" kartu se stejnou hodnotou či barvou,
    vrátí vrátí její index ve svém seznamu, aby ji bylo možné použít.
    Nemá-li takovou, vrátí -1, aby mu byla přidána karta z talónu.
    """


def user_turn() -> int:
    """Realizuje komunikaci s uživatelem, který si má vybrat,
    zda některou ze svých karet odhodí, anebo si lízne další.
    Vrátí index uživatelovi karty, pokud se ji rozhodl odložit,
    anebo vrátí -1, pokud se uživatel rozhodl líznout další kartu.
    Při vybrání odkládané karty je třeba po návratu zkontrolovat,
    zda její hodnota či barva odpovídá kartě na balíčku.
    """


def turn() -> int:
    """Nechá táhnout nejprve uživatele a poté počítač.
    Podle jejich odpovědi upraví příslušně obsah jednotlivých seznamů.
    Zůstanou-li hráčům v ruce karty, vrátí 0.
    Vyhraje-li uživatel, vrátí -1, vyhraje-li počítač, vrátí +1.
    """


def play(colors:int=4, value:int=8, to_deal:int=4) -> None:
    """Realizuje zjednodušenou verzi hry Prší se zadaným okrajovými podmínkami,
    tj. s kartami se zadaným počtem barev a hodnot a se zadaným počtem karet,
    které se mají na počátku každému hráči rozdat.
    """



###########################################################################q
# Testy

def test_prepare() -> None:
    """Prověrka definice funkce prepare()."""
    prepare()
    print_state("test_prepare()")
    face_up_res = True if len(FACE_UP) == 1 else False
    print("FACE_UP test:", f"{face_up_res},",
    f"FACE_UP length: {len(FACE_UP)} (expected: 1)")
    user_hand_test = True if len(USER) == TO_DEAL else False
    print("User hand test:", f"{user_hand_test},",
    f"User hand length: {len(USER)} (expected: {TO_DEAL})")
    computer_hand_test = True if len(COMP) == TO_DEAL else False
    print("Computer hand test:", f"{computer_hand_test},",
    f"Computer hand length: {len(COMP)} (expected: {TO_DEAL})")
    deck_length = len(TALON) + len(FACE_UP)+ len(USER) + len(COMP)
    talon_test = True if deck_length == (VALUES * COLORS) else False
    print(f"Talon test: {talon_test},",
    f"deck length: {deck_length} (expected: {VALUES * COLORS})")


def test_turn() -> None:
    """Prověrka kódu pro realizaci jednoho kola hry funkcí turn().
    """


def test_play() -> None:
    """Prověrka funkce play() řešící odehrání hry.
    """



###########################################################################q
dbg.stop_mod(1, __name__)
