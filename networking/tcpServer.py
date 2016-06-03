"""
Notes: =========================================================================
Notes:  Tcp Server flow:
Notes:      > s = socket.socket(socket_family, socket_type)
Notes: 
Notes:      > s.bind(("hostname", portnumber))
Notes: 
Notes:      > s.listen(# of connections)
Notes: 
Notes:      > c.addr = s.accept()
Notes:      > data = c.recv(size)
Notes:      > c.send(data)
Notes:      > c.close()
Notes: 
Notes:      > s.close()
Notes: 
Notes:      socket.gethostname() returns hostname.
Notes: 
"""

import socket

def Main():
    # server is tuple of hostname/address string and integer port number
    server = (socket.gethostname(), 5000)

    # first argument = address family.
    # Second argument = socket type ; SOCK_STREAM, SOCK_DGRAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to the server address and port
    s.bind(server)

    # Listen and specify maximum concurrent incoming connections.
    s.listen(1)
    print "TCP Server started listening. Waiting for incoming connections ..."

    # Accept incoming connection and return connection id and client address.
    c,addr = s.accept()
    print "Connection received from: ", str(addr)

    while True:
        # Specify max data size to be received in one go.
        data = c.recv(1024)

        if not data:
            print "Connection closed by client :", str(addr)
            break

        print "Received data from %s: %s" %(str(addr), str(data))
        print "Sending data to %s: %s" %(str(addr), str(data))

        # Send data
        c.send(data)
    
    c.close()

if __name__ == "__main__":
    Main()
