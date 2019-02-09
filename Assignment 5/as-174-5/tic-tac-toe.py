a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
lst_of_coor = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
comp_coor = ["b2", "a1", "c3", "a3", "c1", "a2", "b3", "b1", "c2"]
user_used_coor = []
comp_used_coor = []
both_user_used_coor = []

def writeFinal():
    out = open("final.txt", 'w')
    line = "    a   b   c\n  -------------\n1 | " + a1 + " | " + b1 + " | " + c1 + " |\n  -------------\n2 | " + a2 + " | " + b2 + " | " + c2 + " |\n  -------------\n3 | " + a3 + " | " + b3 + " | " + c3 + " |\n  -------------"
    out.write(line)
        
        
def inputCoordinate():
    coor = str(input("Enter your move: "))
    coor = coor.strip().lower()
    while coor in user_used_coor:
        print("This position is already taken.")
        coor = str(input("Enter your move: "))
        coor = coor.strip().lower()
        
    while coor not in lst_of_coor:
        print("Invalid coordinates.")
        coor = str(input("Enter your move: "))
        coor = coor.strip().lower()
    user_used_coor.append(coor)
    user_used_coor.sort()
    both_user_used_coor.append(coor)
    both_user_used_coor.sort()
    return coor

def comp_res():
    for elem in comp_coor:
        if elem in both_user_used_coor:
            nothing = "nothing"
        else:
            print("My move is:",elem)
            user_used_coor.append(elem)
            user_used_coor.sort()
            both_user_used_coor.append(elem)            
            both_user_used_coor.sort()
            break
    return elem

def drawBoard():           
    print("    a   b   c\n  -------------\n1 |",a1,"|",b1,"|",c1,"|\n  -------------\n2 |",a2,"|",b2,"|",c2,"|\n  -------------\n3 |",a3,"|",b3,"|",c3,"|\n  -------------")

while True:
    your_coor = inputCoordinate()
    if your_coor == "a1":
        a1 = "O"
    if your_coor == "a2":
        a2 = "O"    
    if your_coor == "a3":
        a3 = "O"
    if your_coor == "b1":
        b1 = "O"   
    if your_coor == "b2":
        b2 = "O"
    if your_coor == "b3":
        b3 = "O"    
    if your_coor == "c1":
        c1 = "O"
    if your_coor == "c2":
        c2 = "O"   
    if your_coor == "c3":
        c3 = "O"        
    drawBoard()
    if a1 == "O" and a2 == "O" and a3 == "O":
        print("Game over! You win.")
        writeFinal()
        break
    if b1 == "O" and b2 == "O" and b3 == "O":
        print("Game over! You win.")
        writeFinal()
        break        
    if c1 == "O" and c2 == "O" and c3 == "O":
        print("Game over! You win.")
        writeFinal()
        break        
    if a1 == "O" and b1 == "O" and c1 == "O":
        print("Game over! You win.")
        writeFinal()
        break        
    if a2 == "O" and b2 == "O" and c2 == "O":
        print("Game over! You win.")
        writeFinal()
        break        
    if a3 == "O" and b3 == "O" and c3 == "O":
        print("Game over! You win.")
        writeFinal()
        break        
    if a1 == "O" and b2 == "O" and c3 == "O":
        print("Game over! You win.")
        writeFinal()
        break        
    if a3 == "O" and b2 == "O" and c1 == "O":
        print("Game over! You win.")
        writeFinal()
        break  
    if both_user_used_coor == lst_of_coor:
        print("Game over! No winner.")
        writeFinal()
        break
    my_coor = comp_res()
    if my_coor == "a1":
        a1 = "X"
    if my_coor == "a2":
        a2 = "X"    
    if my_coor == "a3":
        a3 = "X"
    if my_coor == "b1":
        b1 = "X"   
    if my_coor == "b2":
        b2 = "X"
    if my_coor == "b3":
        b3 = "X"    
    if my_coor == "c1":
        c1 = "X"
    if my_coor == "c2":
        c2 = "X"   
    if my_coor == "c3":
        c3 = "X"
    drawBoard()
    if a1 == "X" and a2 == "X" and a3 == "X":
        print("Game over! I win.")
        writeFinal()
        break
    if b1 == "X" and b2 == "X" and b3 == "X":
        print("Game over! I win.")
        writeFinal()
        break        
    if c1 == "X" and c2 == "X" and c3 == "X":
        print("Game over! I win.")
        writeFinal()
        break        
    if a1 == "X" and b1 == "X" and c1 == "X":
        print("Game over! I win.")
        writeFinal()
        break        
    if a2 == "X" and b2 == "X" and c2 == "X":
        print("Game over! I win.")
        writeFinal()
        break        
    if a3 == "X" and b3 == "X" and c3 == "X":
        print("Game over! I win.")
        writeFinal()
        break        
    if a1 == "X" and b2 == "X" and c3 == "X":
        print("Game over! I win.")
        writeFinal()
        break        
    if a3 == "X" and b2 == "X" and c1 == "X":
        print("Game over! I win.")
        writeFinal()
        break    
    if both_user_used_coor == lst_of_coor:
        print("Game over! No winner.")
        writeFinal()
        break    
