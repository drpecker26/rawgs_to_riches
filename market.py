"""a market for rawgs and rigs"""

from distribution import UniformDistribution
from operator import attrgetter

# module level variables
rawg_supply_distribution = UniformDistribution(40, 200)
rig_demand_distribution = UniformDistribution(20, 1000)

def buy_rawgs(players):
    """allocate rawgs in the market to players based on their quantities and bids"""
    players = list(players) # copy the list
    rawgs = rawg_supply_distribution()
    while rawgs:
        highest_bidder = max(players, key=attrgetter('rawg_price'))
        players.remove(highest_bidder)
        rawgs_to_sell = min(rawgs, highest_bidder.rawg_demand)
        rawgs -= rawgs_to_sell
        highest_bidder.rawg_quantity += rawgs_to_sell
        
