class Stock:
    __slots__ = ("name", "_shares", "price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, subshares):
        self.shares -= subshares

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("expected an integer")
        self._shares = value

