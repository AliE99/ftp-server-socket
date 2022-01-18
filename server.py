import socket


ip = "127.0.0.1"
port = 1234
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
print(f"\nServer binded on ip: {ip} and port: {port}")

s.listen(5)
print(f"\nServer listening, waiting for connections...")

clientsocket, address = s.accept()
print(f"\nConnected to by address: {address}")

while True:
    # Enter into a while loop to recieve commands from client
    print("\n\nWaiting for instruction")
    data = clientsocket.recv(buffer_size)
    print("\nRecieved instruction: {}".format(data))
    # Check the command and respond correctly
    if data == "UPLD":
        print('upload')
        # upld()
    elif data == "LIST":
        print('list')
        # list_files()
    elif data == "DWLD":
        print('download')
        # dwld()
    elif data == "DELF":
        print('delete')
        # delf()
    elif data == "QUIT":
        print('quit')
        # quit()
    # Reset the data to loop
    data = None
