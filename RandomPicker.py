import random

name_string = input("Give Everybody's Name: ")

names = name_string.split(', ')
print(f'All Persons {names}')
how_many_person = len(names)

person = random.randint(0,(how_many_person-1))

#person_who_will_pay = random.choice(names)

print(f'Print Person Name: {names[person]}')