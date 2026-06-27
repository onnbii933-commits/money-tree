from jose import jwt

SECRET_KEY = "CHANGE_THIS"

ALGORITHM = "HS256"

def create_access_token(user_id):

    payload = {
        "user_id": user_id
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
