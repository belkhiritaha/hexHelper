from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey

#################################################################################################
#################################################################################################
#           DIFFIE-HELLMAN ALGORITHM ( KEY EXCHANGE ) BASED ON DISCRETE LOGARITHM               #
#                               Author : C. Tilmant ( 2019 )                                    #
#################################################################################################
#################################################################################################


#################################################################################################
# Alice : Send Public Information for Key Exchange Request to the server ( publish g, p and A ) #
#################################################################################################

# Generate some parameters form the Diffie-Hellman key exchange
g = 5
Key_Size = 512

#Alice_parameters     = dh.generate_parameters(generator=g, key_size=Key_Size,backend=default_backend())  # a new instance of DHParameters
#Alice_parameters_num = Alice_parameters.parameter_numbers()                                              # a new instance of DHParametersNumbers

Alice_private_key = X25519PrivateKey.generate() # a new instance of DHPrivateKey
Alice_public_key  = Alice_private_key.public_key() # a new instance of DHPublicKey

A_public_key  = Alice_public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
A_private_key = Alice_private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())

# Display Public and Private information from Alice
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Public Information from Alice and send to Bob : ")
print("------------------------------------------------")
#print("\t - Generator (g)    : ", Alice_parameters_num.g)
#print("\t - Prime number (p) : ", Alice_parameters_num.p)
print("\t - Public Key (A)   : \n", A_public_key.decode('utf-8'))

print("Private Information from Alice : ")
print("------------------------------------------------")
print("\t - Private Key (a)  : \n", A_private_key.decode('utf-8'))

#################################################################################################
# Bob : Receive Public Information from Alice and compute public and private information (b, B) #
#################################################################################################

#Exchange_parameters  = dh.DHParameterNumbers(Alice_parameters_num.p, Alice_parameters_num.g)  # a new instance of DHBackEnd
#Bob_parameters       = Exchange_parameters.parameters(default_backend())                      # a new instance of DHParameters
#Bob_parameters_num   = Bob_parameters.parameter_numbers()                                     # a new instance of DHParametersNumbers

Bob_private_key = X25519PrivateKey.generate() # a new instance of DHPrivateKey
Bob_public_key  = Bob_private_key.public_key()          # a new instance of DHPublicKey

B_public_key  = Bob_public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
B_private_key = Bob_private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())

# # Display Public and Private information from Alice
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Public Information from Bob and send to Alice : ")
print("------------------------------------------------")
#print("\t - Generator (g)    : ", Bob_parameters_num.g)
#print("\t - Prime number (p) : ", Bob_parameters_num.p)
print("\t - Public Key (B)   : \n", B_public_key.decode('utf-8'))

print("Private Information from Bob : ")
print("------------------------------------------------")
print("\t - Private Key (b)  : \n", B_private_key.decode('utf-8'))

#################################################################################################
# Alice and Bob : Compute Shared Key                                                            #
#################################################################################################

# Deserialization of public key of Alice for Bob ( A )
Alice_Public_Key_For_Bob = serialization.load_pem_public_key(bytes(A_public_key),backend=default_backend())

# Deserialization of public key of Bob for Alice ( B )
Bob_Public_Key_For_Alice = serialization.load_pem_public_key(bytes(B_public_key),backend=default_backend())

# Display Public key of Alice and Bob
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Public keys of Alice and Bob : ")
print("------------------------------------------------")
print("Same Keys between sending and receiving ? ", A_public_key == Alice_Public_Key_For_Bob.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo) )
print("\t - Reading of public key of Alice by Bob : \n", Alice_Public_Key_For_Bob.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('utf-8'))
print("Same Keys between sending and receiving ? ", B_public_key == Bob_Public_Key_For_Alice.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo) )
print("\t - Reading of public key of Bob by Alice : \n", Bob_Public_Key_For_Alice.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('utf-8'))

# Compute the shared secret for the key exchange
Alice_Shared_Key = Alice_private_key.exchange(Bob_public_key)
Bob_Shared_Key   = Bob_private_key.exchange(Alice_public_key)

# Display Shared Key
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Shared Secret between Alice and Bob : ")
print("------------------------------------------------")
print("\t - Shared Key compute by Alice : ", Alice_Shared_Key.hex())
print("\t - Shared Key compute by Bob   : ", Bob_Shared_Key.hex())