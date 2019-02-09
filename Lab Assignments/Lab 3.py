# Prompt User to enter a score
score = eval(input("What is your score? "))
if score < 0:
    print("Please enter a valid value.")
else:
    Max = eval(input("What is the maximum score? "))
    if Max <= 0 or score > Max:
        print("Please enter a valid value.")
    # Determind the letter grade
    else:
        # Calculate the percentage
        percentage = score / Max * 100    
        if  percentage >= 90:
            print("Your grade is A.")
        elif percentage >= 75:
            print("Your grade is B.")
        elif percentage >= 60:
            print("Your grade is C.")
        elif percentage >= 50:
            print("Your grade is D.")
        else:
            print("Your grade is F.")

input()