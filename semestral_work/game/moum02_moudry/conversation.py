"""
Modul obsahující prvky pro realizaci konverzace ve hře.
"""

is_conversation_happening = False

answers = {
    "průběh": (
        "V této misi musíte dojít až do cíle na tomto "
        "prstenci, tedy do místnosti Maw a tam je potřeba porazit "
        "nepřítele jménem [Arbiter]."
    ),
    "na průběh": (
        "V této misi musíte dojít až do cíle na tomto "
        "prstenci, tedy do místnosti Maw a tam je potřeba porazit "
        "nepřítele jménem [Arbiter]."
    ),
    "ovládání": (
        "Ovládání fungujue na principu zadávání "
        "příkazů, kdy ho stačí napsat do pole a v některých "
        "případech i napsat potřebné parametry, třeba v případě "
        "zvedání věcí z prostoru."
    ),
    "na ovládání": (
        "Ovládání fungujue na principu zadávání "
        "příkazů, kdy ho stačí napsat do pole a v některých "
        "případech i napsat potřebné parametry, třeba v případě "
        "zvedání věcí z prostoru."
    )
}