import re


f=open('row.txt', encoding='utf-8') 
file=f.read()
temp = re.findall('[а-яa-z]+_.*',file)

print(temp)

