
def applicationLoop():
    while(True):
        userInput = input("Choose the financial program you would like to run: \n"
              "  1) Compound Interest Calculator \n"
              "  2) Variable Input Compound Interest Calculator \n"
              "  3) Press any other key to QUIT\n")

        if(userInput == '1'):
            CompInterest()
        if(userInput == '2'):
            VarCompInterest()
        else:
            break

        choice = input("Would you like to run another program or would you like to quit?\n"
                     "1) Run another program\n"
                     "2) Press any other key to QUIT\n")
        if choice == '1':
            continue
        else:
            break
    print("Thank you. Goodbye.")
    return


def CompInterest(): #basic compund interest calculator
    while(True):
        principal = input("what would you like your principal to be?: ")
        try:
            principal = float(principal)
            break
        except ValueError:
            print("Enter an integer or decimal to continue")
            continue
    while (True):
        years = input("How many years would you like to compound for?: ")
        try:
            years = float(years)
            break
        except ValueError:
            print("Enter an integer to continue")
            continue
    while (True):
        percent = input("What yearly interest rate would you like to see?: ")
        try:
            percent = float(percent)
            break
        except ValueError:
            print("Enter an integer or decimal to continue")
            continue

    money = principal*((percent*0.01)+1.00)**years
    print("Your balance after", int(years), "years will be:", money, "\n")
    return


def VarCompInterest(): #basic compund interest calculator with added amounts each year
    while (True):
        principal = input("what would you like your principal to be?: ")
        try:
            principal = float(principal)
            break
        except ValueError:
            print("Enter an integer or decimal to continue")
            continue
    while (True):
        years = input("How many years would you like to compound for?: ")
        try:
            years = int(years)
            break
        except ValueError:
            print("Enter an integer to continue")
            continue
            
    while (True):
        percent = input("What yearly interest rate would you like to see?: ")
        try:
            percent = float(percent)
            break
        except ValueError:
            print("Enter an integer or decimal to continue")
            continue
    while (True):
        addedAmount = input("How much each year would you like to add to your principal?: ")
        try:
            addedAmount = float(addedAmount)
            break
        except ValueError:
            print("Enter an integer or decimal to continue")
            continue
    money = principal*((percent*0.01)+1.00)
    for i in range(1,years):
        money += addedAmount
        print("year:",i, money)
        money = money*((percent*0.01)+1.00)
    print("Your balance after", int(years), "years will be:", money, "\n")
    return


def main():
    applicationLoop()
    return

main()
