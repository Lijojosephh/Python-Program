from graphics import circle,rectangle
from graphics.Three_D_Graphics import cuboid,sphere

print("\n area and perimeter of rectangle")
print("Area of Rectangle=",rectangle.area(7,2))
print("Primeter of Rectangle=",rectangle.perimeter(6,3))

print("\n area of circle")
print("Area of Circle=",circle.area(6))
print("Perimeter of Circle=",circle.perimeter(6))


print("\n cuboid")
print("Area of Cuboid=",cuboid.surfacearea(2,4,7))
print("Perimeter of Cuboid=",cuboid.cuberperimeter(3,7))


print("\n sphere")
print("Area of Cuboid=",sphere.spherearea(7))
print("Perimeter of Cuboid=",sphere.cuberperimeter(3,7))

