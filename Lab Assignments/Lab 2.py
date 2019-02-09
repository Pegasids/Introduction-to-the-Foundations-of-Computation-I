# input value for the two legs
sideA = eval(input("Enter the length of sideA: "))
sideB = eval(input("Enter the length of sideB: "))

# compute the length of sideC
import math
sideC = math.sqrt(sideA ** 2 + sideB ** 2)

# compute the perimeter
perimeter = sideA + sideB + sideC

# compute the area
area = (sideA * sideB) / 2

# display result
print("The length of the hypotenuse is", sideC, ". The perimeter is", perimeter, ". The area is", area, ".")

input()