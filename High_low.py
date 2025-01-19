import random
from art_high_low import logo,vs
data = {
    "Instagram": 685,
    "Cristiano Ronaldo": 648,
    "Lionel Messi": 505,
    "Selena Gomez": 423,
    "Kylie Jenner": 395,
    "Dwayne Johnson": 394,
    "Ariana Grande": 376,
    "Kim Kardashian": 359,
    "Beyoncé": 313,
    "Khloé Kardashian": 305,
    "Nike": 302,
    "Justin Bieber": 295,
    "Kendall Jenner": 290,
    "Taylor Swift": 283,
    "National Geographic": 280,
    "Virat Kohli": 270,
    "Jennifer Lopez": 249,
    "Nicki Minaj": 227,
    "Neymar": 227,
    "Kourtney Kardashian": 220,
    "Miley Cyrus": 213,
    "Katy Perry": 205,
    "Zendaya": 180,
    "Kevin Hart": 177,
    "Real Madrid CF": 170,
    "Cardi B": 164,
    "LeBron James": 159,
    "Demi Lovato": 154,
    "Rihanna": 150,
    "Chris Brown": 144,
    "Drake": 143,
    "Ellen DeGeneres": 137,
    "FC Barcelona": 133,
    "Kylian Mbappé": 122,
    "Billie Eilish": 121,
    "UEFA Champions League": 118,
    "Gal Gadot": 108,
    "Lisa": 105,
    "Vin Diesel": 103,
    "NASA": 97,
    "Shraddha Kapoor": 94,
    "Priyanka Chopra": 93,
    "Narendra Modi": 92,
    "Shakira": 91,
    "NBA": 89,
    "Snoop Dogg": 89,
    "David Beckham": 88,
    "Dua Lipa": 87,
    "Alia Bhatt": 86,
    "Jennie": 86,
    "Gareth Bale": 85,
    "Emma Watson": 84
}

def compare(choice_one,choice_two):
    if data[choice_one]>data[choice_two]:
        return choice_one
    else:
        return choice_two
def checker(choice_1,choice_2):
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input =='a':
        user_input = choice_1
        return_from_compare = compare(user_input,choice_2)
        if return_from_compare==user_input:
            return True
        else:
            return False
    else:
        user_input = choice_2
        return_from_compare = compare(choice_1,user_input)
        if return_from_compare==user_input:
            return True
        else:
            return False
score = 0
random_choice_2 =  random.choice(list(data.keys()))
print(logo)
game_over = True
while game_over:
    random_choice_1 = random_choice_2
    random_choice_2 =  random.choice(list(data.keys()))
    if random_choice_1 == random_choice_2:
        random_choice_2 =  random.choice(list(data.keys()))

    print(f"Compare A: {random_choice_1}.")
    print(vs)
    print(f"Against B: {random_choice_2}.")
    if checker(random_choice_1,random_choice_2) == False:
        game_over = False
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score = score + 1
        print(f"You're right! Current score: {score}.")
        print(logo)
