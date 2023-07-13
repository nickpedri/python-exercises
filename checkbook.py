'''
When run, the application should welcome the user, and prompt them for an action to take:

 -view current balance
 -add a debit (withdrawal)
 -add a credit (deposit)
 -exit

The application should notify the user if the input is invalid and prompt for another choice.

The application should persist between times that it is run.

Example, if you run the application, add some credits, exit the application and run it again, you should still see the
balance that you previously created. In order to do this, your application will need to store its data in a text file.
Consider creating a file where each line in the file represents a single transaction.
Utilize functions to call the balance, debit, credit, and exit
'''

# Create function that presents the user with 4 choices.
def choices():
    print(f'What would you like to do, {name}?')
    print()
    print('1) View current balance')
    print('2) Record a debit (withdraw)')
    print('3) Record a credit (deposit)')
    print('4) Exit')
    print()

# Created function to check for a valid user input.
def check_option():
    while True: # Creates infinite loop that is broken with proper user input
        x = input('Enter number: ')  # Accepts use input for choice of what to do.
        if (x.isdigit() is False) or (x not in ['1', '2', '3', '4']): # Checks that user input is a number and asks for valid number if it isn't.
            print('Please enter a valid number.')
        else:
            return x        # Breaks loop when user inputs proper choice.

# Created function that can open and compile list of integers from checkbook file.
def read_cb():
    cd_r = open('Checkbook_Data.txt', 'r') # Creates variable containing checkbook info
    transactions = cd_r.read().split(',') # Converts data into list of strings
    new = list(map(int, transactions)) # assigns list of data to variable and converts to integer
    return new # Returns list of integers with all withdraws and deposits.

# Created function that will insert a new entry into the checkbook subtracting money.
def withdraw():
    while True:
        x = input('How much would you like to withdraw? ')
        if x.isdigit() is False:
            print('Please enter a valid number!')
            continue
        if int(x) > balance:
            print('You do not have sufficient funds to withdraw this amount!')
            continue
        break
    cd_a = open('Checkbook_Data.txt','a')
    cd_a.write(f',-{x}')
    cd_a.close()
    print(f'${x} withdrawn from account!')

# Created function that will insert a new entry into the checkbook depositing money.
def deposit():
    while True:
        x = input('How much would you like to deposit? ')
        if x.isdigit() is False:
            print('Please enter a valid number!')
            continue
        break
    cd_a = open('Checkbook_Data.txt','a')
    cd_a.write(f',{x}')
    cd_a.close()
    print(f'${x} deposited into the account!')

##################################################################

print('Welcome to the terminal checkbook!')

name = 'Nick'
# name = (input('What is your name? ')).capitalize() # Gives user a name variable

while True:
    balance = sum(read_cb())
    choices()
    to_do = check_option()
    if to_do == '1':
        print(f'Current account balance is ${balance}.')
    elif to_do == '2':
        withdraw()
    elif to_do == '3':
        deposit()
    elif to_do == '4':
        print(f'Have a beautiful day, {name}!')
        break

