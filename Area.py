import math

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

s = (a+b+c)
print("Perimter of triangle is: ", s)
area = ((s*(s-a)*(s-b)*(s-c))**(1/2))
print("Area of triangle is: ", area)

A = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
print("Angle A: ", A)

B = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
print("Angle B: ", B)

C = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
print("Angle C: ", C)

