import jwt
import time
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {"access token": token}


def signJWT(userID: str):
    payload = {"userID": userID, "expiryTime": time.time()}
    jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(jwt_token)


def decodeJWT(token: str):
    decodedJWT = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return decodeJWT if decodedJWT["expiryTime"] > time.time() else None
