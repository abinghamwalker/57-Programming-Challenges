"""Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip and then display both the tip and the total amount of the bill."""

def tip_calculator(bill:float,tip:float) -> float:
    tip_amount = bill * (tip/100)
    return round(tip_amount,2)

def total_bill(bill:float,tip:float) -> float:
    total_amount = (bill * (tip/100)) + bill
    return round(total_amount,2)

bill = float(input("Please enter the total bill amount:"))
tip = float(input ("Please enter the desired tip percentage:"))

tip_calc = tip_calculator(bill, tip)
bill_calc = total_bill(bill, tip)

print(f'The total tip amount is £{tip_calc:.2f}')
print(f'The total bill amount if £{bill_calc:.2f}')


