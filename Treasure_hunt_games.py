print('Welcome to Treasure Island: ')
input_one = input('Input Left or Right: ').lower()

if (input_one == 'left'):
    input_two = input('Swim or Wait: ').lower()
    if(input_two == 'wait'):
        input_three = input('Which Door: Red, Blue, Yellow ').lower()
        if(input_three == 'yellow'):
            print('You Won')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('Game Over')
