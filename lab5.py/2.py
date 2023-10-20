# class Shape:
#     def __init__(self, length):
#         self.length = length
#         self.area01= 0
#     def area(self):
#         print(int(self.length) ** 2)

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__(length)

# x = Square(input())
# x.area()

class Shape:
    def __init__(self, length,width):
        self.length = length
        self.width=width
        self.area01= 0
    def area(self):
        print(int(self.length) * int(self.width))

class Square(Shape):
    def __init__(self, length, width):
        super().__init__(length,width)

x = Square(input(),input())
x.area()
