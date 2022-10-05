def decodeHexFile(filename):
    output = []
    # open file
    file = open(filename, "r")

    # read file
    lines = file.readlines()

    # close file
    file.close()

    intelligible = []

    for line in lines:
        # check if type is 00
        if line[7:9] == "00":
            data = line[9:-3]
            for i in range(0, len(data), 2):
                # get 2 chars
                hex = data[i:i+2]
                # convert to int
                dec = int(hex, 16)
                # convert to char
                char = chr(dec)
                intelligible.append(char)
    return intelligible


def extractIntelligibleStrings(intelligible, n):
    strings = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(0, len(intelligible) - n):
        string = intelligible[i:i+n]
        if all(char in alphabet for char in string):
            strings.append(''.join(string))
    return strings


intelligible = decodeHexFile("firmware_tp3_v3.17.hex")
print(intelligible)
# print(' '.join(extractIntelligibleStrings(intelligible, 4)))