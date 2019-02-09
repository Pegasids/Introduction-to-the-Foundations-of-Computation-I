# prompt the user for input
centimetres = eval(input("Enter the length in centimetres: "))

# get yard and remaining feet and inches
yards = centimetres // (2.54 * 12 * 3)
remainingcentimetres = centimetres % (2.54 * 12 * 3)
feet = remainingcentimetres // (2.54 * 12)
remainingfeet = remainingcentimetres % (2.54 * 12)
inches = remainingfeet / 2.54

# display results
print("The length is", round(yards), "yard,", round(feet), "foot, and", format(inches, ".4f"), "inches")

input()