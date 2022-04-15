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
    Q('První otázka',
      (A(1, 'ANO - První'),
       A(1, 'ANO - Druhá'),
       A(0, 'NE  - Třetí'),
       A(1, 'ANO - Čtvrtá'),
    )),
    Q('Druhá otázka',
      (A(0, 'Nepravdivá odpověď'),
       A(1, 'Pravdivá odpověď'),
       A(0, 'Jiná nepravdivá odpověď'),
       A(1, 'Odpověď, která je také pravdivá'),
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
