#!/usr/bin/python3
""" 4-from_json_string Module """
import json


def from_json_string(my_str):
    """returns a object represented by a JSON string"""
    return json.loads(my_str)
