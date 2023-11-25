import math
a= float(input("nhap a"))
b= float(input(" nhap b"))
c= float(input(" nhap c"))
print("A=", round(math.cos((a**2 - b**2 - c**2)/(-2*b*c)*180)/math.pi))
print("B=", round(math.cos((b**2 - a**2 - c**2)/(-2*a*c)*180)/math.pi))
print("C=", round(math.cos((c**2 - b**2 - a**2)/(-2*b*a)*180)/math.pi))

