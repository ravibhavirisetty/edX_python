
a = {'abc':'qwe','abcd':'dfge','efgh':'abc'}
array = a.keys()
test = []
for i in array:
	if 'abc' in i:
		test.append(i)
print array
print test

for i in test:
	del a[i]

print a