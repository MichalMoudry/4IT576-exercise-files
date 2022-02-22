#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_02__Karel.py
"""
Příkazy zadávané ve výpisech kapitoly:
P02. Knihovny, Karel, rozhodování
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q



#Stránka 1.2.1	Příklad: želva a želví grafika
###########################################################################q
turtle.Turtle()   # Před importem jsou atributy nepoužitelné
import turtle        # Importujeme modul
t = turtle.Turtle()  # Vytvoříme instanci želvy
t.forward(50)        # Želva se hýbe
t.left(90)
t.forward(50)



#Stránka 1.3	Přímý import vyjmenovaných objektů
###########################################################################q
from turtle import Turtle as Želva      # Proměnná Želva
žž = Želva()            #odkazuje na třídu turtle.Turtle
žž.right(90); žž.forward(50)        # Nakreslí čáru dolů



#Stránka 1.5.1	Šablona modulů v doprovodných programech
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/p4_00a_module_template.py
"""



#Stránka 1.5.2	Tělo modulu  p4_02a_ModuleDemo
###########################################################################q
"""
Je uloženo v souboru
#O:/p4_INP/p4_02a_ModuleDemo.py
"""



#Stránka 1.5.3	Práce s vytvořeným modulem
###########################################################################q
import p4_02a_ModuleDemo as m
m       # Systémový podpis načteného modulu
m.text
m.m_fce()



#Stránka 1.5.4	Hvězdičkový import
###########################################################################q
text
from p4_02a_ModuleDemo import text
text
m.text = 'Modifikovaný' + text
print(f'{m.text = }\n{text   = }')
from p4_02a_ModuleDemo import text  # Nové přiřazení hodnoty
text



#Stránka 1.6.1	Ukázka opětovného načtení
###########################################################################q
import p4_02a_ModuleDemo as m2
m2.text   # Nic se nenačetlo, jedná se o původní modul


from importlib import reload
reload(m)



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
