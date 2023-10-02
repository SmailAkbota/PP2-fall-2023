s=input()
a=[int(s) for s in s.split()]
for i in range(1,len(a)):# 5 1 5 1 5
 if a[i]>a[i-1]:
    print(a[i])
