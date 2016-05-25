"""
Notes: =========================================================================
Notes:  Tcp Server flow:
Notes:      > s = socket.socket(socket_family, socket_type)
Notes: 
Notes:      > s.bind(("hostname", portnumber))
Notes: 
Notes:      > data, client_tuple = s.recvfrom(size)
Notes:      > s.sendto(data, client_tuple)
Notes: 
Notes:      > s.close()
Notes: 
"""
import socket

def Main():
    server = ("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(server)

    while True:
        data, addr= s.recvfrom(1024)
        print "Data received from: ", str(addr)
        print "Received data: ", str(data)
        print "Sending data: ", str(data)
        s.sendto(data, addr)
    
    c.close()

if __name__ == "__main__":
    Main()
