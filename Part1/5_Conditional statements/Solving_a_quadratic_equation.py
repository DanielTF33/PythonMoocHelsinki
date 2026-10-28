import math
from math import sqrt

a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

x = (-b + sqrt((b*b)-4*a*c)) / (2*a)
x2 = (-b - sqrt((b*b)-4*a*c)) / (2*a)


print(f"The roots are {x} and {x2}")