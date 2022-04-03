#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul testuje správné zapracování modifikace s kódem »21w22«,
požadující upravit odevzdaný program následovně:

Přidejte mezi scénáře jako čtvrtý obecný testovací scénář, tj. scénář typu
TypeOfScenario.stGENERAL, nazvaný TEST_Z21 s následujícími testovacími kroky:

 0. Krok typu TypeOfStep.tsSTART se startovacím krokem.

 1. Krok typu TypeOfStep.tsNS1_0Args s příkazem
    MAGIE
    Po tomto příkazu hra nezmění svůj stav a odpoví:
    Příkaz MAGIE neznám.

 2. Krok typu TypeOfStep.tsNS1_WRONG_ARG s příkazem
    MAGIE MAGIE
    Ani po tomto příkazu hra nezmění svůj stav a opět odpoví:
    Příkaz MAGIE neznám.

 3. Krok typu TypeOfStep.tsNS_1 s příkazem
    MAGIE KOUZLO
    Po jeho zadání se v batohu objeví předmět KOUZLO.
    (ve hře se po něm kapacita batohu zvětší o jedničku)
    a hra odpoví:
    Získali jste kouzlo, které vám usnadní dosažení cíle.

 4. Krok typu TypeOfStep.tsNS1_WrongCond s příkazem
    MAGIE KOUZLO
    Po tomto příkazu hra nezmění svůj stav a odpoví:
    Neumím provést příkaz MAGIE KOUZLO.

 5. Za tento krok vložte kroky chybového scénáře počínaje krokem následujícím
    za startovacím krokem a konče krokem typu TypeOfStep.tsBAG_FULL,
    při němž se hráč snaží přidat předmět do již zaplněného batohu.
    Všechny kroky budou téměř stejné s odpovídajícími kroky chybového
    scénáře s výjimkou toho, že v těchto krocích bude v batohu navíc
    předmět KOUZLO.

 5. Krok typu TypeOfStep.tsNS_1 s příkazem
    MAGIE <Cíl>
    kde <Cíl> je název cílového prostoru šťastného scénáře.
    Po tomto příkazu se hráč přesune do cílového prostoru
    (pokud tam už byl, zůstane na místě), nastaví se obsah hráčova batohu
    tak, aby odpovídal stavu v závěrečném kroku,
    a změní se i případné další příznaky potřebné pro zdárné ukončení hry.
    Na tento příkaz hra odpoví stejně jako v závěrečném kroku šťastného
    scénáře. Jediným případným rozdílem může být vlastní příkaz,
    který bude ve šťastném scénáři jiný.


Doplňte do hry příkaz nazvaný MAGIE, který bude odpovídat požadavkům
výše popsaného scénáře. Příkaz bude mít následující vlastnosti:

- Při zadání příkazu nebude záležet na velikosti písmen.

- Při prvním zadání příkazu MAGIE s argumentem KOUZLO se se stane následující:

  - Kapacita batohu se zvětší o 1.

  - V batohu se objeví h-objekt nazvaný KOUZLO

  - Hra po zadání tohoto příkazu odpoví:
    Získali jste kouzlo, které vám usnadní dosažení cíle.

- Zadá-li hráč příkazu MAGIE
  s jiným argumentem nebo zadá-li jej bez argumentů,
  stav hry se nezmění a hra odpoví uživateli:
  Příkaz MAGIE neznám.

- Zadá-li hráč po zadáním příkazu s parametrem KOUZLO znovu příkaz
  MAGIE KOUZLO
  stav hry se nezmění a hra odpoví uživateli:
  Neumím provést příkaz MAGIE.

- Požádá-li v dalším průběhu hry hráč o položení h-objektu KOUZLO,
  odpoví hra stejně jako v závěrečném kroku úspěšného scénáře.
  Jinými slovy: závěrečný krok testovacího scénáře modifikované hry
  a jejího šťastného scénáře budou shodné s jediným rozdílem:
  závěrečným příkazem testovacího scénáře bude přechod do cílového prostoru.

Upravte příkaz pro přesun do položení h-objektu tak, aby v případě,
že hráč pokládá h-objekt KOUZLO ukončil hru požadovaným způsobem.

"""

import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api.interfaces import IInterface, IGame
from ..api.scen_types import (TypeOfScenario, tsBAG_FULL,
                              tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN)
from ..api.scenario   import ScenarioStep, Scenario
from .common.errors   import error
from .common.types    import Visitor



############################################################################

class Visitor_z22(Visitor):
    """Pomáhá kontrolovat správnost řešení popsaného v dokumentaci modulu.
    """

    def __init__(self, factory:IInterface):
        super().__init__(factory)


    def before_game_start(self):
        """ Akce, která se má provést před spuštěním hry.
        Cílem metody je prověřit scénáře a případné další pomocné kódy.
        """
        # Zkontroluje korektnost přidaných scénářů
        dbg.prSE(0, 1, 'Visitor_z22.before_game_start')
        check_test_scenario(self.factory)
        dbg.prSE(0, 0, 'Visitor_z22.before_game_start')


    def after_game_start(self, scenario:Scenario):
        """ Akce, která se má provést po provedení startovacího kroku hry
        (tj. ve chvíli, kde je hra již inicializována), ale před jeho testem,
        tj. před ověřením, že stav hry odpovídá scénáři.
        Prověří, že hra deklaruje právě ty akce, které jsou deklarované
        ve scénářích a uloží seznam jejich abecedně seřazených názvů.
        """
        dbg.prSE(0, 1, 'Visitor_z22.after_game_start')
        super().after_game_start(scenario)

        # Porovná úvodní hlášení hry se situací odvozenou ze scénářů

        # Nastaví výchozí stav potřebných proměnných
        self._entered = []
        dbg.prSE(0, 0, 'Visitor_z22.after_game_start')


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
        err0('Není zadán některý scénář, pravděpodobně ten testovací')
    if scenarios[4].name != TEST_SCEN:
        err0(f'Scénář [4] se nejmenuje {TEST_SCEN}')
    happy     = scenarios[0]
    mistake   = scenarios[1]
    test      = scenarios[4]
    expected  = prepare_test_scenario(factory, happy, mistake)
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


def prepare_test_scenario(factory:IInterface,
                          happy:Scenario, mistake:Scenario) -> Scenario:
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
           command = 'MAGIE',
           message = 'Příkaz MAGIE neznám.',
           place   = place,
           neighbors=neighbors, items=items, bag=bag))
    # Krok č. 2
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS1_WRONG_ARG,
           command = 'MAGIE MAGIE',
           message = 'Příkaz MAGIE neznám.',
           place   = place,
           neighbors=neighbors, items=items, bag=bag))
    # Krok č. 3
    bag = bag + ('KOUZLO',)
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS_1,
           command = 'MAGIE KOUZLO',
           message = 'Získali jste kouzlo, které vám usnadní dosažení cíle.',
           place   = place,
           neighbors=neighbors, items=items, bag=bag))
    # Krok č. 4
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS1_WrongCond,
           command = 'MAGIE KOUZLO',
           message = 'Neumím provést příkaz MAGIE KOUZLO.',
           place   = place,
           neighbors=neighbors, items=items, bag=bag))

    for step in mistake.steps[2:]:
        new_bag = step.bag + ('KOUZLO',)
        t_steps.append(ScenarioStep(
            typeOfStep  = step.typeOfStep,
            command     = step.command,
            message     = step.message,
            place       = step.place,
            neighbors   = step.neighbors,
            items       = step.items,
            bag         = new_bag) )
        if step.typeOfStep == tsBAG_FULL:   break

    # Krok č. n+1
    h           = h_steps[-1]
    message     = h.message
    place       = h.place
    neighbors   = h.neighbors
    items       = h.items
    bag         = h.bag
    t_steps.append(ScenarioStep(typeOfStep = scen_types.tsNS_1,
        command  = f'MAGIE {h.place}',
        message  = h.message,
        place    = h.place,
        neighbors= h.neighbors,
        items    = h.items,
        bag      = h.bag) )

    print(f'{60 * "%"}')
    dbg.prSeq(t_steps)
    print(f'{60 * "%"}')
    return Scenario(TEST_SCEN, scen_types.stGENERAL, t_steps)



############################################################################

TEST_ID     = '21w22'
TEST_SCEN   = 'TEST_Z22'
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
