import socket
import sys

serverName = "localhost" # Set the server or IP to scan


for port in range(0,65536): # Loop all TCP ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP socket
    server_address = (serverName, port) # Build the name/port pair used by connect()
    
    try:
        sock.connect(server_address) # Try to connect to localhost on that port.
    except:
        pass # The connection failed, do something

    else:
        print("Connection on port %s successful" % port)
        sock.close() # The connection  was OK, close the connection