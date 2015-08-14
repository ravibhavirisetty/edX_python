
balance = 320000
annualInterestRate = 0.2

originalBalance = balance

low = originalBalance/12
high = (originalBalance * (1 + annualInterestRate/12)**12)/12
min_payment = (low + high)/2

while True:
	for i in range(1,13):
		rem_bal = balance - min_payment
		balance = rem_bal * (1 + annualInterestRate/12)
	if abs(balance) < 0.01:
		print 'Lowest payment:',round(min_payment,2)
		break
	else:
		if balance < 0:
			high = min_payment
		else:
			low = min_payment
		min_payment = (low + high)/2
		balance = originalBalance
