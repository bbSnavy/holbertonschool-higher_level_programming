#!/usr/bin/python3
""" add item """
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    try:
        v = load_from_json_file('add_item.json')
    except:
        v = []
    save_to_json_file(v + sys.argv[1:][:], 'add_item.json')
