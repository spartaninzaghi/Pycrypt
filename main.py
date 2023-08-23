from transact import *
from prompts import *
from exchange import Exchange
from order import Order
from trade import Trade


def choice_error_check(user, menu):
    while True:
        choice = input(menu.format(user)).casefold()
        if choice not in ['1', '2', '3', '4', '5']:
            print(WRONG_CHOICE)
        else:
            return choice


def main():
    exchange = Exchange()
    user = input("\nPlease enter your username: ")

    choice = choice_error_check(user, MENU)

    while choice != '5':

        if choice == "1":
            make_deposit(user, exchange)

        elif choice == "2":
            make_withdrawal(user, exchange)

        elif choice == "3":
            side = input(SIDES).strip.lower()
            order = Order()

        elif choice == "4":
            display_summary(user, exchange)

        choice = choice_error_check(user, MENU_TRUNC)

    print(EXIT_MESSAGE.format(user))


if __name__ == "__main__":
    main()
