n = int(input())
all_n = set(range(1, n + 1))
possible = all_n
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possible & guess) > len(possible) / 2:
        print('YES')
        possible &= guess
    else:
        print('NO')
        possible &= all_n - guess
        
print(' '.join([str(x) for x in sorted(possible)]))
