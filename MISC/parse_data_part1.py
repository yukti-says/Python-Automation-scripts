file_path = "DOCUMENTS/groceries.txt" #defiend file path

with open(file_path, "r") as file:
    data = file.read()
    
print("data:", data)
parsed_data = data.split(", ") #thid function slip the data into a list
print("parsed data:", parsed_data)
print("item at index 2:", parsed_data[2])
#getting data in last
print("last data: ",parsed_data[5])