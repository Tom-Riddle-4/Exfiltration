import jwt

secret_key="hehehehehehehehehehehehehehehehehehehehe"
payload = {"userName":"Tommy",
              "password":"Nagini",
              "userId": 32,
              "role": "Darklord"
              }
token = jwt.encode(payload, secret_key, algorithm="HS256")
print(token)
