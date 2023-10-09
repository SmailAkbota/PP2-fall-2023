s = input()
a = [int(num) for num in s.split()]
mp = {}

for i in range(len(a)):  # Use len(a) to specify the length of the list a
    
    if a[i] not in mp:
        print("no")
        mp[a[i]] = 1
    else:
        print("yes")