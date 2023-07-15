from flask import Flask, request, jsonify
from datetime import datetime as date
import jwt  # pip install pyjwt


app = Flask(__name__)


@app.route("/")
def home():
    return "Ghost API. Send your api key and generate JWT"


@app.route("/create", methods=["POST"])
def create_jwt():
    data = request.get_json()

    # Get Admin API key
    private_key = data.get("private_key")

    # Split the key into ID and SECRET
    id, secret = private_key.split(":")

    # Prepare header and payload
    iat = int(date.now().timestamp())

    header = {"alg": "HS256", "typ": "JWT", "kid": id}
    payload = {"iat": iat, "exp": iat + 5 * 60, "aud": "/admin/"}

    # Create the token (including decoding secret)
    token = jwt.encode(
        payload, bytes.fromhex(secret), algorithm="HS256", headers=header
    )

    return jsonify(token=token)
