
def oddTup(aTup):
	newTup = ()
	for x in xrange(len(aTup)):
		if x%2 == 0:
			newTup += (aTup[x],)
	return newTup

a = (9,1,'Hi',4,'$')

print oddTup(a)