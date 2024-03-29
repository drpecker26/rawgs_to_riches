import market
import unittest
from util.distribution import UniformDistribution

class TestMarket(unittest.TestCase):
    def setUp(self):
        market.clear_players()
        market.rawg_supply_distribution = UniformDistribution(100,100)
        market.rig_demand_distribution = UniformDistribution(100,100)

    def test_buy_rawgs(self):
        # setup
        rawg_demands = [30, 20, 100, 10]
        rawg_prices = [11, 14, 1, 4]
        rawgs_bought = [30, 20, 40, 10]
        for i,(d,p) in enumerate(zip(rawg_demands, rawg_prices)):
            market.add_player(username=i, cash=1000, rawg_demand=d, rawg_price=p)

        # market stuff
        market.buy_rawgs()

        # assert
        for i, r in enumerate(rawgs_bought):
            self.assertEqual(r, market.players[i].rawg_quantity )

    def test_sell_rigs(self):
        # setup
        rig_quantities = [100, 80, 20, 0]
        rig_supplies   = [30,  20, 10, 0]
        rig_prices     = [6,   14, 10, 4]
        rigs_sold      = [30,  20, 10, 0]
        i = 0
        for i, (q,s,p) in enumerate(zip(rig_quantities, rig_supplies, rig_prices)):
            market.add_player(username=i, rig_quantity=q, rig_supply=s, rig_price=p, cash=0)

        # market stuff
        market.sell_rigs()

        #assert
        for i,(q,s) in enumerate(zip(rig_quantities, rigs_sold)):
            self.assertEqual(q-s, market.players[i].rig_quantity)

if __name__ == '__main__':
    unittest.main()
