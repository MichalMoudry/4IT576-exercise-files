#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""\
Balíček se společnými pomocnými programy pro testy hry.¤

Podbalíčky:

Moduly:
    common      - ??? Ještě nevím
    conversion  - Převod textu na ascii

Soubory:

Třídy:

Funkce:

Data:


"""
import dbg
dbg.start_pkg(0, __name__, __doc__)
############################################################################

ERRORS:list[str] = []       # Seznam chyb odhalených při testu



############################################################################
# Odebrání diakritiky

CONVERSION = {
    "Á":"A",  "á":"a",    "Ä":"AE", "ä":"ae",
    "Č":"C",  "č":"c",
    "Ď":"D",  "ď":"d",
    "Ë":"E",  "ë":"e",
    "É":"E",  "é":"e",    "Ě":"E",  "ě":"e",
    "Í":"I",  "í":"i",    "Ï":"I",  "ï":"i",   # "Ï":"IE", "ï":"ie",
    "Ĺ":"L",  "ĺ":"l",    "Ľ":"L",  "ľ":"l",
    "Ň":"N",  "ň":"n",
    "Ó":"O",  "ó":"o",    "Ö":"O",  "ö":"o",   # "Ö":"OE", "ö":"oe",
    "Ô":"O",  "ô":"o",
    "Ŕ":"R",  "ŕ":"r",    "Ř":"R",  "ř":"r",
    "Š":"S",  "š":"s",
    "Ť":"T",  "ť":"t",
    "Ú":"U",  "ú":"u",    "Ü":"U",  "ü":"u",   # "Ü":"UE", "ü":"ue",
    "Ů":"U",  "ů":"u",
    "Ý":"Y",  "ý":"y",    "Ÿ":"Y",  "ÿ":"y",   # "Ÿ":"YE", "ÿ":"ye",
    "Ž":"Z",  "ž":"z",
    "ß":"ss",
    "„":"\"", "“":"\"",   "”":"\"",
    "‚":"\'", "‘":"\'",   "’":"\'",
    "×":"x",  "÷":":",
    "–":"-",  "—":"-",    # ndash, mdash
    "¦":"|",
    "‹":"<",  "›":">",    "«":"<<", "»":">>",
    "©":"(c)","®":"(R)",
    "\xA0":" ",           # nbsp
}

def to_ascii(text:str) -> str:
    """Převede zadaný text do ekvivalentního tvaru bez diakritických
    znamének a dalších ne-ASCII znaků. Znaky chybějící v převodní tabulce
    převede na standardní na odpovídající escape-sekvenci typu \\x, \\u, \\U.
    """
    result = ''
    for c in text:
        if ord(c) < 128:
            result += c
        elif c in CONVERSION:
            result += CONVERSION[c]
        else:
            result += ascii(c)
    return result



############################################################################
dbg.stop_mod(0, __name__)
