import requests
import json

URL = "http://127.0.0.1:8000/userCreate/"

data = {
	'name' : 'Jatin',
	'last_name': 'Kumar',
	'city': 'Delhi',
}

json_data = json.dumps(data)	# converting python object to json string

req = requests.post(url = URL, data = json_data)	# getting request with url = URL, data = json_data

# req.raise_for_status()  # raises exception when not a 2xx req

# if req.status_code != 204:
# 	return req.json()

data = req.json()

print(data)
