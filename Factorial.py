# input the values
n = int(input("Enter the number of factorial: "))

# calculate first factorial number
f = n
count = n

#...............................
while count != 1:
    count = count - 1
    f = f * count
print("The factorial of", n, "is", f)
input()