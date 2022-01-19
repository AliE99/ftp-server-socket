import socket
import os
import struct

# Initialise socket stuff
ip = "127.0.0.1"
port = 1235
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

messages = []


def connection():
    # Connect to the server
    print("Sending server request...")
    try:
        s.connect((ip, port))
        print("Connection established successfully")
    except:
        print("Connection was unsucessful.")


def upload(file_name):
    # Upload a file
    print("\nUploading file: {}...".format(file_name))
    try:
        # Check the file exists
        content = open(file_name, "rb")
    except:
        print("Couldn't open file. Make sure the file name was entered correctly.")
        return
    try:
        s.recv(buffer_size)
        s.send(struct.pack("i", os.path.getsize(file_name)))
    except:
        print("Error sending file details")
    try:
        # Send the file in chunks defined by BUFFER_SIZE
        # Doing it this way allows for unlimited potential file sizes to be sent
        chunk_number = 0
        l = content.read(buffer_size)
        print("\n Start sending the file:\n")
        while l:
            s.send(l)
            message = f"Chunk {chunk_number} is sent..."
            messages.append(message)
            print(message)
            chunk_number += 1
            l = content.read(buffer_size)
        content.close()
        # Get upload performance details
        upload_time = struct.unpack("f", s.recv(4))[0]
        upload_size = struct.unpack("i", s.recv(4))[0]
        print("\nSent file: {}\nTime elapsed: {}s\nFile size: {}b".format(
            file_name, upload_time, upload_size))
    except:
        print("Error sending file")
        return
    return


def getClientMessages():
    return messages


def startClient():
    while True:
        connection()
        print(os.path.join(os.path.dirname(os.path.dirname(__file__)), "icon.jpg"))
        upload(os.path.join(os.path.dirname(os.path.dirname(__file__)), "icon.jpg"))

        prompt = input("\n")
