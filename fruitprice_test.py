import unittest
from fruitprice import fruit_prices

class TestFruitPrice (unittest.TestCase):
    def test_fruitprice (self):
        self.assertAlmostEqual(fruit_prices(1), 2)
        self.assertAlmostEqual(fruit_prices(3), 6)
        self.assertAlmostEqual(fruit_prices(3), 7)
