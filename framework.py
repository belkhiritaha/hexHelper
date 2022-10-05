from checksumCalculator import calculateCheckSum, lookForString
from remove_junk import removeJunk
from translateHex import translateHex


def main():
    while True:
        print("1. Calculate checksum")
        print("2. Remove junk")
        print("3. Translate hex file")
        print("4. Look for string")
        print("5. Exit")
        choice = input("Enter choice: ")


        if choice == "1":
            filename = input("Enter filename: ")
            calculateCheckSum(filename)
        
        elif choice == "2":
            filename = input("Enter filename: ")
            removeJunk(filename)

        elif choice == "3":
            filename = input("Enter filename: ")
            translateHex(filename)

        elif choice == "4":
            filename = input("Enter filename: ")
            string = input("Enter string: ")
            lookForString(filename, string)
        
        else:
            exit()
        




if __name__ == "__main__":
    main()
