#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Pomocný modul pro zrychlené zadávání testů.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

def test(factory):
    from  .test_interface   import test as ti
    from ..tests            import Level
    ti(factory, Level.WHOLE)



############################################################################
dbg.stop_mod(0, __name__)
