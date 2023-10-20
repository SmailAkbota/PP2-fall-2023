def has_33(nums):
    is33 = False
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return not is33
    return is33

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))