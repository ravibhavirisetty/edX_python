
def printMove(fr, to):
	print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
	if n == 1:
		printMove(fr, to)
	else:
		Towers(n-1,fr,spare,to)
		Towers(1,fr,to,spare)
		Towers(n-1,spare,to,fr)

n = int(raw_input('Enter value of \'n\': '))

print 'Solution to the Tower of Hanoi of', n, 'ring(s) - 	'
Towers(n,'f','t','s')
