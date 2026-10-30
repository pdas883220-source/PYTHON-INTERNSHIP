# Day 40 - Python API Requests

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Check response status
if response.status_code == 200:

    # Convert response into JSON
    data = response.json()

    print("User Information:")
    print("ID:", data["id"])
    print("Name:", data["name"])
    print("Username:", data["username"])
    print("Email:", data["email"])
    print("City:", data["address"]["city"])

else:
    print("Failed to fetch data.")