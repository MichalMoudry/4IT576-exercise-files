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

###########################################################################q
# Pomocné funkce

def convert(number: int) -> str:
  """
  Funkce pro převod čísla.
  """
  result = ""
  length = len(str(number))
  if length == 1:
    result += convert_single_digit_number(number)
  elif number > 9 and number < 20:
    result += conver_special_number(number)
  elif length == 2:
    result += convert_two_digit_number(number)
  elif length == 3:
    result += convert_three_digit_number(number)
  return result

def conver_special_number(number: int) -> str:
  """
  Funkce pro převod čísla v rozmezí 10 - 19.
  """
  strings = ("deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
  "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct")
  return strings[int(str(number)[1])]

def convert_single_digit_number(digit: int) -> str:
  """
  Funkce pro převod jednoho čísla. Podmínkou je,
  že argument funkce je číslo.
  """
  strings = ("nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm",
  "osm", "devět")
  return strings[digit]

def convert_two_digit_number(number: int) -> str:
  """
  Funkce pro převod dvou místného čísla, které je v rozmezí 20 - 99.
  Podmínkou je, že argument funkce je číslo.
  """
  strings = ("dvacet", "třicet", "čtyřicet", "padesát", "šedesát",
  "sedmdesát", "osmdesát", "devadesát")
  first_part = strings[int(str(number)[0]) - 2]
  second_part = f" {convert_single_digit_number(int(str(number)[1]))}"
  if second_part == " nula":
    second_part = ""
  return f"{first_part}{second_part}"

def convert_three_digit_number(number: int) -> str:
  """
  Funkce pro převod tří místného čísla, které je v rozmezí 100 - 999.
  Podmínkou je, že argument funkce je číslo.
  """
  strings = ("jedno sto", "dvě stě", "tři sta", "čtyři sta", "pět set",
  "šest set", "sedm set", "osm set", "devět set")
  first_part = strings[int(str(number)[0]) - 1]
  second_part = ""
  if str(number)[1] == "0":
    second_part = convert_single_digit_number(int(str(number)[2]))
  elif str(number)[1] == "1":
    second_part = conver_special_number(int(str(number)[1:3]))
  else:
    second_part = convert_two_digit_number(int(str(number)[1:3]))
  if second_part == "nula":
    second_part = ""
  return f"{first_part} {second_part}"

def check_if_input_is_number(n: int) -> bool:
  """
  Funkce pro prověření, zda hodnota je číslo nebo ne.
  """
  try:
    n = int(n)
    return True
  except:
    return False

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
    if not(check_if_input_is_number(n)): print("Vstup není číslo"); return
    if n > MAX_NUM: print("Vložené číslo je příliš velké"); return
    result = ""
    if n < 0: result += "minus "; n = -(n)
    result += convert(n)
    return result



###########################################################################q
# Testy

def test_number_in_words() -> None:
    """Prověrka definice funkce number_in_words()."""
    import random
    random.seed(66)
    random_number = random.randint(0, 10**6-1)
    for number in test_numbers:
      print(number, number_in_words(number),
      "=SPRÁVNĚ=" if number_in_words(number) == test_numbers[number] else "=ŠPATNĚ=")



###########################################################################q
dbg.stop_mod(1, __name__)
