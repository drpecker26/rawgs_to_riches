class Player(object):
    """a player in rawgs to riches"""
    def __init__(self, cash=1000, rawg_quantity=50, rawg_demand=0, rawg_price=0, rig_quantity=30, rig_supply=0, rig_price=0, username='player', num_factories=0):
        """create a new player"""
        self.username = username
        self.update(cash=cash, rawg_quantity=rawg_quantity, rawg_demand=rawg_demand, rawg_price=rawg_price, rig_quantity=rig_quantity, rig_supply=rig_supply, rig_price=rig_price, num_factories=num_factories)

    def __repr__(self):
        """representation of a player"""
        return '<Player %s: %s>' % (self.username, repr(self.stats()))

    def __setattr__(self, name, value):
        """validate values"""
        # pass the call on to the parent
        object.__setattr__(self, name, value)
        # validate appropriate attributes                   
        if name == 'cash':
            self.validate_cash()
        elif 'rawg' in name:
            self.validate_rawgs()
        elif 'rig' in name:
            self.validate_rigs()
        elif name == 'num_factories':
            self.validate_factories()

    def build_factory(self):
        pass

    def update(self, **kwargs):
        """update and validate"""
        # TODO: don't change values if validation fails
        for attr, value in kwargs.items():
            object.__setattr__(self, attr, value)
        self.validate()

    def stats(self):
        """return this players stats as a dictionary"""
        return {attr: getattr(self, attr) for attr in ['cash', 'rawg_quantity', 'rawg_demand', 'rawg_price', 'rig_quantity', 'rig_supply', 'rig_price']}

    def validate(self):
        """perform all validations"""
        self.validate_cash()
        self.validate_rawgs()
        self.validate_rigs()
        self.validate_factories()


        # Eventually: Allow this. Negative cash gets taxed at a higher interest rate. 
    def validate_cash(self):
        if self.cash < 0:
            raise ValueError('Player cannot have negative cash')

       # Eventually: Allow this. Negative cash gets taxed at a higher interest rate.
    def validate_rawgs(self):
        if self.rawg_demand * self.rawg_price > self.cash:
            raise ValueError('Player does not have enough cash to buy %d rawgs at %.2f each' % (self.rawg_demand, self.rawg_price))

       # Eventually: Change this. Player never decides how many rigs he'd want to sell. 
    def validate_rigs(self):
        if self.rig_supply > self.rig_quantity:
            raise ValueError('Player does not have enough rigs to sell %d rigs' % self.rig_supply)

    def validate_factories(self):
        if self.num_factories < 0: # TODO: is there a max number of factories?
            raise ValueError('Player cannot have negative factories')
            
