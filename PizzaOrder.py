small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small = 2
pepperoni_large_and_medium = 3
chesse = 1
pizza_size = input('Input The Pizza Size: ').lower()
pepperoni = input('Do you want pepperoni: ').lower()
extra_chesse = input('Do you want pepperoni: ').lower()
if pizza_size == 'l' or pizza_size == 'L':
    if pepperoni == 'y' or pepperoni == 'Y':
        if extra_chesse == 'y' or extra_chesse =='Y':
            print(f'Total: {large_pizza+pepperoni_large_and_medium+chesse}')
        else:
            print(f'Total: {large_pizza+pepperoni_large_and_medium}')
    else:
        if extra_chesse == 'y' or extra_chesse == 'Y':
            print(f'Total: {large_pizza+chesse}')
        else:
            print(f'Total: {large_pizza}')
elif pizza_size == 'm' or pizza_size == 'M':
    
    if pepperoni == 'y'or pepperoni == 'Y':
        if extra_chesse == 'y'or extra_chesse == 'Y':
            print(f'Total: {medium_pizza+pepperoni_large_and_medium+chesse}')
        else:
            print(f'Total: {medium_pizza+pepperoni_large_and_medium}')
    else:
        if extra_chesse == 'y' or extra_chesse == 'Y':
            print(f'Total: {medium_pizza+chesse}')
        else:
            print(f'Total: {medium_pizza}')
elif pizza_size == 's' or pizza_size == 'S':
    if pepperoni == 'y'or pepperoni == 'Y':
        if extra_chesse == 'y'or extra_chesse == 'Y':
            print(f'Total: {small_pizza+pepperoni_for_small+chesse}')
        else:
            print(f'Total: {small_pizza+pepperoni_for_small}')
    else:
        if extra_chesse == 'y' or extra_chesse == 'Y':
            print(f'Total: {small_pizza+chesse}')
        else:
            print(f'Total: {small_pizza}')
else:
    print(f'Correct Input')