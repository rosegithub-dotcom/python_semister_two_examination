def employeeBonusCalculations():

    run = 1

    while run == 1:

        salary =  int(input("Enter your salary amount: "))
        yearsOfService =  int(input("Enter your years of service: "))

        if yearsOfService > 4:

            netBonusAmount = int((8/100 * salary))
            
        elif yearsOfService == 3:

            netBonusAmount = int((5/100 * salary))
        else:

            netBonusAmount = 0

        finalPay = salary + netBonusAmount     

        print(f"Your net bonus amount is: {netBonusAmount:,} and your final pay is {finalPay:,}")    

        run = int(input("Press 1 to continue or any number to quit: "))

        if run !=1:
            break


employeeBonusCalculations()