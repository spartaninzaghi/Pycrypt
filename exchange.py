from prompts import *
from order import Order
from trade import Trade
from datetime import datetime


class Account(object):

    def __init__(self, user, asset, amount):
        self.assets = dict()
        self.assets[asset] = amount


class Exchange(object):

    def __init__(self):
        # Portfolios
        self.accounts = {}
        self.open_orders = {}
        self.closed_orders = {}

        # Summaries
        self.trade_history = {}
        self.exchange_log = {}
        self.bid_ask_spread = {}

    def deposit(self, user, asset, amount):
        if self.validate_deposit(amount):
            if user not in self.accounts.keys():
                self.accounts[user] = {
                    'assets': {
                        asset: amount
                    },
                    'account_log': [],
                    'trade_history': []
                }
            elif asset not in self.accounts[user]['assets'].keys():
                self.accounts[user]['assets'][asset] = amount
            else:
                self.accounts[user]['assets'][asset] += amount
            self.accounts[user]['account_log'].append(
                f"Deposited {asset} {amount}, {datetime.now()}")
            return True
        return False

    def withdraw(self, user, asset, amount):
        if self.validate_withdrawal(user, asset, amount):
            if user in self.accounts.keys():
                self.accounts[user]['assets'][asset] -= amount
                self.accounts[user]['account_log'].append(
                    f"Withdrew {asset} {amount}, {datetime.now()}")
                return True
        return False

    def print_last_log(self, user):
        """ Print the most recent log item for the specified user.
        """
        print("\n\t" + "*" * 60)
        print("\t" + self.accounts[user]['account_log'][-1])
        print("\t" + "*" * 60 + "\n")

    def get_active_assets(self, user):
        try:
            return self.accounts[user]['assets'].keys()
        except KeyError:
            print(f"\n\tSorry, your account is currently empty.\n")
            return []

    def print_account_summary(self, asset, user):
        active_assets = self.get_active_assets(user)
        if active_assets:
            if asset == "all":
                print(ALL_BALANCES)
                for i, asset in enumerate(active_assets, 1):
                    print(f"\t{i}. {asset.upper()}: {self.accounts[user]['assets'][asset]}")
            else:
                print(f"\n\t{asset.upper()}: {self.accounts[user]['assets'][asset]}")

    def print_account_log(self, user):
        """
        """
        print("\n\t" + "*" * 50)
        try:
            account_log = self.accounts[user]['account_log']
            print("\t" + "\n\t".join(account_log))
        except KeyError:
            print(NO_ACTIVITY.format(user))
        print("\n\t" + "*" * 50 + "\n")

    def place_order(self, order):
        """ Add an order to the Exchange's open order market
        """
        pass

    def add_sell_order(self, order):
        """ Add a sell order to the Exchange's open order market
        """
        pass

    def add_buy_order(self, order):
        pass


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

    def check_sufficiency(self, user, asset, withdrawal_amount):
        """ Check whether a user has enough funds in their account for a
            withdrawal
        """
        if self.validate_asset(user, asset):
            overflow = (self.accounts[user]['assets'][asset] - withdrawal_amount) < 0
            if overflow:
                print("\n\tSorry, this withdrawal will place you in overdraft.")
                return False
            return True
        return False

    def validate_amount(self, amount):
        """ Ensure that asset amounts are positive.
        """
        return amount >= 0 and type(amount) == float

    def validate_user(self, user: str):
        """ Confirm whether or not a user already has an account in `accounts`.
        """
        return user in accounts

    def validate_asset(self, user, asset: str):
        """ Check whether the `users`' asset exists in our collection of traded assets.
        """
        try:
            valid = asset in self.accounts[user]['assets'].keys()
            if not valid:
                print(f"\n\tSorry, you don't have an existing {asset.upper()} account")
        except KeyError:
            print(f"Sorry {user}, you don't have any assets in your account.")
            return False
        return valid

    def validate_side(self, side: str):
        """ Check whether side is `buy` or `sell`.
        """
        return side in ["buy", "sell"]

    def validate_deposit(self, amount):
        """ Ensure that amounts are positive.
        """
        return self.validate_amount(amount)

    def validate_withdrawal(self, user, asset, withdrawal_amount):
        """ Check whether a user has enough assets to withdraw
        """
        if self.validate_amount(withdrawal_amount):
            if self.check_sufficiency(user, asset, withdrawal_amount):
                return True
        return False

    def validate_buy(self, order, accounts):
        """ Check the validity of a buy order placed by a taker.
        """
        withdrawal_amount = order.price * order.amount
        if self.validate_withdrawal(order.user, order.asset, withdrawal_amount,
                                    accounts):
            pass

    def validate_sell(self, order):
        """ Check the validity of a sell order placed by a taker.
        """
        pass
