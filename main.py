from data import *


def make_drink(drink):
    enough_resources = check_resources(drink)
    if enough_resources:
        drink_price = check_money(drink)
        if drink_price>0:
            resources['water'] = resources['water'] - MENU[drink]['ingredients']['water']
            if 'milk' in MENU[drink]['ingredients']:
                resources['milk'] = resources['milk'] - MENU[drink]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[drink]['ingredients']['coffee']
            profit(drink_price)
            print(f"Enjoy your {drink} ☕")
    else:
        print("Try again later")


def check_resources(drink):
    enough_water = resources['water'] >= MENU[drink]['ingredients']['water']
    if 'milk' in MENU[drink]['ingredients']:
        enough_milk = resources['milk'] >= MENU[drink]['ingredients']['milk']
    else:
        enough_milk = True
    enough_coffee = resources['coffee'] >= MENU[drink]['ingredients']['coffee']
    if enough_water and enough_milk and enough_coffee:
        return True
    else:
        if not enough_water:
            print("Sorry there is not enough water.")
        if not enough_milk:
            print("Sorry there is not enough milk.")
        if not enough_coffee:
            print("Sorry there is not enough coffee.")
        return 0


def check_money(drink):
    cost = MENU[drink]['cost']
    print("Please insert coins.")
    quarters = int(check_coins(input("How many quarters?: ")))
    dimes = int(check_coins(input("How many dimes?: ")))
    nickels = int(check_coins(input("How many nickels?: ")))
    pennies = int(check_coins(input("How many pennies?: ")))
    input_coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if cost <= input_coins:
        change = round(input_coins - cost, 2)
        if change > 0:
            print(f"Here is your ${change} change.")
        return cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_coins(coins):
    if coins.isdigit():
        return coins
    else:
        print("Insert valid coins.")
        coins = input(f"How many coins: ")
        return int(check_coins(coins))


def print_report():
    print("Report:")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


def profit(drink_price):
    global money
    money = money + drink_price


operate = True

while operate:
    choice_drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice_drink == 'espresso' or choice_drink == 'latte' or choice_drink == 'cappuccino':
        make_drink(choice_drink)
    elif choice_drink == 'report':
        print_report()
    elif choice_drink == 'off':
        print("Switching off for repair...")
        operate = False
    else:
        print("Invalid input. Try again (espresso/latte/cappuccino):")


