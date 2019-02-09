h = eval(input("What is the height: "))
r = eval(input("What is the radius: "))
pi = 3.1415926

def vol(h,r,pi):
    return pi * r * r * h

print("The volume is", vol(h,r,pi))

def surf_area(h,r,pi):
    return (2 * pi * r * r) + (2 * pi * r * h)

print("The surface area is", surf_area(h,r,pi))
