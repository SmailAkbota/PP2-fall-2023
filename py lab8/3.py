import os

path = "/Users/akbotasmail/py lab8"

print(os.path.exists(path))
directory = os.getcwd()
portion = directory.split("\\")
print(portion[-1])