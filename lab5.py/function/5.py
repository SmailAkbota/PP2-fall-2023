from itertools import permutations
def permute(string):
    x = list(permutations(string))
    return x

x = "some"
x = permute(x)
for i in x:
    print(''.join(i), end=" ")