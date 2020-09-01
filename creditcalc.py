import math

principal = int(input("Enter the credit principal:"))

print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
calc_type = input()

if calc_type == "m":
    payment = int(input("Enter the monthly payment:"))
    term = int(round(principal / payment))
    if term == 1:
        print("It will take {} month to repay the credit".format(term))
    elif term > 1:
        print("It will take {} months to repay the credit".format(term))

elif calc_type == "p":
    term = int(input("Enter the number of months:"))
    payment = principal / term
    frac, whole = math.modf(payment)
    if frac == 0.0:
        print("Your monthly payment = ", int(payment))
    elif frac != 0.0:
        if frac >= 0.5:
            payment = int(round(payment))
        else:
            payment = int(round(payment)) + 1
        final_payment = 1000 - (payment * (term - 1))
        print("Your monthly payment = {} and the last payment = {}.".format(payment, final_payment))
