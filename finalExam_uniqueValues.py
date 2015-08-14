

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    a = []
    for i in aDict.values():
    	if aDict.values().count(i) == 1:
    		a.append(aDict.keys()[aDict.values().index(i)])
    a.sort()
    return a