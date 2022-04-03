#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul testuje správné zapracování modifikace s kódem »21w12«,
požadující upravit odevzdaný program následovně:

Na konec každé zprávy vypisované jako odpověď hry na zadání příkazu
přidá oproti standardní hře na konec odpovědi řádek s textem:

§Dosud nenavštíveno: ['name1', 'name2', 'name3', ..., 'nameN']

kde v hranatých závorkách bude uveden abecedně seřazený seznam
čárkami oddělených a na malá písmena převedených názvů prostorů,
které hráč během aktuální hry ještě nenavštívil.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api.interfaces import IInterface, IGame
from ..api.scen_types import tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN
from ..api.scenario   import ScenarioStep, Scenario
from .                import test_scenario
from .common.errors   import error
from .common.types    import Visitor
from .common.utils    import compare_containers



############################################################################

class Visitor_z12(Visitor):
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
        if not compare_containers(test_scenario._all_mentioned_places,
                                  self.game.world().places()):
            error('Seznam prostorů hry', scenario, scenario.steps[0],
                  self.game, compare_containers.from_scenario,
                             compare_containers.from_game)
        # Nastaví výchozí stav potřebných proměnných
        self.not_visited = compare_containers.from_game
        self.not_visited.remove(self.game.world().current_place().name.lower())


    def after_step_test(self, step:ScenarioStep, answer:str):
        """Akce, která se má provést po testu aktuálního kroku.
        """
        if step.typeOfStep == tsNOT_START:
            return
        # Aktualizuje  potřebné proměnné
        current_place_name = self.game.world().current_place().name.lower()
        if current_place_name in self.not_visited:
            self.not_visited.remove(current_place_name)
        # Najde a zkontroluje poslední řádek
        parts  = answer.split('\n')
        last_line = parts[-1]
        if not last_line.startswith(START):
            error('Závěrečný řádek nemá požadovaný začátek',
                  self.scenario, step, self.game, START, last_line)
        rest     = last_line[len(START):].strip().lower()
        required = str(self.not_visited)
        if rest != required:
            error('Seznamy nenavštívených prostorů si neodpovídají',
                  self.scenario, step, self.game, required, rest)



############################################################################

TEST_ID     = "21w12"
NO_COMMAND  = {tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN, }
START       = "§Dosud nenavštíveno: "



############################################################################

# from .test_scenario import test_scenarios_from as tsf

def test(factory):
    from  .test_interface   import test as ti
    from ..tests            import Level
    ti(factory, Level.z12)



############################################################################

# from ..z11_no_entered import factory as f
# tf.test(f, 3)



############################################################################
dbg.stop_mod(0, __name__)
