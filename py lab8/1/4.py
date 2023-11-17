import time
import sys

def rootDelay(x, t):
    for i in range(101):
        time.sleep(t/1000/100)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print()
    return x**(1/2)

x = 25100
t = 2123
print(rootDelay(x, t))