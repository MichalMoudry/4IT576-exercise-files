#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Základní čtveřice scénářů pro hru inspirovanou pohádkou o Červené Karkulce.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api.scenario   import ScenarioStep, Scenario
from ..api.scen_types import *  # Především typu kroků



############################################################################
# Základní úspěšný scénář demonstrující průběh hry, při němž hráč
# nezadává žádné chybné příkazy a dosáhne zadaného cíle.
HAPPY = Scenario('', stHAPPY, (
    START_STEP :=
    ScenarioStep(tsSTART, '',                       # Zadaný příkaz
        'Vítejte!\nToto je příběh o Červené Karkulce, babičce a vlkovi.\n'
        'Svými příkazy řídíte Karkulku, aby donesla bábovku a víno \n'
        'babičce v chaloupce za temným lesem. Když přijdete do chaloupky,\n'
        'tak položíte dárky, babičku vzbudíte, pozdravíte,\n'
        'popřejete ji k narozeninám a dárky předáte.\n'
        'Jste-li dobrodružné typy, můžete to místo s babičkou provést\n'
        's vlkem, který spí v temném lese.\n\n'
        'Nebudete-li si vědět rady, zadejte znak ?.',

        'Domeček',                                  # Aktuální prostor
        ('Les',),                                   # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi víno',              # Zadaný příkaz
        'Karkulka dala do košíku objekt: Víno',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Stůl', 'Panenka', ),           # H-objekty v prostoru
        ('Víno', ),                                 # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi bábovka',           # Zadaný příkaz
        'Karkulka dala do košíku objekt: Bábovka',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Stůl', 'Panenka', ),                      # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),
    ScenarioStep(tsGOTO, 'Jdi LES',                 # Zadaný příkaz
        'Karkulka se přesunula do prostoru:\n'
        'Les s jahodami, malinami a pramenem vody',
        'Les',                                      # Aktuální prostor
        ('Domeček', 'Temný_les', ),                 # Aktuální sousedé
        ('Maliny', 'Jahody', 'Studánka', ),         # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),
    ScenarioStep(tsGOTO, 'Jdi temný_les',           # Zadaný příkaz
        'Karkulka se přesunula do prostoru:\n'
        'Temný_les s jeskyní a číhajícím vlkem',
        'Temný_les',                                # Aktuální prostor
        ('Les', 'Jeskyně', 'Chaloupka', ),          # Aktuální sousedé
        ('Vlk',  ),                                 # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),
    ScenarioStep(tsGOTO, 'Jdi chaloupka',           # Zadaný příkaz
        'Karkulka se přesunula do prostoru:\n'
        'Chaloupka, kde bydlí babička',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les',),                             # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', ),            # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož bábovka',       # Zadaný příkaz
        'Karkulka vyndala z košíku objekt: Bábovka',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les',),                             # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', ), # H-objekty v prostoru
        ('Víno', ),                                 # H-Objekty v batohu
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož VÍNO',          # Zadaný příkaz
        'Karkulka vyndala z košíku objekt: Víno',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsNS_1, 'Probuď babička',          # Zadaný příkaz
        'Karkulka probudila osobu: '
        'Babička',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsNS_0, 'Pozdrav',                 # Zadaný příkaz
        'Karkulka pozdravila babičku',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsNS_0, 'Popřej',                  # Zadaný příkaz
        'Karkulka popřála babičce vše nejlepší k narozeninám',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsNS_2, 'Předej Bábovka Víno',     # Zadaný příkaz
        'Karkulka předala babičce předměty: '
        'Bábovka a Víno\n'
        'Úspěšně jste ukončili hru.\n'
        'Děkujeme, že jste si zahráli.',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),
    )
)



############################################################################
# Základní chybový scénář demonstrující průběh hry, při němž hráč
# zadává chybně příkazy k provedení základních akcí
# a současně vyzkouší vyvolání nápovědy a nestandardní ukončení.

ScenarioStep.next_index = -1  # Index kroku před korektním startem

WRONG_START = ScenarioStep(tsNOT_START, 'start', # Zadaný příkaz
        'Prvním příkazem není startovací příkaz.\n' 
        'Hru, která neběží, lze spustit pouze startovacím příkazem.\n',
        '',                                         # Aktuální prostor
        (),                                         # Aktuální sousedé
        (),                                         # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        )

ScenarioStep.next_index = +1  # Index prvního kroku za startem

MISTAKE = Scenario('', stMISTAKES, (
    WRONG_START,

    START_STEP,

    ScenarioStep(tsEMPTY, '',                       # Zadaný příkaz
        'Prázdný příkaz lze použít pouze pro start hry',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsUNKNOWN, 'maso',                 # Zadaný příkaz
        'Tento příkaz neznám: maso',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsMOVE_WA, "jdi",                  # Zadaný příkaz
        'Nevím, kam mám jít.\n'
        'Je třeba zadat jméno cílového prostoru.',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsTAKE_WA, "vezmi",                # Zadaný příkaz
        'Nevím, co mám zvednout.\n'
        'Je třeba zadat jméno zvedaného objektu.',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsPUT_DOWN_WA, "polož",            # Zadaný příkaz
        'Nevím, co mám položit.\n'
        'Je třeba zadat jméno pokládaného objektu.',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsBAD_NEIGHBOR, "jdi do_háje", # Zadaný příkaz
        'Do zadaného prostoru se odsud jít nedá: do_háje.',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsBAD_ITEM, "vezmi whisky",        # Zadaný příkaz
        'Zadaný objekt v prostoru není: whisky',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsUNMOVABLE, "vezmi stůl",         # Zadaný příkaz
        'Zadaný objekt není možno zvednout: stůl',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsTAKE, 'Vezmi víno',              # Zadaný příkaz
        'Karkulka dala do košíku objekt: Víno',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Bábovka', 'Stůl', 'Panenka', ),           # H-objekty v prostoru
        ('Víno', ),                                 # H-Objekty v batohu
        ),

    ScenarioStep(tsTAKE, 'Vezmi bábovka',           # Zadaný příkaz
        'Karkulka dala do košíku objekt: Bábovka',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Stůl', 'Panenka', ),                      # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),

    ScenarioStep(tsBAG_FULL, 'Vezmi panenka',       # Zadaný příkaz
        'Zadaný objekt se už do košíku nevejde: panenka',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Stůl', 'Panenka', ),                      # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),

    ScenarioStep(tsNOT_IN_BAG, 'polož panenka',     # Zadaný příkaz
        'Zadaný objekt v košíku není: panenka',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Stůl', 'Panenka', ),                      # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),

    ScenarioStep(tsHELP, '?',                       # Zadaný příkaz
        'Vaším úkolem je vzít v domečku do košíku bábovku a víno,\n'
        'dovést Červenou Karkulku z domečku až k babičce,\n',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Stůl', 'Panenka', ),                      # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),

    ScenarioStep(tsEND, 'KONEC',                    # Zadaný příkaz
        'Ukončili jste hru.\n'
        'Děkujeme, že jste si zahráli.',
        'Domeček',                                  # Aktuální prostor
        ('Les', ),                                  # Aktuální sousedé
        ('Stůl', 'Panenka', ),                      # H-objekty v prostoru
        ('Bábovka', 'Víno', ),                      # H-Objekty v batohu
        ),

    ),
)



############################################################################
# Základní chybový scénář demonstrující průběh hry, při němž hráč
# # zadává chybně příkazy k provedení rozšiřujících akcí.
ScenarioStep.next_index = 8 # Index prvního nestandardního kroku
MISTAKE_NS = Scenario('', stMISTAKES_NS, (
        HAPPY.steps[0],
        HAPPY.steps[1],   # Vezmi víno
        HAPPY.steps[2],   # Vezmi Bábovka
        HAPPY.steps[3],   # Jdi les
        HAPPY.steps[4],   # Jdi Temný_les
        HAPPY.steps[5],   # Jdi Chaloupka
        HAPPY.steps[6],   # Polož Bábovka
        HAPPY.steps[7],   # Polož Víno

    ScenarioStep(tsNS0_WrongCond, 'Pozdrav',        # Zadaný příkaz
        'Nemá smysl zdravit, babička ještě není probuzená.',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS1_0Args, 'Probuď',             # Zadaný příkaz
        'Nevím, koho mám probudit',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS1_WRONG_ARG, 'Probuď Stůl',    # Zadaný příkaz
        'Nelze budit předmět: Stůl',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS1_WRONG_ARG, 'Probuď vlk', # Zadaný příkaz
        'Nelze budit objekt, který není přítomen: vlk',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS_1, 'Probuď babička',          # Zadaný příkaz
        'Karkulka probudila osobu: Babička',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS1_WrongCond, 'Probuď babička', # Zadaný příkaz
        'Nelze budit osobu, která je již probuzená: Babička',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS0_WrongCond, 'popřej',                  # Zadaný příkaz
        'Karkulka ještě babičku nepozdravila',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS2_WrongCond, 'Předej Bábovka víno', # Zadaný příkaz
        'Karkulka ještě babičku nepozdravila',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS_0, 'Pozdrav',                 # Zadaný příkaz
        'Karkulka pozdravila babičku',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS2_WrongCond, 'Předej Bábovka víno', # Zadaný příkaz
        'Karkulka ještě babičce nepopřála',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS_0, 'Popřej',                  # Zadaný příkaz
        'Karkulka popřála babičce vše nejlepší k narozeninám',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS2_1Args, 'Předej něco',        # Zadaný příkaz
        'Je třeba předat 2 věci. Byl však zadán pouze objekt: něco',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS2_WRONG_1stARG, 'Předej postel víno', # Zadaný příkaz
        'Nelze předat nepřenosný předmět: Postel',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsNS2_WRONG_2ndARG, 'Předej Bábovka vlk', # Zadaný příkaz
        'Nelze předat nepřítomný předmět: vlk',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),

    ScenarioStep(tsEND, 'konec',                    # Zadaný příkaz
        'Ukončili jste hru.\n'
        'Děkujeme, že jste si zahráli.',
        'Chaloupka',                                # Aktuální prostor
        ('Temný_les', ),                            # Aktuální sousedé
        ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
        (),                                         # H-Objekty v batohu
        ),
    ),
)



############################################################################

ScenarioStep.next_index = +1  # Index prvního kroku za startem

REQUIRED = Scenario('REQUIRED', stREQUIRED, (
    START_STEP,

    ScenarioStep(tsGOTO, 'Jdi LES',                 # Zadaný příkaz
        'Karkulka se přesunula do prostoru:\n'
        'Les s jahodami, malinami a pramenem vody',
        'Les',                                      # Aktuální prostor
        ('Domeček', 'Temný_les', ),                 # Aktuální sousedé
        ('Maliny', 'Jahody', 'Studánka', ),         # H-objekty v prostoru
        ( ),                                        # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi maliny',            # Zadaný příkaz
        'Karkulka dala do košíku objekt: Maliny',
        'Les',                                      # Aktuální prostor
        ('Domeček', 'Temný_les', ),                 # Aktuální sousedé
        ('Jahody', 'Studánka', ),                   # H-objekty v prostoru
        ('Maliny', ),                               # H-Objekty v batohu
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož maliny',        # Zadaný příkaz
        'Karkulka vyndala z košíku objekt: Maliny',
        'Les',                                      # Aktuální prostor
        ('Domeček', 'Temný_les', ),                 # Aktuální sousedé
        ('Maliny', 'Jahody', 'Studánka', ),         # H-objekty v prostoru
        ( ),                                        # H-Objekty v batohu
        ),
    ScenarioStep(tsHELP, '?',                       # Zadaný příkaz
        'Vaším úkolem je vzít v domečku do košíku bábovku a víno,\n'
        'dovést Červenou Karkulku z domečku až k babičce,\n',
        'Les',                                      # Aktuální prostor
        ('Domeček', 'Temný_les', ),                 # Aktuální sousedé
        ('Maliny', 'Jahody', 'Studánka', ),         # H-objekty v prostoru
        ( ),                                        # H-Objekty v batohu
        ),
    ScenarioStep(tsEND, 'KONEC',                    # Zadaný příkaz
        'Ukončili jste hru.\nDěkujeme, že jste si zahráli.',
        'Les',                                      # Aktuální prostor
        ('Domeček', 'Temný_les', ),                 # Aktuální sousedé
        ('Maliny', 'Jahody', 'Studánka', ),         # H-objekty v prostoru
        ( ),                                        # H-Objekty v batohu
        ),

))



############################################################################

SCENARIOS = ( HAPPY,
              MISTAKE,
              MISTAKE_NS,
              REQUIRED,
            )



############################################################################
dbg.stop_mod(0, __name__)
