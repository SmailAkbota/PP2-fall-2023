def upsLows(s):
    up = 0
    low = 0
    for i in s:
        if(i == i.upper()):
            up+=1
        else:
            low +=1
    return [up, low]

x = "Akbota"
print(upsLows(x))