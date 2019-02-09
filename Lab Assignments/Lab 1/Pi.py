print("wait.......")
pi = 0
for n in range (0, 10000000):
    pi = (4 * ((-1) ** n) / ((2 * n) + 1)) + pi
print(pi)
input()
