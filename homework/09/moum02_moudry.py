#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul s řešením domácího úkolu č. 9.

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
    Q('Kolik je povinně pojmenovaných argumentů v následující metodě?'
      """
      def test_method(arg1, arg2, /, arg3, *, arg4):
        print("Hodnoty:")
        print((arg1, arg2, arg3, arg4))
      """,
      (A(0, '2'),
       A(1, '1'),
       A(0, '3'),
       A(0, 'Definice metody obsahuje syntaktickou chybu')
    )),
    Q('Co bude vypsáno do konzole pomocí tohoto kódu?\n'
      """
      for src in range(1, 5), range(5, 8), (9, 10):
      for x in src:
          if x < 5:
              print(x, end="")
      """,
      (A(0, '1\n2\n3\n4'),
       A(0, '1234'),
       A(1, 'Program vyhodí chybu'),
       A(0, '12345'),
    )),
    Q('Která z těchto metod neslouží pro práci s prvky slovníku?',
      (A(0, 'get(key, default=None)'),
       A(0, 'popitem()'),
       A(0, 'pop(key, default=None)'),
       A(1, 'containskey(key)'),
    )),
    Q('Co je výsledkem tohoto kódu?\n'
      """
      number = 100
      while number > 0:
          if number % 2 == 0:
              print(number)
          number -= 1
      """,
      (A(0, 'Výpis prvočísel z intervalu <0, 100>'),
       A(0, 'Výpis sudých čísel od nuly nahoru, přičemž vypsaná '
            'čísla jsou v intervalu (0, 100)'),
       A(1, 'Výpis sudých čísel od stovky dolu, přičemž vypsaná čísla '
            'jsou v intervalu (0, 100>'),
       A(0, 'Kód skončí chybou'),
    )),
    Q('Jak se mažou objekty v jazyce Python?',
      (A(1, 'del nazev_objektu'),
       A(0, 'delete nazev_objektu'),
       A(0, '_ = nazev_objetu'),
       A(0, 'drop(nazev_objektu)'),
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
