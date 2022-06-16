import socket
import sys

serverName = "localhost"

for port in range(0,65536):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    server_address = (serverName, port)
    try:
        sock.connect(server_address)
    except:
        pass
    else:
        print("Connection on port %s, " % port, end= '')
        try:
            data = sock.recv(100)
        except:
            print("no received data")
        else:
            print("data: %s" % data)
        sock.close()
