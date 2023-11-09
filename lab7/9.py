import re

def spaces(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

with open("row.txt","r") as file:
    text = file.read()

print(spaces(text))
