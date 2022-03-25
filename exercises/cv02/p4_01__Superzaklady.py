#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_01__Superzáklady.py
"""
Příkazy zadávané ve výpisech kapitoly:
01  Superzáklady
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q



#Stránka 2.3	Komentáře a počáteční mezery
###########################################################################q
123 + 456 #Před zadáním příkazu nesmí být zbytečná mezera
 432 - 10 #Tady jedna byla



#Stránka 2.4	Literály reálných čísel
###########################################################################q
123_456_789_0_123_456_789_0_123_456_789.
123e-3
123.
123e3



#Stránka 2.4.1	Nekonečna a nesmyslná čísla
###########################################################################q
float('INF'), float('-Inf'), -float('-inf'), float('NaN')
float('-inf') * -float('inf'),  float('inf')/float('inf')
123 / float('inf'), 123 / float('-inf'), -123 / float('-inf')



#Stránka 2.5	Literály komplexních čísel
###########################################################################q
1 + 1J
1+j  # Znak j nelze zapsat samotný
2j  #Imaginární čísla se v závorkách netisknou
0+3j



#Stránka 2.6	Stringové literály
###########################################################################q
"Text v uvozovkách"
'Text v apostrofech'
"Potřebuji 'apostrof'"
'Potřebuji "uvozovky"'



#Stránka 2.6.1	Víceřádkové stringy
###########################################################################q
"""několikařádkový
text"""
'''
Jiný způsob\
'zápisu'
'''
'''Musí být 'odděleny''''
""     #Dvojice uvozovek či apostrofů označuje prázdný string
"'Sousedící' stringové literály"  'Python "automaticky" sloučí'



#Stránka 2.8	Hodnota None
###########################################################################q
None
0



#Stránka 2.9	Hodnota Ellipsis
###########################################################################q
...



#Stránka 3.2	Program = posloupnost příkazů
###########################################################################q
2 ** 10;   0x400;    355/113



#Stránka 3.4.1	Vytvoření proměnné
###########################################################################q
a = 123     #Vytvářím a inicializuji novou proměnnou
a           #Nechávám zobrazit její hodnotu
a = a + x   #Proměnná x ještě není vytvořena
x = 456     #Vytvářím a současně inicializuji proměnnou x
a = a + x   #Proměnná x je již použitelná
a           #Obsah proměnné a se změnil



#Stránka 3.4.2	Nebezpečné změny hodnot
###########################################################################q
a = "Sto dvacet tři"  #Opět měním hodnotu proměnné a
x = a + x             #String není možné sčítat s číslem
b = 'miliónů'    #Vytvářím a inicializuji proměnnou b
a + b            #Dva stringy již sčítat mohu
a + ' ' + b
mezera = ' '
a + mezera + b



#Stránka 3.4.3	Pomocná proměnná _ a její využití
###########################################################################q
_   #Na počátku není proměnná definována
123 #Výsledek jsme neuložil => uložil se do proměnné _
_   #Už je definovaná, obsahuje neuložený výsledek
a = 7  #Nebylo třeba nic ukládat,
_      #a proto se její obsah nezměnil
456    #Nový neuložený výsledek změní hodnotu proměnné
_      #Už je tam nová hodnota



#Stránka 3.5.1	Příklady použití složeného přiřazení
###########################################################################q
a  = 1; b = 10; c = 100;
# Ekvivalent: b = b  * (a+c), tj. b = 10 * (100+1)
b *= a + c; b
c**= 2*a; c # Ekvivalent: c = c ** (2*a), tj. c = c ** 2
# Často se používá pro přičtení či odečtení jedničky
c += 1;  c



#Stránka 3.6	Volání funkcí
###########################################################################q
a = 123;   b = 'miliónů';   mezera = ' '
str(a) + mezera + b



#Stránka 3.6.1	Příklad: zadání údajů z klávesnice
###########################################################################q
input('Jak vás mám oslovovat? ')
Vaše blahorodí
print('Dobrý den,', _)



#Stránka 3.8.1	Použití formátovaných stringů
###########################################################################q
print(f'''\
Sčítání:{  6 + 4 = }, {'AB'+"CD"=};   Odčítání: {4-6=};
Násobení: {6 * 4 = }, {3*'21' = },{ '21' * 3 = };
Dělení:   {6/4=};  Celočíselné: {6//4=};  Zbytek: {6%4=};
Mocnění:  {6**4 = },  {36**2 = }
''')



#Stránka 3.9.1	Ukázka formátování f stringů
###########################################################################q
print(f'{(s1:="string")=} × s2={(s2:="STRING")};   '
      f's1={s1} × {s2=}')
print(f'{(s1:="string")=!s} × s2={(s2:="STRING")!r};   '
      f's1={s1!r} × {s2=!s}')



#Stránka 3.10	Zadání skupiny hodnot
###########################################################################q
x = y = z = 123
x, y, z
x, y, z = 10, 20, 30
x, y, z
z, x, y = x, y, z
x, y, z



#Stránka 3.10.1	N tice hodnot
###########################################################################q
1,       # Jednoprvková n tice
1,2,3,   # Použití čárky zavádí n tici i bez závorek
()       # Prázdná n-tice



#Stránka 3.11	Přiřazovací výraz
###########################################################################q
f'{(a:=5) = }'



#Stránka 3.12	Více příkazů na řádku × více výrazů na řádku
###########################################################################q
x = 'Přiřazovaná hodnota';   x
a = 1;   b = 10;   c = 100;   print(a, b, c)
(a := 11);   (b := 22);   print(f'{a=}, {b=}')
(a := 99),   (b := 88),   print(f'{a=}, {b=}')



#Stránka 4.2	Třída – instance – typ
###########################################################################q
print(f'{type(123) = }\n{type(1.0) = }\n{type("X") = }')



#Stránka 5.4.1	Příklad: želva a želví grafika
###########################################################################q
turtle.Turtle()   # Před importem jsou atributy nepoužitelné
import turtle        # Importujeme modul
t = turtle.Turtle()  # Vytvoříme instanci želvy
t.forward(50)        # Želva se hýbe
t.left(90)
t.forward(50)



#Stránka 5.5	Přímý import vyjmenovaných objektů
###########################################################################q
from turtle import Turtle as Želva      # Proměnná Želva
žž = Želva()            #odkazuje na třídu turtle.Turtle
žž.right(90); žž.forward(50)        # Nakreslí čáru dolů



#Stránka 6.1	Příklad: demonstrační modul p4_01a_Script
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/p4_01a_Script.py
"""



#Stránka 6.1.1	Import modulu p4_01a_Script
###########################################################################q
import p4_01a_Script

p4_01a_Script.pozdrav      # Atributy jiného modulu =>
p4_01a_Script.__name__     # => je třeba kvalifikovat
__name__   # Atributy aktuálního modulu se nekvalifikují



#Stránka 6.1.2	Spuštění skriptu z příkazového řádku
###########################################################################q
# p4_01a_Script.py



#Stránka 6.4.1	Šablona modulů v doprovodných programech
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/p4_00a_module_template.py
"""



#Stránka 6.4.2	Tělo modulu  p4_01b_ModuleDemo
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/p4_01b_ModuleDemo.py
"""



#Stránka 6.4.3	Práce s vytvořeným modulem
###########################################################################q
import p4_01b_ModuleDemo as m
m       # Systémový podpis načteného modulu
m.text  # Atribut importovaného modulu
m.dbg.prDict()



#Stránka 6.5	Přímý import a jeho vlastnosti
###########################################################################q
text
from p4_01b_ModuleDemo import text
text
m.text = 'Modifikovaný ' + text
print(f'{m.text = }\n{text   = }')
from p4_01b_ModuleDemo import text  # Nové přiřazení hodnoty
text



#Stránka 6.6	Hvězdičkový import
###########################################################################q
m.dbg.prDict() # Půjčím si atribut dbg modulu m, svůj nemám
from p4_01b_ModuleDemo import *  # Importuji všechny veřejné
dbg.prDict()  # Už ho mám, právě jsem jej importoval
m._text  # Explicitním zadáním získám i neveřejné atributy



#Stránka 7.1.1	Opětné načtení modulu p4_01b_ModuleDemo
###########################################################################q
import p4_01b_ModuleDemo as m2 # Objekt modulu již existuje =>
m2.text     # => nic se nenačetlo, atribut má původní hodnotu
from importlib import reload
reload(m)   # Argumentem je proměnná odkazující na modul
m2.text     # Atribut modulu se změnil
text        # Přímo importovaný atribut je beze změn



#Stránka 0.X:	Popisek
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/xxx.py
"""
#---------------------------------------------------------------------------
                                                                       #SYNC
###########################################################################q
dbg.stop_mod(1, __name__)
