import math
def area(r):
    return math.pi*r*r
def perimeter(r):
    return 2*math.pi*r
r=int(input("Enter the radius of circle -"))
print("Area of a cirle:",area(r))
print("perimeter of a circle:",perimeter(r))
