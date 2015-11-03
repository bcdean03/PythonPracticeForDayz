__author__ = 'abelamadou'
import socket


def main():
    print socket.gethostbyname(socket.getfqdn())#get a the server address on this network
    # s = socket.socket()
    # # s.connect(("localhost",5002))#request a connection with the listening server
    # # s.connect(("10.1.10.18",5002))#request a connection with the listening server
    # s.connect(("192.168.1.141",5002))#request a connection with the listening server
    # # s.connect(("10.50.3.113",50002))#request a connection with the listening server
    # msg = raw_input("->",)
    # while msg != 'q':
    #     s.send(msg)#Send message down the socket to the server, (Takes the byte to send)
    #     data = s.recv(1024)#This will wait for data to come back from the server, and will grab buffer of 1024, (Takes a buffer length)
    #     print "Received from server:", str(data)
    #     msg = raw_input("->",)
    # s.close#Closes a socket/connection and frees the port


if __name__ == '__main__':
    main()

