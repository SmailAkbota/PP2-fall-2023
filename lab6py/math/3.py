import math
n = int(input("N of sides: "))
l = int(input("L of side: "))
p = n*l
a = l/(2 * math.tan(math.pi/n))
area = p*a/2
print('area:')
print(round(area))