import unittest
from stats import Stats

class TestStats(unittest.TestCase):
    def test_update(self):
        s = Stats()
        s.update("STR", 15)
        self.assertEqual(s.STR, 15)
