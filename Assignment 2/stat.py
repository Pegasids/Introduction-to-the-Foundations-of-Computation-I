# function for the average score
def average(total):
    return total / number_of_student

# input the number of cases
number_of_case = int(input())
count = 0

# array
list = []

# number of cases to repeat
for i in range(1, number_of_case + 1):
    number_of_student = int(input())
    total = 0
    count = count + 1
    n = 0
    lastscore = -1
    
    # number of students to repeat
    for b in range(1,number_of_student + 1):
        n = n + 1
        
        # input student's name
        name = input()
        
        # input student's score
        score = int(input())
        
        # find maximum score along with the student's name
        if score > lastscore:
            maximum = score
            maximumname = name
            
        # calculate the total of scores
        total = total + score
        lastscore = score
        
    # array output
    temp_output = "Case " + str(count) + "\n" + str("%.2f" % average(total)) + "\n" + str("%.2f" % maximum) + " " + maximumname
    list.append(temp_output)

# print the output
print()
for i in range(0, number_of_case):
    print(list[i])
