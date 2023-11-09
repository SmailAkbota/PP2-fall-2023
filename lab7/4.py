import re
f=open('row.txt', encoding='utf-8') 
file=f.read()
temp = re.findall("[А-Я]{1}[а-я]+",file)

print(temp)
# import re
# import codecs

# with codecs.open('row.txt', encoding='utf-8') as f:
#     x = []
#     for line in f:
#         l = re.findall(r"^[А-Я]+[а-я]+", line)
#         if(l): x.append(l)

# print(x)

