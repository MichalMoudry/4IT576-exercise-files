"""
Modul obsahující definici testovacích případů pro třídu Action.
"""

import unittest

from classes.action import Action

class ActionTests(unittest.TestCase):
    """
    Třída obsahující metody pro testování třídy Action.
    """

    def setUp(self) -> None:
        """
        Metoda pro nastavení test fixture.
        """
        callable_function = lambda val : val % 2 == 0
        self.test_action = Action(
            "Test action",
            "Test action description",
            callable_function
        )
        return super().setUp()
    
    def test_init(self):
        """
        Funkce pro otestování metody __init__.
        """
        self.assertEqual(self.test_action.name, "Test action")
        self.assertEqual(
            self.test_action.description,
            "Test action description"
        )
        res = self.test_action._execute(2)
        self.assertTrue(res)