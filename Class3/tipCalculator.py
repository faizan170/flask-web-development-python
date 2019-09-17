def calcTip(bill):
    '''
        Accepts a parameter as user bill
        No tip if bill less than or equal to 500.
        If bill is between 500 and 5000. Tip will be 3%
        else. Tip will be 2%
    '''
    if bill <= 500:
        tip = 0
    elif bill <= 5000:
        tip = bill * 0.02
    else:
        tip = bill * 0.03
    return tip

# This loops continues to execute. You can set limit to it and break accordingly
while True:
    bill = float(input("Enter user bill: "))
    tip = calcTip(bill)
    print("Your Tip is:", round(tip, 2))

    