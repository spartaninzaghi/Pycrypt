class Trade(object):

  def __init__(self, buyer, seller, amount, asset, price):
    self.buyer = buyer
    self.seller = seller
    self.amount = amount
    self.asset = asset
    self.price = price

  def __str__(self):
    return f"""
      Buyer  : {self.buyer}
      Seller : {self.seller}
      Asset  : {self.asset}
      Amount : {self.amount}
      Price  : {self.price}
    """