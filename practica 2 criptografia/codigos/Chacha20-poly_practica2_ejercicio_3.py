from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:

    textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
    clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
    nonce_mensaje = get_random_bytes(12)
    datos_asociados = bytes('Datos no cifrados sólo autenticados', 'utf-8')
    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    cipher.update(datos_asociados)
    texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)
    mensaje_enviado = { "nonce": b64encode(nonce_mensaje).decode(),"datos asociados": b64encode(datos_asociados).decode(), "texto cifrado": b64encode(texto_cifrado).decode(), "tag": b64encode(tag).decode()}
    json_mensaje = json.dumps(mensaje_enviado)
    print("Mensaje: ", json_mensaje)


    decipher = ChaCha20_Poly1305.new(key=clave, nonce=b64decode(mensaje_enviado["nonce"]))
    datos_asociados_malo = bytes("Pedro me ha cambiado el mensaje","utf-8")
    decipher.update(datos_asociados)
    plaintext = decipher.decrypt_and_verify(b64decode(mensaje_enviado["texto cifrado"]),b64decode(mensaje_enviado["tag"]))
    print('Datos cifrados en claro = ',plaintext.decode('utf-8'))
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)