"""
Python Practice Exercises: Basics to Dictionaries
Complete these exercises to refresh your Python fundamentals
"""

# ============================================
# 1. BASIC VARIABLES & DATA TYPES
# ============================================

# Exercise 1.1: Create variables with different data types
# TODO: Create a string, integer, float, and boolean variable
# name = ...
# age = ...
# height = ...
# is_student = ...

# Exercise 1.2: Print and use type()
# TODO: Print the type of each variable above using type()

# Exercise 1.3: Simple arithmetic
# TODO: Create two numbers and perform +, -, *, /, //, % operations
# num1 = ...
# num2 = ...

# ============================================
# 2. STRINGS
# ============================================

# Exercise 2.1: String operations
# TODO: Create a string and:
# - Print its length
# - Convert to uppercase and lowercase
# - Check if it contains a specific word

# Exercise 2.2: String indexing and slicing
# TODO: Create a string like "Hello World"
# - Print the first character
# - Print the last character
# - Print characters from index 2 to 5
# - Print every other character

# Exercise 2.3: String methods
# TODO: Use these string methods:
# - .split() to split a sentence into words
# - .replace() to replace words
# - .find() to find a substring

# ============================================
# 3. INPUT & OUTPUT
# ============================================

# Exercise 3.1: Get user input
# TODO: Ask user for their name and age, then print a greeting
# Use: input() function

# Exercise 3.2: Convert input types
# TODO: Get a number from user as input (remember it's a string)
# Convert it to int or float and perform arithmetic

# ============================================
# 4. LISTS
# ============================================

# Exercise 4.1: Create and access lists
# TODO: Create a list of 5 fruits
# - Print the first, last, and middle element
# - Print the length of the list

# Exercise 4.2: List methods
# TODO: Create a list and practice:
# - .append() - add an element
# - .remove() - remove an element
# - .pop() - remove last element
# - .insert() - insert at specific position
# - .sort() - sort the list
# - .reverse() - reverse the list

# Exercise 4.3: List slicing
# TODO: Create a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# - Get elements from index 2 to 5
# - Get the first 3 elements
# - Get the last 4 elements
# - Get every other element

# Exercise 4.4: Looping through lists
# TODO: Create a list of numbers and:
# - Print each element with a for loop
# - Print each element with index using enumerate()

# ============================================
# 5. CONDITIONALS
# ============================================

# Exercise 5.1: Simple if/elif/else
# TODO: Get a number from user and check if it's positive, negative, or zero

# Exercise 5.2: Multiple conditions
# TODO: Get age from user and check:
# - If age < 13: "Too young"
# - If 13 <= age < 18: "Teenager"
# - If 18 <= age < 65: "Adult"
# - Else: "Senior"

# Exercise 5.3: Nested conditions
# TODO: Check if a number is between 1-100 AND even

# Exercise 5.4: Boolean logic
# TODO: Create conditions using 'and', 'or', 'not'
# Example: if x > 0 and x < 10 and x % 2 == 0:

# ============================================
# 6. LOOPS
# ============================================

# Exercise 6.1: For loop basics
# TODO: Print numbers 1 to 10 using a for loop

# Exercise 6.2: Range function
# TODO: Use range() to print:
# - Numbers 1 to 10
# - Numbers 0 to 9
# - Numbers 1 to 20 with step 2 (odd numbers)
# - Numbers 10 down to 1

# Exercise 6.3: While loop
# TODO: Create a while loop that counts down from 10 to 1

# Exercise 6.4: Loop with break and continue
# TODO: Print numbers 1 to 10, but:
# - Skip number 5 (use continue)
# - Stop at number 7 (use break)

# Exercise 6.5: Nested loops
# TODO: Create a 3x3 multiplication table using nested loops

# ============================================
# 7. FUNCTIONS
# ============================================

# Exercise 7.1: Simple function
# TODO: Create a function that greets a person by name
# def greet(name):
#     ...

# Exercise 7.2: Function with return value
# TODO: Create a function that adds two numbers and returns the result
# def add(a, b):
#     ...

# Exercise 7.3: Function with default parameters
# TODO: Create a function that greets someone
# If no name provided, use "Friend"
# def welcome(name="Friend"):
#     ...

# Exercise 7.4: Function with multiple return values
# TODO: Create a function that returns both sum and product of two numbers
# def calculate(a, b):
#     ...
#     return sum, product

# Exercise 7.5: Function with *args (variable arguments)
# TODO: Create a function that adds any number of arguments
# def sum_all(*numbers):
#     ...

# Exercise 7.6: Function with **kwargs (keyword arguments)
# TODO: Create a function that prints info about a person
# def print_person(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")

# ============================================
# 8. DICTIONARIES
# ============================================

# Exercise 8.1: Create and access dictionaries
# TODO: Create a dictionary with student info (name, age, grade)
# - Print specific values using keys
# student = {"name": "John", ...}
# print(student["name"])

# Exercise 8.2: Dictionary methods
# TODO: Create a dictionary and practice:
# - .keys() - get all keys
# - .values() - get all values
# - .items() - get key-value pairs
# - .get() - safely get a value

# Exercise 8.3: Add and update dictionary items
# TODO: Create an empty dictionary and:
# - Add new key-value pairs
# - Update existing values
# - Delete items using del or .pop()

# Exercise 8.4: Loop through dictionary
# TODO: Create a dictionary and:
# - Print all key-value pairs
# - Print only keys
# - Print only values

# Exercise 8.5: Nested dictionaries
# TODO: Create a dictionary of students, each with grades:
# students = {
#     "John": {"math": 85, "english": 90},
#     "Jane": {"math": 92, "english": 88}
# }
# Access John's math grade

# Exercise 8.6: Dictionary in a list
# TODO: Create a list of dictionaries representing people
# people = [
#     {"name": "John", "age": 25},
#     {"name": "Jane", "age": 23}
# ]
# Loop through and print each person's info

# Exercise 8.7: Counting with dictionaries
# TODO: Create a list of words: ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Use a dictionary to count occurrences of each word

# ============================================
# CHALLENGE EXERCISES
# ============================================

# Challenge 1: Temperature converter function
# TODO: Create a function that converts Celsius to Fahrenheit
# Formula: F = (C × 9/5) + 32
# Test with multiple values

# Challenge 2: List operations
# TODO: Create a list of numbers and find:
# - The maximum value
# - The minimum value
# - The sum
# - The average

# Challenge 3: Word frequency counter
# TODO: Get a sentence from user, count frequency of each word
# Create a dictionary with word as key and count as value

# Challenge 4: Grade calculator
# TODO: Create a dictionary with student names as keys and list of grades as values
# Calculate average grade for each student
# Find who has the highest average

# Challenge 5: Inventory system
# TODO: Create a dictionary representing a store inventory:
# inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 8
# }
# Add functions to:
# - Add items
# - Remove items
# - Display inventory
# - Calculate total value (assume each item costs $1)

# ============================================
# BONUS: Mix everything together
# ============================================

# Bonus Challenge: Build a simple contact book
# TODO: Create a program that:
# 1. Stores contacts in a dictionary (name -> phone number)
# 2. Has functions to:
#    - Add a new contact
#    - Remove a contact
#    - Search for a contact
#    - Display all contacts
# 3. Uses a loop to let user choose actions repeatedly
# 4. Continue until user chooses to exit

print("=" * 50)
print("Practice Exercises: Basics to Dictionaries")
print("=" * 50)
print("\nSolve the exercises above to refresh your Python skills!")
print("Start with the basics and work your way up to dictionaries.")
print("\nGood luck! 🚀")
