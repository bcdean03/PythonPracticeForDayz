__author__ = 'abelamadou'

# https://www.youtube.com/watch?v=i1SW4q9yUEs
# import threading
# from random import randrange
# def pt(name,l):
#     print name,"Starting..."
#     while(l):
#         print name + ":",l.pop(randrange(0,len(l)))
#     print name,"Ended..."
#
# def main():
#    # print threading.active_count()
#    # print threading.activeCount()
#    count = 2
#    tup=[10,30,3,"M","A"]
#    for i in range(count):
#         t= threading.Thread(target=pt,args=("t"+str(i),tup))
#         t.start()
#     # pass
# if __name__ == '__main__':
#     main()

# https://www.youtube.com/watch?v=VO53cz-lleU
# import threading
# from threading import Thread, currentThread
# class pracT (Thread):
#     def run(self):
#         for _ in xrange(10):
#             print(currentThread().getName())
# t1 = pracT(name="t1:Sending message")
# t2 = pracT(name="t2:Resceiving message")
# t1.start()
# t2.start()
# t1 = pracT(name="t1:")
# t2 = pracT(name="t2:")
# t3 = pracT(name="t3:")
# t4 = pracT(name="t4:")
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()

# https://www.youtube.com/watch?v=4a777yQwj04&list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1
