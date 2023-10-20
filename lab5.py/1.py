class MyClass:
    def getString(self, x):
        self.x = x
    def printString(self):
        print(self.x.upper())
s=MyClass()
s.getString(input())
s.printString()
