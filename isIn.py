
# works if the string is sorted in alphabetical order

def isIn(char,aStr):
	if aStr == '':
		return False
	if len(aStr) == 1:
		return aStr == char

	i = len(aStr)/2
	testChar = aStr[i]

	if char == testChar:
		return True
	elif char < testChar:
		return isIn(char,aStr[:i])
	elif char > testChar:
		return isIn(char,aStr[i+1:])

print isIn('a','abcde')