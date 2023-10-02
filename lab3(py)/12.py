a = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
k = d[0]
C = d[1]
b = []
for i in range(len(a)+1):
    if i<k:
        b.append(a[i])
    elif i==k:
        b.append(C)
    elif i>k:
        b.append(a[i-1])
print(' '.join([str(i) for i in b]))