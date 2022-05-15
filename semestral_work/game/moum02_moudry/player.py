"""
Informace o hráči hry.
"""

from .text_constants import IS_LIBRARY_OPEN, DO_YOU_HAVE_LIBRARY_KEY

def initialize() -> None:
    """
    Inicializuje stav hráče.
    """
    global progress
    progress[DO_YOU_HAVE_LIBRARY_KEY] = "Ne"
    progress[IS_LIBRARY_OPEN] = "Ne"

progress:dict[str, str] = {
    DO_YOU_HAVE_LIBRARY_KEY: "Ne",
    IS_LIBRARY_OPEN: "Ne"
}