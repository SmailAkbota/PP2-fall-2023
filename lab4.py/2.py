s=input()
t=input()
a=[int(s) for s in s.split()]
b=[int(t) for t in t.split()]
c=a+b
d=set(c)
print(len(c)-len(d))