#!/usr/bin/python3
"""Define a module"""


import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
json_file = "add_item.json"

if not os.path.exists(json_file):
    arg_list = []
else:
    arg_list = load_from_json_file(json_file)
arg_list.extend(sys.argv[1:])
save_to_json_file(arg_list, json_file)
