import sys


def tax_calculation(income):
    require_anmount = int(income) - 3500
    require_to_pay = require_anmount * rest_deduction(require_anmount) - fixnumber(require_anmount)

    return require_to_pay


def rest_deduction(require_anmount):
    if require_anmount <= 1500:
        return float(0.03)
    elif require_anmount < 4500 and require_anmount > 1500:
        return float(0.1)
    elif require_anmount < 9000 and require_anmount > 4500:
        return float(0.2)
    elif require_anmount < 35000 and require_anmount > 9000:
        return float(0.25) 
    elif require_anmount < 55000 and require_anmount > 35000:
        return float(0.3)
    elif require_anmount < 80000 and require_anmount > 55000:
        return float(0.35)
    elif require_anmount > 80000:
        return float(0.45)

def fixnumber(require_anmount):
    if require_anmount <= 1500:
        return 0
    elif require_anmount < 4500 and require_anmount > 1500:
        return 105
    elif require_anmount < 9000 and require_anmount > 4500:
        return 555
    elif require_anmount < 35000 and require_anmount > 9000:
        return 1005
    elif require_anmount < 55000 and require_anmount > 35000:
        return 2755
    elif require_anmount < 80000 and require_anmount > 55000:
        return 5505
    elif require_anmount > 80000:
        return 13505


try:
    result = tax_calculation(sys.argv[1])
except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")
else:
    format_result = format(result, ".2f")
    print(format_result)

