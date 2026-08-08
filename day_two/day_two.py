#Subscripting
print("hello" [0])

#String
print("123" + "345")

#Integer = Whole number
print( 123 + 345)

#Large integers
print( 123456789)

#Float
print(3.1423)

#Boolean
print(True)
print(False)

#type
print(type(12345))


#Mathematical operators
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(6 // 3)

#PEMDAS

# ()
# **
# * OR /
# + -

print(3/3 + 3/3 - 3)

#BMI

height = 1.65
weight = 84

bmi = weight/ height ** 2

print(bmi)

print(int(bmi))
print(round(bmi))
print(round(bmi, 2))


#Number Manipulation and F strings

#score
score = 0

#user scores a point

score += 1
print(score)

#f-strings
# print("Your score is" + str(score))
is_winning = True 

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
