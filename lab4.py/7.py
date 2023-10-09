n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    question = input()
    if question == "HELP":
        break
    answers = set(map(int, question.split()))
    response = input()
    if response == "YES":
        possible_numbers &= answers
    else:
        possible_numbers -= answers

print(*sorted(possible_numbers))