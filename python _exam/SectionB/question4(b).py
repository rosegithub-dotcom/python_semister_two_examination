def saccoTransactions():

    accountBalance = 0
    run = 1

    while run == 1:

        print("\nWelcome to, WITU Sacco.")

        #menu
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')


        studentChoice = int(input("Enter your selection(1,2,or 3): "))

        #performing the transactions basing on the student choice
        
        if studentChoice == 1:

            print('\n...Processing a deposit transaction...')
            depositAmount =  int(input("Enter amount to be deposited: "))

            #check if deposit amount is less than 1000
            if depositAmount < 1000:

                print('\nMinimum deposit is 1000')

            else:
                accountBalance += depositAmount

                print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')


        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount =  int(input("Enter amount to be withdrawn: "))

            if accountBalance == 0:

                print("Your balance is 0") 

            elif withdrawAmount < 500:

                print("Mininum withdraw amount is 500")

            elif withdrawAmount > accountBalance:

                print(f"Withdraw failed, insufficient funds")

            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')

            
        elif studentChoice == 3:
             print(f'Your account balance is {accountBalance:,}')

            

        else:
            print("You entered  a wrong choice!! Please select 1, 2, or 3\n")


        run = int(input("Enter 1 to continue or any number to exit: "))

        if run!=1:
            print("Thanks for using our sacco")
            break

saccoTransactions()

