# Test script
"""
Zadejte po jedné kontrolní otázce z následujících oblastí:
    Definice metod
    Podmíněný příkaz
    Cyklus se vstupní podmínou
    Cyklus s parametrem
    Práce se slovníkem

Otázky mohou být jako teoretické (syntaxe, pravidla používání, ...), tak praktické
(ukázka programu s dotazem na jeho výsledek včetně možnosti zhroucení či syntaktické chyby).
"""
import moum02_moudry as moum

#moum.self_test()

is_even = lambda number : number % 2 == 0

print(is_even(3))