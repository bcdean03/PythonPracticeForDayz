__author__ = 'abelamadou'
# https://docs.python.org/2/library/thread.html
# http://effbot.org/zone/thread-synchronization.htm
# https://docs.python.org/2/library/threading.html#condition-objects
# http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
from threading import *
import time
import random

global items,c_for_m,lock_print,condition, n_smk, missing
missing=-1
n_smk=0
produced = False
c_for_m =Condition(RLock())
# lock_print = Lock()
c_for_prd = Condition(RLock())
c_for_smk = Condition(RLock())
# c_for_nxtr = Condition(RLock())
items= {0:"Paper",1:"Tabacco",2:"Lighter"}

class Producer (Thread):
    __rangeSet = 3
    missing = 0
    def run(self):
        while True:
            global n_smk
            time.sleep(1)
            with c_for_prd:
                if(n_smk == 3):
                    with c_for_smk:
                        self.getItemReady()
                        c_for_smk.notifyAll()
                        n_smk=0
                    c_for_prd.wait()
                    # with c_for_smk:
                    #     global n_smk
                    #     n_smk=0
                    # with lock_print: print "!!!Going to Reset Items!!!\n"
                    print("!!!Going to Reset Items!!!\n")
                    # with lock_m:lock_m.notifyAll()
                else:
                    # with lock_print: print ">>Waiting for Smokers to be ready<<"
                    print(">>Waiting for Smokers to be ready<<")
    def getItemReady(self):
        i1=random.randrange(0,self.__rangeSet)
        i2=i1
        while(i1==i2):
            i2=random.randrange(0,self.__rangeSet)
        # missing = filter(lambda x: x!=i1 and x!=i2, items)[0]
        with c_for_m:
            global missing
            missing = filter(lambda x: x!=i1 and x!=i2, items)[0]
            # with lock_print:
            print("Produced:",items.get(i1), items.get(i2))
            print("Missing:", items.get(missing))



class Smoker (Thread):
    def __init__(self,n,hI):
        Thread.__init__(self,name=n)
        self.haveI = hI
    def run(self):
      while True:
        with c_for_smk:
            global n_smk
            n_smk+=1
            # with lock_print:
            print("{} READY".format(self.name))
            c_for_smk.wait()
            # with lock_print:
            print("{} GOING TO TRY TO SMOKE".format(self.name))
            self.try_to_smoke()
    def try_to_smoke(self):
        with c_for_m:
            if(self.haveI == missing):
                # with lock_print:
                print("{} is Smoking".format(self.name))
                time.sleep(2)
                with c_for_prd: c_for_prd.notify()
                # lock_m.wait()
            else:
                # with lock_print:
                print("{} do not have missing Item".format(self.name))
                # with c_for_nxtr:c_for_nxtr.wait()
                # lock_m.wait()

    # pass

def driver():

    prd = Producer()
    smk1 = Smoker("Smk1",0)#Paper
    smk2 = Smoker("Smk2",1)#Tabaco
    smk3 = Smoker("Smk3",2)#Lighther
    smk1.start()
    smk2.start()
    smk3.start()
    prd.start()


    # lock_print.acquire()
    # condition.acquire()
    # try:
    #      print("Going to wait", lock_print.locked())
    #      # condition.notify()
    #      print("Come back", lock_print.locked())
    # finally:
    #     # lock_print.release()
    #     condition.release()
    # with lock_print:
    #     print("HHHHHH")


if __name__ == '__main__':
    driver()