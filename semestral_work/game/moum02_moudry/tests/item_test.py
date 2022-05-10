"""
Modul obsahující definici testovacích případů pro třídu Item.
"""

import unittest
from ..item import Item, UNMOVABLE_ITEM_WEIGHT

class ItemTests(unittest.TestCase):
    """
    Třída obsahující metody pro testování třídy Item.
    """

    def setUp(self) -> None:
        """
        Metoda pro nastavení test fixture.
        """
        self.test_items = (
            Item("_Test item 1"),
            Item("#Test item 2")
        )
        return super().setUp()

    def test_weight(self):
        """
        Metoda pro testování nastavení váhy během inicializace.
        """
        item1_weight = self.test_items[0].weight
        item2_weight = self.test_items[1].weight
        self.assertEqual(item1_weight, 1)
        self.assertEqual(item2_weight, UNMOVABLE_ITEM_WEIGHT)

    def test_name(self):
        """
        Metoda pro testování názvu věcí.
        """
        item1_name = self.test_items[0].name
        item2_name = self.test_items[1].name
        self.assertEqual(item1_name, "Test item 1")
        self.assertEqual(item2_name, "Test item 2")