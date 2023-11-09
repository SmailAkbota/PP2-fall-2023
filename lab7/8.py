import re

def text_match(text):
        x= re.split("[A-Z]",text)
        return x
        
with open("row.txt","r") as file:
    text = file.read()

print(text_match(text))
