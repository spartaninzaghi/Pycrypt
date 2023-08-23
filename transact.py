from prompts import *
from exchange import Exchange


def amount_error_check():
    """ Check whether the amount entered by the user is valid (can be typecasted to float).
    
    Args:
        None.
        
    Returns:
        amount (float): Valid amount as a floating point value.
    """
    while True:
        try:
            amount = float(input("\n\tEnter asset amount: "))
            break
        except TypeError:
            print("\nAmount Invalid! Please try again")
    return amount


def summary_error_check():
    """ Check whether the user's selection is part of the allowed options.
        If the user's choice is invalid, keep on asking until a valid option
        is entered.
    
    Args:
        None.
        
    Returns:
        summary (str): The number denoting the user's choice of summary as a `str`.
    """
    while True:
        summary = input(SUMMARIES)
        if summary not in ['1', '2', '3']:
            print(WRONG_CHOICE)
        else:
            return summary


def asset_error_check(user, exchange):
    """
    """
    while True:
        asset = input("\n\tEnter asset type: ").casefold()
        if not exchange.validate_asset(user, asset):
            print("\tPlease try again.\n")
        else:
            return asset


def make_deposit(user, exchange):
    """ Deposit a given amount into the user's account within the exchange.
    
    Args:
        user (str): The username of the person currently signed in & using the program.
        exchange: The exchange of type `Exchange`, where transactions happen.
    
    Returns:
        None.
    """
    asset = input("\n\tEnter asset type: ").casefold()
    amount = amount_error_check()

    success = exchange.deposit(user, asset, amount)
    while not success:
        choice = input(RETRY_DEPOSIT)
        if choice == "1":
            asset = input("\n\tEnter asset type: ").casefold()
            amount = amount_error_check()
            success = exchange.deposit(user, asset, amount)
        else: # return to main menu
            break
    if success:
        print(f"\n\t{amount} of {asset.upper()} deposited successfully\n")


def make_withdrawal(user, exchange):
    """ Withdraw a given amount from the user's account within the exchange.
    
    Args:
        user (str): The username of the person currently signed in & using the program.
        exchange: The exchange of type `Exchange`, where transactions happen.
    
    Returns:
        None.
    """
    asset = asset_error_check(user, exchange)
    amount = amount_error_check()

    success = exchange.withdraw(user, asset, amount)
    while not success:
        choice = input(RETRY_WITHDRAWAL)
        if choice == "1":
            asset = asset_error_check(user, exchange)
            amount = amount_error_check()
            success = exchange.withdraw(user, asset, amount)
        else: # return to main menu
            break
    if success:
        print(f"\n\t{amount} of {asset.upper()} withdrawn successfully\n")    


def display_summary(user, exchange):
    """ Display the results of one of the 3 summary options for the user.
    
    Args:
        user (str): The username of the person currently signed in & using the program.
        exchange: The exchange of type `Exchange`, where transactions happen.
        
    Returns:
        None.
    """
    summary = summary_error_check()

    if summary == '1':
        active_assets = [a.upper() for a in exchange.get_active_assets(user)]
        if active_assets:
            print("\n\t" + "\n\t".join(active_assets) + "\n\tAll")
            asset = input("\n\tSELECTION : ").casefold()
            exchange.print_account_summary(asset, user)
        else:
            pass

    elif summary == '2':
        exchange.print_account_log(user)
    else:
        pass
