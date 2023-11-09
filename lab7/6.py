import re
f=open('row.txt', encoding='utf-8')
file=f.read()
temp = re.sub("\s|[ ,.]" , ":",file)
print(temp)