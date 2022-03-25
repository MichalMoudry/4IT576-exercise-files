#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Zadání domácího úkolu, v němž má student(ka) demonstrovat zvládnutí
doposud probrané látky prostřednictvím realizace převodníku čísla na string.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q
# Identifikační a informační konstanty

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'MOUM02'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
AUTHOR_NAME = 'MOUDRÝ Michal'

# Zdroje, z nichž autor(ka) čerpal(a) při řešení úkolu
SOURCES = """\
???
"""

# Problémy, které se vyskytly při zpracování probrané látky a řešení DU
PROBLEMS = """\
Prezentace
"""

# Poznámky a připomínky k výkladu
COMMENTS = """\
Žádné
"""

# Největší číslo, které je váš program schopen korektně převést
# Číslo si můžete nastavit sami,
# ale mělo by být alespoň 10**6-1, tj. 999_999
MAX_NUM:int = 2**64-1   # Zde největší číslo typu long z jiných jazyků


############################################################################
# Testovací data

# Tuto konstantu neupravujte. Netroufáte-li si na kompletní převodník,
# definujte program, kterým správně projde jen prvních 15 z nich,
# tj do čísla 505_000 včetně.
# Nezapomeňte ale zprávě nastavit konstantu MAX_NUM
test_numbers = {
        0 : 'nula',
        1 : 'jedna',
       11 : 'jedenáct',
       15 : 'patnáct',
       20 : 'dvacet',
       21 : 'dvacet jedna',
       44 : 'čtyřicet čtyři',
      100 : 'jedno sto',
      106 : 'jedno sto šest',
      270 : 'dvě stě sedmdesát',
      488 : 'čtyři sta osmdesát osm',
    1_234 : 'jeden tisíc dvě stě třicet čtyři',
    2_000 : 'dva tisíce',
  202_000 : 'dvě stě dva tisíce',
  505_000 : 'pět set pět tisíc',
2_345_678 : 'dva miliony tři sta čtyřicet pět tisíc šest set sedmdesát osm',
1_004_000 : 'jeden milion jeden tisíc jedna',
 1_001_001_001_001_001_001 : ('jeden trilion jedna biliarda jeden bilion '
            'jedna miliarda jeden milion jeden tisíc jedna'),
 2_002_002_002_002_002_002 : ('dva triliony dvě biliardy dva biliony '
            'dvě miliardy dva miliony dva tisíce dva'),
 5_005_005_005_005_005_005 : ('pět trilionů pět biliard pět bilionů '
            'pět miliard pět milionů pět tisíc pět'),
-9_223_372_036_854_775_808 : ('minus devět trilionů '
            'dvě stě dvacet tři biliard tři sta sedmdesát dva bilionů '
            'třicet šest miliard osm set padesát čtyři milionů '
            'sedm set sedmdesát pět tisíc osm set osm')
}



###########################################################################q
# Požadované funkce

def number_in_words(n:int) -> str:
    """Převede zadané číslo na slovní vyjádření v češtině,
    přičemž největší převeditelné číslo definuje konstanta MAX_NUM
    """



###########################################################################q
# Testy

def test_number_in_words() -> None:
    """Prověrka definice funkce number_in_words()."""



###########################################################################q
dbg.stop_mod(1, __name__)
