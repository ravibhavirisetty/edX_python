
def howMany(a):
	values = a.values()
	i = 0
	for x in values:
		i += len(x)
	return i

def biggest(a):
    keys = a.keys()
    i = []
    for x in keys:
        i.append(len(a[x]))
    while True:
        try:
            return keys[i.index(max(i))]
        except:
            return None

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print 'biggest =', biggest(animals)

f = {}

print 'biggest =', biggest(f)