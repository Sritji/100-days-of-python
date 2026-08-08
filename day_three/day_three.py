print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
else:
        print("sorry you have to grow taller before you can ride")


#modulo %
# #10 % 3 = 1
# 
#
number_to_check =  int(input("What number do you want to check?"))     
print(number_to_check)   
if number_to_check % 2 == 0:
      print(
            "This is an even Number")
else:
      print("This is an odd number") 





#Nested  if statements and elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
          print("please pay $5.")
    elif age <= 18 and age >12:
          print("please pay $7.")      
    else:  
          print("please pay $12.")    
else:
        print("sorry you have to grow taller before you can ride")


#multiple if statement in succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
          bill = 5
          print("Children ticket cost $5.")
    elif age <= 18 and age >12:
          bill = 7
          print("Youth ticket cost $7.")      
    else:  
          print("Adult ticket cost $12.")
          bill = 12
    wants_photo = input("Do you want to have a photo take? Type y for yes and n for No.")
    if wants_photo == "y":
          #add$3 dollars to bill
          bill +=3

    print(f"Your final bill is ${bill}")      
else: 
        print("sorry you have to grow taller before you can ride")


#Pizza deliveries
print("Welcome to PYthon Pizza Deliviries!")        
size = input("WHat size do you want? S,M or L")
pepporoni = input("DO you want pepporini on your pizza? Y or N:")
extra_cheese = input("DO you want extra cheese on your pizza? Y or N:")

bill = 0
if size == "S":
      bill+= 15
elif size == "M":
      bill+= 20
elif size == "L":
      bill += 24        
else:
      print("You typed the wrong inputs.")

if pepporoni == "Y":
    if size == "S":
      bill+= 2
    else: 
      bill+= 3

if extra_cheese == "Y":
      bill += 1
print(f"Your final bill is {bill}.")            
      

   # Logical Operators
   # and
   # or
   # not     