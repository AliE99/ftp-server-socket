import socket
import time
import struct
from _thread import *

ip = "127.0.0.1"
port = 1234
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
print(f"\nServer binded on ip: {ip} and port: {port}")

s.listen(1)
print(f"\nServer listening, waiting for connections...")

clientsocket, address = s.accept()
print(f"\nConnected to by address: {address}")


def upload():
    clientsocket.send("1".encode())
    file_size = struct.unpack("i", clientsocket.recv(4))[0]
    # Initialise and enter loop to recive file content
    start_time = time.time()
    output_file = open('received.jpg', "wb")
    # This keeps track of how many bytes we have recieved, so we know when to stop the loop
    bytes_recieved = 0
    print("\nStart recieving the file:\n")
    chunk_number = 0
    while bytes_recieved < file_size:
        l = clientsocket.recv(buffer_size)
        print(f"Chunk {chunk_number} is Received...")
        chunk_number += 1
        output_file.write(l)
        bytes_recieved += buffer_size
    output_file.close()
    print("\nRecieved file: {}".format('received.jpg'))
    # Send upload performance details
    clientsocket.send(struct.pack("f", time.time() - start_time))
    clientsocket.send(struct.pack("i", file_size))
    return



while 1:
    (clientConnetion, addr) = clientsocket.accept()
    start_new_thread(upload, (clientConnetion, addr))
    threadCounter = threadCounter+1
    print()
    print("Client "+str(threadCounter) + " is  Connected ")
    print()
