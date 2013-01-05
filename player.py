class Player(object):
    """a player in rawgs to riches"""
    def __init__(self, cash=0, rawg_quantity=0, rawg_demand=0, rawg_price=0, rig_quantity=0, rig_supply=0, rig_price=0):
        """create a new player"""
        self.cash = 0
        self.rawg_quantity = rawg_quantity
        self.rawg_demand = rawg_demand
        self.rawg_price = rawg_price
        self.rig_quantity = rig_quantity
        self.rig_supply = rig_supply
        self.rig_price = rig_price

    def __repr__(self):
        """representation of a player"""
        return '<player: %s>' % ', '.join(['%s: %s' % (attr, repr(getattr(self, attr))) for attr in dir(self) if '__' not in attr])

    def __setattr__(self, name, value):
        """validate values"""
        if 'name' == 'cash':
            if (value < 0):
                raise ValueError('Player cannot have negative cash')
        if 'rawg' in name:
            # make sure values are valid
            pass
        if 'rig' in name:
            # make sure values are valid
            pass
        # pass the call on to the parent
        object.__setattr__(self, name, value)
