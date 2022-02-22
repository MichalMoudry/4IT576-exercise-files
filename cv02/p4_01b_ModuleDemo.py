#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/p4_01b_ModuleDemo.py
"""
Modul pro předvádění některých vlastnosti modulů a práce s nimi.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

text = f'Datový atribut modulu {__name__}'
print("Při zavádění se hodnoty výrazových příkazů nezobrazují")
text   # Výrazový příkaz => při zavádění modulu se nevytiskne
print('Chcete-li objekt zobrazit, musíte jej vytisknout\n',
      f'{text=}')

text2 = 'Druhý datový atribut'
_text = 'Neveřejný datový atribut'

############################################################################
dbg.stop_mod (0, __name__)
