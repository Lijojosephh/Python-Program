from graphics import circle,rectangle
from  graphics.threeD_graphics import cuboid,sphere

print("circle Operations")
print("area of circle=",circle.area(5))
print("perimeter of circle=",circle.perimeter(6))


print("rectangle Operations")
print("area of rectangle=",rectangle.area(4,6))
print("perimeter of rectangle=",rectangle.perimeter(5,7))

print("cuboid Operation")
print("Area of cuboid=",cuboid.area(3,4,5))
print("perimeter of cuboid=",cuboid.perimeter(3,4,5))

print("sphere Operation")
print("Area of sphere=",sphere.area(6))
print("volume of sphere=", sphere.volume(5))
