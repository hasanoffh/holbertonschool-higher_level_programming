#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        response_json = r.json()

        if response_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(response_json.get('id'),
                                   response_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
