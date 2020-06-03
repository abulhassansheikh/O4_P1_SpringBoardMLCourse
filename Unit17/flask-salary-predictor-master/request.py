import requests

# URL
url = 'http://127.0.0.1:5000/api'

# Change the value of experience that you want to test
payload = {
	'exp':"Air Filter Elements"
}

r = requests.post(url,json=payload)

print(r.json())

