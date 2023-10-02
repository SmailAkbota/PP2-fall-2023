a = [int(i) for i in input().split()]
minindex, minelem = 0, a[0]
maxindex, maxelem = 0, a[0]
for i in range(1,len(a)):
    if a[i] > maxelem:
        maxelem, maxindex = a[i], i
    if a[i] < minelem:
        minelem, minindex = a[i], i
a[minindex], a[maxindex] = maxelem, minelem
print(' '.join([str(i) for i in a]))
