seznam = [1, "dvojka", 3.14, True]
print(seznam)

# Pozn.: True je 1 a 1 je už v množině
mnozina = {1, "dvojka", 3.14, True}
print(mnozina)

slovnik = {1:int, "dvojka":str, 3.14:float, True:bool, "key":3535}
print(slovnik)
print("key:", slovnik["key"])

print("")

generator = (x*x for x in range(5))
tuple_with_generator = tuple(generator)
print(tuple_with_generator)
# Generator lze použít jen jednou
print(tuple(generator))

# Variabilní počet argumentů
def hp(*param: int) -> None:
    print("Zadané argumenty:", param)
## Dvouhvězdičkový parameter
def hp2(**param: int) -> None:
    print("Zadané argumenty:", param)

hp(1, 2, 3, 4)
hp2(a=1, b=3, c=4)