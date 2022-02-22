#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_02__Karel.py
"""
Příkazy zadávané ve výpisech kapitoly:
P02. Knihovny, Karel, rozhodování
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q



#Stránka 1.2.1	Příklady definice funkce
###########################################################################q
def jednořádková(): print('Volána jednořádková funkce')

def víceřádková():
    print('První příkaz')
    print('Druhý příkaz')
    print('Třetí příkaz')

jednořádková()
víceřádková()



#Stránka 1.2.2	Funkce a její atributy
###########################################################################q
def fce():  fce.call+=1;  print(f'Funkce volána {fce.call} krát')

fce.call = 0  # Atribut funkce, v němž bude pořadí volání
fce()
xxx = fce;   xxx()



#Stránka 1.2.4	Příklad: definice funkce pozdrav()
###########################################################################q
def pozdrav():
    """Zjistí požadované oslovení a popřeje dobrý den."""
    oslovení = input('Jak vás mám oslovovat? ')
    print('Dobrý den,', oslovení)

pozdrav()    # Volání definované funkce
šéfe
help(pozdrav)
pozdrav.__doc__



#Stránka 1.5	Definice prázdné funkce
###########################################################################q
def prázdná_s_dokumentací(): """Dokumentační komentář."""

def prázdná_s_výpustkou(): ...

def prázdná_s_příkazem_pass(): pass

prázdná_s_dokumentací()
prázdná_s_výpustkou()
prázdná_s_příkazem_pass()



#Stránka 2.2	Parametr, argument, anotace
###########################################################################q
def anot_demo(počet:int, string:str) -> str:
    return počet * string



#Stránka 2.2.1	Zjištění anotací
###########################################################################q
anot_demo.__annotations__



#Stránka 2.3.1	Příklad 1 – povolená zadání
###########################################################################q
def pos_key_demo(p1, p2, p3, p4='Nezadán', p5='Nezadán'):
    """Pomocná funkce pro demonstraci možností
    zadávání argumentů."""
    print(f'{p1=}, {p2=}, {p3=}, {p4=}, {p5=}')

pos_key_demo('a1', 'a2', 'a3', 'a4')
pos_key_demo(10, 20, p5=55, p3=33)



#Stránka 2.3.2	Příklad 2 – chybné zadání
###########################################################################q
pos_key_demo(10, 30, p5=55, p2=22)



#Stránka 2.5	Povinně poziční, resp. pojmenované argumenty
###########################################################################q
def fce(pos1, pos2=2, /, gen1=11, gen2=22, *, kwd1=111, kwd2=222):
    """První dva argumenty jsou povinně poziční,
    druhé dva nemají specifikován povinný způsob zadávání
    a poslední dva jsou povinně pojmenované.
    Povinně zadaný musí být pouze argument pos1."""
    print(f'{pos1=}, {pos2=}, {gen1=}, {gen2=}, {kwd1=}, {kwd2=}')



#Stránka 2.5.1	Příklady užití výše definované funkce
###########################################################################q
fce(1, 2, 10, 20, kwd1=110, kwd2=220)
fce(1, 2, 10, gen2=21, kwd1=111, kwd2=221)
fce(1, 2, gen1=12, gen2=22, kwd1=112, kwd2=222)



#Stránka 2.5.2	Volání funkce jako argument
###########################################################################q
def dotaz() -> str:
    return input('Jak vás mám oslovovat? ')

def pozdrav(oslovení: str) -> None:
    print(f'Dobrý den {oslovení}')

pozdrav(dotaz())
kámo



#Stránka 4.3.1	Příklady vytvoření světa s robotem
###########################################################################q
from robotcz import *
new_world(1,5)    # Prázdný svět o jednom řádku a pěti sloupcích
new_world('0123456789', # Svět o dvou řádcích a deseti sloupcích
          ' .:…∷…:. #') # s políčky obsahujícími značky nebo zeď
k = Karel()     # Umístí robota do levého dolního rohu
_               # Tisk podpisu naposledy vytvořeného světa



#Stránka 4.5.1	Demonstrace akcí
###########################################################################q
step(k)            # Posune robota o krok vpřed
turn_left(k)       # Otočí robota vlevo
put(k); step(k)    # Položí značku a popojde
pick(k); turn_left(k); step(k)  # Zvedne, otočí se a popojde
step(k)  # Pokusí se posunout o krok vpřed do okrajové zdi



#Stránka 4.6.1	Demonstrace testů
###########################################################################q
is_wall(k)                  # Stojí čelem k okrajové zdi
turn_left(k);   is_wall(k)  # Nyní má před sebou volno
is_east(k)                  # Hledí na jih
turn_left(k);   is_east(k)  # Po otočce hledí na východ
r = Karel(-1,-2)    # Nový robot vpravo před zdí
robot_before(r)     # Před ním je zeď, ne robot => vrátí None
is_wall(r)          # Testuje neokrajovou zeď



#Stránka 4.7.1	Demonstrace zakrytí a odkrytí
###########################################################################q
turn_left(k);  turn_left(k);  turn_left(k)  # Pomalá vpravo
def turn_right(k:Karel) -> Karel:
    """Otočí zadaného robota rychle vpravo."""
    hide(k)   # Další akce budou prováděny rychle a tajně
    turn_left(k);  turn_left(k);  turn_left(k)
    unhide(k) # Vracíme se k pomalému, veřejnému provádění
    return k

k; turn_right(k)       # Rychlá otočka vpravo



#Stránka 4.7.2	Vnoření příkazů k zakrytí a odkrytí
###########################################################################q
def turn_about(k:Karel) -> Karel:
    """Otočí zadaného robota čelem vzad."""
    hide(k)    # Zapínáme zrychlené provádění
    turn_left(k);  turn_left(k)
    unhide(k)  # Vracíme se k veřejnému provádění
    return k

def step_back(k:Karel) -> Karel:
    """Udělá se zadaným robotem krok zpět."""
    hide(k)    # Zapínáme zrychlené provádění
    turn_about(k);  step(k);  turn_about(k)
    unhide(k)  # Vracíme se k veřejnému provádění
    return k

turn_about(k); step_back(r)  # První se otočí, druhý couvne



#Stránka 5.2.1	Asociativita binárních operátorů – příklady
###########################################################################q
(16 / 4 / 2)  ==  ((16 / 4) / 2)  ==  (4 / 2)  ==  2
4 ** 3 ** 2  ==  4 ** (3 ** 2) == 4 ** 9 == 262_144
a = (b := c := 7)
a = (b := (c := 7)); a, b, c



#Stránka 6.2.1	Porovnání reálných čísel
###########################################################################q
c1 = (100 * 0.1) / 3
c2 = (100 / 3) * 0.1
c1 - c2



#Stránka 6.2.2	Zřetězené porovnávání
###########################################################################q
1 < 5 < 17 < 99
25 < 125 > 100
1  <  12  < 123  <  1234  <  12345



#Stránka 6.2.3	Porovnávání textů
###########################################################################q
'a'  >  'B'  <  'C'  <  'č'  >  'd'



#Stránka 6.2.4	Porovnávání totožnosti objektů
###########################################################################q
a = 'Dobrý ';   b = 'den!';   ab = a + b
print(f'''\
Objekty:   {ab = },   {a+b = }
Rovnost:   {ab == (a+b) = }
Totožnost: {ab is (a+b) = }'''
    )



#Stránka 6.3.1	Příklady s logickými operátory
###########################################################################q
(a := 5 > 3)      #Výsledek je uložen v proměnné
not a
'' and 'cokoliv'  #Levý operand je False => Levý
1 and 'R'         #Levý operand je True => Pravý
'' or 'cokoliv'   #Levý operand je False => Pravý
1 or ''           #Levý operand je True => Levý
# Hodnoty prvních tří operandů jsou False =>
# => výsledkem je hodnota posledního
not a or 0 or "" or "poslední"



#Stránka 6.3.2	Příklad: funkce free_before()
###########################################################################q
from robotcz import *
def free_before(k:Karel) -> bool:
    """Zjistí, zda je pole před zadaným robotem volné."""
    return not(is_wall(k) or robot_before(k))

w=new_world(1, 5);    k1=Karel();    k2=Karel(col=1);    w
k1,; k2,        free_before(k2)    # Otočen na východ: volno
turn_left(k2),  free_before(k2)    # Otočen na sever: zeď
turn_left(k2),  free_before(k2)    # Otočen na západ, je před ním robot



#Stránka 7.1	Podmíněný výraz
###########################################################################q
def ifExpr(value) -> str:
    """Nahradí znaménko jeho slovním vyjádřením."""
    return (('plus ' if value > 0 else 'minus ')
         +  str(abs(value)))

f'{ifExpr(+5) = },     {ifExpr(-5) = }'



#Stránka 7.3	Jednoduchý podmíněný příkaz
###########################################################################q
def ifThen(číslo):
    znam = 'plus '
    if číslo < 0:
        znam  = 'minus '
        číslo = -číslo
    return znam + str(číslo)

ifThen(5), ifThen(-5)



#Stránka 7.3.1	Příklad: opatrný krok – cautious_step
###########################################################################q
def cautious_step(k:Karel) -> Karel:
    """Popojde s robotem vpřed jen je-li to možné."""
    if free_before(k):
        step(k)
    return k

w = new_world(1, 5);   k1 = Karel();   k2 = Karel(col=2)
k1; cautious_step(k1);  cautious_step(k1);
turn_left(k1);   cautious_step(k1)
turn_left(k1);   cautious_step(k1)



#Stránka 7.3.2	Zvýraznění vypnutí a zapnutí viditelnosti
###########################################################################q
def turn_right(k:Karel) -> Karel:
    """Otočí zadaného robota rychle vpravo."""
    if hide(k): # Rychle prováděné akce se odsadí jako tělo
        turn_left(k)
        turn_left(k)
        turn_left(k)
    unhide(k)
    return k

turn_right(k1)       # Rychlá otočka vpravo



#Stránka 7.3.3	Funkce are_2_markers() a zanořování bloků
###########################################################################q
def are_2_markers(k:Karel) -> bool:
    """Zjistí, zda jsou pod robotem právě dvě značky."""
    result = False
    if is_marker(k):
        pick(k)             # Zvedne první značku
        if is_marker(k):
            pick(k)         # Zvedne druhou značku
            result = not is_marker(k)   # Třetí by už byla moc
            put(k)          # Položí druhou značku
        put(k)              # Položí první značku
    return result

def a2m(): result=are_2_markers(k); step(k); return result

w=new_world('012345');  k=Karel()
a2m(), a2m(), a2m(), a2m(), a2m(),



#Stránka 7.4	Úplný podmíněný příkaz
###########################################################################q
def ifElse(číslo):
    if číslo > 0:
        text = "plus " \
             + str(číslo)
    else:
        text = ("minus "
             + str(-číslo))
    return text

ifElse(5), ifElse(-5)



#Stránka 7.5.1	Více větví – definice funkce
###########################################################################q
def jabloň(sezóna):
    """Demonstrace použití rozšířeného podmíněného příkazu."""
    if   sezóna == 'zima':  činnost = 'spí'
    elif sezóna == 'jaro':  činnost = 'kvete'
    elif sezóna == 'léto':
         činnost = 'zraje'
    elif sezóna == 'podzim':
         činnost= 'plodí'
    else:
         return f'Špatně zadaná sezóna: {sezóna}'
    return f'Je-li {sezóna}, jabloň {činnost}'

print(f"{jabloň('jaro')}\n{jabloň('podzim')}\n{jabloň('nevím')}")



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
