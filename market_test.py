import market
from player import Player
import unittest
from distribution import UniformDistribution

class TestMarket(unittest.TestCase):
    def setUp(self):
        rawg_demands = [30, 20, 100, 10]
        rawg_prices = [11, 14, 1, 4]
        self.players = [Player(rawg_demand=d, rawg_price=p) for (d,p) in zip(rawg_demands, rawg_prices)]
        market.rawg_supply_distribution = UniformDistribution(100,100)

    def test_buy_rawgs(self):
        market.buy_rawgs(self.players)
        rawg_quantities = [30, 20, 40, 10]
        self.assertEqual(rawg_quantities, [p.rawg_quantity for p in self.players])
        
if __name__ == '__main__':
    unittest.main()
