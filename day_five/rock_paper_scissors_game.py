import random as rd
lives = 0

while lives <4:
    computer_choice = rd.choice(["rock", "paper", "scissors"])
    user_choice = input("Pick between rock, paper and scissors").lower()

    draw_condition =(computer_choice ==user_choice)

    if (computer_choice == "rock" and user_choice == "paper" 
    or computer_choice == "scissors" and user_choice == "rock"
    or computer_choice == "paper" and user_choice == "scissors"):
        print("You won")
    elif computer_choice == user_choice:
        print("Its a draw")
    else:
        print("you lost")    
    print(computer_choice)   
    print(f"You have used ", lives )
    choice = input("Do you wish to continue playing? (Yes/No): ").lower()
    if choice == "yes":
            lives = lives + 1
            continue
    else:
        warning = input("Are you sure you want to quit!!!!: ").lower()
        
        if warning == "yes":
                break
        else:
                continue
print("Thank you for playing!")