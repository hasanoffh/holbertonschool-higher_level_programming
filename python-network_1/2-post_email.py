#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    
    # Məlumatı URL-encoded formatına salırıq
    data = urllib.parse.urlencode(values)
    # Bayt formatına çeviririk (POST sorğusu üçün bu mütləqdir)
    data = data.encode('ascii')
    
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
