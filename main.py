from art import logo
from random import randint

EASY_TURNS = 10
HARD_TURNS = 5

# Function to set difficulty
def set_difficulty():
    level = input("Choose the type of difficulty 'easy'😀 or select 'hard'😤: ")
    if level == "easy":
        return EASY_TURNS
    elif level == "hard":
        return HARD_TURNS

# Function to check users' guess against actual answer
def check_answer(user_answer,actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_answer> actual_answer:
        print("The guessed answer is  high 😰")
        return turns -1
    elif user_answer < actual_answer:
        print("The guessed answer is low 😰 ")
        return turns -1
    else:
        print(f"You got it🥳! The answer was {actual_answer}")

def game():
    print(logo)
    print("Welcome to the number guess game !")
    print("I'm thinking of a number between 1 to 100")
    # Choosing a random number between 1 and 100.
    answer = randint(a=1, b=100)
    print(f"Psst, the correct answer is {answer}")
    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"you have {turns} lives left. Come on you can do it 🥳 ")
        # Let the user guess a number
        guess = int(input("Make a guess : "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns== 0:
            print("You've run out of Lives😭, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
while True:
    game()
    play_again = input("Do you want to play the game again Type 'y' else Type 'n' if No : ")
    if play_again == 'y':
        play_again= True
    if play_again == 'n':
        print("Thank you for playing the game !!!")
        break


