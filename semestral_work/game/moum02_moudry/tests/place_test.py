"""
Modul obsahující definici testovacích případů pro třídu Place.
"""

import unittest

from classes.place import Place
from classes.item import Item

class PlaceTestMethods(unittest.TestCase):
    """
    Třída obsahující metody pro testování trídy Place.
    """

    def setUp(self) -> None:
        """
        Metoda pro nastavení test fixture.
        """
        self.place = Place(
            "Test place",
            "Test place description",
            ("the_pillar_of_autumn", "knihovna"),
            ("_Test item 1", "_Test item 2", "#Test item 3"),
            True
        )
        self.place.initialize()
        return super().setUp()
    
    def test_init(self):
        """
        Funkce pro otestování metody __init__.
        """
        self.assertEqual(self.place.name, "Test place")
        self.assertEqual(self.place.description, "Test place description")
        self.assertTrue(self.place.is_locked)