__author__ = 'abelamadou'
'''User Datagram Protocol (UDP):
    *Un-Reliable Connection-less based protocol
        >Never actually connect with the other devices, it purley sends data off to an address whether their is a computer there or not
        >No guarantee that the data will get to the other device
        >If it is lost in the Internet it is lost forever
    *It is verry fast
        >Great for real time software like: VOIP, Online Games, Streaming
    *Don't listen and accept connection, because their is no connection happening here
        just receiving data and sending data
'''
# https://www.youtube.com/watch?v=XiVVYfgDolU
# https://www.youtube.com/watch?v=PkfwX6RjRaI
import socket
import time

def main():
    host = 'localhost'
    port = 5000
    s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#(Need to pass in the family and the socket type)
    s.bind((host,port))
    # s.setblocking(0)#Set socket to nonblocking: This means whenever it tries to receive from, it will not block,
                    #it is going to try to receive data from the stream. If nothing there, it will throw an erro
    print("Server starting.......")

    while True:
        # If used 'setblocking'
        # try:
        #     data, addr = s.recvfrom(1024)
        #     print "Message from: ", str(addr)
        #     print"From connect user:", str(data)
        #     data = str(data).upper()
        #     print 'Sending:', str(data)
        #     s.sendto(data, addr)#(Takes data you want to send, and the addr you want to send to), because UDP is not connected all the time, thus why need to specifie who sending to
        # except:
        #     print "Received Nothing"
        #     time.sleep(2)
        data, addr = s.recvfrom(1024)
        print "Message from: ", str(addr)
        print"From connect user:", str(data)
        data = str(data).upper()
        print 'Sending:', str(data)
        s.sendto(data, addr)#(Takes data you want to send, and the addr you want to send to), because UDP is not connected all the time, thus why need to specifie who sending to
    s.close()
if __name__ == '__main__':
    main()