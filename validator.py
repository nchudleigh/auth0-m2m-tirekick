import json
from urllib.request import urlopen

from authlib.oauth2.rfc7523 import JWTBearerTokenValidator
from authlib.jose.rfc7517.jwk import JsonWebKey


class Auth0JWTBearerTokenValidator(JWTBearerTokenValidator):
    def __init__(self, domain, audience):
        issuer = f"https://{domain}/"

        # Get the public key from Auth0, and convert to JWK url
        jsonurl = urlopen(f"{issuer}.well-known/jwks.json")

        # Download the public key, parse it, and convert to JWK public key
        public_key = JsonWebKey.import_key_set(json.loads(jsonurl.read()))

        # Initialize the JWT bearer token validator with the public key
        super(Auth0JWTBearerTokenValidator, self).__init__(public_key)

        # Set the JWK options
        self.claims_options = {
            "exp": {"essential": True},
            "aud": {"essential": True, "value": audience},
            "iss": {"essential": True, "value": issuer},
        }
