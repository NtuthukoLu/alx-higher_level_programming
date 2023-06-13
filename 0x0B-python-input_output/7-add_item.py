#!/usr/bin/python3
"""scipt tht Adds and saves argu to list """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fileName = "add_item.json"
List = []

try:
    List = load_from_json_file(fileName)
except:
    pass

for i in range(1, len(sys.argv)):
    List.append(sys.argv[i])
save_to_json_file(List, fileName)
