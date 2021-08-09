#!/usr/bin/python3
# A program to scan all TCP ports of a specified
# computer name.
# (c) 2018 Warren Toomey, GPL3
#
import socket
import sys

# Set the server's name or IP that we will scan
serverName = "localhost"

# Loop over all possible TCP ports
for port in range(0,65536):

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Build the name/port pair used by connect()
    server_address = (serverName, port)

    try:
        # Try to connect to localhost on that port.
        sock.connect(server_address)

    except:
        # The connection failed, do something
        pass

    else:
        # The connection  was OK, close the connection
        print("Connection on port %s successful" % port)
        sock.close()
