import os
from dotenv import load_dotenv

load_dotenv()

AUDIENCE = os.getenv("AUDIENCE")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
MGMT_API_ACCESS_TOKEN = os.getenv("MGMT_API_ACCESS_TOKEN")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")


print(
    "https://dev-kq8sk6mb.us.auth0.com/authorize?"
    f"client_id={CLIENT_ID}&"
    "redirect_uri=http://localhost:5000/callback&"
    "response_type=token&"
    "__scope=email&"
    f"__audience={AUDIENCE}&"
    "nonce=12345&"
    "state=12345"
)
