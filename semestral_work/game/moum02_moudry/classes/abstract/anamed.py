class ANamed():
    """Instance představují objekty v prostorech či batohu.
    """

    def __init__(self, name:str, **args):
        """Inicializuje objekt zadaným názvem.
        """
        super().__init__(**args)
        self._name = name

    @property
    def name(self) -> str:
        """Vrátí název daného objektu.
        """
        return self._name


    def __str__(self) -> str:
        """Vrátí uživatelský textový podpis jako název dané instance.
        """
        return self._name
    
    # TODO: Asi smazat?
    def __repr__(self) -> str:
        """Vrátí uživatelský textový podpis jako název dané instance.
        """
        return self._name