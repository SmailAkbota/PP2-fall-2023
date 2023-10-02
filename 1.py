s = input()  # s == '1 2 3'
a = s.split()
for i in range(len(a)):
    if i%2==0:
        print(a[i])
