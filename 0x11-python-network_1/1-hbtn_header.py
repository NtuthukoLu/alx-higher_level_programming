#!/usr/bin/python3
"""takes in url send req to url and displays
"""
from urllib import request
import sys


if __name__ == "__main__":
    http = request.Request(sys.argv[1])
    with request.urlopen(http) as page:
        print(page.info()['X-Request-Id'])
