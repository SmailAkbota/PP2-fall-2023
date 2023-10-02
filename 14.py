a = [int(a) for a in input().split()]
elem = 0
for i in range(len(a)):
    k = 0
    for j in range(len(a)):
        elem = a[i]
        if i != j and a[i] == a[j]:
            k = 1
    if k == 0:
        print(elem, end = ' ')