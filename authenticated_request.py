import os
import http.client
import json

from dotenv import load_dotenv

load_dotenv()


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
audience = os.getenv("AUDIENCE")

auth0_domain = os.getenv("AUTH0_DOMAIN")

# Get a fresh auth0 token
conn = http.client.HTTPSConnection(auth0_domain)
payload = json.dumps(
    {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": audience,
        "grant_type": "client_credentials",
    }
)
conn.request("POST", "/oauth/token", payload, {"content-type": "application/json"})
res = conn.getresponse()
data = res.read()
response = json.loads(data.decode("utf-8"))
access_token = response["access_token"]


# Set up connection and auth headers
conn = http.client.HTTPConnection("localhost:5000")
headers = {
    "authorization": f"Bearer {access_token}",
}


def make_request(path, authenticated=True):
    if not authenticated:
        conn.request("GET", path)
    else:
        conn.request("GET", path, headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


# Make unauthenticated request to API, no headers needed
make_request("/api/public", authenticated=False)

# Make authenticated request to API
make_request("/api/private")

# Make authenticated request to API with read scope requirement
make_request("/api/private-scoped")
