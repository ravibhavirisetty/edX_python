
def gcd(a,b):
	c = min(a,b)
	while a%c!=0 or b%c!=0:
		c -= 1
	return c

a = int(raw_input('Enter an interger \'A\': '))
b = int(raw_input('Enter an interger \'B\': '))

print 'GCD of', a, 'and', b, '=', gcd(a,b)