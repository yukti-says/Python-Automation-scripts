# inputFile = open("inputFile.txt" , 'r')
# print(inputFile.read())
# inputFile.close()

# now do not print the whole data print only those who have passed the test
# inputFile = open("inputFile.txt" , 'r')
# lines = inputFile.readlines()
# passed = []
# for line in lines:
#     if "P" in line:
#         passed.append(line)
#         inputFile.close()

# print(passed)
# 
# Another way 
# split the data , it has name then a white space and then a age and then grade like P / F so one input having indexes like 0 , 1, 2
openFile = open("inputFile.txt" , 'r')
for line in openFile:
    line_split = line.split()
    if(line_split[2] == "P"):
        print(line)

openFile.close()               