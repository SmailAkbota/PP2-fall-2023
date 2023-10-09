n=int(input())
b=set()
for i in range(n):
    line=input()
    word=line.split()
    b.update(word)
print(len(b))    