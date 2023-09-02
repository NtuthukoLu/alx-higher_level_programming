#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve a challenge.
"""
import requests
    import sys

if __name__ == "__main__":
    url = "https://api.github.com/"
    username = sys.argv[1]
    repo = sys.argv[2]
    commits_url = url + "repos/{}/{}/commits".format(username, repo)
    response = requests.get(commits_url)
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            my_obj = response.json()
            for i, obj in enumerate(my_obj):
                if i == 10:
                    break
                if type(obj) is dict:
                    name = obj.get('commit').get('author').get('name')
                    print("{}: {}".format(obj.get('sha'), name))
        except ValueError as invalid_json:
            pass
