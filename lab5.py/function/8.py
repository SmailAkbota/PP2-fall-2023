def spy_game(nums):
    zzs = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zzs.append(0)
        elif nums[i] == 7:
            zzs.append(7)
    
    return zzs == [0, 0, 7]

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))