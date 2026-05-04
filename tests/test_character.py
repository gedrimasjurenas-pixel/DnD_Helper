import unittest
from character import Character

class TestCharacter(unittest.TestCase):
    def test_damage(self):
        c = Character("Test", "Mage", "None")
        c.take_damage(5)
        self.assertEqual(c.health, 5)

    def test_heal(self):
        c = Character("Test", "Mage", "None")
        c.take_damage(5)
        c.heal(3)
        self.assertEqual(c.health, 8)
