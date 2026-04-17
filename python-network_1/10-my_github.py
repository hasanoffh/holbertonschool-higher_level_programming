#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id.
"""
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(r.json().get("id"))
    except ValueError:
        print("None")
