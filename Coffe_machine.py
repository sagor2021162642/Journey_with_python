
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
        return True
def process_coin():
    print('Please insert Coin')
    total = int(input('How many quarters: '))*0.25
    total += int(input('How many dimes: '))*0.1
    total += int(input('How many nickles: '))*0.05
    total += int(input('How many pennies: '))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    global profit
    if money_received >=drink_cost:
        change = round(money_received - drink_cost,2)
        print(f'Here is your change: {change}')
        profit +=drink_cost
        return True
    else:
        print('Sorry that\'s not enough money. Money Refunded')
        return False
def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f'Here is your {drink_name}')
game_on = True
while game_on:
    user_input  = input('What would you like? (espresso/latte/cappuccino):')
    if user_input == 'off':
        game_on = False
    elif user_input == 'report':
        print(f'Water: {resources['water']}')
        print(f'Milk: {resources['milk']}')
        print(f'Coffee: {resources['coffee']}')
        print(f'Money: {profit}')
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffe(user_input, drink['ingredients'])