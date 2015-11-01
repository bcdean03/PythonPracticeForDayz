__author__ = 'abelamadou'
import socket


def main():
    host = 'localhost'
    port = 50001 # have to be different because technicly setting up another server
    port = 0 #Port # of 0 means it will pick any free port that is currently on the computer
    server = ('localhost',5000)#Specify server sending to

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    msg = raw_input("->")
    while msg != 'q':
        s.sendto(msg,server)
        data, addr = s.recvfrom(1024) # receive from addr, data with size 1024
        print "Received from server:", str(data)
        msg = raw_input("->")
    s.close()



if __name__ == '__main__':
    main()