from menu import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

profit = 0
total = 0


def coins():
    global total
    print("Please insert coins.")
    total = 0.25 * float(input("How many quarters?"))
    total += (0.10 * float(input("How many dimes?")))
    total += (0.05 * float(input("How many nickles?")))
    total += (0.01 * float(input("How many pennies?")))
    return total


def resource_match(drink):
    global order_continue
    for i in resources:
        if MENU[drink]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            order_continue = False
        else:
            resources[i] -= MENU[drink]["ingredients"][i]


order_continue = True

while order_continue:
    order = input("What would you like? (espresso/latte/cappuccino)")

    if order == 'report':
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        resource_match(drink=order)
        if order_continue == False:
            print("Please come back later. Good bye!")
            break
        cost = MENU[order]["cost"]
        paid = coins()
        if paid < cost:
            print("Sorry that's not enough money. Money refunded.")
        elif paid >= cost:
            change = round(paid - cost, 2)
            profit += cost
            print(f"Here is ${change} in change.\nHere is your {order}☕. Enjoy!")
    elif order == 'off':
        print("Turning off. Good bye!")
        break
    else:
        print("Wrong order. Good bye!")
        break

    if input("Would you like another drink? Type 'y' for yes, 'n' for no.") == 'n':
        print("Have a good day!😄")
        order_continue = False


        ----------------------------------------------------------------------
        menu.py
        
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
}



