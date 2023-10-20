def unique(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    return temp

x = [1, 7, 4, 5, 5, 7, 9, 1, 1]
print(unique(x))