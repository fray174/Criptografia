from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets

salt = secrets.token_bytes(16)
master_secret = secrets.token_bytes(64)
print(master_secret.hex())
key1, key2, key3 = HKDF(master_secret, 32, salt, SHA512, 3)

print("Clave key1: ", key1.hex())
print("Clave key2: ", key2.hex())
print("Clave key2: ", key3.hex())

master_secret_practica = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")
salt_practica = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
key1_disp, key2_disp = HKDF(master_secret_practica, 32, salt_practica, SHA512, 2)

print("Clave Cifrado: ", key1_disp.hex())
print("Clave MAC: ", key2_disp.hex())
