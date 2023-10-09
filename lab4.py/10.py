N, K = [int(s) for s in input().split()]
l= set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
x = set(l)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    x -= {a + b*i for i in range(max_strikes)}
print(len(l) - len(x))
