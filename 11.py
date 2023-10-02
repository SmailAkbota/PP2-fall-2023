numbers = list(map(int, input().split()))
k = int(input())
for i in range(k, len(numbers) - 1):
    numbers[i] = numbers[i + 1]
numbers.pop()
print(" ".join(map(str, numbers)))