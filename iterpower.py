
def iterPower(base, exp):
	power = 1
	if exp == 0:
		return power
	elif exp > 0:
		while exp > 0:
			power *= base
			exp -= 1
		return power

base = float(raw_input('Enter the base number: '))
exp = int(raw_input('Enter a power: '))

print base, '^', exp, '=', iterPower(base,exp)