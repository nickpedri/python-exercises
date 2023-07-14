import json
import datetime as dt

c = json.load(open('Checkbook.json'))  # Created object that can reference the dictionary
ct = dt.datetime.now().isoformat(' ', 'seconds')  # Created variable that equals current timestamp down to the seconds


def choices():
    print()
    print(f'What would you like to do, {name}?')
    print()
    print('1) View current balance')
    print('2) Record a debit (withdraw)')
    print('3) Record a credit (deposit)')
    print('4) Show transaction history')
    print('5) Show categories')
    print('6) Search transactions')
    print('7) Exit')
    print()


def check_option():
    while True:  # Creates infinite loop that is broken with proper user input
        x = input('Enter number: ')  # Accepts use input for choice of what to do.
        if x not in ['1', '2', '3', '4', '5', '6', '7']:  # Checks that user input is a valid number.
            print('Please enter a valid number.')
        else:
            return x        # Breaks loop when user inputs proper choice.


def cb_balance():
    transactions = []
    for t in c:
        transactions.append(t['amount'])
    total = sum(transactions)
    return total


def deposit():
    while True:
        x = input('How much would you like to deposit? ')  # Asks user how much to withdraw
        if (x.replace('.', '').isdigit() is False) or (x.count('.') > 1):  # Checks if the input is a valid input
            print('Please enter a valid number!')
            continue
        x = float(x)
        break  # Breaks loop for input check
    cat = categories()
    description = input('Enter a description for this transaction: ')
    new = {"amount": round(x, 2),
           "category": cat,
           "date_time": ct,
           "description": description}
    c.append(new)
    with open('Checkbook.json', 'w') as f:
        json.dump(c, f, indent=5)
    print(f'${round(x,2):.2f} deposited into the account!')  # Tells user action done


def withdraw():
    while True:
        x = input('How much would you like to withdraw? ')  # Asks user how much to withdraw
        if (x.replace('.', '').isdigit() is False) or (x.count('.') > 1):  # Checks if the input is a valid input
            print('Please enter a valid number!')
            continue
        elif float(x) > cb_balance():  # Alerts user if user tries to withdraw more than they have.
            print('You do not have sufficient funds to withdraw this amount!')
            continue
        x = float(x)
        break  # Breaks loop for input check
    cat = categories()
    description = input('Enter a description for this transaction: ')
    new = {"amount": round(-x, 2),
           "category": cat,
           "date_time": ct,
           "description": description}
    c.append(new)
    with open('Checkbook.json', 'w') as f:
        json.dump(c, f, indent=5)
    print(f'${round(float(x),2):.2f} withdrawn from account!')  # Tells user action done


def categories():
    print('Enter category number')
    print('1. Housing\n2. Transportation\n3. Food\n4. Utilities\n5. Insurance\n'
          '6. Medical\n7. Savings\n8. Entertainment\n9. Misc')
    while True:
        x = input('Choose category: ')
        if x == '1':
            return 'Housing'
        elif x == '2':
            return 'Transportation'
        elif x == '3':
            return 'Food'
        elif x == '4':
            return 'Utilities'
        elif x == '5':
            return 'Insurance'
        elif x == '6':
            return 'Medical'
        elif x == '7':
            return 'Savings'
        elif x == '8':
            return 'Entertainment'
        elif x == '9':
            return 'Misc'
        else:
            print('Please enter a valid category number')


def history():
    i = 0
    for t in c:
        print(f'{i+1}.) {t}')
        i += 1

def edit():
    while True:
        x = input('Would you like to modify a past transaction? Y/N ').lower()
        if x == 'y':
            history()
            y = input('Which transaction would you like to modify? ')
            pass
        if x == 'n':
            break
        else:
            print('Please enter Y or N.')

def cats():
    x = categories()
    for t in c:
        if t['category'] == x:
            print(t)


def search():
    x = input('What would you like to search for?').lower()
    r = 0
    for t in c:
        if t['description'].count(x) > 0:
            print(t)
            r += 1
    if r == 0:
        print('No results found.')
    else:
        print(f'{r} result(s) found.')

#######################################################################################################################


print('Welcome to the terminal checkbook!')

name = 'Nick'  # name = (input('What is your name? ')).capitalize() # Gives user a name variable


while True:
    choices()
    to_do = check_option()
    if to_do == '1':
        print(f'Current account balance is ${cb_balance():.2f}')
    elif to_do == '2':
        withdraw()
    elif to_do == '3':
        deposit()
    elif to_do == '4':
        history()
        pass
    elif to_do == '5':
        cats()
    elif to_do == '6':
        search()
    elif to_do == '7':
        print(f'Have a beautiful day, {name}!')
        break
