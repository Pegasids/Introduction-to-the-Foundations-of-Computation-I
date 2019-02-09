from wordplay import *
import os
import random
s = ""
all_pron = all_homophones()
all_anag = all_anagrams()
inv = invert_dict(all_homophones())
count = 0
txtfile = str(input("File name: "))
while True:
    if os.path.isfile(txtfile):
        fin = open(txtfile, 'r')
        break
    else:
        print("File DNE.")
        txtfile = str(input("File name: "))
        
    print("File does not exist.")
new = "new_" + txtfile
opt = input("Number of lines to be changed: ")
if opt == "all" or "All" or "ALL":
    opt = False
else:
    opt = int(opt)
for line in fin:
    count += 1
    line = line.split()
    each_line = []
    for word in line:
        pron = pronunciation(word, all_pron)
        sign = signature(word)
        word1 = all_anag.get(sign)
        if pron != "":
            lst_of_word = inv.get(pron)
            if len(lst_of_word) > 1 :
                while True:
                    sample_word = random.choice(lst_of_word)
                    if sample_word != word:
                        word = sample_word                    
                        break                    
        elif word1 != None:
            word = random.choice(word1)
        each_line.append(word)
    for each in each_line:
        print(each, end = " ")
    print()
    if count == opt:
        break
    s += "\n"
fin.close()
'''
print(s)
out = open(new,'w')
out.write(s)
out.close() '''