from checksumCalculator import calculateCheckSum, lookForString
from remove_junk import removeJunk
from translateHex import translateHex
from mqtt_subscribe import mqtt_subscribe
from mqtt_publish import mqtt_publish


def main():
    # publish
    mqtt_publish("user", "password", "172.16.32.7", 1884, "/ISIMA/S7_DH/GROUPE_LEGER_BELKHIRI/PublicKeyIoT", "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VuAyEA8YIWSn2teMxUPKLr4SWLiThJdyzRfO0kD8MARjKIcXY=\n-----END PUBLIC KEY-----", 100)

    # subscribe
    mqtt_subscribe("", "", "172.16.32.7", 1884, "/ISIMA/S7_DH/GROUPE_LEGER_BELKHIRI/PublicKeyServer")

    # while True:
        # print("1. Calculate checksum")
        # print("2. Remove junk")
        # print("3. Translate hex file")
        # print("4. Look for string")
        # print("5. Mqtt subscribe and listen")
        # print("6. Mqtt publish")
        # print("7. Exit")
#         # choice = input("Enter choice: ")
# 

        # if choice == "1":
            # filename = input("Enter filename: ")
#             # calculateCheckSum(filename)
#         
        # elif choice == "2":
            # filename = input("Enter filename: ")
#             # removeJunk(filename)

        # elif choice == "3":
            # filename = input("Enter filename: ")
#             # translateHex(filename)

        # elif choice == "4":
            # filename = input("Enter filename: ")
            # string = input("Enter string: ")
#             # lookForString(filename, string)

        # elif choice == "5":
            # user = input("Enter user: ")
            # passwd = input("Enter password: ")
            # server = input("Enter server: ")
            # port = int(input("Enter port: "))
            # topic = input("Enter topic: ")
#             # mqtt_subscribe(user, passwd, server, port, topic)
#         
        # elif choice == "6":
            # user = input("Enter user: ")
            # passwd = input("Enter password: ")
            # server = input("Enter server: ")
            # port = int(input("Enter port: "))
            # topic = input("Enter topic: ")
            # msg = input("Enter message: ")
            # iter = int(input("Nombre itération: "))
#             # mqtt_publish(user, passwd, server, port, topic, msg, iter)
#         
        # # else:
        #     exit()
        




if __name__ == "__main__":
    main()
