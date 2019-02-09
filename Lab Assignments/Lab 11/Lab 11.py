fin = open("names.txt", "r")
names = {}
for line in fin:
    line = line.strip("\n")
    if line not in names:
        names[line] = 1
    elif line in names:
        names[line] = names[line] + 1
fin.close()
times = max(names.values())

def rev_lookup(dictionary, times):
    lst =[]
    for key in dictionary:
        if names[key] == times:
            lst.append(key)
    lst.sort()
    aw = ""
    for word in lst:
        aw = aw + word + " "
    return aw

fout = open("output.txt", "w")
line1 = "The most frequent names are: " + rev_lookup(names, times) + "\n"
line2 = "Each of these names occur: " + str(max(names.values())) + " times"
all_lines = line1 + line2
fout.write(all_lines)
fout.close()