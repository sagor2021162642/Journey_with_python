#Step 1 
import random
from hangman_art import logo,stages
from hangman_words import word_list

#word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(f"The chosen word id : {chosen_word}")
length_chosen_word = len(chosen_word)

live = 6

print(logo)

empty_list = []
for index in range(0,length_chosen_word):
    #guess = input("Enter Letter: ").lower()
    empty_list.append("_")
        
end_game = True
while end_game:
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#for index in range(0,length_chosen_word):
    guess = input("Enter Letter: ").lower()
    if guess in empty_list:
        print(f"You've already guessed {guess}")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #empty_list = []
    for index in range(0,length_chosen_word):
        #guess = input("Enter Letter: ").lower()
        #empty_list.append("_")
        if guess == chosen_word[index]:
            empty_list[index]=guess
        
    #print(empty_list)
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        live -=1 
        if live == 0:
            print("Gave Over You lose")
            end_game = False
    
    print(f"{' '.join(empty_list)}")
    
    if "_" not in empty_list:
        end_game = False
        print('Game Over you win')
    print(stages[live])

#for letter in chosen_word:
    #if letter == guess:
        #dsh
    #else:
        #print('worng')