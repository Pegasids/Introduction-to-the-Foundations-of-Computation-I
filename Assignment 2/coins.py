import sgenrand
repeat = 'y'

# program greeting
print("The purpose of this exercise is to enter a number of coin values")
print("that add up to a displayed target value.\n")
print("Enter coins values as 1-penny, 5-nickel, 10-dime,and 25-quarter.")
print("Hit return after the last entered coin value.")
print("--------------------")

# starting the game
while repeat == 'y':
    
    # generate a random number between 1 and 99
    n = sgenrand.randint(1,99)
    
    # print the question
    print("Enter coins that add up to", n,"cents, one per line.\n")
    
    a = 0
    count = 1
    # the game
    while a <= n:
        
        # let user enters the answers
        if count == 1:
            b = input("Enter first coin: ")
        if count > 1:
            b = input("Enter next coin: ")
        if b == "":
            break
        if b != '1' and b != '5' and b != '10' and b != '25':
            print("Invalid entry")
            continue
        
        # calculations
        b = int(b)
        a += b
        count += 1
        
    # determind the result
    if a == n:
        print("Correct!")
    if a > n:
        print("Sorry - total amount exceeds", n,"cents.")
    if a < n:
        print("Sorry - you only entered", a,"cents.")

    # ask if user wants to try again
    print()
    repeat = 'go in'
    while repeat != 'y' and repeat != 'n':
        repeat = input("Try again (y/n)?: ")
        if repeat != 'y' and repeat != 'n':
            print("Invalid entry")
    
# program ending
print("Thanks for playing ... goodbye")