
def isWordGuessed(secretWord, lettersGuessed):
	for i in secretWord:
		if i in lettersGuessed:
			guess = True
		else:
			guess = False	

	return guess

print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])