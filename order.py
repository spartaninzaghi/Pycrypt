class Order(object):

    def __init__(self, user, side, asset, amount, price):
        self.user = user
        self.side = side
        self.asset = asset
        self.amount = amount
        self.price = price

    def __str__(self):
        return f"""
        User   : {self.user}
        Side   : {self.side}
        Asset  : {self.asset}
        Amount : {self.amount}
        Price  : {self.price}
    """

class BuyOrder(Order):
    pass


class SellOrder(Order):
    pass

