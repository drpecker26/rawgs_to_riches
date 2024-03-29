"""a market for rawgs and rigs"""

from util.distribution import UniformDistribution
from operator import attrgetter
from player import Player

# module level variables
rawg_supply_distribution = UniformDistribution(40, 200)
rig_demand_distribution = UniformDistribution(20, 1000)
players = {}

def add_player(username, **kwargs):
    """add a player"""
    global players
    # TODO: make this atomic
    if username in players:
        raise KeyError('Username is already taken')
    players[username] = Player(username=username, **kwargs)

def clear_players():
    global players
    players = {}

def buy_rawgs():
    """sell rawgs to players"""
    remaining_players = players.values()
    rawg_supply = rawg_supply_distribution()
    while rawg_supply and remaining_players:
        highest_bidder = max(remaining_players, key=attrgetter('rawg_price'))
        remaining_players.remove(highest_bidder)
        rawgs_to_sell = min(rawg_supply, highest_bidder.rawg_demand)
        rawg_supply -= rawgs_to_sell
        new_cash = highest_bidder.cash - rawgs_to_sell * highest_bidder.rawg_price
        new_rawg_quantity = highest_bidder.rawg_quantity + rawgs_to_sell
        highest_bidder.update(cash=new_cash, rawg_quantity=new_rawg_quantity) # TODO: handle validation failure
        
def sell_rigs():
    """buy rigs from players"""
    remaining_players = players.values()
    rig_demand = rig_demand_distribution()
    while rig_demand and remaining_players:
        lowest_seller = min(remaining_players, key=attrgetter('rig_price'))
        remaining_players.remove(lowest_seller)
        rigs_to_buy = min(rig_demand, lowest_seller.rig_supply)
        rig_demand -= rigs_to_buy
        new_cash = lowest_seller.cash + rigs_to_buy * lowest_seller.rig_price
        new_rig_quantity = lowest_seller.rig_quantity - rigs_to_buy
        lowest_seller.update(cash=new_cash, rig_quantity=new_rig_quantity) # TODO: handle validation failure
