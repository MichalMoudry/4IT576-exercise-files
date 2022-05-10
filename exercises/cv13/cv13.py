from datetime import datetime

# Definice dekorátoru
def decorator(fce):
    def wrapper_fce(*args, **kwargs):
        print(f"Function: {fce.__name__}")
        print(f"Date: {datetime.today()}")
        print(35*"-")
        fce(*args, **kwargs)
    return wrapper_fce

@decorator
def print_val(value):
    print(f"Input: {value}")

print_val(5)