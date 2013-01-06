"""a market for rawgs and rigs"""

from util.distribution import UniformDistribution
from operator import attrgetter

# module level variables
rawg_supply_distribution = UniformDistribution(40, 200)
rig_demand_distribution = UniformDistribution(20, 1000)

def buy_rawgs(players):
    """sell rawgs to players"""
    players = list(players) # copy the list
    rawg_supply = rawg_supply_distribution()
    while rawg_supply and players:
        highest_bidder = max(players, key=attrgetter('rawg_price'))
        players.remove(highest_bidder)
        rawgs_to_sell = min(rawg_supply, highest_bidder.rawg_demand)
        rawg_supply -= rawgs_to_sell
        highest_bidder.cash -= rawgs_to_sell * highest_bidder.rawg_price
        highest_bidder.rawg_quantity += rawgs_to_sell
        
def sell_rigs(players):
    """buy rigs from players"""
    players = list(players) # copy the list
    rig_demand = rig_demand_distribution()
    while rig_demand and players:
        lowest_seller = min(players, key=attrgetter('rig_price'))
        players.remove(lowest_seller)
        rigs_to_buy = min(rig_demand, lowest_seller.rig_supply)
        rig_demand -= rigs_to_buy
        lowest_seller.rig_quantity -= rigs_to_buy
        lowest_seller.cash += rigs_to_buy + lowest_seller.rig_price
