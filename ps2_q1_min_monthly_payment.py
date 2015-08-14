
balance = 4213				# current balance
annualInterestRate = 0.2	# annual interest rate
monthlyPaymentRate = 0.04	# min monthly rate

total_balance_paid = 0.0

for i in range(1,13):
	min_payment = round(monthlyPaymentRate*balance,2)
	total_balance_paid += min_payment
	unpaid_balance = balance - min_payment
	month_interest = annualInterestRate/12
	balance = round(unpaid_balance + (unpaid_balance*month_interest),2)
	print 'Month: ' + str(i)
	print 'Minimum monthly payment: ' + str(min_payment)
	print 'Remaining balance: ' + str(balance)

print 'Total paid: ' + str(total_balance_paid)
print 'Remaining balance: ' + str(balance)