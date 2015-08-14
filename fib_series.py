
def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return (fib(n-1) + fib(n-2))

n = int(raw_input('Enter an integer to know its Fibonacci number: '))

print 'Fibonacci number for',n,'is:',fib(n)