s=input()
a=[int(s) for s in s.split()]
max=-21474836480
for i in range(0,len(a)):
    if max<a[i]:
        max=a[i]
        c=i
print(max,c)