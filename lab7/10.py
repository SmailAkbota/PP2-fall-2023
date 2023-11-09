import re
import codecs

with codecs.open('row.txt', encoding='utf-8') as f:
    x = []
    for line in f:
        temp = re.sub("(\w)([А-Я])", lambda l: "_".join(l.group(0).lower()), line)
        if(temp): x.append(temp)

print(x)