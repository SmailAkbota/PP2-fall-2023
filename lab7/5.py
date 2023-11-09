import re
f=open('row.txt', encoding='utf-8')
file=f.read()
temp = re.findall(r'.*а.*б\b', file)
print(temp)

