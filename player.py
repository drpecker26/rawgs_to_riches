class Player(object):
    """a player in rawgs to riches"""
    def __init__(self, cash=0, rawg_quantity=0, rawg_demand=0, rawg_price=0, rig_quantity=0, rig_supply=0, rig_price=0, username='player'):
        """create a new player"""
        # use object.__setattr__ to bypass validations
        object.__setattr__(self, 'cash', cash)
        object.__setattr__(self, 'rawg_quantity', rawg_quantity)
        object.__setattr__(self, 'rawg_demand', rawg_demand)
        object.__setattr__(self, 'rawg_price', rawg_price)
        object.__setattr__(self, 'rig_quantity', rig_quantity)
        object.__setattr__(self, 'rig_supply', rig_supply)
        object.__setattr__(self, 'rig_price', rig_price)
        object.__setattr__(self, 'username', username)

        # validate everything
        self.validate()

    def validate(self):
        """perform all validations"""
        self.validate_cash()
        self.validate_rawgs()
        self.validate_rigs()

    def update(self, **kwargs):
        """update and validate"""
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)
        self.validate()

    def stats(self):
        """return this players stats as a dictionary"""
        return {attr: getattr(self, attr) for attr in ['cash', 'rawg_quantity', 'rawg_demand', 'rawg_price', 'rig_quantity', 'rig_supply', 'rig_price']}

    def __repr__(self):
        """representation of a player"""
        return '<Player %s: %s>' % (self.username, repr(self.stats()))

    def validate_cash(self):
        if self.cash < 0:
            raise ValueError('Player cannot have negative cash')

    def validate_rawgs(self):
        if self.rawg_demand * self.rawg_price > self.cash:
            raise ValueError('Player does not have enough cash to buy %d rawgs at %.2f each' % (self.rawg_demand, self.rawg_price))

    def validate_rigs(self):
        if self.rig_supply > self.rig_quantity:
            raise ValueError('Player does not have enough rigs to sell %d rigs' % self.rig_supply)

    def __setattr__(self, name, value):
        """validate values"""
        # pass the call on to the parent
        object.__setattr__(self, name, value)
        # validate appropriate attributes                   
        if 'name' == 'cash':
            self.validate_cash()
        if 'rawg' in name:
            self.validate_rawgs()
        if 'rig' in name:
            self.validate_rigs()
