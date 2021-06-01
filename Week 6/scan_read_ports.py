#!/usr/bin/python3
# A program to scan all TCP ports of a specified
# computer name. If a TCP connection is successful,
# try to read data from the other end and print it.
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

    # Set the timeout on the socket to one second
    # and create an address/port pair as a list
    sock.settimeout(1)
    server_address = (serverName, port)

    # Try to connect to localhost on that port.
    try:
        sock.connect(server_address)

    except:
        # The connection failed, do something
        pass
    
    # We got a TCP connect. Now attempt to read from
    # the connect. This will fail if we don't get any
    # data after one second. Start with no data.
    else:
        print("Connection on port %s, " % port, end= '')

	# Try to read up to 100 bytes of data
        try:
            data = sock.recv(100)

        except:
            # Nothing was read
            print("no received data")

        else:
            # Print out any received data. If nothing was
            # read, data will already be an empty string
            print("data: %s" % data)

	# Always close the open socket
        sock.close()
