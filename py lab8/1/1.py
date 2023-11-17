def mult(lst):
    res = 1;
    for i in lst:
        res *= i
    return res

x = [1, 2, 9, 6]
print(mult(x))