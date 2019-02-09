mainlist = str(input()).split(" ")
list_1 = mainlist
mini = list_1[0]
for i in list_1:
    if mini > i:
        mini = i

while mini in list_1:
    index = list_1.index(mini)
    list_1[index] = 'X'

if list_1.count('X') == len(list_1):
    n = str(len(list_1)) + '*' + 'X'
    print(n)
else:
    print(list_1)