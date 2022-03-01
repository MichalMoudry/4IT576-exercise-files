# Funkce
# Lambda výrazy
fahr2cels = lambda fahr: round(5 * (fahr - 32) / 9)
def print_temperature_conversion(fahrenheit: float) -> str:
    """
    Metoda pro tisk převodu stupňů fahrenheit na celsius.
    """
    print(f"{fahrenheit}\N{DEGREE FAHRENHEIT}  is {fahr2cels(fahrenheit)}\N{DEGREE CELSIUS}")

print_temperature_conversion(100);


# Rozhodování
def ifExpr(value) -> str:
    return (("plus " if value > 0 else "minus ") + str(abs(value)))

print(ifExpr(5), ifExpr(-5))
## plus 5 minus 5