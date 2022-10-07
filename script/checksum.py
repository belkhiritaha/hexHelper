
def hexInt(a):
    return (int(a,16))

def hex2bin (name):
    f = open(name, 'r')
    s = f.read()
    f.close()


    #length=bin[0]
    #address=bin[1:3]
    #type=bin[3]
    #data=bin[4:4+length]
    #checksum=bin[-1]

    lines=s.split("\n")
    data=[]
    for l in lines:
        if len(l)>=9 and l[7]==l[8]=="0":
            data+=list(map(hexInt,l[9:-2]))

    datapaire=[]
    for i in range(0,len(data),2):
        datapaire+=[data[i]*16+data[i+1]]

    return datapaire

def extraitText (name,n=5):
    data=hex2bin(name)
    affichable=list(range(32,127))#+list(range(128,155))

    deb=0
    fin=0

    strlist=[]
    s=""

    for i in range(len(data)):
        if data[i] in affichable:
            pass
        else:
            #print(f"{deb} {fin}")
            if (fin-deb)>n:
                for j in range(deb,fin):
                    s+=chr(data[j])
                strlist+=[s]
                s=""
            deb=fin+1
        fin+=1

    if (fin-deb)>n:
        for j in range(deb,fin):
            s+=chr(data[j])
        strlist+=[s]

    return strlist



name=r"P:\TP\ZZ2\Securite Systemes Embarques\Python\mqtt_connection\programme_reference.ino.hex"
#name=r"P:\TP\ZZ2\Sécurité Systèmes Embarqués\Python\mqtt_connection\tibolemoch.hex"

def checksumstr(s):
    somme=0
    for i in range(1,len(s)-2,2):
        somme+=int(s[i:i+2],16)
    somme=256-somme%256

    somme=hex(somme)
    somme=somme[2:].upper()

    if int(somme,16)<16:
        somme="0"+somme

    return s[:-2]+somme

def checksumfile(fname):
    f=open(fname,"r")
    txt=f.read()
    f.close()
    lines=txt.split("\n")
    fin=""
    atm=0
    for l in lines:
        l[3:7]=hex(atm)
        fin+=checksumstr(l)+"\n"
        atm+=(len(l)-1)/2

    f=open(fname,"w")
    f.write(fin[:-1])
    f.close()

