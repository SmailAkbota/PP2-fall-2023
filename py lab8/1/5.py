def ifTrue(tup):
    for i in tup:
        if not i:
            return False
    return True

x = (True, True, True, True)
y = (True, False, True, True)

print(ifTrue(x))
print(ifTrue(y))