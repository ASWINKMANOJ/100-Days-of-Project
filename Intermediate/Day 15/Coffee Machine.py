MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(order_ingredients):
    """Checks whether the machine have sufficient ingredients or not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def payment_process():
    """Returns the total coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .10
    total += int(input("How many nickles? ")) * .05
    total += int(input("How many pennies? ")) * .01
    return total


def transaction(order_req, money_received):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= order_req["cost"]:
        change = round((money_received - order_req['cost']), 2)
        global profit
        profit += order_req['cost']
        print(f'Here is your ${change} in change.')
        return True
    else:
        print("Insufficient amount. Here is your Refund.")
        return False


def user_order(drink_name, ingredient):
    """Deduct the required ingredients from the resources."""
    for item in ingredient:
        resources[item] = (resources[item]) - (ingredient[item])
    print(f"Here's your {drink_name} ☕️. Enjoy!")


stop = True

while stop:
    order = input("what would you like? (espresso/latte/cappuccino) : ").lower()
    if order == 'no':
        stop = False
    elif order == 'profit':
        print(profit)
    elif order == 'balance':
        print(f'water: {resources["water"]}')
        print(f'milk: {resources["milk"]}')
        print(f'coffee: {resources["coffee"]}')
    else:
        drink = MENU[order]
        order_ingredient = drink["ingredients"]
        if is_resource_sufficient(order_ingredient):
            money = payment_process()
            if transaction(drink, money):
                user_order(order, order_ingredient)
