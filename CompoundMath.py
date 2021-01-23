
def CompInterest(principal, years, percent): #basic compund interest calculator

    principal = float(principal)
    years = float(years)
    percent = float(percent)

    money = principal*((percent*0.01)+1.00)**years
    money = round(money, 2)
    print("Your balance after", int(years), "years will be: $", money, "\n")
    return