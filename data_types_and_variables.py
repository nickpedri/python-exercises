print("99.9 is: " + str(type(99.9)))
print("'False' is: " + str(type('False')))
print("False is: " + str(type(False)))
print("'0' is: " + str(type('0')))
print("0 is: " + str(type(0)))
print("True is: " + str(type(True)))
print("'True' is: " + str(type('True')))
print("[{}] is: " + str(type([{}])))
print("{'a':[]} is: " + str(type({'a':[]})))

'''
2. What data type would best represent the following?

A. A term or phrase typed into a search box
STRING

B. Whether or not a user is logged in
BOOLEAN

C. A discount amount to apply to a user's shopping cart
FLOAT/INT

D. Whether or not a coupon code is valid
BOOLEAN

E. An email address typed into a registration form
STRING

F. The price of a product
STRING

G. The email addresses collected from a registration form
LIST

H. Information about applicants to Codeup's data science program
DICTIONARY

'''
# 3. For each of the following code blocks:
#
# Read the expression and predict the evaluated results
#
# Execute the expression in a Python REPL.
#nickolaspedrimiranda@Nickolass-Air python-exercises % PYTHON
'''
Python 3.10.9 (main, Mar  1 2023, 12:20:14) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> '1' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> '1' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 6 % 4
2
>>> type(6 % 4)
<class 'int'>
>>> type(type(6 % 4))
<class 'type'>
>>> '3 + 4 is ' + 3 + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 0 < 0
False
>>> 'False' == False
False
>>> True == 'True'
False
>>> 5 >= -5
True
>>> True or "42"
True
>>> 6 % 5
1
>>> 5 < 4 and 1 == 1
False
>>> 'codeup' == 'codeup' and 'codeup' == 'Codeup'
False
>>> 4 >= 0 and 1 !== '1'
  File "<stdin>", line 1
    4 >= 0 and 1 !== '1'
                   ^
SyntaxError: invalid syntax
>>> 6 % 3 == 0
True
>>> 5 % 2 != 0
True
>>> [1] + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> [1] + [2]
[1, 2]
>>> [1] * 2
[1, 1]
>>> [1] * [2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>> [] + [] == []
True
>>> {} + {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> 
'''


# 4. Describe the following scenarios. You will need to create and assign variables and use operators.

#5. You have rented some movies for your kids:

#The Little Mermaid for 3 days
#Brother Bear for 5 days
#Hercules for 1 day
#If the daily fee to rent a movie is 3 dollars, how much will you have to pay?
X = 3
Y = 5
Z = 1
fee = 3
TOTAL = (X+Y+Z) * fee

print("The total cost of renting the movies was: $" + str(TOTAL))

'''
6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

They pay you the following hourly rates:

Google: 400 dollars
Amazon: 380 dollars
Facebook: 350 dollars
This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

How much will you receive in payment for this week?
'''

G = 400
A = 380
F = 350

payment = (10*F)+(6*G)+(4*A)

print("I will recieve $"+str(payment)+" this week!")

#7. A student can be enrolled to a class only if the class is not
# full and the class schedule does not conflict with her current schedule.

student = "Nick"
class_full = False
free_time = True

if(class_full == False and free_time == True):
    print(student + " can enroll!")
else:
    print(student + " cannot enroll!")


#8. A product offer can be applied only if people buys more than 2 items, and the offer
# has not expired. Premium members do not need to buy a specific amount of products.

item_quantity = 3
offer_expired = False
premium_member = False

if((item_quantity > 2 or premium_member == True) and offer_expired == False):
    print("Product offer can be applied!")
else:
    print("Product offer cannot be applied!")

#9. Continue working in the data_types_and_variables.py file. Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

#Create a variable that holds a boolean value for each of the following conditions:

#The password must be at least 5 characters
check = len(password) >= 5
print(check)

#The username must be no more than 20 characters
user_check = len(password) <= 20
print(user_check)


#The password must not be the same as the username
pass_user = username != password
print(pass_user)

#Bonus Neither the username or password can start or end with whitespace
bonus = password[0] != ' ' and password[-1] != ' ' and\
        username[0] != ' ' and username[-1] != ' '

print(bonus)

better_bonus_pass = password == password.strip()
better_bonus_user = username == username.strip()

print(better_bonus_pass)
print(better_bonus_user)