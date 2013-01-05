from player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pass

    def test_cash(self):
        p = Player(cash=2)
        with self.assertRaises(ValueError):
            p = Player(cash=-2)

    def test_rawgs(self):
        with self.assertRaises(ValueError):
            p = Player(cash=100, rawg_demand=25, rawg_price=5)

    def test_rigs(self):
        with self.assertRaises(ValueError):
            p = Player(rig_quantity=50, rig_supply=100)
        

if __name__ == '__main__':
    unittest.main()
