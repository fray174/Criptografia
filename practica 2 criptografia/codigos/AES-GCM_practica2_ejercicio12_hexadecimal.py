import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoParaCifrar_bytes = bytes('He descubierto el error y no volveré a hacerlo mal ', 'UTF-8')
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')

nonce = b64decode('9Yccn/f5nJJhAt2S')



cipher = AES.new(clave, AES.MODE_GCM,nonce=nonce)

 
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoParaCifrar_bytes)

nonce_b64 = b64encode(cipher.nonce).decode('utf-8')
texto_cifrado_hex = texto_cifrado_bytes.hex()
tag_b64 =b64encode(tag).decode('utf-8')
mensaje_json = json.dumps({'nonce':nonce_b64, 'tag': tag_b64, 'texto cifrado':texto_cifrado_hex})
print(mensaje_json)

#Descifrado
print("----------- descifrado ------")
try:
    b64 = json.loads(mensaje_json)
    nonce_desc_bytes = b64decode(b64['nonce'])
    texto_cifrado_hex = texto_cifrado_bytes.hex()
    tag_desc_bytes = b64decode(b64['tag'])

    cipher = AES.new(clave, AES.MODE_GCM, nonce=nonce_desc_bytes)
    mensaje_des_bytes = cipher.decrypt_and_verify(texto_cifrado_bytes,tag_desc_bytes)
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 