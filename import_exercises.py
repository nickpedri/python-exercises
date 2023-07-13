
# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
import function_exercises
import function_exercises as fe
from function_exercises import get_letter_grade as grade
print('################### IMPORT EXERCISES #########################')

print('################### QUESTION 1 #########################')

print(function_exercises.handle_commas('1,1,1,1,1,,4,,23,51,2,512,5,123,4'))
print(fe.is_two('2'))
print(grade(75))

# a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

# DONE IN TERMINAL

# b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly.
# Call this function with values you choose and print the result.

# done in other file. here is code:

from function_exercises import calculate_tip as ct

print(ct(200 ,.1))
print(ct(300 ,.15))
print(ct(100 ,.1))

# c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias.
# Test this function in your notebook.

# done in jupyter notebook

# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.

print('################### QUESTION 2 #########################')
# 2. Read about and use the itertools module from the python standard library to help you solve the following problems.
# Note: Many of these functions in this library return an object, to see the results of the function, cast this object as a list.

import itertools as i

    # How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?

print(list(i.product('abc' ,'123', repeat = 1)))
print(len(list(i.product('abc' ,'123', repeat = 1))))

    # How many different combinations are there of 2 letters from "abcd"?
print(list(i.combinations_with_replacement('abcd', 2)))

    # How many different permutations are there of 2 letters from "abcd"?
print(list(i.permutations('abcd', 2)))


print('################### QUESTION 3 #########################')
# 3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).

# Use the load function from the json module to open this file.

import json
import collections
d = json.load(open('profiles.json'))

# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:


# Total number of users
users = len(d)
print(f' {users} users')

# Number of active users
active_user_count = 0
for user in d: active_user_count += 1 if user.get('isActive') == True else 0

print(f'{active_user_count} users are active.')

# Number of inactive users
inactive_user_count = 0
for user in d:
    if user.get('isActive') == False:
        inactive_user_count += 1

print(f'{inactive_user_count} users are inactive.')

# Grand total of balances for all users
balance = 0

for user in d:
    balance += float(user['balance'].replace('$', '').replace(',', ''))

print(f'The added balance of all users is ${balance}.')
# Average balance per user

average = (balance /users)

print(f'The average balance per user is ${average}.')

# User with the lowest balance

low = float(d[0]['balance'].replace('$' ,'').replace(',', ''))
low_user = d[0]['name']
for user in d:
    if float(user['balance'].replace('$' ,'').replace(',', '')) < low:
        low_user = user['name']
        low = float(user['balance'].replace('$' ,'').replace(',', ''))

print(f'The user with  lowest balance is {low_user} with a balance of ${low}.')

# User with the highest balance

high = float(d[0]['balance'].replace('$' ,'').replace(',' ,''))
high_user = d[0]['name']
for user in d:
    if float(user['balance'].replace('$' ,'').replace(',' ,'')) > high:
        high_user = user['name']
        high = float(user['balance'].replace('$' ,'').replace(',' ,''))

print(f'The user with  lowest balance is {high_user} with a balance of ${high}.')


# Most common favorite fruit
fruits = []
for user in d:
    fruits.append(user['favoriteFruit'])

froot = {}

for fruit in fruits:
    if fruit not in froot.keys():
        froot[fruit] = 1
    elif fruit in froot.keys():
        froot[fruit] += 1


print(froot)


print(collections.Counter(fruits))


# Least most common favorite fruit

print(collections.Counter(fruits))


# Total number of unread messages for all users

unread = 0

for user in d:
    msg = ''
    for l in user['greeting']:
        if l.isdigit():
            msg += l
    unread += int(msg)

print(f'There is a total of {unread} messages.')

####### testing max function ########
def findMax(num):
   rem = 0
   while(num):
     rem = num%10
     return rem

# using max(arg1, arg2, *args, key)
num = 11,48,33,17,19
print('Number with max remainder is:', max(num, key=findMax))