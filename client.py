import socket
# Initialise socket stuff
ip = "127.0.0.1"
port = 1234
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connection():
    # Connect to the server
    print("Sending server request...")
    try:
        s.connect((ip, port))
        print("Connection established successfully")
    except:
        print("Connection was unsucessful.")



while True:
    # Listen for a command
    prompt = input("\nEnter a command: ")
    if prompt[:4].upper() == "CONN":
        connection()
    elif prompt[:4].upper() == "UPLD":
        print("under construction!")
        # upld(prompt[5:])
    elif prompt[:4].upper() == "LIST":
        print("under construction!")
        # list_files()
    elif prompt[:4].upper() == "DWLD":
        # dwld(prompt[5:])
        print("under construction!")
    elif prompt[:4].upper() == "DELF":
        # delf(prompt[5:])
        print("under construction!")
    elif prompt[:4].upper() == "QUIT":
        # quit()
        print("under construction!")
        break
    else:
        print("Command not recognised; please try again")



