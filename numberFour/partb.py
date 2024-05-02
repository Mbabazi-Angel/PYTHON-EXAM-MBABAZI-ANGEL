def wituSacco():
    accountBalance = 0
    while run == 1:
        print("Welcome to WITU Sacco")
        
#menu
print('1.Deposit Money')
print('2.Withdraw Money')
print('3.Check Deposit')

studentChoice = int(input("Enter choice 1,2,3: "))
print('\n... Processing a deposit transaction...')

if studentChoice == 1:
    print('\n...Processing a deposit transaction')
    depositAmount =int(input("Enter deposit amount: "))
    
    if depositAmount<1000:
        print("\n Minimum deposit is 1000")
    else:
        accountBalance =+ depositAmount
        print(f"Dear student, you have deposited {depositAmount} and your new balance is {accountBalance}")

elif studentChoice == 2:
    print('\n..Processing a withdraw transaction...')
    withdrawAmount = int(input("Enter withdraw amount:"))
    if accountBalance == 0:
        print('Your account balance is 0 ')
    elif withdrawAmount < 500:
        print("Minimum withdraw amount is 500")
    elif withdrawAmount > accountBalance:
        print(f'Withdraw failed, inssufficient funds')
    else:
        accountBalance += withdrawAmount
        print(f'Dear student, you have withdrawn {withdrawAmount}') 

elif studentChoice == 3:
    print('\n... Processing a check deposit transaction...')
    if depositAmount<1000:
        print("\n Minimum deposit is 1000")
    else:
        print(f'\n Your account balance is {accountBalance}')    

else:
    print("You entered a wrong choice! please select 1,2 or 3")
    
run = int(input("Enter 1 to continue or any numer to exit"))

if run != 1:
    print("Thanks for using WITU Sacco")

wituSacco()
break