MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost": 0
}

global quaters, dimes, nickles, pennies, water, milk, coffee, cost, total_coins, result

should = True
while True:
    result = input("What would you like? (espresso/latte/cappuccino): ").lower()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    cost = resources["cost"]


    def resource():
        print(f"water: {water}\nmilk: {milk}\ncoffee: {coffee}\ncost: {cost}")


    def calculate_coins():
        global quaters, dimes, nickles, pennies, water, milk, coffee, cost, total_coins, result
        quaters = float(input("Enter the Quaters: $"))
        dimes = float(input("Enter the Dimes: $"))
        nickles = float(input("Enter the Nickles: $"))
        pennies = float(input("Enter the Pennies: $"))
        quaters = .25 * quaters
        dimes = .10 * dimes
        nickles = .05 * nickles
        pennies = .01 * pennies
        total_coins = quaters + dimes + nickles + pennies
        total_coins = round(total_coins, 2)


    if result == "espresso" or result == "latte" or result == "cappuccino":
        calculate_coins()


    def espresso():
        global quaters, dimes, nickles, pennies, water, milk, coffee, cost, total_coins, result
        if total_coins >= MENU["espresso"]["cost"]:
            if water >= MENU["espresso"]["ingredients"]["water"] and coffee >= MENU["espresso"]["ingredients"][
                "coffee"]:
                print(f"Here is your {result}! ☕")
                w =round ((MENU["espresso"]["cost"]),2)
                print(f"Here is your Change {total_coins - w}")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                resources["cost"] += MENU["espresso"]["cost"]


            else:
                print(f"Sorry! Not enough resource to produce {result}.")
                print(f"Here is Your coins{total_coins}")
        else:
            print(f"You Does not have enough money \nHere is your Coins {total_coins} .")


    def latte():
        global quaters, dimes, nickles, pennies, water, milk, coffee, cost, total_coins, result
        if total_coins >= MENU["latte"]["cost"]:
            if water >= MENU["latte"]["ingredients"]["water"] and coffee >= MENU["latte"]["ingredients"][
                "coffee"] and milk >= MENU["latte"]["ingredients"]["milk"]:
                print(f"Here is your {result}! ☕")
                w = round((MENU["espresso"]["cost"]), 2)
                print(f"Here is your Change {total_coins - w}")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["cost"] += MENU["latte"]["cost"]

            else:
                print(f"Sorry! Not enough resource to produce {result}.")
                print(f"Here is Your coins{total_coins}")
        else:
            print(f"You Does not have enough money \nHere is your Coins {total_coins} .")


    def cappuccino():
        global quaters, dimes, nickles, pennies, water, milk, coffee, cost, total_coins, result
        if total_coins >= MENU["cappuccino"]["cost"]:
            if water >= MENU["cappuccino"]["ingredients"]["water"] and coffee >= MENU["cappuccino"]["ingredients"][
                "coffee"] and milk >= MENU["latte"]["ingredients"]["milk"]:
                print(f"Here is your {result}! ☕")
                w = round((MENU["espresso"]["cost"]), 2)
                print(f"Here is your Change {total_coins - w}")
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["cost"] += MENU["cappuccino"]["cost"]

            else:
                print(f"Sorry! Not enough resource to produce {result}.")
                print(f"Here is Your coins{total_coins}")
        else:
            print(f"You Does not have enough money \nHere is your Coins {total_coins} .")


    if result == "espresso":
        espresso()
    elif result == "latte":
        latte()
    elif result == "cappuccino":
        cappuccino()
    elif result == "resource":
        resource()
    elif result == "off":
        exit()
        should = False
    else:
        print("Invalid output! try again")



