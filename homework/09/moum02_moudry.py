#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_DU_Assignment/DU_09_test.py
"""
Zadání domácího úkolu, v němž má student(ka) zadat několik testových otázek
k doposud probrané látce. Převzatý komentář - já na dokumentaci kašlu.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'MOUM02'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
AUTHOR_NAME = 'MOUDRÝ Michal'

# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
Žádné
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
    Q('Je string možným zdrojem hodnot?',
      (A(1, 'Ano'),
       A(0, 'Ne'),
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
      (A(1, 'get(key, default=None)'),
       A(1, 'popitem()'),
       A(1, 'pop(key, default=None)'),
       A(0, 'containskey(key)'),
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
       A(0, 'Kód skončí chybou'),
       A(1, 'Výpis sudých čísel od stovky dolu, přičemž vypsaná čísla '
            'jsou v intervalu (0, 100>'),
    )),
    Q('Pátá otázka',
      (A(1, 'ANO - První'),
       A(1, 'ANO - Druhá'),
       A(0, 'NE  - Třetí'),
       A(1, 'ANO - Čtvrtá'),
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
