import re
f=open('row.txt','r',encoding='utf-8')
file=f.read()
x=re.findall('ab{2,3}',file)
print(len(x))
print(x) 