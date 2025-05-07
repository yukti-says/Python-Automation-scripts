import re #working with regular expressions ,#extract data from text

# uncomment the following line of code and fill in 
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") #data in this format we want

example = "The number is 123-456-7890."

# uncomment the following line of code and fill in 
result = phoneNumRegex.search(example) #search for the pattern in the example string

# uncomment the following lines of code and fill in 
if result:
    print("Phone number found:", result.group()) #group() will return the matched string
    print("Area code:", result.group()[0:3]) #group(0) will return the entire matched string