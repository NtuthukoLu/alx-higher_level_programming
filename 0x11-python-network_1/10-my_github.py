#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    http = requests.get(url, auth=HTTPBasicAuth(username, token)).json()
    print(http.get('id'))
