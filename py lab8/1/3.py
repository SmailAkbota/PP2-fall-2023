def palin(s):
    rev = ''
    for i in reversed(range(len(s))):
        rev += s[i]
    return s == rev

x = "catstac"
y = "black"

print(palin(x))
print(palin(y))