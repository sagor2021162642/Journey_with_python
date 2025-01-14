rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0,2)
if user_choice == 0:
    print(rock)
    if computer_choice == 0:
        print(f'Computer chose:\n{rock}\nIt\'s a draw')
    elif computer_choice == 1:
        print(f'Computer chose:\n{paper}\nYou lose')
    else:
        print(f'Computer chose:\n{scissors}\nYou win')
elif user_choice == 1:
    print(paper)
    if computer_choice == 0:
        print(f'Computer chose:\n{rock}\nYou win')
    elif computer_choice == 1:
        print(f'Computer chose:\n{paper}\nIt\'s a draw')
    else:
        print(f'Computer chose:\n{scissors}\nYou lose')
else:
    print(scissors)
    if computer_choice == 0:
        print(f'Computer chose:\n{rock}\nYou lose')
    elif computer_choice == 1:
        print(f'Computer chose:\n{paper}\nYou win')
    else:
        print(f'Computer chose:\n{scissors}\nIt\'s a draw')