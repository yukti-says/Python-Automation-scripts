import csv

file_path = "MISC/groceries.csv"

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader) #this will seperate data from headers
    # for row in csv_reader:
    #     row[1] = int(row[1]) #this will convert the quantity value into int type 
    #     print(row)

    for row in csv_reader:
        row[1] = int(row[1])
        if(row[1] >= 4):
            print(row)
        # if(row[1] == "4"):
        #     print(row)