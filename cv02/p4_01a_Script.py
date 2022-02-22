"""
Modul s definici atributů a přímo prováděných akcí.
"""

# Datové atributy modulu
pozdrav     = 'Dobrý den'
představení = f'Já jsem datový atribut modulu {__name__}'

# Definice akcí, které se při zavádění modulu provedou
# Použití atributu definovaného v daném modulu se nekvalifikuje
print(f'{pozdrav}\n{představení}\n{__doc__=}\n')
input("Až se pokocháš, stiskni Enter")
