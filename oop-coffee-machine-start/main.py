from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()
order_continue = True

while order_continue:
    order = input(f"What would you like? Type {menu.get_items()}: ")

    if order == 'report':
        coffeemaker.report()
        money_machine.report()
    elif order in menu.get_items():
        order_item = menu.find_drink(order)
        cost = order_item.cost
        if coffeemaker.is_resource_sufficient(order_item):
            if money_machine.make_payment(cost):
                coffeemaker.make_coffee(order_item)
    elif order == 'off':
        order_continue = False