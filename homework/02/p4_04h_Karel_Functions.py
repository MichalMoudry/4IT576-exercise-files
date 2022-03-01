#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_04h_Karel_Functions.py
"""
Návrhy funkcí v rámci domácího úkolu po probrání funkcí a Karla.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

from robotcz import *



###########################################################################q

def double_step(k:Karel) -> Karel:
    """Udělá zrychlený dvojitý krok;"""
    hide(k);    (
        step(k),        step(k),
    );unhide(k)


def put_left(k:Karel) -> Karel:
    """Položí značku na políčko vlevo od zadaného robota
    a vrátí odkaz na svůj argument, který zdánlivě nezměnil pozici."""
    hide(k);    (
        put_left(k),    step(k),
        put(k),         turn_about(k),
        step(k),        put_left(k),
    );unhide(k)


def pick_left(k:Karel) -> Karel:
    """Položí značku na políčko vlevo od zadaného robota
    a vrátí odkaz na svůj argument, který zdánlivě nezměnil pozici."""
    hide(k);    (
        put_left(k),    step(k),
        pick(k),        turn_about(k),
        step(k),        put_left(k),
    );unhide(k)


def turn_about(k:Karel) -> Karel:
    """Otočí zadaného robota o 180°."""
    hide(k);    (
        turn_left(k),   turn_left(k),
    );unhide(k)
    return k


def turn_right(k:Karel) -> Karel:
    """Otočí zadaného robota o 180°."""
    hide(k);    (
        turn_left(k),   turn_left(k),   turn_left(k),
    );unhide(k)
    return k



###########################################################################q

def turn_about(k:Karel) -> Karel:
    """Otočí zadaného robota o 180°."""
    hide(k);    (
        turn_left(k),   turn_left(k),
    );unhide(k)
    return k


def put_step(k:Karel) -> Karel:
    """Položí značku a udělá krok. """
    put(k);   step(k)
    return k


def put_korner(k:Karel) -> Karel:
    """Položí značku, před ní další, na žé se otočí vlevo
    a zajde za roh.
    """
    put_step(k)     # Položí značku a dojde na budoucí roh
    put(k);   turn_left(k);   step(k)   # Položí a zahne
    return k


def put_around(k:Karel) -> Karel:
    """Položí značky na políčka kolem zadaného robota, přičemž jeho
    výsledná pozice bude shodná s pozicí výchozí. Nic netestuje,
    předpokládá, že na žádném z okolních polí není zeď či robot.
    """
    hide(k)
    (   step(k), turn_left(k),      # Postaví se na okruh
        put_korner(put_korner(put_korner(put_korner(k)))),  # Obloží značky
        turn_left(k),   step(k),    # Vrátí se na původní pozici
        turn_about(k),              # Natočí se do původního směru
    )
    unhide(k)
    return k



###########################################################################q

def step_back(k:Karel) -> Karel:
    """Popojde se zadaným robotem krok vzad a vrátí odkaz na daného robota.
    """
    hide(k)
    turn_about(k);    step(k);    turn_about(k)
    unhide(k)
    return k


def put_5(k:Karel) -> Karel:
    """Položí pod zadaného robota 5 značek a vrátí odkaz na daného robota.
    """
    put( put( put( put( put(k)))))
    return k


def put_10(k:Karel) -> Karel:
    """Položí pod zadaného robota 5 značek."""
    put_5( put_5(k))
    return k


def sb_put10(k:Karel) -> Karel:
    """Couvne a položí 10 značek."""
    step_back(k)
    put_10(k)
    return k


def letter(k:Karel) -> Karel:
    """Něco udělá."""
    # hide(k)
    put_10(k)                                           # 59
    sb_put10(k);    sb_put10(k)                         # 60
    turn_left(k);   step_back(k);       turn_left(k)    # 64
    sb_put10(k)                                         # 67
    turn_left(k);   step(k);            put_10(k)       # 69
    turn_left(k);   step_back(k);       sb_put10(k)     # 72
    step(k);        step(k);            put_10(k)       # 75
    turn_left(k);   double_step(k);     turn_right(k)   # 78
    step(k)                                             # 84
    # unhide(k)
    return k



###########################################################################q
dbg.stop_mod(1, __name__)
