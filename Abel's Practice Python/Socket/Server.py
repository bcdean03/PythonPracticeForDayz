__author__ = 'abelamadou'
# https://www.youtube.com/watch?v=XiVVYfgDolU
import socket
'''TCP:
    *Transmision Control Protocol
    *Reliable Connection based Protocol
        >Forms connection with the other device and keeps the connection going until it's closed
        >If piece of Data is lost through the internet, the protocol will organize the data to be re-sent
    *Ordered & Error checked (simple checksum)
       >Also checks if the data is corrupt and arrived in an ordered manner
    *Used by Web Browsers, Email, SSH,FTP etc...
    *Slower then other protocols, because of all the checking and making sure all the datas are there
'''

def main():
    host = "localhost"
    port = 5000
    s=socket.socket()#Create new socket object
    s.bind((host,port))#takes a tuple of host and port
    s.listen(2)#Tell server to start listening for connection (# of connection want to listen to at a time)
    c,addr = s.accept() #returns a connection witch is a new Socket and the address; Accepts a connectoin when found/ returns new socket obj
    # (client,(ip,port))= s.accept()
    print "Connection from: {}".format(str(addr))
    d,ad = s.accept()
    print "Connection from: {}".format(str(ad))
    while True:
        data = c.recv(1)#Going to receive some byte from the connection with max byte of 1024
        if not data:# c.recv will return false if the connection was closed
            break
        print "Received:", str(data)
        data = str(data).upper()
        print "Sending: ", str(data)
        c.send(data)
    c.close()



if __name__ == '__main__':
    main()

