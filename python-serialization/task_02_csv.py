#!/usr/bin/python3
"""
    Module containing functions that takes CSV and converts to JSON
"""
import csv
import json


def convert_csv_to_json(filename):
    """Function to convert CSV to JSON"""

    try:
        with open(filename, 'r') as f:
            data = csv.DictReader(f)

            data1 = list(data)

        json_file = 'data.json'

        with open(json_file, 'w') as f:
            json.dumps(f, data, indent=4)
            return True
    except Exception as e:
        print(f'Exception: {e}')
        return False
    
csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")