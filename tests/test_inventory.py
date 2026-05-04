import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
    def test_add_item(self):
        inv = Inventory()
        inv.add_item("Sword")
        self.assertIn("Sword", inv.items)
