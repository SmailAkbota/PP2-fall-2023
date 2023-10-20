def filter(n):
    isPrime = True
    for i in range(2, n):
        if not (n % i):
            isPrime = False
            return isPrime
    return isPrime

a = input()
a = a.split()
primes = [x for x in a if filter(int(x))]

print(primes)