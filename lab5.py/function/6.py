def rever(x):
    temp = []
    for i in reversed(range(len(x))):
        temp.append(x[i])
    return temp

x = "My name is akbota"
x = x.split(" ")
x = rever(x)
for i in x:
    print(i, end=" ")