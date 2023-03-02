from menu import MENU, resources

resources["money"] = 0

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = resources["money"]

quarters = 0
dimes = 0
nickles = 0
pennies = 0

def coins():
    global quarters
    global dimes
    global nickles
    global pennies
    print("Please insert coins.")
    quarters = 0.25 * float(input("How many quarters?"))
    dimes = 0.10 * float(input("How many dimes?"))
    nickles = 0.05 * float(input("How many nickles?"))
    pennies = 0.01 * float(input("How many pennies?"))

def resource_match(drink):
    global water
    global milk
    global coffee
    global money
    global change
    for ingredient in resources:
        if ingredient not in MENU[drink]["ingredients"]:
            MENU[drink]["ingredients"][ingredient] = 0
    water -= MENU[drink]["ingredients"]["water"]
    milk -= MENU[drink]["ingredients"]["milk"]
    coffee -= MENU[drink]["ingredients"]["coffee"]
    if water < 0:
        print("Sorry, there is not enough water.")
    elif milk < 0:
        print("Sorry, there is not enough milk.")
    elif coffee < 0:
        print("Sorry, there is not enough coffee.")
    else:
        money += cost
        print(f"Here is ${change} in change.\nHere is your {order}☕. Enjoy!")

order_continue = True

while order_continue:
    order = input("What would you like? (espresso/latte/cappuccino)")

    if order == 'report':
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        cost = MENU[order]["cost"]
        coins()
        paid = round(quarters + dimes + nickles + pennies, 2)
        if paid < cost:
            print("Sorry that's not enough money. Money refunded.")
        elif paid >= cost:
            change = paid - cost
            resource_match(drink = order)
    else:
        print("Wrong order. Good bye!")
        order_continue = False

    if input("Would you like another drink? Type 'y' for yes, 'n' for no." ) == 'n':
        print("Have a good day!😄")
        order_continue = False

