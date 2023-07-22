import http.client
import base64
import json

# User data
username = "username"
api_token_id = "token id"
api_token_secret = "secret token"

# Base64 encoding of the API token
api_token = f"{api_token_id}:{api_token_secret}"
encoded_api_token = base64.b64encode(api_token.encode()).decode()

# Query parameters
url = "/v1/messages"
host = "api.bulksms.com"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {encoded_api_token}"
}

# number - Changeable, phone numbers
body = f"Hello! SMS content"
payload = {
    "to": number,
    "body": body,
    "routingGroup": "ECONOMY",
    "encoding": "TEXT"
}

# Send the request
conn = http.client.HTTPSConnection(host)
conn.request("POST", url, json.dumps(payload), headers)

# Getting the answer
response = conn.getresponse()

# Reading the answer
data = response.read().decode()
print(data)

# Close the link
conn.close()
