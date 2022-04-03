#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Šťastný scénář pro hru inspirovanou pohádkou o Červené Karkulce.
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

SCENARIOS = ( HAPPY,
            # MISTAKE,
            # MISTAKE_NS,
            # START,
            )



############################################################################
dbg.stop_mod(0, __name__)
