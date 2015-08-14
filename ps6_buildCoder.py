
def buildCoder(shift):
	d = {}

    for i in range(len(string.ascii_lowercase)):
        s = (i + shift)  % 26
        c = string.ascii_lowercase[i]
        sc = string.ascii_lowercase[s]
        d[c] = sc
        d[c.upper()] = sc.upper()
 
    return d