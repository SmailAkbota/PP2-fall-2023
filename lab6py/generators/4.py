def squares(a, b):
    while a <= b:
        yield a ** 2
        a += 1
   
a = 1  
b = int(input())

for square in squares(a, b):
    print(square)