
def Xor(inp,key):
    sortie=["" for c in inp]
    lk=len(key)
    for i in range(len(inp)):
        sortie[i]=chr(ord(inp[i]) ^ ord(key[i%lk]))
    return sortie


def toCdecl(ch,prefix="char tab"):
    outp=list(ch)
    return prefix+"[{}]".format(len(outp)+1)+r"""="\x"""+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r"""";"""


if __name__ == '__main__':
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","F")))
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","5")))
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","F5")))
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","ZZ2_F5")))
    print (toCdecl(Xor("ZZ2_F5","F5")))