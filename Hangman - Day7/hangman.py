import random 
from hangman_words import word_list
from hangman_art import stages, logo


#List of words
lives = 6

print(logo)
#Randomly pick a word
chosen_word = random.choice(word_list)
print(chosen_word)
# place holder with same number of blanks as words

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

# print(chosen_word)
while not game_over:
    print(f"*********************** You  have {lives}/ 6 left")
    guess = input("Guess a letter:").lower()
    # print(guess)
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""

    #Check if letter exist in the random word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter    
        else:
            display += "_"
    print(display) 

    if guess not in chosen_word:
         print(f"You guessed {guess}, thats not in the word. You lose a life")
         lives -=1
         if lives == 0:
            game_over =True
            print(f"+++++++++++++++++++ It was {chosen_word} You Lose!!!!!+++++++++++++++++++")

    if "_" not in display:
        game_over = True
        print("You win.")   
    print(stages[lives])        