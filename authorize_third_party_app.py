import http.client
import json
import random
from dotenv import load_dotenv

from get_mgmt_api_token import CLIENT_ID

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
conn = http.client.HTTPSConnection("dev-kq8sk6mb.us.auth0.com")

conn.request("GET", f"/authorize?client_id={CLIENT_ID}")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
