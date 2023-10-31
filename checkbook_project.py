import os

# Check if the 'balance.txt' file exists
if os.path.exists('balance.txt'):
    # If the file exists, read the initial balance from it
    with open('balance.txt', 'r') as file:
        cur_bal = float(file.read())
else:
    # If the file doesn't exist, start with a balance of 0
    cur_bal = 0

print(' ')

while True:
  
    space = ' '
    print('(1) View current balance')
    print('(2) Make a withdrawal')
    print('(3) Make a deposit')
    print('(4) Exit')
    user_input = (input('Your choice? [1, 2, 3, 4]: '))
    
    if user_input == '4' :      ##EXITS PROGRAM
        print('***EXIT***')
        break
        
    elif user_input == '1':     ##RETURNS CURRENT BALANCE
        
        print(space)
        print(f'Your current balance is {cur_bal:.2f}')
        print(space)
        
    elif user_input == '2':     ##WITHDRAWALS FROM CURRENT BALANCE
        
        print(space)
        try:
            with_amt = float(input('Enter withdrawal amount xx.xx : '))
            cur_bal = cur_bal - float(with_amt)
            print(f'You have withdrawn {with_amt:.2f}. Your new balance is {cur_bal:.2f}')
            print(space)
            
        except ValueError:
            print('Invalid input')

            print(space)
        
    elif user_input == '3':     ##DEPOSITS INTO CURRENT BALANCE
        
        print(space)
        try:
            dep_amt = float(input('Enter deposit amount xx.xx : '))
            cur_bal = cur_bal + float(dep_amt)
            print(f'You have deposited {dep_amt:.2f}. Your new balance is {cur_bal:.2f}')
            print(space)
        
        except ValueError:
            print('Invalid input')

            print(space)
        
    else:                       ##PROMPTS FOR VALID RESPONSE
        
        print(space)
        print('Invalid response. Choose from the following: ')
        print(space)
        
with open('balance.txt', 'w') as file:
    file.write(str(cur_bal))