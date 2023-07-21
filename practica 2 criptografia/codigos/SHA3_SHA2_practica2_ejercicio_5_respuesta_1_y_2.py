import hashlib


#SHA2-256
m = hashlib.sha256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA256: " + m.digest().hex())

#SHA2-512
m = hashlib.sha512()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA512: " + m.digest().hex())


s = hashlib.sha3_256()


print(s.name)


print(s.digest_size)

s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","UTF-8"))

print(s.hexdigest())