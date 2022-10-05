def removeJunk(filename):
    output = []
    # open file
    file = open(filename, "r")

    # read file
    lines = file.readlines()

    # close file
    file.close()

    # calculate checksum
    for line in lines:
        #checksum = bytesSum(line)
        clean = line[9:-3]
        output.append(clean)

    # write to file
    file = open(filename, "w")
    file.writelines(output)
    file.close()