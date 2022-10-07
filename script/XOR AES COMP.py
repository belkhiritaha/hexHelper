import random
from chiffrement_xor import *
import base64
#from Crypto.Cipher import AES
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import cryptography

n=16

clefXOR = "tbpy"

clefAES = b"TiboLaPUttYpuTTy"
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(clefAES), modes.CBC(iv), cryptography.hazmat.backends.default_backend())
encryptor = cipher.encryptor()



alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

payload = [ (not(i%2))*"ON"+(i%2)*"OFF" + str(i).rjust(4,"0") + "".join([random.choice(alphabet) for j in range(8)]) for i in range(n)]
payloadXor = [base64.b64encode(("".join(Xor(p,clefXOR))).encode("ascii")).decode("ascii") for p in payload]
payloadAes = [base64.b64encode(encryptor.update((p.ljust(16,"0")).encode("ascii"))).decode("ascii") for p in payload]

decryptor = cipher.decryptor()
decryptedAES = [decryptor.update(base64.b64decode(p)) for p in payloadAes ]
decryptedXOR = ["".join(Xor(base64.b64decode(p).decode("ascii"),clefXOR)) for p in payloadXor ]

for i in range(n):
    print(f"Payload : {payload[i]}  ,PayloadXor : {payloadXor[i]} ,DecryptedXor : {decryptedXOR[i]} ,PaylaodAES : {payloadAes[i]}, DecryptedAES : {decryptedAES[i]}")
