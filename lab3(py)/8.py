numbers = list(map(int, input().split()))

unique_count = 1  


for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        unique_count += 1

print(unique_count)