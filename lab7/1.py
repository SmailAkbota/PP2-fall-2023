# import re
# file=open('row.txt','r',encoding="utf-8")
# text=file.read()
# x=re.search('ab*',text)
# if x:
#     print(x.group())
#     print("yes")
# else:
#     print("not found")

# file.close()        

import re
f=open('row.txt','r',encoding='utf-8')
file=f.read()
x=re.findall('ab*',file)
print(len(x))
print(x)