# open inputFile.txt with the intention of reading it
inputFile = open("inputFile.txt", "r")

# open passFile.txt with the intention of writing it
passFile = open("passFile.txt" , "w")



# open failFile.txt with the intention of writing it
failFile = open("failFile.txt" , "w")


# loop through each line in inputFile.txt
# uncomment the following lines of code and fill in
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        #write pass ones in passFile.txt
        passFile.write(line)
    else:
        #write fail ones in failFile.txt
        failFile.write(line)
# close inputFile.txt


#now open both the files
passFile = open("passFile.txt" , "r")
failFile = open("failFile.txt" , "r")
print("pass File : " , passFile.read())
print("fail File: ", failFile.read())
inputFile.close()

# close passFile.txt
passFile.close()


# close failFile.txt
passFile.close()
