def bytesSum(line):
    sum = 0
    # add all bytes to sum
    for i in range(1,len(line)-2, 2):
        sum += int(line[i:i+2], 16)

    # convert to hex
    sum = hex(sum)

    # get least significant byte
    sum = sum[-2:]

    # get 2's complement
    hexAlphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    comp = int(hexAlphabet[15 - hexAlphabet.index(sum[0].upper())] + hexAlphabet[15 - hexAlphabet.index(sum[1].upper())], 16) + 1
    comp = hex(comp)

    # transform to upper
    comp = comp.upper()

    return comp[-2:]


def calculateCheckSum(filename):
    output = []
    # open file
    file = open(filename, "r")

    # read file
    lines = file.readlines()

    # close file
    file.close()

    # calculate checksum
    for line in lines:
        checksum = bytesSum(line)
        output.append(line[:-2] + checksum)

    # write to file
    file = open("hexFile.txt", "w")
    file.writelines(output)
    file.close()



def lookForString(filename, string):
    # open file
    file = open(filename, "r")

    # read file
    lines = file.readlines()

    # close file
    file.close()

    # translate string to hex
    hexString = ""
    for char in string:
        hexString += hex(ord(char))[2:]
    hexString = hexString.upper()

    print(string + " in hex: " + hexString)

    myDict = {}
    for line in lines:
        data = line[9:-3]
        if line[7:9] == "00":
            myDict[line] = data
        else:
            myDict[line] = ""

    # join all data
    data = ""
    for key in myDict:
        data += myDict[key]

    # look for string
    if hexString in data:
        print("String found!")
        for key in myDict:
            if hexString in myDict[key]:
                print(key)
    else:
        print("String not found!")