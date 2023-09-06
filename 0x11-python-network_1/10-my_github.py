#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
import sys

if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]
url = "https://api.github.com/user"

try:
    response = requests.get(url, auth=(username, access_token))
    if response.status_code == 200:
        data = response.json()
        print(data["id"])
    else:
        print(None)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
