def palin(s):
    temp = ''
    for i in reversed(range(len(s))):
        temp += s[i]
    return temp == s

x = "hello"
y = "worlddlrow"
print(palin(x))
print(palin(y))