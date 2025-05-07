import json

file_path = "MISC/groceries.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data) #data is loaded and saved into parsed_data

print("apples quantity:", parsed_data["apples"])