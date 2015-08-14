
# guess the number between 0 and 99
# raviteja bhavirisetty

a = 0
b = 100
print 'Please think of a number between 0 and 100!'
while True:
	c = (a + b)/2
	print 'Is your secret number ' + str(c) + '?'
	guess = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
	if guess == 'l':
		a = c
	elif guess == 'h':
		b = c
	elif guess == 'c':
		print 'Game over. Your secret number was: ' + str(c) + '.'
		break
	else:
		print 'error'