#!/usr/bin/python3
"""script for posting data to web servers
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    http = requests.post(url, data={'q': q})
    try:
        my_dict = http.json()
        id = my_dict.get('id')
        name = my_dict.get('name')
        if len(my_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as e:
        print("Not a valid JSON")
