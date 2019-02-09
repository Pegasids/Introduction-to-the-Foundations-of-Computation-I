def highestLetter(p):
    letter = "abcdefghijklmnopqrstuvwxyz"
    last_value = -500
    for i in range (len(p)):
        value = letter.index(p[i])
        if value > last_value:
            highest_letter = value
        last_value = value
     
    print(letter[highest_letter])

p = str(input())
p = str(p.lower())
highestLetter(p)