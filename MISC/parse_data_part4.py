import xml.etree.ElementTree as ET

file_path = "MISC/groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()
small = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price)  < 2.0:
        small.append(name )

    # print(name, price)
print("Less Than 4 Items: ")
print(small)    