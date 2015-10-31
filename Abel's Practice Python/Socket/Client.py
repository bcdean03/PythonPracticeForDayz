__author__ = 'abelamadou'
import socket


def main():

    s = socket.socket()
    s.connect(("localhost",5000))#request a connection with the listening server
    msg = raw_input("->",)
    while msg != 'q':
        s.send(msg)#Send message down the socket to the server, (Takes the byte to send)
        data = s.recv(1024)#This will wait for data to come back from the server, and will grab buffer of 1024, (Takes a buffer length)
        print "Received from server:", str(data)
        msg = raw_input("->",)
    s.close#Closes a socket/connection and frees the port


if __name__ == '__main__':
    main()

