# 1. Define a function named is_two. It should accept one input and return True if the passed input is either
# the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == '2' #returns TRUE OR FALSE based on the value of the result of the == operator

print(is_two(2))
print(is_two('2'))
print(is_two('not two'))

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
vowels = ['a','e','i','o','u']
def is_vowel(x):
    return x.lower() in vowels #returns the given TRUE OR FALSE if the vowel is in the provided list.

print(is_vowel('a'))
print(is_vowel('E'))
print(is_vowel('Q'))

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant,
# False otherwise. Use your is_vowel function to accomplish this.

vowels = ['a','e','i','o','u']
def is_consonant(x):
    return not x.lower() in vowels

print(is_consonant('q'))
print(is_consonant('t'))
print(is_consonant('E'))

# 4. Define a function that accepts a string that is a word. The function should capitalize the first
# letter of the word if the word starts with a consonant.
def capitalize_if_consonant(x):
    return x.capitalize() if is_consonant(x[0]) else x

print(capitalize_if_consonant('cheese'))
print(capitalize_if_consonant('america'))
print(capitalize_if_consonant('work'))

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and
# the bill total, and return the amount to tip.
def calculate_tip(tip,bill):
    return bill * tip

print(calculate_tip(.1,100))
print(calculate_tip(.15,200))
print(calculate_tip(.1,5))

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage,
# and return the price after the discount is applied.
def apply_discount(price,discount):
    return price - (price * discount)

print(apply_discount(100,.1))
print(apply_discount(1000,.05))
print(apply_discount(150,.2))

# 7. Define a function named handle_commas. It should accept a string that is a number that contains
# commas in it as input, and return a number as output.
def handle_commas(n):
    return int(n.replace(',',''))

print(handle_commas('1,000'))
print(handle_commas('1,000,000'))
print(handle_commas('1,005,6,2,34,,5,6,60'))
print(type(handle_commas('1,005,6,2,34,,5,6,60')))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade
# associated with that number (A-F).

def get_letter_grade(grade):
    letter_grade = ''
    if grade >= 88:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 67:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'E'
    return letter_grade

print(get_letter_grade(98))
print(get_letter_grade(85))
print(get_letter_grade(75))
print(get_letter_grade(65))
print(get_letter_grade(45))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):
    new_word = x
    for letter in x:
        if letter.lower() in vowels:
            new_word = new_word.replace(letter,'')
    return new_word

print(remove_vowels('TESTeeeeettttBAHASFK'))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores

def normalize_name(x):
    normal_name = ''
    for l in x:
        if l.isalpha() == True or l.isdigit() == True or l.isspace() == True:
            normal_name += l
    return normal_name.strip().lower().replace(' ','_')

print(normalize_name('     XX%%FA jjSG   .fasd&@%^@#$fas    '))

# for example:
    # Name will become name
    # First Name will become first_name
    # % Completed will become completed


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(x):
    result = []
    sum = 0
    for n in x:
        sum += n
        result.append(sum)
    return result

print (cumulative_sum( [1,2,3,4,5,6,7] ))

# Additional Exercise
    # Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

##### Bonus

# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27