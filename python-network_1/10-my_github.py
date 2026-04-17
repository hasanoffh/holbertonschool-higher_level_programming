#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    # Basic Authentication istifadə edərək sorğu göndəririk
    r = requests.get(url, auth=(username, token))
    
    try:
        # Cavabı JSON formatında oxuyuruq
        user_data = r.json()
        # 'id' açarını çap edirik, yoxdursa None qaytarır
        print(user_data.get('id'))
    except ValueError:
        print("None")
