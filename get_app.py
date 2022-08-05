import http.client
import json
import random
import os

from dotenv import load_dotenv

conn = http.client.HTTPSConnection("dev-kq8sk6mb.us.auth0.com")

load_dotenv()
mgmt_access_token = os.getenv("MGMT_API_ACCESS_TOKEN")
headers = {"authorization": f"Bearer {mgmt_access_token}"}

conn.request(
    "GET",
    f"/api/v2/clients/{response['client_id']}?fields=is_first_party&include_fields=true",
    headers=headers,
)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
