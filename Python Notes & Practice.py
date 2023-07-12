# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax.
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce
# output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.

fruits_with_more_than_two_vowels = []
vowels = ["a", "e", "i", "o", "u"]

for fruit in fruits:
    count = 0
    for letter in fruit:
        if letter in vowels:
            count += 1
    if count > 2:
            fruits_with_more_than_two_vowels.append(fruit)
            continue


print(fruits_with_more_than_two_vowels)

fruits_with_only_two_vowels = []
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
for fruit in fruits:
    count = 0
    for letter in fruit:
        if letter in vowels:
            count += 1
    if count == 2:
            fruits_with_only_two_vowels.append(fruit)
            continue

print(fruits_with_only_two_vowels)


# Exercise 5 - make a list that contains each fruit with more than 5 characters


five_character_fruit_or_more = [f for f in fruits if len(f) > 5]
print(five_character_fruit_or_more)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruit_is_five = [f for f in fruits if len(f) == 5]
print(fruit_is_five)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
less_than_five = [f for f in fruits if len(f) < 5]
print(less_than_five)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruit_count = []
for fruit in fruits:
    count = 0
    for letter in fruit:
        count += 1
    fruit_count.append(count)

print(fruit_count)


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = []

for fruit in fruits:
    if 'a' in fruit:
        fruits_with_letter_a.append(fruit)

gg = [fruit for fruit in fruits if 'a' in fruit]

print(fruits_with_letter_a)
print(gg)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

even_numbers = [n for n in numbers if n%2 ==0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [n for n in numbers if n%2 !=0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [n for n in numbers if n < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_numeral_or_more = [n for n in numbers if (abs(n) >= 10)]
print(two_numeral_or_more)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each
# element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n**2 for n in numbers]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 != 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
numbers_plus_5 = [n + 5 for n in numbers]
print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list.
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]
#
# How many students are there?
student_count = 0
for s in students:
    student_count += 1
print(str(student_count) + ' students.')

# How many students prefer light coffee? For each type of coffee roast?
light_coffee = 0
dark_coffee = 0
medium_coffee = 0

for student in students:
    if student.get('coffee_preference') == 'light':
        light_coffee += 1
    if student.get('coffee_preference') == 'dark':
        dark_coffee += 1
    if student.get('coffee_preference') == 'medium':
        medium_coffee += 1

print('Light: ' + str(light_coffee))
print('Medium: ' + str(medium_coffee))
print('Dark: ' + str(dark_coffee))

# How many types of each pet are there?
pets = []
for student in students:
    for pet in student.get('pets'):
        if pet.get('species') not in pets:
            pets.append(pet.get('species'))

print(pets)

# How many grades does each student have? Do they all have the same number of grades?
#Each student has 4 grades. They have different grades.

# What is each student's grade average?
for student in students:
    average = (sum(student.get('grades')))/len(student.get('grades'))
    print(student.get('student') + ' ' + str(average))

# How many pets does each student have?

for student in students:
    print(student.get('student') + ' ' + str(len(student.get('pets'))) + ' pet(s)!')

# How many students are in web development? data science?
wed_dev_count = 0
for student in students:
    if student.get('course') == 'web development':
        wed_dev_count += 1

print(wed_dev_count)

# What is the average number of pets for students in web development?
pet_count = 0
for student in students:
    pet_count += len(student['pets'])

print(pet_count)

# What is the average pet age for students in data science?
# What is most frequent coffee preference for data science students?
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?
# What is the average name length?
# What is the highest pet age for light coffee drinkers?



############ FUNCTIONS

def sayhello(name='World', greeting='Hello'):
    return '{}, {}!'.format(greeting, name)

print(sayhello('Codeup', greeting='Salutations')) # Okay


#################################################################################################
print('#################################################################################################')
#################################################################################################

import function_exercises as fe
from function_exercises import is_consonant as cons

print(cons('b'))