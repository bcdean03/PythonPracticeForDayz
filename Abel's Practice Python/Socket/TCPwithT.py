__author__ = 'abelamadou'
from threading import Thread
from socket import *

class Task(Thread):
    def __init__(self, n, skt):
        Thread.__init__(self, name=n)
        #first item in list goes to self.c, then the rest of the list goes to address
        self.c,self.addr = skt

    def run(self):
        print "Connection from > {} {}".format(self.name,str(self.addr))
        while True:
            data = self.c.recv(1024)#Going to receive some byte from the connection with max byte of 1024
            if not data:# c.recv will return false if the connection was closed
               print("!!!Ended connection with %s!!!"%(self.name))
               break
            print "Received:", str(data),"from(",self.name+")"
            data = str(data).upper()
            print "Sending:", str(data),"to(",self.name+")"
            self.c.send(data)
        self.c.close()

def main():
    # host = "localhost"
    host = "10.1.10.18"
    # host = "10.50.3.3"
    port = 5002
    s = socket()
    s.bind((host,port))
    s.listen(1)
    print 'Going to Start listening.........'
    cl = 0
    end = ''
    while True:
    # while end!='q':
        cl+=1
        Task("Client:%d"%(cl),s.accept()).start()
        # end = raw_input("Do you want to close the Socket!?")
    s.close()



if __name__ == '__main__':
    main()