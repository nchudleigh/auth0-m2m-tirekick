import http.client
import json
import random
import os

conn = http.client.HTTPSConnection("dev-kq8sk6mb.us.auth0.com")

payload = json.dumps(
    {
        "client_name": f"Callback {random.randint(1, 100)}",
        "is_first_party": False,
        "redirect_uris": [
            "http://localhost:5000/callback",
            "http://localhost:5000/callback2",
        ],
    }
)

headers = {"content-type": "application/json"}

conn.request("POST", "/oidc/register", payload, headers)

res = conn.getresponse()
data = res.read()

response = json.loads(data.decode("utf-8"))

print(f"Client Name: {response['client_name']}")
print(f"Client ID: {response['client_id']}")
print(f"Client Secret: {response['client_secret']}")
