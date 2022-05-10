"""
Modul obsahující definici testovacích případů pro třídu Place.
"""

import unittest

from ..place import Place

class PlaceTests(unittest.TestCase):
    """
    Třída obsahující metody pro testování třídy Place.
    """

    def setUp(self) -> None:
        """
        Metoda pro nastavení test fixture.
        """
        self.test_place = Place(
            "Test place",
            "Test place description",
            ("the_pillar_of_autumn", "knihovna"),
            ("_Test item 1", "_Test item 2", "#Test item 3"),
            True
        )
        self.test_place.initialize()
        return super().setUp()
    
    def test_init(self):
        """
        Funkce pro otestování metody __init__.
        """
        self.assertEqual(self.test_place.name, "Test place")
        self.assertEqual(
            self.test_place.description,
            "Test place description"
        )
        self.assertTrue(self.test_place.is_locked)
        test_place_names = ("the_pillar_of_autumn", "knihovna")
        self.assertTrue(
            len(test_place_names) == len(self.test_place.neighbors)
        )

    def test_is_locked_property(self):
        """
        Funkce pro otestování vlastnosti is_locked.
        """
        initial_value = self.test_place.is_locked
        self.test_place.is_locked = not(self.test_place.is_locked)
        self.assertNotEqual(initial_value, self.test_place.is_locked)