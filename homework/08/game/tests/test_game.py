#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Modul s testy běhu hry.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api import BasicActions, scen_types, state_of
from ..api.interfaces   import IInterface, IGame
from ..api.scenario     import ScenarioStep, Scenario
from .common.types      import Visitor
from .                  import Level



############################################################################

def test_game_from(factory:IInterface, ID:int) -> None:
    """Test hry podle zadaných scénářů
    """
    # dbg.prSE(0,1,'test_game_from', f'{factory.AUTHOR_ID} - '
    #                                f'{factory.authorOrigName()}')
    global game
    game = factory.game()
    fss  = factory.all_scenarios()
    dbg.prIN(0,f'{Level(ID) = }')
    dbg.prIN(0,f'{fss = }')
    dbg.prIN(0,f'{ID_2_SCENARIOS = }')
    dbg.prIN(0,f'{ID_2_SCENARIOS[Level(ID)] = }')
    scen_list = []
    dbg.prSE(0,1,'Cyklus')
    for i in ID_2_SCENARIOS[Level(ID)]:
        dbg.prIN(0, f'{i = },   {fss[i] = }')
        item = fss[i]
        scen_list.append(item)
    scenarios = tuple(scen_list)
    dbg.prSE(0,1,'Cyklus')
    # scenarios = tuple(fss[i] for i in ID_2_SCENARIOS[Level(ID)])
    # def prep_scen():
    #     dbg.prSE(0, 1, 'prep_scen', f'{ID=}, {Level(ID)}')
    #     dbg.prIN(0, f'{ID_2_SCENARIOS = }')
    #     result = []
    #     for i in ID_2_SCENARIOS[Level(ID)]:
    #         dbg.prIN(0, f'{i = }')
    #         dbg.prIN(0, f'{fss[i] = }')
    #         result.append(fss[i])
    #     dbg.prSE(0, 0, 'prep_scen', f'{result = }')
    #     return tuple(result)
    # scenarios = prep_scen()
    visitor   = _get_visitor_for(ID, factory)
    print(f'\nSCENARIOS: {scenarios}\n')
    visitor.before_game_start()
    for s in scenarios:
        print(f'Testovaný scénář: {s.name}')
        _test_by(s, visitor)
    dbg.prSE(0,0,'test_game_from')



############################################################################
#
# def _get_scenarios_for(ID:Level, factory:IInterface) -> tuple[Scenario]:
#     """Podle zadaného ID vrátí správnou n-tici scénářů.
#     """
#     scenarios = factory.scenarios()
#     if ID <= Level.BASIC:
#         return (scenarios[3],)
#     if ID == Level.MISTAKES:
#         return (scenarios[3], scenarios[3], scenarios[1],)
#     if ID >= Level.WHOLE:
#         return (scenarios[0], scenarios[0], scenarios[1], scenarios[2],)
#

def _get_visitor_for(ID:Level, factory:IInterface) -> Visitor:
    """Vrátí návštěvníka odpovídajícího zadané hladině.
    """
    if ID <= Level.WHOLE:
        return Visitor(factory)
    if ID == Level.z01:
        from .test_z01 import Visitor_z01
        return Visitor_z01(factory)
    if ID == Level.z11:
        from .test_z11 import Visitor_z11
        return Visitor_z11(factory)
    if ID == Level.z12:
        from .test_z12 import Visitor_z12
        return Visitor_z12(factory)
    if ID == Level.z13:
        from .test_z13 import Visitor_z13
        return Visitor_z13(factory)
    if ID == Level.z14:
        from .test_z14 import Visitor_z14
        return Visitor_z14(factory)
    if ID == Level.z21:
        from .test_z21 import Visitor_z21
        return Visitor_z21(factory)
    raise Exception (
        f'\nVe funkci test_game._get_visitor_for() není zadán návštěvník '
        f'pro hladinu {ID}')


def _test_by(scenario:Scenario, visitor:Visitor) -> None:
    """Otestuje zadanou hru podle zadaného scénáře
    za pomoci zadaného návštěvníka.
    """
    # dbg.prSE(0, 1, 'test_game._test_by', f'{scenario=}, ')
    from_scenario:list[str]
    from_game    :list[str]

    def _error(reason:str, step:ScenarioStep, expected, obtained):
        """Zobrazí chybové hlášení upozorňující na příčinu chyby.
        """
        message = (f'Při vyhodnocování {step.index}. kroku scénáře '
                     f'{scenario.name} byla odhalena chyba:\n'
                   f'Chybným objekt:   {reason}\n'
                   f'Očekávaný objekt: {str(expected)}\n'
                   f'Obdržený objekt:  {str(obtained)}\n\n')
        print(message)
        print(f'Očekávaný stav hry po provedení testovaného příkazu:\n'
              f'{step}')
        print(f'\nObdržený stav hry po provedení testovaného příkazu:')
        print(f'{state_of(game)}')
        raise Exception

    def compare_containers(scen_cont, game_cont):
        """Porovná názvy v kontejneru scen_cont s názvy objektů
        v kontejneru game_cont bez ohledu na velikost písmen
        a vrátí informaci o tom, zda se liší (liší se = True).
        """
        # dbg.prSE(2, 1, 'test_by', f'{scen_cont=}, {game_cont=}')
        if not ('__iter__' in dir(game_cont)):
            _error('objekt hry není kontejner', step, scen_cont, game_cont)
        nonlocal from_scenario, from_game
        from_scenario = [item     .lower() for item in scen_cont].sort()
        from_game     = [item.name.lower() for item in game_cont].sort()
        # dbg.prSE(2, 0, 'test_by')
        return from_scenario != from_game

    # Zde začíná vlastní tělo funkce
    step:ScenarioStep
    for step in scenario.steps:
        print(f'{step.index}. {(command:=step.command)}\n{30*"-"}')
        try:
            answer = game.execute_command(command)
            print(f'{answer}')
            if Scenario.print_state:
                print(f'{30*"-"}\n{state_of(game)}')
            print(f'{30*"="}\n')
        except Exception as ex:
            print(f'Při vykonávání příkazu '
                  f'{step.index}. {(command:=step.command)}\n'
                  f'byla vyhozena výjimka {ex}')
            raise ex

        # print(f'Očekávaný stav hry po provedení testovaného příkazu:\n'
        #       f'{step}')
        # print(f'\nObdržený stav hry po provedení testovaného příkazu:')
        # print(f'{state_of(game)}')

        if step.typeOfStep == scen_types.tsSTART:
            visitor.after_game_start(scenario)
        visitor.before_step_test(step, answer)
        if (not answer or
            step.message.lower() != answer[:len(step.message)].lower()
        ):
            _error('odpověď hry', step, step.message, answer)
        if step.typeOfStep == scen_types.tsNOT_START:
            continue
        current_place = game.world().current_place()
        if step.place != current_place.name:
            _error('aktuální prostor', step, step.place, current_place)
        if compare_containers(step.neighbors, current_place.neighbors):
            _error('aktuální sousedé', step, from_scenario, from_game)
        if compare_containers(step.items, current_place.items):
            _error('objekty v aktuálním prostoru', step, from_scenario,
                                                         from_game)
        if compare_containers(step.bag, game.bag().items):
            _error('objekty v batohu', step, from_scenario, from_game)
        visitor.after_step_test(step, answer)
    visitor.after_game_end()
    if game.is_alive():
        # dbg.prSE(0, 0, 'test_game._test_by', f'=== NEUKONČENO ===')
        _error('Po ukončení scénáře není hra ukončena', step, (), ())
    # dbg.prSE(0, 0, 'test_game._test_by', f'{scenario=}, ')


def _verify_is_alive(step:ScenarioStep, the_last:bool):
    """Prověří, jestli testovaná hra správně hlásí svoji spuštěnost
    (před startem a po skončení ne, jinak ano).
    """
    game_is_alive = game.is_alive()
    if (step.typeOfStep == scen_types.tsNOT_START)  or  the_last:
        if game_is_alive:
            prefix = ("Po ukončení hry" if the_last
                else  "Před startem hry ")
            raise Exception(prefix + " hra hlásí, že je spuštěná,"
                                   + " přestože má být vypnutá")
    else:
        if not game_is_alive:
            raise Exception("Hra tvrdí, že je vypnutá přestože má běžet")



############################################################################

ID_2_SCENARIOS = {
    Level.START     : (3,),
    Level.WORLD     : (3,),
    Level.BASIC     : (3,),
    Level.MISTAKES  : (3, 3, 1),
    Level.WHOLE     : (0, 0, 1, 2),
    Level.z00       : (0, 0, 1, 2),
    Level.z01       : (0, 0, 1, 2),
    Level.z11       : (0, 0, 1, 2),
    Level.z12       : (0, 0, 1, 2),
    Level.z13       : (0, 0, 1, 2),
    Level.z14       : (0, 0, 1, 2),
    Level.z21       : (0, 0, 1, 2, 4, 4),
}


############################################################################
dbg.stop_mod(0, __name__)
