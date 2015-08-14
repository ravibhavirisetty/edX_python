
balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
newbalance = balance
monthlyPayment = 0

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance

    for month in range(1,13):
        newbalance -= monthlyPayment
        newbalance += monthlyInterestRate * newbalance

print "Lowest Payment:", monthlyPayment