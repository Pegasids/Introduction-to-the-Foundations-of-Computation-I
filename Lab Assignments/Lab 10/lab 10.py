import os.path
import sys
while True:
    
    file = input("Enter a filename: ")
    bak = file + ".bak"
    if os.path.isfile(file):
        break
    else:
        print("File", file, "does not exist")

if os.path.isfile(bak):
    print("File", bak, "exists")
    answer = input("Overwrite? (y/n): ")
    if answer == "y":
        fin = open(file, 'r')
        a = fin.read()
        fout = open(bak, 'w')
        lineall = a
        fout.write(lineall)
        fout.close()
        fin.close()
    if answer == "n":
        SystemExit
else:
    fin = open(file, 'r')
    a = fin.read()
    fout = open(bak, 'w')
    lineall = a
    fout.write(lineall)
    fout.close()
    fin.close()


word = str(input("Enter the string to be removed: "))
b = a.replace(word, "X")

origout = open(file,'w')
origout.write(b)
origout.close()

print("Done")