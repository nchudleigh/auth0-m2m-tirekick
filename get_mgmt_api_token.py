import http.client

conn = http.client.HTTPSConnection("dev-kq8sk6mb.us.auth0.com")
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

payload = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "audience": "https://dev-kq8sk6mb.us.auth0.com/api/v2/",
    "grant_type": "client_credentials",
}

headers = {"content-type": "application/json"}

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
