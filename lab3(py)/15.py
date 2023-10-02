N,k=[int(elem) for elem in input().split()]
a=(['I' for I in range(N)])
c=(['.' for i in range(N)])
for i in range(k):
    b1,b2=[int(elem) for elem in input().split()]
    a[b1-1:b2]=c[b1-1:b2]
print(''.join(a))