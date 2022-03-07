from res import MENU
from res import resources

def get_keys(command):
    return "milk" in MENU[command]["ingredients"].keys()

def check_resources(command):

    if MENU[command]["ingredients"]["water"] > resources["water"]:
        print("Insufficient water to complete your order")
        return False
    elif get_keys(command):
        if MENU[command]["ingredients"]["milk"] > resources["milk"]:
            print("Insufficient milk to complete your order")
            return False
        else:
            if MENU[command]["ingredients"]["coffee"] > resources["coffee"]:
                print("Insufficient coffee to complete your order")
                return False
            else:
                return True
    elif MENU[command]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient coffee to complete your order")
        return False
    else:
        return True

def get_coins():
    quarters = input('Quarters: ')
    dimes = input('Dimes: ')
    nickles = input("Nickles: ")
    pennies = input("Pennies: ")
    value = (int(quarters)*0.25)+(int(dimes)*0.10)+(int(nickles)*0.05)+(int(pennies)*0.01)
    return value


while True:
    command = input(">What would you like? (espresso/latte/cappuccino) ")
    if command.casefold() == "report".casefold():
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        if resources["money"] != 0:
            print(f'Money: {resources["money"]}$')

    elif command.casefold() == "off".casefold():
        print("Now turning off")
        break
    elif command.casefold() == "espresso" or command.casefold() == "latte" or command.casefold() == "cappuccino":
        if check_resources(command):
            value = get_coins()
            if value < MENU[command]["cost"]:
                print("Sorry, that's not enough money. Money refunded")
            else:
                resources["money"] += MENU[command]["cost"]
                print(f'Here is {round(value-int(MENU[command]["cost"]), 2)}$ dollars in change')
                if command.casefold() == "latte" or command.casefold() == "cappuccino":
                    resources["milk"] -= MENU[command]['ingredients']["milk"]
                resources["water"] -= MENU[command]['ingredients']['water']
                resources['coffee'] -= MENU[command]['ingredients']['coffee']
                print(f'Here is your {command}. Enjoy!')

    else:
        print("Please enter a valid argument")