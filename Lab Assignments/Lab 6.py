while True:
    word = input("Enter a word: ")
    
    if word == "":
            print("Goodbye!")
            break    
    
    if 'e' not in word and len(word) < 3:
        word = 'x' * len(word)
        print(word)
   
    if 'e' not in word and len(word) >= 3:
        word = word[:-4] + 'xxx'
        print(word)
        
    while 'e' in word:
            x = word.find('e')
            x = int(x)
            word = word[:x] + 'x' + word[x+1:]
            if 'e' not in word:
                print(word)
                break  
