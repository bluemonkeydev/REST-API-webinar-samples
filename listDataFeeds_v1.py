import requests
import json

api_key_value = '[YOUR KEY]'

payload = {'api_key': api_key_value}

response = requests.get("https://documentapi.brightplanet.com/documentapi/dataFeeds", params=payload)
response.raise_for_status()
response.encoding = 'utf-8'
j = response.json()

print json.dumps(j, indent=4)
