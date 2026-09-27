# declare
name = "Ritji"
age = 15
height = 150
is_student = False

# checking types

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

num1 = 25
num2 = 12

# operations
add = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2

print(add)
print(sub)
print(div)
print(mul)

#length check
print(len(name))
print(name.upper())
print(name.title())

if "Ritji" in name:
    print("found")


#finding

# printing by index
greet = "Hello World"
print(greet[0])
print(greet[-1])
print(greet[2:6])
print(greet[::2])

#replacing  and finding

text = "Hello i love python"
words = text.split()
print(words)
new_text = text.replace("python", "coding")
print(new_text)
index = text.find("love")
print(index)


#inputs
# user_name = input("What is your name?")
# user_age = int(input("What is your age?"))

# print(f"Users name is {user_name} and user is {user_age} years. User will be {user_age + 10} in ten years")

fruits = ['banana', 'apple', 'grapes', 'pear','mango']
print(fruits[::2])
print(len(fruits))
fruits.append("lemon")
print(fruits)
fruits.remove("apple")
print(fruits)

for fruit in fruits:
    print(fruit)
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}: {fruit}")

#conditionals
con_age =66

if con_age < 13:
    print("Too Young")
elif con_age >= 13 and con_age <18:
    print("Teenager")
elif con_age >= 18 and con_age <65:
    print("Adult")
else:
    print("Senior")        

num_check = 6

if num_check > 0 and num_check <101:
    if num_check % 2 == 0:
        print("Even")
    else:
        print("Odd")    
else:
    print("Not in range")    

if num_check > 0 and num_check <10 and num_check % 2 == 0 :
    print("Used And and is even")   
else:
    print("Not Okay")    


for number in range(1, 10):
    print(number)    