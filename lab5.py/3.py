class Shape:
    def __init__(self, length,width):
        self.length = length
        self.width=width

        self.area2= 0
    def area(self):
        print(int(self.length)*int(self.width))

class Rectangle(Shape):
   def __init__(self, length, width):
        super().__init__(length, width)

x = Shape(int(input()), int(input()))
print(x.length, x.width) 

x.area()