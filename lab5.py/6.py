def filter(n):
    isPrime = True
    for i in range(2, n):
        if not (n % i):
            isPrime = False
            return isPrime
    return isPrime

a = [3, 17, 6, 10, 8, 5, 12]
primes = [x for x in a if filter(x)]

print(primes)