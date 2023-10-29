n = int(input())
l = [x**2 for x in range(1, n+1)]
gen = iter(l)
print('all squares')
for i in gen:
    print(i)