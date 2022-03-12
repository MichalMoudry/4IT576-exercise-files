#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Zadání domácího úkolu, v němž má student(ka) demonstrovat zvládnutí
doposud probrané látky.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

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
Žádné
"""


###########################################################################q
# Importy

# from robotcz import *
import random


###########################################################################q
# Abecedně seřazené pomocné funkce

def get_stone_weaknesses() -> str:
    """
    Funkce, která vrátí elementy, jež porazí kámen (papír, Spock), přičemž
    elementy jsou vráceny jako string.
    """
    return "pS"

def get_scissor_weaknesses() -> str:
    """
    Funkce, která vrátí elementy, jež porazí nůžky (kámen, Spock), přičemž
    elementy jsou vráceny jako string.
    """
    return "kS"

def get_paper_weaknesses() -> str:
    """
    Funkce, která vrátí elementy, jež porazí kámen (nůžky, tapír), přičemž
    elementy jsou vráceny jako string.
    """
    return "nt"

def get_tapir_weaknesses() -> str:
    """
    Funkce, která vrátí elementy, jež porazí tapíra (nůžky, kámen), přičemž
    elementy jsou vráceny jako string.
    """
    return "nk"

def get_spock_weaknesses() -> str:
    """
    Funkce, která vrátí elementy, jež porazí Spocka (papír, tapír), přičemž
    elementy jsou vráceny jako string.
    """
    return "pt"

def handle_user_input(user_input: str) -> bool:
    """
    Funkce pro zpracování uživatelského vstupu ve funkci roshambo().
    """
    res = True
    if "konec" in user_input or user_input == "":
        res = False
    return res

def get_appropriate_weakness(element: str) -> str:
    """
    Funkce, která vrátí správné slabosti pro určený element.
    """
    if element == "k":
        return get_stone_weaknesses()
    elif element == "n":
        return get_scissor_weaknesses()
    elif element == "p":
        return get_paper_weaknesses()
    elif element == "t":
        return get_tapir_weaknesses()
    elif element == "S":
        return get_spock_weaknesses()

def get_random_number(big_bang: bool) -> int:
    """
    Funkce pro získání pseudonáhodného čísla podle parametrů hry.
    """
    if big_bang:
        return random.randint(1, 5)
    else:
        return random.randint(1, 3)

###########################################################################q
# Požadované funkce

def winner(player1:str, player2:str) -> int:
    """Vrátí informaci o výherci ve hře kámen-papír-nůžky, případně
    v rozšířené big-bangové verzi kámen-nůžky-papír-tapír-Spock.
    V argumentech očekává první znak slova zadávaný jednotlivými hráči.

    Vrátí -1 je-li výhercem player1, 0 při remíze a +1 vyhraje-li player2.
    Špatné zadání neočekává - o korektní zadání se stará volající kód.
    Parametr big_bang zadává, bude-li se jednat o standardní (implicitně)
    nebo rozšířenou (big_bang == True) verzi.
    """
    if player1 == player2:
        return 0
    if player2 in get_appropriate_weakness(player1):
        return 1
    else:
        return -1

def roshambo(big_bang=False) -> None:
    """Spustí hru kámen-papír-nůžky, případně její big-bangovou verzi
    kámen-papír-nůžky-tapír-Spock mezi hráčem a počítačem. Hra probíhá
    v textovém režimu prostřednictvím standardního vstupu a výstupu.
    Parametr big_bang zadává, bude-li se jednat o standardní (implicitně)
    nebo rozšířenou (big_bang == True) verzi.
    Hra se průběžně ptá hráče, který zadá první znak názvu příslušné volby
    (kámen - nůžky - papír - tapír - Spock).
    Chce-li hru ukončit, zadá prázdný string.
    Po každém zadání zobrazí odpověď počítače (generuje se náhodná),
    celkové skóre a dotaz na další volbu.
    Zadá-li hráč špatný znak (případně nezadá nic), upozorní ho na to
    a zopakuje svoji otázku.
    """
    is_game = True
    decision = 0
    while is_game:
        decision = get_random_number(big_bang)
        print("--------Vítejte ve hře kámen, nůžky, papír--------")
        print("Vaše možnosti:\n- kámen\n- nůžky\n- papír")
        if big_bang:
            print("- tapír\n- Spock")
        print("- konec")
        print("--- rozhodnutí", decision)
        response = input("Zadejte akci: ")
        is_game = handle_user_input(response)

def my_function_4(costs: tuple, connections: tuple) -> int:
    """
    Funkce pro výpočet účelové funkce v rámci přiřazovacího problému.
    Tato funkce slouží pro ověření výsledku, tedy zde nejde o nalezení
    optimálního řešení přiřazovacího problému.

    Pozn.: data se musejí vkládat po sloupcích a ne řádcích.

    𝑥𝑖𝑗 ∈ {0,1}

    Proměnné 𝑥𝑖𝑗 určující, zda 𝑖−tá jednotka z 
    první skupiny bude přiřazena 𝑗−té jednotce ze 
    skupiny druhé.

    𝑖 = 1, 2, …, 𝑛

    𝑗 = 1, 2, …, 𝑛

    𝑖 = 𝑗

    n … počet jednotek ve skupinách
    """
    result = 0
    for connection in enumerate(connections):
        prefrence = 0
        for cost in enumerate(costs[connection[0]]):
            prefrence += cost[1] * connection[1][cost[0]]
        result += prefrence
    return result

###########################################################################q
# Testy

def test_winner() -> None:
    """Prověrka definice funkce winner()."""
    roshambo.allowed = 'knp'
    expected = 0, -1, +1,   +1, 0, -1,   -1, +1, 0
    for i, (u, c) in enumerate((('k', 'k'), ('k', 'n'), ('k', 'p'),
                                ('n', 'k'), ('n', 'n'), ('n', 'p'),
                                ('p', 'k'), ('p', 'n'), ('p', 'p'))):
        w = winner(u, c)
        print(f'{u} x {c} = {w:+} - '
              f'{"SPRÁVNĚ" if w==expected[i] else "=CHYBA="}')


def test_roshambo() -> None:
    """Prověrka definice funkce roshambo()."""
    import builtins as b
    b_input = b.input
    b.input = dbg.input
    dbg.INPUTS = ('k', 'k', 'k', 'n', 'n', 'n', 'n', 'p', 'p', 'p', '')
    #              0    1    2    0    1    1    2    2    0    1
    expected   = ( 0,  -1,  +1,  +1,   0,   0,  -1,   0,  -1,  +1, None)
    import random
    dbg.TST = 1
    random.seed(43)
    dbg.TST = 1
    roshambo()
    b.input = b_input
    dbg.TST = 0


def test_my_function_4() -> None:
    """
    Prověrka definice funkce my_function_4().

    Pozn.: očekáváná hodnota funkce je 34, protože jsem použil data
    z domácího úkolu, tedy vím, že výsledek je správně.
    """
    # Test špatných dat
    result = my_function_4(
        ((3, 6, 1, 0, 0), (6, 3, 1, 0, 0), (0, 1, 1, 7, 1),
        (1, 0, 7, 1, 1), (0, 0, 0, 2, 8)),

        ((0, 1, 0, 0, 0), (1, 0, 0, 0, 0), (0, 0, 0, 1, 0),
        (0, 0, 1, 0, 0))
    )
    print(f"Výsledek účelové funkce: {result} "
    + f'{"SPRÁVNĚ" if result==34 else "=CHYBA="} (očekáváná hodnota 34)')
    # Test správných dat
    result = my_function_4(
        ((3, 6, 1, 0, 0), (6, 3, 1, 0, 0), (0, 1, 1, 7, 1),
        (1, 0, 7, 1, 1), (0, 0, 0, 2, 8)),

        ((0, 1, 0, 0, 0), (1, 0, 0, 0, 0), (0, 0, 0, 1, 0),
        (0, 0, 1, 0, 0), (0, 0, 0, 0, 1))
    )
    print(f"Výsledek účelové funkce: {result} "
    + f'{"SPRÁVNĚ" if result==34 else "=CHYBA="} (očekáváná hodnota 34)')


###########################################################################q
dbg.stop_mod(1, __name__)
