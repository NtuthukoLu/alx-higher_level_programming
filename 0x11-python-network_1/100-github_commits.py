#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve a challenge.
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name, owner_name = sys.argv[1], sys.argv[2]
url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    commits = response.json()

    for commit in commits[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code}")
except KeyError as e:
    print(f"KeyError: {e}")
