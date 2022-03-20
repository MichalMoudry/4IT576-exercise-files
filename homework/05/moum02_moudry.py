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

def change_cards_deck(card: str, orig: list[str],
destination: list[str]) -> None:
    """
    Funkce pro přesunutí karty z balíčku do libovolné destinace.
    """
    orig.remove(card)
    destination.append(card)

def compare_cards(card1: str, card2: str) -> bool:
    """
    Funkce pro porovnání, zda jsou karty mezi sebou kompatibilní.
    """
    if card1[0] in card2:
        return True
    elif card1[1] in card2:
        return True
    else:
        return False

def fill_talon_deck(deck: list[str]) -> None:
    """
    Funkce pro naplnění lízacího balíčku.
    """
    for card in deck:
        TALON.append(card)

def get_available_colors(colors: int) -> list[str]:
    """
    Funkce pro získání povolených barev ve hře.
    """
    colors_list: list[str] = []
    for index, color in enumerate(COLOR):
        if index + 1 <= colors:
            colors_list.append(color)
    return colors_list

def get_available_values(value: int) -> list[str]:
    """
    Funkce pro získání povolených hodnot ve hře.
    """
    values_list: list[str] = []
    for index, val in enumerate(VALUE):
        if index + 1 <= value:
            values_list.append(val)
    return values_list

def get_face_up_last_card() -> str:
    """
    Funkce pro získání poslední karty z balíčku FACE_UP.
    """
    return FACE_UP[len(FACE_UP) - 1]

def get_random_card_from_deck(deck: list[str]) -> str:
    """
    Funkce, která vrátí náhodnou kartu z talónu.
    """
    card = deck[random.randint(0, len(deck) - 1)]
    return card

def get_turn_result() -> int:
    """
    Funkce pro získání výsledku kola hry Prší.
    """
    if len(USER) == 0:
        return -1
    elif len(COMP) == 0:
        return 1
    else:
        return 0

def handle_empty_talon() -> None:
    """
    Funkce pro vyřešení situace, kdy lízací balíček je prázdný
    """
    last_card = get_face_up_last_card()
    face_up_length = len(FACE_UP) - 1
    for index, card in enumerate(FACE_UP):
        if index != face_up_length:
            TALON.append(card)
    FACE_UP.clear()
    FACE_UP.append(last_card)
    deck = shuffle_deck(TALON)
    TALON.clear()
    fill_talon_deck(deck)

def handle_card_draw(user_decision: int, computer_decision: int) -> None:
    """
    Funkce pro zachycení, zda si chce nějaká strana líznout kartu.
    """
    if len(TALON) == 0:
        handle_empty_talon()
    card = ""
    if user_decision == -1 and len(TALON) > 0:
        card = get_random_card_from_deck(TALON)
        change_cards_deck(card, TALON, USER)
    if computer_decision == -1 and len(TALON) > 0:
        card = get_random_card_from_deck(TALON)
        change_cards_deck(card, TALON, COMP)

def handle_user_input(inpt: str) -> int:
    """
    Funkce pro zvládnutí vstupu uživatele.

    Vstup musí být číslo.
    """
    if inpt == "":
        return -1
    if int(inpt) in range(1, len(USER) + 1):
        return int(inpt) - 1
    else:
        return -1

def initial_hand_fill(deck: list[str], to: list[str],
to_deal: int = TO_DEAL) -> None:
    """
    Funkce pro rozdání karet určité straně.
    """
    card = ""
    deck_length = len(deck)
    for i in range(to_deal):
        card = deck[deck_length - (i + 1)]
        change_cards_deck(card, deck, to)

def initial_deck_fill(deck: list[str], colors: list[str] = COLOR,
values: list[str] = VALUE) -> list[str]:
    """
    Funkce pro prvotní naplnění losovacího balíčku
    """
    for color in colors:
        for number in values:
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
        change_cards_deck(random_card, deck, new_deck)
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

def print_user_turn_info() -> None:
    """
    Funkce pro vypsání začátečních informací na začátku uživatelova
    tahu.
    """
    print(f"\nVaše karty: {USER}")
    print(60*"-")
    print(f"Počet karet počítače: {len(COMP)}")
    print(f"Odkládací balíček: ['{get_face_up_last_card()}']")
    print(60*"-")
    print("Možnosti:")
    print(f"- Zahrát kartu (1 - {len(USER)})")
    print("- Líznout si kartu (0)")

def print_game_result(result: int) -> None:
    """
    Funkce pro vypsání výsledku hry.
    """
    if result == -1:
        print("Gratulujeme! Vyhráli jste hru.")
    else:
        print("Bohužel jste prohráli hru.")

###########################################################################q
# Požadované funkce

def prepare(colors:list[str] = COLOR, value:list[str] = VALUE,
to_deal: int = TO_DEAL) -> None:
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
    deck = initial_deck_fill(deck, colors, value)
    initial_hand_fill(deck, USER, to_deal)
    initial_hand_fill(deck, COMP, to_deal)
    face_up_card = deck[len(deck) - 1]
    change_cards_deck(face_up_card, deck, FACE_UP)
    fill_talon_deck(deck)


def comp_turn() -> int:
    """Realizuje další tah počítače.
    Má-li počítač "v ruce" kartu se stejnou hodnotou či barvou,
    vrátí vrátí její index ve svém seznamu, aby ji bylo možné použít.
    Nemá-li takovou, vrátí -1, aby mu byla přidána karta z talónu.
    """
    index = 0
    face_up_last_card = get_face_up_last_card()
    selected_index = -1
    while index < len(COMP):
        if compare_cards(COMP[index], face_up_last_card):
            selected_index = index
            break
        index += 1
    return selected_index


def user_turn() -> int:
    """Realizuje komunikaci s uživatelem, který si má vybrat,
    zda některou ze svých karet odhodí, anebo si lízne další.
    Vrátí index uživatelovi karty, pokud se ji rozhodl odložit,
    anebo vrátí -1, pokud se uživatel rozhodl líznout další kartu.
    Při vybrání odkládané karty je třeba po návratu zkontrolovat,
    zda její hodnota či barva odpovídá kartě na balíčku.
    """
    print_user_turn_info()
    res = handle_user_input(input("Zadejte vaše rozhodnutí: "))
    return res


def turn() -> int:
    """Nechá táhnout nejprve uživatele a poté počítač.
    Podle jejich odpovědi upraví příslušně obsah jednotlivých seznamů.
    Zůstanou-li hráčům v ruce karty, vrátí 0.
    Vyhraje-li uživatel, vrátí -1, vyhraje-li počítač, vrátí +1.
    """
    is_user_input_invalid = True
    while is_user_input_invalid:
        usr_turn = user_turn()
        if usr_turn != -1:
            face_up_last_card = get_face_up_last_card()
            if compare_cards(USER[usr_turn], face_up_last_card):
                change_cards_deck(USER[usr_turn], USER, FACE_UP)
                is_user_input_invalid = False
            else:
                print("--- Nehodná karta zvolena! ---")
        elif usr_turn == -1:
            is_user_input_invalid = False
    computer_turn = comp_turn()
    handle_card_draw(usr_turn, computer_turn)
    if computer_turn != -1:
        change_cards_deck(COMP[computer_turn], COMP, FACE_UP)
    return get_turn_result()


def play(colors:int=4, value:int=8, to_deal:int=4) -> None:
    """Realizuje zjednodušenou verzi hry Prší se zadaným okrajovými
    podmínkami, tj. s kartami se zadaným počtem barev a hodnot a
    se zadaným počtem karet, které se mají na počátku každému hráči
    rozdat.
    """
    if (colors <= len(COLOR) and colors > 0
    ) and value <= len(VALUE) and value > 0:
        available_colors: list[str] = get_available_colors(colors)
        available_values: list[str] = get_available_values(value)
        prepare(available_colors, available_values, to_deal)
        game_progress = 0
        while game_progress == 0:
            game_progress = turn()
        print_game_result(game_progress)



###########################################################################q
# Testy

def test_prepare() -> None:
    """Prověrka definice funkce prepare()."""
    prepare()
    print_state("test_prepare()")
    face_up_res = True if len(FACE_UP) == 1 else False
    print("Test odkládacího balíčku:", f"{face_up_res}",
    f"\n\tVelikost odkládacího balíčku: {len(FACE_UP)} (očekáváno: 1)")
    user_hand_test = True if len(USER) == TO_DEAL else False
    print("Ruka uživatele test:", f"{user_hand_test}",
    f"\n\tDélka balíčku uživatele: {len(USER)} (očekáváno: {TO_DEAL})")
    computer_hand_test = True if len(COMP) == TO_DEAL else False
    print("Test ruky počítače:", f"{computer_hand_test}",
    f"\n\tDélka balíčku počítače: {len(COMP)} (očekáváno: {TO_DEAL})")
    deck_length = len(TALON) + len(FACE_UP)+ len(USER) + len(COMP)
    talon_test = True if deck_length == (VALUES * COLORS) else False
    print(f"Test lízacího balíčku: {talon_test}",
    f"\n\tDélka balíčku: {deck_length} (očekáváno: {VALUES * COLORS})")


def test_turn() -> None:
    """Prověrka kódu pro realizaci jednoho kola hry funkcí turn().
    """
    import builtins as b
    b_input = b.input
    b.input = dbg.input
    dbg.INPUTS = ('1', '0')
    dbg.TST = 1
    random.seed(42)
    dbg.TST = 1
    prepare()
    print(f"Výsledek kola: {turn()} (očekáváno: 0)")
    print_state("test_turn()")
    print("Je J♥ v odkládacím balíčku?", True if "J♥" in FACE_UP else False,
    "(očekáváno: True)")
    print("Bylo J♥ odebráno z ruky hráče?",
    True if not("J♥" in USER) else False, "(očekáváno: True)")
    user_orig_length = len(USER)
    talon_orig_length = len(TALON)
    turn()
    user_modified_length = len(USER)
    talon_modified_length = len(TALON)
    print("Přidána karta do balíčku uživatele?",
    True if user_orig_length + 1 == user_modified_length else False)
    print("Byla odebrána karta z odebíracího balíčku?",
    True if talon_orig_length == talon_modified_length + 1 else False)
    b.input = b_input
    dbg.TST = 0


def test_play() -> None:
    """Prověrka funkce play() řešící odehrání hry.
    """
    import builtins as b
    b_input = b.input
    b.input = dbg.input
    dbg.INPUTS = ('1', '0', '2', '3', '1', '0', '2', '3', '1', '0',
    '2', '3', '1', '0', '52', '3', '1', '0', '4', '3', '1', '0', '2',
    '3', '4', '0', '2', '3', '1', '0', '2', '3', '1', '0', '2', '3',
    '1', '0', '2', '3', '1', '0', '2', '3', '1', '0', '2', '3', '1',
    '1', '1', '0', '')
    dbg.TST = 1
    random.seed(50)
    dbg.TST = 1
    play()
    b.input = b_input
    dbg.TST = 0


###########################################################################q
dbg.stop_mod(1, __name__)
