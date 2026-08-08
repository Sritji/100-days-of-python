print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left " or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake, there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross\n').lower()
    if choice2 == "wait":
        choice3 = input("YOu arrived at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose\n").lower()
        if choice3 == "red":
            print("Fire. Game over")
        elif choice3 == "yellow":
            print("You found the treasure. You win")
        elif choice3 == "blue":
            print("Empty room. Game over")
        else:     
            print("Door chosen does not exist. Game over")
    else:    
        print("Attacked. Game Over.")
else:    
    print("You fell into a hole. Game Over.")
    