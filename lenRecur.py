
def lenRecur(astr):
	if astr == '':
		return 0
	else:
		return 1 + lenRecur(astr[1:])

s = raw_input('Enter a string to know its length: ')

print 'Length of the string is:', lenRecur(s)