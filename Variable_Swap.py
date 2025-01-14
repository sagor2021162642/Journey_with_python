#Step Number 1
variable_1 = input('Input Variable One: ')
variable_2 = input('Input Variable Two: ')
extra_variable = None
print(variable_1+' '+variable_2)
#Step Number 2
extra_variable = variable_1
variable_1 = variable_2
variable_2 = extra_variable
print(variable_1+' '+variable_2)