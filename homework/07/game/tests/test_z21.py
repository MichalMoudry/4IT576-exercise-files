#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul testuje správné zapracování modifikace s kódem »21w21«,
požadující upravit odevzdaný program následovně:

Přidejte mezi scénáře jako čtvrtý obecný testovací scénář, tj. scénář typu
TypeOfScenario.stGENERAL nazvaný TEST_Z21 s následujícími testovacími kroky:

 0. Krok typu TypeOfStep.tsSTART se startovacím krokem.

 1. Krok typu TypeOfStep.tsNS1_0Args s příkazem
    ABRAKADABRA
    Po tomto příkazu hra nezmění svůj stav a odpoví:
    Příkaz ABRAKADABRA neznám.

 2. Krok typu TypeOfStep.tsNS1_WRONG_ARG s příkazem
    ABRAKADABRA ABRAKADABRA
    Ani po tomto příkazu hra nezmění svůj stav a opět odpoví:
    Příkaz ABRAKADABRA neznám.

 3. Krok typu TypeOfStep.tsNS_1 s příkazem
    ABRAKADABRA ZKRATKA
    Po jeho zadání se hráč přesune do prostoru ZKRATKA a hra odpoví:
    Přesunuli jste se do prostoru ZKRATKA.

 4. Krok typu TypeOfStep.tsNS1_WrongCond s příkazem
    ABRAKADABRA ZKRATKA
    Po tomto příkazu hra nezmění svůj stav a odpoví:
    Neumím provést příkaz ABRAKADABRA ZKRATKA.

 5. Krok typu TypeOfStep.tsNS_1 s příkazem
    ABRAKADABRA <Cíl>
    kde <Cíl> je název cílového prostoru šťastného scénáře.
    Po tomto příkazu bude prostor <Cíl> přidán mezi sousedy prostoru ZKRATKA,
    se změní obsah hráčova batohu tak, aby odpovídal stavu
    v závěrečném kroku, a změní se i případné další příznaky potřebné
    pro zdárné ukončení hry. Po zadání příkazu proto hra hráči odpoví:
    Vše je připraveno pro přesun do cíle.

 6. Krok typu TypeOfStep.tsGOTO s příkazem žádajícím o přesun do cílového
    prostoru. Na tento příkaz hra odpoví stejně jako v závěrečném kroku
    šťastného scénáře. Jediným případným rozdílem může být vlastní příkaz,
    který může být ve šťastném scénáři jiný.

Doplňte do hry příkaz nazvaný ABRAKADABRA, který bude odpovídat požadavkům
výše popsaného scénáře. Příkaz bude mít následující vlastnosti:

- Při zadání příkazu ani jeho parametrů nebude záležet na velikosti písmen.

- Při zadání příkazu s parametrem ZKRATKA se hráč přesune do prostoru
  nazvaného ZKRATKA beze změny obsahu batohu.
  Tento prostor nebude mít ve výchozím stavu žádné sousedy,
  ani nebude sousedem žádného existujícího prostoru
  a nebudou v něm ani žádné h-objekty.

- Zadá-li hráč v některém z prostorů hry příkaz ABRAKADABRA
  s jiným parametrem nebo zadá-li jej bez parametrů, odpoví hra uživateli:
  Příkaz ABRAKADABRA neznám

- Zadáte-li v prostoru ZKRATKA příkaz
  ABRAKADABRA <Cíl>
  kde <Cíl> je název cílového prostoru šťastného scénáře, stane se tento
  prostor sousedem prostoru ZKRATKA.
  Navíc se upraví obsah batohu hráče spolu se sousedy a obsahem cílového
  prostoru tak, aby odpovídaly stavu v závěrečném kroku úspěšného scénáře.

- Přejde-li v následujícím kroku hráč do cílového prostoru, odpoví hra
  stejně jako v závěrečném kroku úspěšného scénáře. Jinými slovy:
  závěrečný krok testovacího scénáře modifikované hry a šťastného scénáře
  budou shodné s jediným rozdílem: závěrečným příkazem testovacího scénáře
  bude přechod do cílového prostoru.

- Zadá-li hráč v prostoru ZKRATKA příkaz ABRAKADABRA s jiným parametrem
  než <Cíl> nebo zadá-li jej bez parametrů, odpoví hra uživateli:
  Neumím provést příkaz ABRAKADABRA XXX
  kde XXX zastupuje zadaný parametr.

Upravte příkaz pro přesun do sousedního prostoru tak, aby v případě,
že se hráč přesouvá z prostoru ZKRATKA ukončil hru požadovaným způsobem.

"""

import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api.interfaces import IInterface, IGame
from ..api.scen_types import TypeOfScenario, tsSTART, tsEMPTY, tsNOT_START, \
    tsUNKNOWN
from ..api.scenario   import ScenarioStep, Scenario
from .common.errors   import error
from .common.types    import Visitor



############################################################################

class Visitor_z21(Visitor):
    """Pomáhá kontrolovat správnost řešení popsaného v dokumentaci modulu.
    """

    def __init__(self, factory:IInterface):
        super().__init__(factory)


    def before_game_start(self):
        """ Akce, která se má provést před spuštěním hry.
        Cílem metody je prověřit scénáře a případné další pomocné kódy.
        """
        # Zkontroluje korektnost přidaných scénářů
        check_test_scenario(self.factory)


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


    # def after_step_test(self, step:ScenarioStep, answer:str):
    #     """Akce, která se má provést po testu aktuálního kroku.
    #     """



############################################################################

def check_test_scenario(factory:IInterface):
    """Prověří existenci přidaného scénáře a to,
    že odpovídá požadavkům zadání.
    """
    scenarios = factory.all_scenarios()
    if len(scenarios) < 5:
        err0('Není zadán některý scénář, pravděpodobně ten  testovací')
    if scenarios[4].name != TEST_SCEN:
        err0(f'Scénář [4] se nejmenuje {TEST_SCEN}')
    happy     = scenarios[0]
    test      = scenarios[4]
    expected  = prepare_test_scenario(factory, happy)
    e_steps = expected.steps
    t_steps = test    .steps
    if len(t_steps) < len(e_steps):
        err0('Testovací scénář neobsahuje všechny požadované kroky')
    for index in range(len(e_steps)):
        if reason := steps_differs(e_steps[index], t_steps[index]):
            err1(reason, e_steps[index], t_steps[index])


def steps_differs(expected:ScenarioStep, obtained:ScenarioStep) -> str:
    """Porovná kroky scénáře jsou-li vzájemně ekvivalentní.
    """
    def containers_differs(expected:tuple[str], obtained:tuple[str]) -> str:
        """Porovná obsahy dvou kontejnerů."""
        ex = [s.lower() for s in expected]
        ob = [s.lower() for s in obtained]
        ex.sort();   ob.sort()
        return ex != ob

    if expected.typeOfStep != obtained.typeOfStep:
        return 'Typ kroku se liší'
    if expected.command.lower() != obtained.command.lower():
        return 'Zadané příkazy se liší'
    if expected.message.lower() != obtained.message.lower():
        return 'Zadané odpovědi se liší'
    if expected.place.lower() != obtained.place.lower():
        return 'Zadané prostory se liší'
    if containers_differs(expected.neighbors, obtained.neighbors):
        return 'Zadaní sousedé se liší'
    if containers_differs(expected.items, obtained.items):
        return 'Zadané h-objekty v prostoru se liší'
    if containers_differs(expected.bag, obtained.bag):
        return 'Zadané obsahy batohu se liší'
    return None



def err0(reason:str) -> None:
    """Chyba odhalená před tím, než se začnou procházet kroky scénáře.
    """
    msg = f'\n{reason}\n'
    print(msg)
    raise Exception(msg)


def err1(reason:str, expected:ScenarioStep, obtained:ScenarioStep) -> None:
    """Chyba odhalená při procházení kroků scénáře před spuštěním hry.
    """
    msg = (f'\n{expected.index}'
           f'. krok testovacího scénáře neodpovídá požadavkům - {reason}:\n'
           f'Očekáván krok typu {expected.typeOfStep}:\n{expected}\n\n'
           f'Obdržen krok typu {obtained.typeOfStep}:\n{obtained}\n')
    print(msg)
    raise Exception('Krok testovacího scénáře neodpovídá požadavkům')


def prepare_test_scenario(factory:IInterface, happy:Scenario) -> Scenario:
    """Odvodí požadovanou podobu testovacího scénáře.
    """
    from ..api import scen_types
    h_steps = happy.steps
    t_steps = [h := h_steps[0]]
    ScenarioStep.next_index = 1
    place       = h.place
    neighbors   = h.neighbors
    items       = h.items
    bag         = h.bag
    # Krok č. 1
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS1_0Args,
                   command = 'ABRAKADABRA',
                   message ='Příkaz ABRAKADABRA neznám.',
                   place   = place,
                   neighbors=neighbors, items=items, bag=bag))
    # Krok č. 2
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS1_WRONG_ARG,
                   command = 'ABRAKADABRA ABRAKADABRA',
                   message ='Příkaz ABRAKADABRA neznám.',
                   place   = place,
                   neighbors=neighbors, items=items, bag=bag))
    # Krok č. 3
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS_1,
                   command = 'ABRAKADABRA ZKRATKA',
                   message = 'Přesunuli jste se do prostoru ZKRATKA.',
                   place   = 'ZKRATKA',
                   neighbors=(), items=(), bag=bag))
    # Krok č. 4
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS1_WrongCond,
                   command = 'ABRAKADABRA ZKRATKA',
                   message = 'Neumím provést příkaz ABRAKADABRA ZKRATKA.',
                   place   = 'ZKRATKA',
                   neighbors=(), items=(), bag=bag))
    # Krok č. 5
    h           = h_steps[-1]
    place       = h.place
    neighbors   = h.neighbors
    items       = h.items
    bag         = h.bag
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS_1,
                   command = f'ABRAKADABRA {place}',
                   message = 'Vše je připraveno pro přesun do cíle.',
                   place   = 'ZKRATKA',
                   neighbors=(place, ), items=(), bag=bag))
    # Krok č. 6
    command = factory.game().basic_actions().MOVE_NAME
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsGOTO,
                   command  = f'{command} {place}',
                   message  = h.message,
                   place    = place,
                   neighbors=neighbors, items=items, bag=bag))

    print(f'{60 * "%"}')
    dbg.prSeq(t_steps)
    print(f'{60 * "%"}')
    return Scenario(TEST_SCEN, scen_types.stGENERAL, t_steps)



############################################################################

TEST_ID     = '21w21'
TEST_SCEN   = 'TEST_Z21'
NO_COMMAND  = {tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN, }



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
