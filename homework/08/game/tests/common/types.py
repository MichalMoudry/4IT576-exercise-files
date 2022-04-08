#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""Balíček rodičů tříd používaných při testování
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ...api.scenario    import ScenarioStep, Scenario
from ...api.interfaces  import IInterface, IGame
from  ..                import test_scenario
from   .utils           import compare_containers
from   .errors          import error



############################################################################

class Visitor:
    """Rodič tříd návštěvníků testů.
    Definuje sadu funkcí požadovaných od návštěvníka testů
    schopných ovlivnit způsob testování hry podle jimi známých dispozic.

    Slouží především k tomu, aby bylo možno doplnit základní testy
    o doplňkové kontroly prověřující, zda byly správně zapracovány
    všechny úpravy vyžadované při obhajobách aplikace.

    Třída definuje všechny metody návštěvníka jako prázdné s tím,
    že pro každé zadání požadované modifikace pro obhajobu
    bude definován odpovídající potomek kontrolující správnost řešení.
    """

    def __init__(self, factory:IInterface):
        self.factory    = factory
        self.game:IGame = factory.game()


    @staticmethod
    def are_imperfect_scenarios_allowed(self):
        """Vrátí informaci o tom, je-li v prověřovaném zadání povoleno
        testování hry i v případě, kdy správce scénářů neprojde verifikací.
        """
        return False


    def before_game_start(self):
        """ Akce, která se má provést před spuštěním hry.
        Cílem metody je prověřit scénáře a případné další pomocné kódy.
        """


    def after_game_start(self, scenario:Scenario):
        """ Akce, která se má provést po provedení startovacího kroku hry
        (tj. ve chvíli, kde je hra již inicializována), ale před jeho testem,
        tj. před ověřením, že stav hry odpovídá scénáři.
        Cílem metody je připravit potřebné informace o testované hře.
        """
        if not compare_containers(test_scenario.ALL_ACTIONS,
                                  self.game.all_actions()):
            error('Seznam dostupných akcí', scenario, scenario.steps[0],
               self.game, compare_containers.from_scenario,
                          compare_containers.from_game)
        self.scenario = scenario


    def before_step_test(self, step:ScenarioStep, answer:str):
        """Akce, která se má provést po provedení kroku hry, ale před jeho
        testem, tj. před ověřením, že stav hry odpovídá scénáři.
        Parametr »step« představuje aktuálně testovaný krok scénáře
        a parametr »answer« představuje odpověď hry.
        """


    def after_step_test(self, step:ScenarioStep, answer:str):
        """Akce, která se má provést po testu aktuálního kroku.
        Parametr »step« představuje aktuálně testovaný krok scénáře
        a parametr »answer« představuje odpověď hry.
        """


    def after_game_end(self, verbose_message:str='',
                   exception:Exception=None, summary:'GameSummary'=None):
        """Akce, která se má provést po testu posledního kroku.
        Význam parametrů je následující:
        »step«      - Kompletní zpráva o průběhu testu
        »exception« - Případná vyhazovaná výjimka
        »summary«   - Přepravka s informacemi o předpokládaném průběhu hry
                      podle scénářů
        """



############################################################################



############################################################################
dbg.stop_mod(0, __name__)
