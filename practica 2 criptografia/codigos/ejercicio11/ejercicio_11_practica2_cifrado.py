from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os


#Cargar las claves
my_path = os.path.abspath(os.getcwd())
path_file_publ = my_path + "/clave-rsa-oaep-publ.pem"
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"

key_priv = RSA.importKey(open(path_file_priv).read())

key_publ = RSA.importKey(open(path_file_publ).read())


#Cifrado

msg = bytes.fromhex('e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72')

encryptor = PKCS1_OAEP.new(key_publ, SHA256)
encrypted = encryptor.encrypt(msg)

print("Cifrado:", encrypted.hex())
