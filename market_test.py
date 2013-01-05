import market
from player import Player
import unittest
from distribution import UniformDistribution

class TestMarket(unittest.TestCase):
    def setUp(self):
        market.rawg_supply_distribution = UniformDistribution(100,100)
        market.rig_demand_distribution = UniformDistribution(100,100)

    def test_buy_rawgs(self):
        # setup
        # todo: cash
        rawg_demands = [30, 20, 100, 10]
        rawg_prices = [11, 14, 1, 4]
        rawgs_bought = [30, 20, 40, 10]
        players = [Player(rawg_demand=d, rawg_price=p) for (d,p) in zip(rawg_demands, rawg_prices)]

        # market stuff
        market.buy_rawgs(players)

        # assert
        self.assertEqual(rawgs_bought, [p.rawg_quantity for p in players])
        
    def test_sell_rigs(self):
        # setup
        rig_quantities = [100, 80, 20, 0]
        rig_supplies   = [30,  20, 10, 0]
        rig_prices     = [6,   14, 10, 4]
        rigs_sold      = [30,  20, 10, 0]
        players = [Player(rig_quantity=q, rig_supply=s, rig_price=p, cash=0) for (q,s,p) in zip(rig_quantities, rig_supplies, rig_prices)]
        
        # market stuff
        market.sell_rigs(players)

        #assert
        self.assertEqual([q-s for q,s in zip(rig_quantities, rigs_sold)], [p.rig_quantity for p in players])

if __name__ == '__main__':
    unittest.main()
