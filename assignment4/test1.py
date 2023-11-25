import math
def isValid(side1, side2, side3):
    if (side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1:
        return True
    else: return False

def area(side1, side2, side3):
    if isValid(side1, side2, side3):
        half_perimeter=(side1+side2+side3)/2
        area=math.sqrt(half_perimeter*(half_perimeter-side1)*(half_perimeter-side2)*(half_perimeter-side3))
        return area
    else: print("Inputs is invalid")

a=int(input("Nhập cạnh a:"))
b=int(input("Nhập cạnh b:"))
c=int(input("Nhập cạnh c:"))
result=area(a,b,c)
print(result)


