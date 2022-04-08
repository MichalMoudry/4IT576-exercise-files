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
    ScenarioStep(tsSTART, '', # Zadaný příkaz
        'Vítejte ve hře Halo, kdy vaším cílem je se dostat do místnosti'
        ' "The Maw",\npřičemž pro úspěšné dokončení hry je třeba donést'
        ' tzv. Index a použít ho\n na postavu Arbiter, který se nachází'
        ' v zamčené knihovně, tedy je třeba\nknihovnu odemknouta sebrat'
        ' Index do batohu.\n\nPro zobrazení'
        ' nápovědy je třeba zadat příkaz: ?.',
        'The_Pillar_of_Autumn', # Aktuální prostor
        ('Halo',), # Aktuální sousedé
        ('Assault_Rifle', 'Jacob_Keyes', ), # H-objekty v prostoru
        ('Pistole', 'generátor_štítu', ), # H-Objekty v batohu
        ),
    ScenarioStep(tsNS_1, "oslov jacob_keyes",
        "Pokoušíte se zeptat objektu Jacob_Keyes. Jaký je váš dotaz?",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole', 'generátor_štítu',),
        ),
    ScenarioStep(tsNS_0, "ukončit_rozhovor",
        "Rozhovor byl úspěšně ukončen.",
        "The_Pillar_of_Autumn",
        ('Halo',),
        ('Assault_Rifle', 'Jacob_Keyes',),
        ('Pistole', 'generátor_štítu',),
        ),
    ScenarioStep(tsGOTO, "jdi Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu",)
        ),
    ScenarioStep(tsGOTO, "jdi kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu",)
        ),
    ScenarioStep(tsGOTO, "jdi Laboratoř",
        "Proběhl přesun na: Laboratoř\n"
        "Sousedící místnosti: kontrolní_místnost_prstence",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "Klíč_ke_knihovně", "[Elite]"),
        ("Pistole", "generátor_štítu",)
        ),
    ScenarioStep(tsTAKE, "zvedni Klíč_ke_knihovně",
        "Předmět byl zvednut",
        "Laboratoř",
        ("kontrolní_místnost_prstence",),
        ("Plasma_pistol", "[Elite]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, "jdi kontrolní_místnost_prstence",
        "Proběhl přesun na: kontrolní_místnost_prstence\n"
        "Sousedící místnosti: Halo; Laboratoř",
        "kontrolní_místnost_prstence",
        ("Halo", "Laboratoř"),
        ("Needler", "[Flood]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, "jdi Halo",
        "Proběhl přesun na: Halo\nSousedící místnosti:\n"
        "Kontrolní_místnost_prstence; Kartograf; The_Pillar_of_Autumn",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsNS_0, "přehled",
        "---------- Přehled ----------\n"
        "- Obsah batohu: ('Pistole', 'Klíč_ke_knihovně')\n"
        "- Počet životů: 100\n"
        "- Velikost štítu: 150\n\n"
        "----- Postup -----\n"
        "- Máte klíč ke knihovně? Ano\n"
        "- Odemkli jste knihovnu? Ne\n",
        "Halo",
        ("kontrolní_místnost_prstence", "Kartograf",
        "The_Pillar_of_Autumn"),
        ("Needler", "Plasma_Pistol", "[Grunt]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsGOTO, "jdi Kartograf",
        "Proběhl přesun na: Kartograf\nSousedící místnosti:\n"
        "Knihovna; Halo",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsNS_1, "otevři knihovnu",
        "Místnost (knihovna) byla otevřena",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]"),
        ("Pistole", "generátor_štítu", "Klíč_ke_knihovně")
        ),
    ScenarioStep(tsPUT_DOWN, "polož Klíč_ke_knihovně",
        "Věc (Klíč_ke_knihovně) byla položena",
        "Kartograf",
        ("Knihovna", "Halo"),
        ("Carbine", "[Forerunner]", "Klíč_ke_knihovně"),
        ("Pistole", "generátor_štítu")
        ),
    ScenarioStep(tsGOTO, "jdi Knihovna",
        "Proběhl přesun na: Knihovna\nSousedící místnosti:\n"
        "TRC; Kartograf",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole", "Index"),
        ("Pistole", "generátor_štítu")
        ),
    ScenarioStep(tsTAKE, "zvedni Index",
        "Předmět (Index) byl zvednut",
        "Knihovna",
        ("TRC", "Kartograf"),
        ("Pistole",),
        ("Pistole", "generátor_štítu", "Index")
        ),
    ScenarioStep(tsGOTO, "jdi TRC",
        "Proběhl přesun na: TRC\nSousedící místnosti:\n"
        "The_Maw; Knihovna",
        "TRC",
        ("the_maw", "Knihovna"),
        ("[Grunt]", "[Covenant]"),
        ("Pistole", "generátor_štítu", "Index")
        ),
    ScenarioStep(tsGOTO, "jdi the_maw",
        "Proběhl přesun na: The Maw\nSousedící místnosti:\nTRC",
        "the_maw",
        ("TRC", "Kartograf"),
        ("[Arbiter]",),
        ("Pistole", "generátor_štítu", "Index")
        ),
    ScenarioStep(tsNS_2, "použij Index [Arbiter]",
        "Předmět (Index) byl použit na [Arbiter]",
        "the_maw",
        ("TRC", "Kartograf"),
        (),
        ("Pistole", "generátor_štítu")
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
