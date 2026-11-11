class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return( self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1=rectangle(10,20)
r2=rectangle(30,40)
print("area of first rectangle=",r1.area())
print("area of second rectangle=",r2.area())
print("perimeter of first rectangle=",r1.perimeter())
print("perimeter of second rectangle=",r2.perimeter())
if r1.area()>r2.area():
    print("Area of r1 is greater than Area of r2")
else:
    print("Area of r2 is greater than Area of r1") 