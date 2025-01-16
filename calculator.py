from calculator_logo import logo
def add(number_1,number_2):
    result = number_1 + number_2
    return result
def mul(number_1,number_2):
    result = number_1 * number_2
    return result
def sub(number_1,number_2):
    result = number_1 - number_2
    return result
def div(number_1,number_2):
    result = number_1 / number_2
    return result
def calculator_function():
    print(logo)
    num_1 = float(input('Enter First Number: '))
    operation ={'+':add,'-':sub,'*':mul,'/':div}
    for symbol in operation:
        print(symbol)
    infinity_loop = True
    while infinity_loop:
        operration_symbol = input('Enter operation: ')
        num_2 = float(input('Enter Second Number: '))
        calculation_function = operation[operration_symbol]
        answer = calculation_function(num_1,num_2)
        print(answer)
        if input('Want to continue with answer? yes or no: ') == 'no':
            infinity_loop = False
            calculator_function()
        else:
            num_1 = answer
calculator_function()