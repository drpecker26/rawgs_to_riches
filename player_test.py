from player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pass

    def test_cash(self):
        p = Player(cash=2)
        self.assertRaises(ValueError, p = Player(cash=-2))

    def test_rawgs(self):
        pass

    def test_rigs(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
