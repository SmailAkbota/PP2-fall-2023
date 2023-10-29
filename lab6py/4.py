from datetime import datetime 

x = datetime(2023, 10, 31).timestamp()
y = datetime.now().timestamp()
diff = x-y
print("Seconds left to halloween ")
print(round(diff))