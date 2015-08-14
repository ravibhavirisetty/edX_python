
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Raviteja Bhavirisetty

# Quiz

# Problem 1
# 1-1:	True
# 1-2:	False
# 1-3:	False
# 1-4:	False
# 1-5:	False
# 1-6:	False
# 1-7:	True
# 1-8:	False
# 1-9:	True
# 1-10:	False

# Problem 2
# 2-1:	tuple
# 2-2:	Testing compares program output to the expected output.
#		Debugging is a process to studey the events leading upto an error
# 2-3:	type(s) can be 'list'
# 2-4:	abstraction
# 2-5:	cloning

# Problem 3
# 3-1:	["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"] and ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
# 3-2:	Nothing is wrong; the code is fine as-is

# Problem 4
def myLog(x, b):
    if x<b:
        return 0
    else:
        return 1 + myLog(x/b,b)


# Problem 5
def lessThan4(aList):
	a = []
	for i in aList:
		if len(i) < 4:
			a.append(i)
	return a


# Problem 6
def sumDigits(value):
    return value and (value % 10 + sumDigits(value // 10))


# Problem 7
def keysWithValue(aDict, target):
	output = []
	for i in aDict.keys():
		if aDict[i] == target:
			output.append(i)
	return output


# Problem 8
def f(s):
    return 'a' in s

def satisfiesF(L):
	for n, i in enumerate(L):
		if not f(i):
			L[n] = '!'
	for i in range(0,L.count('!')):
		L.remove('!')
	return len(L)

run_satisfiesF(L, satisfiesF)
