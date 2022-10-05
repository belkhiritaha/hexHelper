def translateHex(filename):
    # open file
    file = open(filename, "r")

    # read file
    lines = file.readlines()

    # close file
    file.close()

    # loop 2 chars at a time
    for line in lines:
        for i in range(0, len(line), 2):
            # get 2 chars
            hex = line[i:i+2]
            # convert to int
            dec = int(hex, 16)
            # convert to char
            char = chr(dec)
            # print char
            print(char, end='')
    
    