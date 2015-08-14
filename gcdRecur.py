
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)

a = int(raw_input('Enter an interger \'A\': '))
b = int(raw_input('Enter an interger \'B\': '))

print 'GCD of', a, 'and', b, '=', gcdRecur(a,b)