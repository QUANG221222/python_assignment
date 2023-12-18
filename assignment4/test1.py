import math
def isValid(side1, side2, side3):
    if (side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1:
        return True
    else: return False
def area(side1, side2, side3):
    if(isValid):
        half_parameter=(side1+side2+side3)/2
        area=math.sqrt(half_parameter*(half_parameter-side1)*(half_parameter-side2)*(half_parameter-side3))
        print("The area of the triangle is",round(area,2))
    else:
        print("Inputs are invalid")

a,b,c=eval(input("Enter 3 side of triangle:"))
area(a,b,c)


