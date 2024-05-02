def wituSacco():
    accountBalance = 0
    run = 1
    while run == 1:
        print("Welcome to WITU Sacco")
        
        #menu
        print('1.Deposit Money')
        print('2.Withdraw Money')
        print('3.Check Deposit')
        
        studentChoice = int(input("Enter choice 1, 2, or 3: "))
        
        if studentChoice == 1:
            print('\n... Processing a deposit transaction...')
            depositAmount = int(input("Enter deposit amount: "))
            
            if depositAmount < 1000:
                print("\nMinimum deposit is 1000")
            else:
                accountBalance += depositAmount
                print(f"Dear student, you have deposited {depositAmount} and your new balance is {accountBalance}")

        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount = int(input("Enter withdraw amount: "))
            if accountBalance == 0:
                print('Your account balance is 0')
            elif withdrawAmount < 500:
                print("Minimum withdraw amount is 500")
            elif withdrawAmount > accountBalance:
                print('Withdraw failed, insufficient funds')
            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount}') 

        elif studentChoice == 3:
            print('\n...Processing a check deposit transaction...')
            print(f'Your account balance is {accountBalance}')    

        else:
            print("You entered a wrong choice! Please select 1, 2, or 3")
            
        run = int(input("Enter 1 to continue or any number to exit: "))

    print("Thanks for using WITU Sacco")

wituSacco()

