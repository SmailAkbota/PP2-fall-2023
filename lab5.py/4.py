class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def  Show(self):
        print(self.x,self.y)  
    def Move(self,a,b):
        self.x=a
        self.y=b
    def Dist(self,x1,y1):
        print((self.x-x1)**2+(self.y-y1)**2)**1/2
print("Enter p1 : ")
p1 = Point(int(input()), int(input()))
print("Enter p2 : ")
p2 = Point(int(input()), int(input()))
print("p1 : ", end="")
p1.Show()
print("p2  ", end="")
p2.Show()
print("Enter: ")
p2.Move(int(input()), int(input()))
print("p2 new: ", end="")
p2.Show()
print("distance between p1 and p2: ", end="")
p1.Dist(p2.x, p2.y)


