"""
Modul obsahující definici testovacích případů pro třídu ANamed.
"""
import unittest
from classes.abstract.anamed import ANamed

class ANamedTests(unittest.TestCase):
    """
    Třída obsahující metody pro testování třídy ANamed.
    """

    def setUp(self) -> None:
        """
        Metoda pro nastavení test fixture.
        """
        self.test_anamed = ANamed("Test named 1")
        return super().setUp()
    
    def test_init(self):
        """
        Metoda pro testování metody __init__.
        """
        self.assertEqual(self.test_anamed.name, "Test named 1")
    
    def test_str(self):
        """
        Metoda pro testování metody __str__.
        """
        self.assertEqual(
            self.test_anamed.__str__(),
            self.test_anamed.name
        )