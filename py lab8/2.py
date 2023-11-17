import os

path = "/Users/akbotasmail/py lab8"

print(os.path.exists(path))

if os.access(path, os.R_OK):
    print("You can access")
else:
    print("No access")

if os.access(path, os.W_OK):
    print("You can write")
else:
    print("No writing")

if os.access(path, os.X_OK):
    print("You can execute")
else:
    print("No executing")   