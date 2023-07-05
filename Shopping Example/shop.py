# Task 3 - HW 6

# Global Constants
items = {"apples": 50, "bananas": 20, "oranges": 150, "pears": 100, "grapes": 10}

AVAILABLE_MONEY = 100
INITIAL_COUNT = 0
MAX_COUNT = 3


# Press the green button in the gutter to run the script.
def welcome():
    return "Welcome to the fruit shop!"


def display_items_with_exit():
    """
    Display the items with exit option
    :return: 
    """""
    for item in items:
        print(item + ":" + str(items[item]))

    return input("Choose an Item to bur or press E to exit shopping:")


def exit_shopping():
    print("Exiting the shop, Thank you for shopping")
    exit()


def check_funds(money, choice):
    if money >= items[choice]:
        return True
    else:
        return False


class ExceededMaxCountException(Exception):
    """
     Custom Exception class to handle max tries
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidInputException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def begin_shopping(choice, money, number_of_tries):
    # check if he wants to exit
    if choice == "e":
        exit_shopping()

    if money < 0:
        raise InvalidInputException("Invalid amount in the account")

    if choice not in items:
        raise InvalidInputException("Invalid input")

    if number_of_tries >= MAX_COUNT:
        raise ExceededMaxCountException("Exceeded number of tries")

    # Check if user has money
    if check_funds(money, choice):
        money -= items[choice]
        return "Here’s your " + choice + "! and you are left with " + str(money)

    else:
        try:
            amount = input("You don't have enough money to buy this item. Press E to exit")
            begin_shopping(choice, money + int(amount), number_of_tries + 1)
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    print(welcome())
    user_choice = display_items_with_exit()
    print(begin_shopping(user_choice.lower(), AVAILABLE_MONEY, INITIAL_COUNT))
