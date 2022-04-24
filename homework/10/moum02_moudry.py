#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul s řešením domácího úkolu č. 10.

Zadání domácího úkolu:
  V souboru upravte definici n-tice questions tak, aby obsahovala vámi
  navržené otázky, přičemž jednotlivé otázky budou definovány
  jako instance třídy question_test.Question,
  na níž odkazuje importovaná proměnná Q.

  Ke každé otázce budou nabídnuty nejméně čtyři odpovědi, přičemž
  jednotlivé odpovědibudou definovány jako instance třídy
  question_test.Answer,na níž odkazuje importovaná proměnná A.
  Vše demonstruje definice n-tice questions, jejíž prvky nahradíte
  vlastními. Její funkci si můžete vyzkoušet spuštěním funkce
  self_test() umístěné na konci modulu.
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

from question_test import * # A, Q, test_seq



###########################################################################q
# Řešení

questions = (
  Q("Jaký systémový atribut odkazuje na na string reprezentující"
    " název modulu?",
    (A(0, "__file__"),
    A(1, "__name__"),
    A(0, "__doc__"),
    A(0, "__package__")
  )),
  Q("Co lze považovat za výraz?",
    (A(0, "Přiřazení hodnoty do proměnné"),
    A(1, "Volání funkce"),
    A(1, "Zadání hodnoty (literál nebo název proměnné)"),
    A(1, "Operace s hodnotami, které samy mohou být výsledkem výrazů")
  )),
  Q("Jaký je správný syntax formátovacích stringů v jazyce Python?",
    (A(0, '$"{nazev_promenne}"'),
    A(0, 'format!("test value: {}", 6 + 10)'),
    A(1, "F'{6 + 4}'"),
    A(1, "f'{30 ** 10}'")
  )),
  Q("Co bude vypsáno do konzole pomocí tohoto kódu?\n"
    """
    x, y, z = "test", 15, 23.17

    y, z, x = x, 17.83, z

    print(x, repr(y), z)
    """,
    (A(1, "23.17 'test' 17.83"),
    A(0, "test 15 23.17"),
    A(0, "'test' 15 23.17"),
    A(0, "Program vyhodí chybu")
  )),
  Q("Co vše platí o jazyku Python?",
    (A(1, "Všechno je objekt"),
    A(0, "Je staticky typovaný"),
    A(1, "Program je tvořen posloupností příkazů"),
    A(0, "Zdrojové soubory mají příponu .pyz")
  )),
  Q("Jaké soubory mají příponu .pyc?",
    (A(0, "Přeložené soubory určené pro spuštěné v okenním režimu"),
    A(1, "Přeložené soubory"),
    A(0, "Zdrojové soubory"),
    A(0, "Spustitelná komplexní aplikace")
  )),
  Q("Co bude vypsáno do konzole pomocí tohoto kódu?\n"
    """
    is_even = lambda number : number % 2 == 0

    print(is_even(3))
    """,
    (A(0, "True"),
    A(0, "Program vyhodí chybu"),
    A(0, "false"),
    A(1, "False")
  )),
  Q("",
    (A(0, ""),
    A(0, ""),
    A(0, ""),
    A(0, "")
  )),
  Q("",
    (A(0, ""),
    A(0, ""),
    A(0, ""),
    A(0, "")
  )),
  Q("",
    (A(0, ""),
    A(0, ""),
    A(0, ""),
    A(0, "")
  )),
)



###########################################################################q
#Test

def self_test():
    """Cvičně položí postupně všechny otázky z n-tice "collections"
    a vyhodnotí odpovědi na ně.
    """
    test_seq(questions)



###########################################################################q
dbg.stop_mod(1, __name__)
