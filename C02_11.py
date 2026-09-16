square = lambda a: a * a
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h

a=float(input("enter the side of square: "))
print("Area of Square =", square(a))

l=float(input("enter the length of rectangle: "))
b=float(input("enter the breadth of rectangle: "))
print("Area of Rectangle =", rectangle(l,b))


b=float(input("enter the base of triangle: "))
h=float(input("enter the height of triangle: "))
print("Area of Triangle =", triangle(b,h))
