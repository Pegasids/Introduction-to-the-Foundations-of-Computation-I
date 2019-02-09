# prompt the user to enter the amount of Canadian dollar
CAD = eval(input("What is the amount of Canadian dollars you wish to convert? "))

# prompt the user to enter the exchange rate
rate = eval(input("What is the current exchange rate? "))

# compute conversion
newcurrency = CAD * rate

# round the new value to 2 decimal places
newcurrency = format(newcurrency, ".2f")

# display results
print("The amount in the Foreign Currency is:", newcurrency)

input()