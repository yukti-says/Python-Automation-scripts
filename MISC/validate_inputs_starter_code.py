import pyinputplus as pyip

print("\nEXAMPLE 1")

# uncomment the following line of code and fill in 
result = pyip.inputInt("Enter number of bags: ",min=0) 
print("you will use ", result , "bags")

# uncomment the following line of code
# print("\nYou will use", result, "store bags.")

print("\nEXAMPLE 2")

# uncomment the following line of code and fill in 
result = pyip.inputMenu(["red" , "blue" , "green"] , lettered = False , numbered = True)

# uncomment the following line of code
print("\nYou have chosen a", result, "marker.")

print("\nEXAMPLE 3")

# uncomment the following line of code and fill in 
result = pyip.inputEmail("ENter your email : ")


# uncomment the following line of code
print("\nThe email you entered:", result)