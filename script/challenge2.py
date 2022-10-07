# -*- coding: utf-8 -*-
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import cryptography
import os

def EncodeXor(tabMessage,tabKey):
    sortie=b""
    lk=len(tabKey)
    for i in range(len(tabMessage)):
        sortie+=(tabMessage[i] ^ tabKey[i%lk]).to_bytes(1,"big")
    return sortie

def DecodeXor(tabMessage,tabKey):
    return EncodeXor(tabMessage,tabKey)

def Indice(table,element):
    return table.index(element)

def EncodeBase64(tabMessage): #octets -> octets       #j'ai un \n en trop a la fin ???
    return base64.encodebytes(tabMessage).replace(b"\n",b"")

def DecodeBase64(strMessage): #ASCII UTF8 -> octets
    return base64.decodebytes(toTab(strMessage))

def EncodeAES_ECB(strMessage,tabKey): #str -> tab
    """ Chiffrement AES-ECB 128 bits de strMessage avec tabKey comme clef.
    La taille de chaine est quelconque et sera complétée par des
    caractères espace si nécessaire. tabKey est un tableau 16 éléments.
    Avant chiffrement la chaine est encodée en utf8 """
    padMessage=strMessage.ljust( (16*(len(strMessage)//16 + (not (len(strMessage)%16==0)))) , " ")
    #print (padMessage)

    tabMessage = toTab(padMessage)
    cipher = Cipher(algorithms.AES(bytes(tabKey)), modes.ECB(), cryptography.hazmat.backends.default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(tabMessage)
    #print (encrypted)
    return encrypted

def DecodeAES_ECB(tabMessage,tabKey): #tab -> tab
    """ Dechiffrement AES ECB de tabMessage. La clef tabKey est un tableau de 16 éléments.
        Retourne un tableau d'octets. Les caractères espace en fin de
        tableau sont supprimés."""

    cipher = Cipher(algorithms.AES(bytes(tabKey)), modes.ECB(), cryptography.hazmat.backends.default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(tabMessage)
    #print(decrypted) #print sans strip
    return decrypted.rstrip(b" ") #potentiellement juste strip

def Contient(aiguille,chaine):
    return aiguille in chaine

def EstImprimable(caractere):
    return caractere in """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """

def EstImprimableBytStr(chaine,charlist=b"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """):
    imprimable=True
    i=0
    while imprimable and i<len(chaine):
        imprimable=chaine[i] in charlist
        i+=1
    return imprimable

def Remplace(chaine,avant,apres):
    return chaine.replace(avant,apres)

def Extraire(chaine,separation,n):
    return chaine.split(separation)[n]

def Format(n):
    return str(n).rjust(4,"0")

def toTab(strMessage):
    return strMessage.encode("utf-8")

def toStr(strMessage):
    return strMessage.decode("utf-8")

def bruteXor(tabMessage,n,imprimable=b"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """):
    limp=len(imprimable)
    def genMot(k,n): #genere le Kième mot de longueur n
        mot=b""
        for i in range(n):
            mot+=bytes(imprimable[(k//(limp**i))%limp:(k//(limp**i))%limp+1])
        return mot

    for k in range(limp**n):
        currKey=genMot(k,n)
        #print(currKey)
        decoded=DecodeXor(tabMessage,currKey)
        #print(decoded)
        if EstImprimableBytStr(decoded,b"ABCDEF0123456789O.-"): #and decoded[:2]==b"ON":
            print(f"{decoded} |-| {currKey})")

def bruteXor2(tabMessage,n,imprimable=b"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """):
    possible = [imprimable for i in range(n)]
    def incMot (mot,possible):
        stop=False
        i=0
        while not stop:
            if mot[i] == possible[i][-1]:
                mot[i] = possible[i][-1]
            else:
                stop=True
            i+=1
        return mot


    for i in range(len(imprimable)):
        test = imprimable[i:i+1]*n
        decrypted = DecodeXor(tabMessage,test)
        for j in range(len(decrypted)):
            if not (decrypted[j] in imprimable):
                try: possible[j%n].remove(test[j%n])
                except: pass

    key=[possible[i][0] for i in range(n)]
    while True:
        decrypted = DecodeXor(tabMessage,key)
        print(f"{decrypted} |-| {key})")
        key=incMot(key,possible)



def fullMaj(chaine):
    charlist=b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    imprimable=True
    i=0
    while imprimable and i<len(chaine):
        imprimable=chaine[i] in charlist
        i+=1
    return imprimable



def smartBreakXor(tabMessage,known,n=None):    #necessite len(known) >= n     #n = longueur de clef si connue, sinon laisser vide
    """déchiffre le XOR a partir d'un mot connu"""
    if not n:
        for i in range(1,len(known)+1):
            smartBreakXor(tabMessage,known,i)
        return

    for start in range(len(tabMessage)-n+1):
        key=[0 for i in range(n)]
        for i in range(n):
            key[(i+start)%n]=tabMessage[start+i] ^ known[i]
        decoded=DecodeXor(tabMessage,key)
        if known in decoded: # and fullMaj(key):
            print(decoded,bytes(key))



def main():
    """ Tests, toutes les lignes sont correctes (résultat : True). Complèter les fonctions."""
    import sys
    #print (sys.version)

    print (EncodeXor("Bonjour".encode(),"A".encode())==b'\x03./+.43')
    print (DecodeXor(b"\n'..-","B".encode()).decode()=="Hello")
    print (EncodeXor(b"GoodBye",b"ABA")==b'\x06-.%\x008$')
    print (DecodeXor(b'\x0e42;8',b"ZWZ")=="Tchao".encode())
    print (Indice([1,2,3,4,5,6],3)==2)
    print (EncodeBase64(b"Une Chaine")==b"VW5lIENoYWluZQ==")
    print (DecodeBase64("VW5lIENoYWluZQ==")==b"Une Chaine")
    print (EncodeAES_ECB("Elements",[161, 216, 149, 60, 177, 180, 108, 234, 176, 12, 149, 45, 255, 157, 80, 136])==b'Z\xf5T\xef\x9f\x8bg\x15\xb3E\xe7&gm\x96\x1d')
    print (DecodeAES_ECB(b'Z\xf5T\xef\x9f\x8bg\x15\xb3E\xe7&gm\x96\x1d',[161, 216, 149, 60, 177, 180, 108, 234, 176, 12, 149, 45, 255, 157, 80, 136])==b"Elements")
    print (Contient("OK","Le resultat est OK !")==True)
    print (Contient("OK","Le resultat est Ok !")==False)
    print (EstImprimable("A")==True)
    print (EstImprimable("\x07")==False)
    print (EstImprimable(" ")==True)
    print (EstImprimableBytStr(b"Abcde")==True)
    print (EstImprimableBytStr(b"Abc\x07e")==False)
    print (EstImprimableBytStr(b"SALU A TOUS LAI ZAMI C TIBOPUTI POKEMON")==True)
    print (EstImprimableBytStr(b"Abcd\x07")==False)
    print (Remplace("Ceci est une string typique","string","chaine")=="Ceci est une chaine typique")
    print (Extraire("ROUGE,0034,4EF563",",",1)=="0034")
    print (Format(3)=="0003")
    print (Format(123)=="0123")
    print (toStr(b"\x41\x42")=="AB")
    print (toTab("CD")==b"\x43\x44")

    bruteXor(DecodeBase64("eXwEYXp8c21jBAMfY31xaH0="),10,b"""ABCDEFGHIJKLMNOPQRSTUVWXYZ""")
    #smartBreakXor(b"tyklW7ilEVS9LGi1GXKyxw==",b"ON00")#,14)
    #bruteXor2(EncodeXor(b"SALU-A-TOUS-LAI-ZAMI-C-TIBOPUTI-POKEMON",b"AZ8U"),4,b"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/_""")
    return

"""
if __name__ == '__main__':
    #print(EncodeXor(b"/ISIMA/SECRET_YIDIISTSA/CHALLENGE_1/DEFI_6/GROUPE_XX/LEDS/#",b"XORKEYDESPROFS"))
    main()"""
