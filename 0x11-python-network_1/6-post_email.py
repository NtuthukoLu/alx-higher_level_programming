#!/usr/bin/python3
"""script for posting data to web servers
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    http = requests.post(url, value)
    print(http.text)
