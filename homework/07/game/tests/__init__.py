#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""\
Balíček s testy hry v jednotlivých fázích vývoje.¤

Data:
    LIMITS          - Minimální povinné počty klíčových objektů

Třídy:
    Level           - Výčtový typ definující hladinu testování

Funkce:
    print_err_msg() - Tiskne zásobník s popisem aktuální chyby

Podbalíčky:
    common          - Balíček modulů s pomocnými programy

Moduly:
    test_factory    - Test továrního objektu
    test_scenario   - Test scénářů
    test_game       - Test hry

Soubory:


"""
import dbg
dbg.start_pkg(0, __name__, __doc__)
############################################################################

from collections import namedtuple

LIMITS = (namedtuple('Limits', 'minSteps minPlaces minVisited minNSActions')
          (12,  # Minimální počet kroků scénáře HAPPY
            6,  # Minimální počet prostorů
            4,  # Minimální počet navštívených prostorů
            4)) # Minimální počet vlastních (= nestandardních) akcí



############################################################################

from enum import IntEnum

class Level(IntEnum):
    """Hladiny podrobností testů.
    """
    FACTORY = 0 # Testuje se jenom tovární objekt
    HAPPY   = 1 # Očekává se jen šťastný scénář definovaný jako n-tice
    SCENARIOS=2 # Scénáře jsou definované jako instance třídy Scenario,
                # testuje se scénář startovní, šťastný, chybový
                # a chybový scénář nadstandardních akcí
    ARCHITECTURE=3# Testuje se přítomnost požadovaných objektů a metod
    START   = 4 # Testuje se, že se hra úspěšně odstartuje
    WORLD   = 5 # Testuje se, že hra úspěšně vybuduje svůj svět
    BASIC   = 6 # Testuje se zprovoznění základních akcí
    MISTAKES= 7 # Testuje se, že základní akce jsou navržené robustní
    WHOLE   = 8 # Testuje se úspěšné zprovoznění celé hry


    # Demonstrační rozšiřující zadání
    z00 = 8     # Výchozí stav totožný s kompletní hrou
    z01 = 101
    # Rozšiřující zadání popsaná v dokumentaci testovacího modulu
    z11 = 111;    z21 = 121
    z12 = 112;    z22 = 122
    z13 = 113;    z23 = 123
    z14 = 114;    z24 = 124
    z15 = 115;    z25 = 125
    z16 = 116;    z26 = 126
    z17 = 117;    z27 = 127
    z18 = 118;    z28 = 128
    z19 = 119;    z29 = 129

    # def __lt__(self, other): return self.value <  other.value
    # def __le__(self, other): return self.value <= other.value
    # def __ge__(self, other): return self.value >= other.value
    # def __gt__(self, other): return self.value >  other.value



############################################################################

from ..api.interfaces   import IInterface

def test(module:IInterface, ID:Level) -> bool:
    """Otestuje zadaný tovární objekt a jím poskytnuté objekty hry.
    Zprávu o testu tiskne na standardní výstup.
    """
    from .test_interface import test as ti
    ti(module, ID)



############################################################################

def print_err_msg():
    """Zjistí si aktuální chybu a vytiskne výpis zásobníku.
    """
    import sys, traceback as TB
    tbo = sys.exc_info()[2]
    TB.print_tb(tbo)



############################################################################
dbg.stop_mod(0, __name__)
