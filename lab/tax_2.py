import sys

insurance_rate = 0.835

def tax_calculation(income):
    if income * insurance_rate <= 3500:
        return float(0)
    else:
        require_anmount = float(income) * insurance_rate - 3500
        require_to_pay = require_anmount * rest_deduction(require_anmount) - fixnumber(require_anmount)
        return float(require_to_pay)


def final_income(income, require_to_pay):

    final_income = income * insurance_rate  - require_to_pay
    return final_income


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



for arg in sys.argv[1:]:
    front = arg.split(':')
    print(front[0] + ':', end = '')
    try:
        income = float(front[1])
    except ValueError:
        print("Parameter Error")
    else:    
        tax_to_pay = tax_calculation(income)
        result = final_income(income, tax_to_pay)
        format_result = format(result, ".2f")
        print(format_result)


