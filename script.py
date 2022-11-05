# importing necessary libries 
import csv
import json
from hashlib import sha256
import os

# column names of the csv 
COLUMN_NAMES = ['TEAM NAMES', 'Series Number' ,'Filename',
            'Name', 'Description', 'Gender', 'Attributes', 'UUID', 'Hash']

# General template of a CHIP 007 JSON file. Using it to create individual jsons per row
chip_007 = {
    "format": "CHIP-0007",
    "name": "defualt",
    "description": "defualt",
    "minting_tool": "SuperMinter/2.5.2",
    "sensitive_content": False,
    "series_number": 0,
    "series_total": 420,
    "attribute": [],
    "collection": {
        "name": "Zuri NFT Tickets for Free Lunch",
        "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
        "attributes": [
            {
            "type": "description",
            "value": "Rewards for accomplishments during HNGi9."
            }
        ]
    }
}

def change_to_list_of_dicts(attributes : str):
    """Function to convert the value of the attributes column from a string to a list of dictionaries 

    Args:
        attributes (str): the values of the attributes column

    Returns:
        list : List of dictionaries extracted from the given string
    """
    attributes = attributes.strip(";")
    container = []
    key_and_value = [val.strip().split(":") for val in attributes.split(";")]
    container = [{val[0].strip() : val[1].strip()} for val in key_and_value]
    return container
    
# function to create the CHIP007 json, encode it, and append it to a list 
def create_json_and_encode(csv_path : str):
    """Function to create a CHIP 007 json object for each row and encode it using sha256

    Args:
        csv_path (str): Path to the csv file 

    Returns:
        list: List of rows in the csv file along with their respective sha256 encodings
    """
    
    list_of_rows = []
    with open(csv_path, encoding='utf-8') as csv_file:
        csv_content = csv.DictReader(csv_file)
        for row in csv_content:
            chip_007["name"] = row["Name"]
            chip_007["description"] = row["Description"]
            chip_007["series_number"] = int(row["Series Number"])
            chip_007["attribute"] = change_to_list_of_dicts(row["Attributes"])
            encoding = json.dumps(chip_007, sort_keys=True).encode('utf-8')
            encoding = sha256(encoding).hexdigest()
            row["Hash"] = encoding
            list_of_rows.append(row)
            
        print("Calculating sha256...........................Done", '\n')
            
        return list_of_rows
        

def create_csv(path : str):
    """Generate the final csv with the encoded CHIP 007 json object

    Args:
        path (str): Path to the csv file
    """
    filename = path.split("\\")[-1].split(".")[0]
    with open(f"{filename}.output.csv", 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = COLUMN_NAMES)
        writer.writeheader()
        writer.writerows(create_json_and_encode(path))
        print(f"Successfully created {filename}.output.csv!")
    
if __name__ == "__main__":
    create_csv("csv\hng.csv")