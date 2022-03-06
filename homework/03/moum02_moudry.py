#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Zdroje:
    Prezentace

Problémy:
    žádné

Připomínky:
    žádné

Nápověda:
    - Odkaz na aktuální svět robotů získáte zvoláním funkce active_world()
    - Řádky jsou indexovány shora od nuly, sloupce zleva také od nuly.
    - Definované funkce by neměly mít více jak 8 příkazů,
      leda by se jednalo o speciální případ, který více příkazů vyžaduje
      pro zvýšení přehlednosti. Takové situace jsou ale opravdu výjimečné.
      Vyskytnou se např. při velkém množství větví elif nebo case.
      Obávám se však, že to nebude příklad vašich programů.
      Potřebujete-li definovat složitější definici, definujte pomocné funkce,
      které z té definované funkce ve správnou chvíli zavoláte,
      jak jsme si to ukazovali na hodině.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

from robotcz import *


###########################################################################q

def turn_right(k: Karel) -> None:
    """
    Otočí zadaného robota rychle vpravo.
    """
    if hide(k):
        turn_left(k)
        turn_left(k)
        turn_left(k)
    unhide(k)

def move_diagonally(k: Karel) -> None:
    """
    Funkce pro posunu robota po diagonále světa.
    """
    hide(k)
    step(k)
    turn_left(k)
    step(k)
    turn_right(k)
    unhide(k)

def handle_east_direction_check(k: Karel) -> bool:
    """
    Funkce pro zkontrolování, zda jde o poslední řádek, pokud
    robot přišel z levé strany předchozího řádku.
    """
    turn_left(k)
    res = k.is_wall()
    turn_right(k)
    return res

def handle_west_direction_check(k: Karel) -> bool:
    """
    Funkce pro zkontrolování, zda jde o poslední řádek, pokud
    robot přišel z pravé strany předchozího řádku.
    """
    turn_right(k)
    res = k.is_wall()
    turn_left(k)
    return res

def is_last_row(k: Karel) -> bool:
    """
    Funkce pro kontrolu, zda jde o poslední řádek.
    """
    hide(k)
    result = False
    if k.is_east():
        result = handle_east_direction_check(k)
    else:
        result = handle_west_direction_check(k)
    unhide(k)
    return result

def handle_east_column_check(k: Karel) -> bool:
    """
    Funkce pro kontrolu, zda vpravo od robota není zeď.
    """
    turn_left(k)
    result = k.is_wall()
    turn_right(k)
    return result

def handle_west_column_check(k: Karel) -> bool:
    """
    Funkce pro kontrolu, zda vlevo od robota není zeď.
    """
    turn_right(k)
    result = k.is_wall()
    turn_left(k)
    return result

def is_last_column(k: Karel) -> bool:
    """
    Funkce pro kontrolu, zda jde o poslední sloupec.
    """
    result = False
    hide(k)
    result = handle_east_column_check(k)
    if not(result):
        result = handle_west_column_check(k)
    unhide(k)
    return result

def crlf(k: Karel, condition: bool) -> None:
    """
    Funkce pro posunutí robota na nový řádek, včetně
    jeho správného nasměrování.
    """
    if condition:
        turn_left(k)
        step(k)
        turn_left(k)
    else:
        turn_right(k)
        step(k)
        turn_right(k)

def go(k: Karel, sign_number: int) -> None:
    """
    Funkce pro posunutí robota na konec řádku či sloupce.
    """
    while not(is_wall(k)):
        ensure_markers(k, sign_number)
        step(k)
    else:
        ensure_markers(k, sign_number)

def step_through_rows(k: Karel, row_index: int = 1,
increment: bool = True) -> None:
    """
    Funkce pro průchod řádky.

    Pozn.: Index (resp. číslo řádku) je v základu počítáno od jedné,
    což lze změnit v parametru row_index.
    """
    go(k, row_index)
    crlf(k, k.is_east())
    if increment:
        row_index = row_index + 1
    if is_last_row(k):
        go(k, row_index)
    else:
        step_through_rows(k, row_index, increment)

def step_through_columns(k: Karel, column_index: int = 1) -> None:
    """
    Funkce pro průchod sloupci.
    """
    go(k, column_index)
    crlf(k, column_index % 2 == 0)
    column_index = column_index + 1
    if is_last_column(k):
        go(k, column_index)
    else:
        step_through_columns(k, column_index)

def orient_robot_for_column_crawl(k: Karel) -> None:
    """
    Funkce pro otočení robota do správného směru pro průchod sloupci.

    Pozn.: Zatím je zde zachycena situace, kdy robot je v základu otočen
    na východ, tedy v budoucnu je třeba zachytit situace, kdy v základu je
    otočen na jiné směry (samozřejmě pokud taková informace bude dostupná).
    """
    if k.is_east():
        k.turn_left()

def author_name() -> str:
    """
    Funkce, která vrátí jméno autora.
    """
    return "MOUDRÝ Michal"

def author_id() -> str:
    """
    Funkce, která vrátí identifikační řetězec autora.
    """
    return "MOUM02"



###########################################################################q

def ensure_markers(k: Karel, n: int) -> Karel:
    """
    Zabezpečí, že na políčku, na němž robot stojí, bude právě n značek.

    Pokud celkový počet značek na daném políčku přesáhne
    maximální povolený počet, tak je ohlášena chyba.
    """
    while k.is_marker():
        pick(k)
    while n > 0:
        put(k)
        n = n - 1
    return k


def fill_the_board(k:Karel) -> Karel:
    """Zaplní aktuální svět značkami tak, že na každém jeho políčku bude
    po jedné značce.
    Funkce předpokládá, že na dvorku nejsou žádné zdi ani jiní roboti.
    Neví ale, kde se nachází robot zadaný jako argument a současně neví,
    jestli již ně některých políčcích nejsou umístěny nějaké značky.
    Na koncovou pozici robota nejsou kladeny žádné požadavky.
    Musí jenom zůstat na dvorku.
    """
    step_through_rows(k, increment=False)
    return k


# NEPOVINNÁ FUNKCE PRO TY ZKUŠENĚJŠÍ
def fill_in(k: Karel, row_num: bool = True) -> Karel:
    """Zaplní aktuální svět značkami tak, že na každém jeho políčku bude
    tolik značek, kolik je při (row_num == True) index jeho řádku,
    a při (row_num == False) index jeho sloupce.
    Funkce předpokládá, že na dvorku nejsou žádné zdi ani jiní roboti.
    Neví ale, kde se nachází robot zadaný jako argument a současně neví,
    jestli již ně některých políčcích nejsou umístěny nějaké značky.
    Na koncovou pozici robota nejsou kladeny žádné požadavky.
    Musí jenom zůstat na dvorku.
    V rámci testu nevytvářejte nový dvorek, ale použijte aktuální.
    """
    if row_num:
        step_through_rows(k)
    elif not(row_num):
        orient_robot_for_column_crawl(k)
        step_through_columns(k)
    return k


def my_function_3(k:Karel, n: int = 1, increment: bool = False) -> Karel:
    """
    Tato funkce položí n značek na každé políčko diagonály světa, přičemž
    existuje možnost na každém novém políčku přidat o jednu značku navíc.

    Předpokladem této metody je, že robot se nachází v jeho základní pozici.
    """
    while not(k.is_wall()) and not(is_last_row(k)):
        ensure_markers(k, n)
        if increment:
            n = n + 1
        move_diagonally(k)
    else:
        ensure_markers(k, n)
    return k



###########################################################################q

def test_ensure_markers() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    ensure_markers().
    """


def test_fill_the_board() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    fill_in().
    V rámci tohoto testu nevytvářejte nový dvorek, ale použijte aktuální.
   """


# NEPOVINNÁ FUNKCE PRO TY ZKUŠENĚJŠÍ
def test_fill_in() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    fill_in().
    V rámci tohoto testu nevytvářejte nový dvorek, ale použijte aktuální.
    """


def test_my_function_3() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    my_function_3().
    """



###########################################################################q
dbg.stop_mod(1, __name__)
