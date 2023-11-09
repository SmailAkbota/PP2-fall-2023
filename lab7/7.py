import re
import codecs

with codecs.open('row.txt', encoding='utf-8') as f:
    x = []
    for line in f:
        temp = re.sub("_([а-яА-Я])", lambda l: l.group(0).upper(), line)
        if(temp): x.append(temp)

print(x)