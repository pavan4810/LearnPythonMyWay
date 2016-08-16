"""
Notes: =========================================================================
Notes:  Tcp Client flow:
Notes:      > c = socket.socket(socket_family, socket_type)
Notes: 
Notes:      > c.connect(server hostname and port tuple)
Notes: 
Notes:      > c.send(data)
Notes:      > data = c.recv(size)
Notes: 
Notes:      > c.close()
Notes: 
"""
import socket

def Main():
    server = (socket.gethostname(), 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(server)
    print "Connected to: ", str(server)

    while True:
        try:
            sdata = raw_input("Enter data to be sent to server: >")
        except:
            print "Good Bye"
            exit(0)

        sdata = sdata.strip("\n\r")
        s.send(sdata)
        rdata = s.recv(1024)
        if not rdata:
            print "Connection closed by server:", str(addr)
            break

        print "Received data: ", str(rdata)
    
    c.close()

if __name__ == "__main__":
    Main()
