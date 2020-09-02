import math
import sys

args = sys.argv
print(args)
arg_dict = {}
if len(args) == 5:
    for arg in args:
        if arg == "creditcalc.py":
            pass
        else:
            eq = arg.find("=")
            key = arg[2:eq]
            value = arg[eq + 1:]
            arg_dict.update({key: value})
elif len(args) != 5:
    print("Incorrect parameters")

if arg_dict["type"] == "annuity" and len(args) == 5:
    if "periods" not in arg_dict:
        principal = int(arg_dict["principal"])
        payment = float(arg_dict['payment'])
        interest = float(arg_dict["interest"]) / 1200
        x = payment / (payment - interest * principal)
        term = math.ceil(math.log(x, 1 + interest))
        overpayment = int((payment * term) - principal)
        print(term)
        if term < 12:
            print("It will take {} months to repay this credit!".format(term))
            print("Overpayment = ", overpayment)
        elif term == 12:
            print("It will take 1 year to repay this credit!")
            print("Overpayment = ", overpayment)
        elif term > 12:
            years = term // 12
            months = term % 12
            if months != 0:
                print("It will take {} years and {} months to repay this credit!".format(years, months))
                print("Overpayment = ", overpayment)
            elif months == 0:
                print("It will take {} years to repay this credit!".format(years))
                print("Overpayment = ", overpayment)

    elif "payment" not in arg_dict:
        principal = int(arg_dict["principal"])
        term = int(arg_dict["periods"])
        interest = float(arg_dict["interest"]) / 1200
        payment = math.ceil(interest * (1 / (1 - (1 + interest) ** (-term))) * principal)
        overpayment = (payment * term) - principal
        print("Your annuity payment = {}!".format(payment))
        print("Overpayment = ", overpayment)

    elif "principal" not in arg_dict:
        payment = float(arg_dict["payment"])
        term = int(arg_dict["periods"])
        interest = float(arg_dict["interest"]) / 1200
        denom = (1 + interest) ** term - 1
        numer = interest * (1 + interest) ** term
        x = numer / denom
        principal = math.floor(payment / x)
        overpayment = int((payment * term) - principal)
        print("Your credit principal = {}!".format(principal))
        print("Overpayment = ", overpayment)

elif arg_dict["type"] == "diff" and len(args) == 5:
    print(arg_dict)
    principal = int(arg_dict["principal"])
    term = int(arg_dict["periods"])
    interest = float(arg_dict["interest"]) / 1200
    total = 0
    for x in range(1, term + 1):
        payment = math.ceil((principal / term) + interest * (principal - ((principal * (x - 1)) / term)))
        total += payment
        print("Month {}: payment is {}".format(x, payment))
    print("Overpayment = ", int(total - principal))
