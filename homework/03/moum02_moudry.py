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
        turn_left_180_degrees(k)
        turn_left(k)
    unhide(k)

def turn_left_180_degrees(k: Karel) -> None:
    """
    Funkce pro otočení robota o 180 stupňů vlevo.
    """
    turn_left(k)
    turn_left(k)

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

def go_up(k: Karel) -> None:
    """
    Funkce pro posunutí robota na nový řádek.
    """
    if k.is_east():
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

def step_through_rows(k: Karel, row_index: int = 0) -> None:
    """
    Funkce pro průchod řádky.

    Pozn.: Index (resp. číslo řádku) je v základu počítáno od nuly,
    což lze změnit v parametru row_index.
    """
    go(k, row_index)
    go_up(k)
    row_index = row_index + 1
    if is_last_row(k):
        go(k, row_index)
    else:
        step_through_rows(k, row_index)

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


def ensure_markers(k: Karel, n: int) -> Karel:
    """
    Zabezpečí, že na políčku, na němž robot stojí, bude právě n značek.

    Pokud celkový počet značek na daném políčku přesáhne
    maximální povolený počet, tak je ohlášena chyba.
    """
    while n > 0:
        put(k)
        n = n - 1
    return k


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
    return k


def my_function_3(k: Karel) -> Karel:
    """Definice vaší vlastní funkce, která bude používat pouze doposud
    probrané konstrukce, tj. rozhodování, rekurzi a cykly s podmínkou.
    (Nemusí samozřejmě používat všechny najednou, ale nebude používat jiné.)
    Funkce by měla mít nejméně 5 příkazů.
    Může definovat další parametry, ale všechny musejí mít přiřazenou
    implicitní hodnotu.
    V dokumentačním komentáři musí být popsána prováděná činnost
    včetně všech předpokladů a okrajových podmínek.
    """
    return k



###########################################################################q


def test_ensure_markers() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    ensure_markers().
    """


def test_fill_in() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    fill_in().
    """


def test_my_function_3() -> None:
    """Testovací funkce, která prověří správnost definice funkce
    my_function_3().
    """



###########################################################################q
dbg.stop_mod(1, __name__)
