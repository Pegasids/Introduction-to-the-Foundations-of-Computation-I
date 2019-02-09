words = ['cow', 'horse', 'deer', 'elephant', 'lion', 'tiger', 'baboon', 'donkey', 'fox', 'giraffe']
# hangman greeting
print("Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")
word_num = input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
while word_num is not int or word_num == "" or int(word_num) > 9 or int(word_num) < 0:
    if word_num == "":
        print("Empty input!")
        word_num = input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
        continue  
    try:
        if int(word_num) > 9 or int(word_num) < 0:
            print("Index is out of range!")
            word_num = input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
            continue
    except:
        ValueError
    
    if word_num in "1234567890":
        break      
    if word_num is not int:
        print("Input must be an integer!")
        word_num = input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
        continue
        
word_num = int(word_num)
answer = words[word_num]
print("The length of the word is:",len(answer))
print("""\
______
|   |
|
|
|
|_____""")
bad_guesses = []
lst = (("_" + " ") * len(answer)).split()
up_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo_alphabet = "abcdefghijklmnopqrstuvwxyz"
def ask():
    count = 1
    while count <= 6:
        guess = input("Please enter the letter you guess: ")
        if guess in up_alphabet or guess in lo_alphabet:
            if len(guess) == 1:
                guess = guess.lower()
            else:
                print("You need to input a single alphabetic character!")
                continue
        else:
            print("You need to input a single alphabetic character!")
            continue
        
        if guess not in answer:
            bad_guesses.append(guess)
            print("Wrong!",guess, "is not in the word")
            showmatch(guess)
            print("wrong_list:", bad_guesses)
            count += 1
            DrawGallows(count)
        if guess in answer:
            print("Correct!",guess, "is in the word")
            showmatch(guess)
            print("wrong_list:", bad_guesses)
            if answer == show(lst):
                print("Game over! You win.")
                break            
            DrawGallows(count)
        if count > 6:
            print("""\
______
|   |
|   0
|  /|\\
|  / \\ 
|_____""")               
            print("Game over! You lose.")
            print("The word is:",answer)

def showmatch(guess):
    elem_position = -1
    for elem in answer:
        elem_position += 1
        if guess in elem:
            lst[elem_position] = guess
    
    print("word_match:",show(lst))

def show(lst):
    out = ""
    for elem in lst:
        out = out + elem
    return out


def DrawGallows(count):
    if count == 1:
        print("""\
______
|   |
|   
|
|
|_____""")
    if count == 2:
        print("""\
______
|   |
|   0
|   
|
|_____""")
    if count == 3:
        print("""\
______
|   |
|   0
|   |
|
|_____""")
    if count == 4:
        print("""\
______
|   |
|   0
|  /|
|
|_____""")
    if count == 5:
        print("""\
______
|   |
|   0
|  /|\\
|  
|_____""")
    if count == 6:
        print("""\
______
|   |
|   0
|  /|\\
|  / 
|_____""")    




ask()    