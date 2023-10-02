s=input()
a=[int(s) for s in s.split()]
b=[]
for i in range(1,len(a)):
    if a[i]>0 and a[i-1]>0:
        b.append(int(a[i-1]))
        b.append(int(a[i]))

    elif a[i]<0 and a[i-1]<0:
        b.append(int(a[i-1]))
        b.append(int(a[i]))
    else:
        print(" ")  
if len(b)==0:
    print(" ")   
else:
    print(b[0],b[1])    