
def genPrimes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

p = genPrimes()

for i in range(40):
    print p.next()