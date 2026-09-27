from random import randint
from art import logo

SIMPLE_DIFFICULTY = 10
ADVANCED_DIFFICULTY = 5

def check_answer(user_guess, correct_answer, remaining_turns):
    if user_guess < correct_answer:
        print("Too low.")
        return remaining_turns - 1
    elif user_guess > correct_answer:
        print("Too high.")
        return remaining_turns - 1
    else:
        print(f"You got it! The answer was {correct_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return SIMPLE_DIFFICULTY
    elif level == "hard":
        return ADVANCED_DIFFICULTY
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        return set_difficulty()        

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    correct_number = randint(1, 100)        
    print(f"The correct answer is {correct_number}")
    
    remaining_turns = set_difficulty()
    current_guess = 0
    
    while current_guess != correct_number:
        print(f"You have {remaining_turns} attempts remaining to guess the number.")
        current_guess = int(input("Make a guess: "))
        remaining_turns = check_answer(current_guess, correct_number, remaining_turns)
        
        if remaining_turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif current_guess != correct_number:
            print("Guess again.")

play_game()

