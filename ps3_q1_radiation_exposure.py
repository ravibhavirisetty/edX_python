
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start,stop,step):
	exposure = 0.0
	k = start
	while k<stop:
		exposure += step * f(k)
		k += step
	return exposure

print radiationExposure(5,11,1)