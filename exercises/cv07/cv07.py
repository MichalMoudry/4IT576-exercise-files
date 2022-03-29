from unicodedata import name


class Třída12a:
    """
    Test třída.
    """
    print("start")
    def metoda(self, parametr: str):
        """
        Test metoda.
        """
        return f"Parameter: {parametr}"
    print("end")

class Třída12b:
    """
    Třída počítající vlastní instance.
    """
    instance:int = 0

    def __init__(self, name: str = "Nezadán") -> None:
        Třída12b.instance += 1
        self.ID = Třída12b.instance
        self.name = name

    def __repr__(self) -> str:
        """
        Systémový popis třídy Třída12b.
        """
        return f"Třída_{self.ID}_{self.name}"

instance = Třída12a()
print(instance.metoda("Test parameter"))

instance_b_1 = Třída12b("Instance 1")
instance_b_2 = Třída12b("Instance 2")
instance_b_3 = Třída12b("Instance 3")
instance_b_1.instance = 1
print(f"Počet instancí: {Třída12b.instance}", (instance_b_1, instance_b_2, instance_b_3))
print(instance_b_1.instance)