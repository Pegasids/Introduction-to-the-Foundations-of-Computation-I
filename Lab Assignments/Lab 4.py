# input values for n and m
n = int(input("n = ? "))
m = int(input("m = ? "))

a = 1
# calculate
for i in range (1, n+1):
    a = a * i
    if i >= n-m:
        print(a)
input()