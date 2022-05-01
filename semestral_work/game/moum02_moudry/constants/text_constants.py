"""
Konstanty pro textové výstupy aplikace.
"""

# Konstanty pro textové výstupy aplikace
UNKNOWN_COMMAND = "Neznámý příkaz"
AVAILABLE_COMMANDS = ("Příkazy, které lze zadat:\n"
"- jdi [místo]\n"
"- zvedni [věc]\n"
"- přehled\n"
"- otevři [místnost]\n"
"- polož [věc]\n"
"- použij [věc] [cíl]\n"
"- ?\n"
"- oslov [osoba]\n"
"- ukončit_rozhovor\n"
"- konec")
WELCOME_MESSAGE = (
"Vítejte ve hře Halo, kdy vaším cílem je se dostat "
"do místnosti 'The Maw',\npřičemž pro úspěšné dokončení hry je "
"třeba donést tzv. Index a\npoužít ho na postavu Arbiter, který se "
"nachází v zamčené knihovně,\ntedy je třeba knihovnu odemknouta sebrat"
"Index do batohu.\n\nPro zobrazení nápovědy je třeba zadat příkaz: ?."
)
END_TALK_TEXT = "Rozhovor byl úspěšně ukončen."
ITEM_TAKE_TEXT = "Předmět byl zvednut"
GAME_END = "Hra byla ukončena"
ROOM_MOVE = "Proběhl přesun na:"
NEIGHBOURING_ROOMS_TEXT = "Sousední místnosti:"

## Errors
EMPTY_COMMAND = "Prázdný příkaz"
WRONG_NEIGHBOUR = "Zadané místo není sousedem"
OBJECT_NOT_PRESENT = "Objekt není v této místnosti"
WRONG_START_TEXT = ("Prvním příkazem není startovací příkaz.\n"
"Hru, která neběží, lze spustit pouze startovacím příkazem.\n")
COMMAND_MISSING_PARAMS = "Příkazu chybí požadované parametry"
WRONG_ARGUMENT = "Špatný argument parametru"
MISSING_ARGUMENT = "Nebyl zadán argument příkazu"
ITEM_NOT_IN_BAG = "Předmět není v batohu"
BAG_FULL = "Váš batoh je plný"
WRONG_ITEM_TARGET = "Špatný cíl použití věci"
UNUSEABLE_ITEM = "Tuto věc nelze použít"
OPEN_WRONG_COND = "Tato místnost není zavřená nebo ani neexistuje"
ROOM_IS_LOCKED = "Místnost je zamčená"
MISSING_KEY = "Nemáte potřebný klíč v batohu"