import requests

response = requests.get('http://127.0.0.1:5000/transformationslist')

print("Entire JSON response")
print(response.json())

