import jwt

print(" --- inicio ---")

encoded_jwt = jwt.encode({"": "Don Pepito de los palotes", "rol":"isNormal"}, "Con KeepCoding aprendemos", algorithm="HS256")
#encoded_jwt = jwt.encode({"": "Don Pepito de los palotes", "rol":"isAdmin"}, "Con KeepCoding aprendemos", algorithm="HS256")

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt)

