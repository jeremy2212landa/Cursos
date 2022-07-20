#usr/bin/python3

from cryptography.fernet import Fernet

def writekey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyfile:
        keyfile.write(key)

def loadkey():
    return open("key.key", "rb").read()

writekey()
key = loadkey()

message ="test from python encrypt wih fernet".encode()
f = Fernet(key)
encrypted = f.encrypt(message)
print(f"{encrypted}")