import csv 
import json
import xml.etree.ElementTree as ET

txt_file_path = "assets/parse_data/groceries.txt"
csv_file_path = "assets/parse_data/groceries.csv"
json_file_path = "assets/parse_data/groceries.json"
xml_file_path = "assets/parse_data/groceries.xml"

def read_txt_file(txt_file_path):
    with open(txt_file_path, "r") as file:
        data = file.read()
    # file is closed here, even if file.read() had raised an error

    
    print("Text file content:" ,data)
    parsed_data = data.split(", ")
    print("Parsed text file content:", parsed_data)
    print("Items in index 2:", parsed_data[2])
    
    
def read_csv_file(csv_file_path):
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  
        print(headers)
        for row in csv_reader:
            row[1] = int(row[1])
            print(row) 
            
def read_json_file(json_file_path):
    with open(json_file_path, "r") as file:
        data = file.read()
        
    parsed_data = json.loads(data)
    print("JSON file content:", parsed_data)
    print("apples quantity:", parsed_data["apples"])
    
def read_xml_file(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    # print("Root tag:", root.tag)
    # for child in root:
    #     print("Child:", child.tag, child.attrib, child.text)
    
    items_over_6 = []
    
    for item in root.findall("grocery_item"):
        name = item.find("name").text
        price = float(item.find("price").text)
        print(name, price)
        if price > 6.00:
            items_over_6.append(name)
        print("Items with price over 6:", items_over_6)
        
if __name__ == "__main__":
                    
    read_txt_file(txt_file_path)
    read_csv_file(csv_file_path)
    read_json_file(json_file_path)
    read_xml_file(xml_file_path)
    
    