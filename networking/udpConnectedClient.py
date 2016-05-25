"""
Notes: =========================================================================
Notes: UDP Client flow (Connected sockets):
Notes: 
Notes:      > c = socket.socket(socket_family, socket_type)
Notes: 
Notes:      > c.bind(client_tuple)
Notes: 
Notes:      > c.sendto(data, server_tuple)
Notes:      > data, server_tuple = c.recvfrom(size)
Notes: 
Notes:      > c.close()
Notes: 
"""

import socket

def Main():
    client = ("127.0.0.1", 5001)
    server = ("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(client)

    while True:
        try:
            sdata = raw_input("Enter data to be sent to server: >")
        except:
            print "Good Bye"
            exit(0)
        else:
            sdata = sdata.strip("\n\r")

        print "Sending data to %s: %s" %(str(server), str(sdata))
        s.sendto(sdata, server)
        rdata, addr = s.recvfrom(1024)
        print "Received data from %s: %s" %(str(addr), str(rdata))
    
    c.close()

if __name__ == "__main__":
    Main()
