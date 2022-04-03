#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul testuje správné zapracování modifikace s kódem »21w01«,
požadující upravit odevzdaný program následovně:

Na konec každé zprávy vypisované jako odpověď hry na zadání příkazu
přidá oproti standardní hře na konec odpovědi řádek s textem:

§Doposud zadáno: ['name1', 'name2', 'name3', ..., 'nameN']

kde v hranatých závorkách bude uveden abecedně seřazený seznam
čárkami oddělených a na malá písmena převedených názvů akcí,
které hráč během aktuální hry doposud zadal.
Názvy opakovaně zadaných akcí se nebudou opakovat.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api.interfaces import IInterface, IGame
from ..api.scen_types import tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN
from ..api.scenario   import ScenarioStep, Scenario
from .common.errors   import error
from .common.types    import Visitor



############################################################################

class Visitor_z01(Visitor):
    """Pomáhá kontrolovat správnost řešení popsaného v dokumentaci modulu.
    """

    def __init__(self, factory:IInterface):
        super().__init__(factory)


    def after_game_start(self, scenario:Scenario):
        """ Akce, která se má provést po provedení startovacího kroku hry
        (tj. ve chvíli, kde je hra již inicializována), ale před jeho testem,
        tj. před ověřením, že stav hry odpovídá scénáři.
        Prověří, že hra deklaruje právě ty akce, které jsou deklarované
        ve scénářích a uloží seznam jejich abecedně seřazených názvů.
        """
        super().after_game_start(scenario)
        # Porovná úvodní hlášení hry se situací odvozenou ze scénářů

        # Nastaví výchozí stav potřebných proměnných
        self._entered = []


    def after_step_test(self, step:ScenarioStep, answer:str):
        """Akce, která se má provést po testu aktuálního kroku.
        """
        if step.typeOfStep == tsNOT_START:
            return
        # Aktualizuje  potřebné proměnné
        command = step.command
        words   = command.strip().split()
        if not (step.typeOfStep in NO_COMMAND):
            action_name = words[0].lower()
            if action_name not in self._entered:
                self._entered.append(action_name)
                self._entered.sort()
        # Najde a zkontroluje poslední řádek
        parts  = answer.split('\n')
        last_line = parts[-1]
        if not last_line.startswith(START):
            error('Závěrečný řádek nemá požadovaný začátek',
                  self.scenario, step, self.game, START, last_line)
        rest     = last_line[len(START):].strip()
        required = str(self._entered)
        if rest != required:
            error('Seznamy si neodpovídají',
                  self.scenario, step, self.game, required, rest)





############################################################################

TEST_ID     = '21w01'
NO_COMMAND  = {tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN, }
START       = '§Doposud zadáno: '



############################################################################

# from .test_scenario import test_scenarios_from as tsf

def test(factory):
    from  .test_interface   import test as ti
    from ..tests            import Level
    ti(factory, Level.z01)



############################################################################

# from ..z11_no_entered import factory as f
# tf.test(f, 3)



############################################################################
dbg.stop_mod(0, __name__)
