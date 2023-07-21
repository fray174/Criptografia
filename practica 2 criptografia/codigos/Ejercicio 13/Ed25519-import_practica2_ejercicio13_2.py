import ed25519


publickey = open("ed25519-publ","rb").read()
privatekey = open("ed25519-priv","rb").read()
signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
signature = signedKey.sign(msg, encoding='hex')

print("Firma Generada (64 bytes):", signature)

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
