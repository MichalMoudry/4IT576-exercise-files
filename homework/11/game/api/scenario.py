#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Třídy pro konstrukci scénářů:
    ScenarioStep
    Scenario

Definované proměnné:
    next_index      - Index následujícího kroku
    HAPPY_NAME      - Povinný název šťastného scénáře
    MISTAKE_NAME    - Povinný název chybového scénáře
    MISTAKE_NS_NAME - Povinný název chybového scénáře rozšiřujících akcí
    START_NAME      - Doporučený název scénáře obsahujícího pouze povinné
                      akce, tj. scénáře přidávaného na počátku vývoje hry
    SCENARIO_NAMES  - N-tice výš zmíněných názvů scénářů

"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from collections import namedtuple
from .scen_types import TypeOfScenario, TypeOfStep



############################################################################

# Definuje pomocnou třídu pojmenovanou ScenarioStep
_Step = namedtuple('ScenarioStep', 'index typeOfStep command message '
                                   'place neighbors items bag')

def ScenarioStep(typeOfStep:TypeOfStep, command:str, message:str, place:str,
                 neighbors:tuple[str], items:tuple[str], bag:tuple[str]):
    """Funkce vystupuje vůči okolnímu programu jako konstruktor,
    který vytváří instance třídy ScenarioStep, přičemž očekává argumenty:
    typeOfStep:TypeOfStep   - Typ kroku scénáře
    command:str             - Zadávaný příkaz
    message:str             - Odpověď hry
    place:str               - Název aktuálního prostoru
    neighbors:tuple[str]    - Aktuální sousedé aktuálního prostoru
    items:tuple[str]        - Aktuální předměty v aktuálním prostoru
    bag:tuple[str]          - Aktuální předměty v batohu
    """
    result = ScenarioStep.new(ScenarioStep.next_index, typeOfStep,
             command, message, place, neighbors, items, bag)
    # Původní konstruktor pojmenovaných n-tic nevyhovuje, protože
    # po každém kroku je třeba inkrementovat index následujícího kroku
    ScenarioStep.next_index += 1
    return result

# Odkaz na konstruktor třídy ukládáme do atributu funkce
ScenarioStep.new = _Step
del _Step

# Atribut next_index zadává vypisovaný index následujícího kroku, jenž
# je vhodné inicializovat vždy při zadávání počátečního kroku scénáře
ScenarioStep.next_index = 0

def __repr__(self):     # Název v rámci modulu nekoliduje
    return (f'{self.index}. krok: {self.command}\n{30*"-"}\n'
            f'{self.message}\n{60*"-"}\n'
            f'Aktuální prostor:    {self.place}\n'
            f'Sousedé prostoru:    {self.neighbors}\n'
            f'Předměty v prostoru: {self.items}\n'
            f'Předměty v batohu:   {self.bag}\n{60*"="}\n')

# Funkci přiřadíme jako atribut třídě pojmenované n-tice
ScenarioStep.new.__repr__ = __repr__
del __repr__   # Smažu dočasnou proměnnou



############################################################################

class Scenario:
    """Třída scénářů definujících požadované chování hry.
    """
    print_state = False     # Zda při testu průběžně zobrazovat stav

    def __init__(self, name:str, scenario_type:TypeOfScenario,
                 steps:tuple[ScenarioStep]|list[ScenarioStep]):
        self._type = scenario_type
        self._name = (name if scenario_type.ordinal > 2
                      else SCENARIO_NAMES[scenario_type.ordinal])
        self._steps = steps


    def __repr__(self) -> str:
        """Jako systémový podpis daného scénáře vrátí jeho název.
        """
        return self._name


    @property
    def name(self) -> str:
        """Vrátí název daného scénáře.
        """
        return self._name


    @property
    def steps(self) -> tuple['ScenarioStep']:
        """Vrátí n-tici kroků daného scénáře.
        """
        return self._steps


    @property
    def type(self) -> TypeOfScenario:
        """Vrátí typ daného scénáře.
        """
        return self._type


    def simulate(self, with_state:bool=False) -> None:
        """Vytiskne jednoduchou simulaci běhu hry podle šťastného scénáře,
        přičemž hodnota argumentu with_state určuje,
        zda se v každém kroku zobrazí pouze příkaz a odpověď hry (False),
        anebo se navíc vytisknou informace o požadovaném stavu hry
        po provedeném kroku (True).
        """
        print(f'\nSimulace scénáře: {self._name}\n{60*"#"}')
        for step in self.steps:
            if with_state:
                print(step)
            else:
                print(f'{step.index}. {step.command}\n{30*"-"}\n'
                      f'{step.message}\n{60*"="}\n')
        input(f'{60*"#"}\n=== Konec simulace scénáře {self._name} ===\n\n'
              f'Stiskněte Enter')



############################################################################

HAPPY_NAME      = "HAPPY"
MISTAKE_NAME    = "MISTAKES"
MISTAKE_NS_NAME = "MISTAKES_NS"
START_NAME      = "START"

SCENARIO_NAMES  = (HAPPY_NAME, MISTAKE_NAME, MISTAKE_NS_NAME, START_NAME)



############################################################################
dbg.stop_mod(0, __name__)
