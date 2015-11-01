__author__ = 'abelamadou'
# https://docs.python.org/2/library/thread.html
# http://effbot.org/zone/thread-synchronization.htm
# https://docs.python.org/2/library/threading.html#condition-objects
'''

In Python 2.5 and later, you can also use the with statement.
When used with a lock, this statement automatically acquires
the lock before entering the block, and releases it
when leaving the block:
'''
from threading import *
import time
import random

global items,c_for_m,lock_print,condition, n_smk, missing
missing, n_smk, produced, c_for_m, c_for_prd, c_for_smk, items=-1,\
                                                                0,\
                                                                False,\
                                                                Condition(RLock()),\
                                                                Condition(RLock()),\
                                                                Condition(RLock()),\
                                                                {0:"Paper",1:"Tabacco",2:"Lighter"}

class Producer (Thread):
    __rangeSet = 3
    missing = 0
    def run(self):
        while True:
            global n_smk #Number of smokers ready to smoke, abel thinks. Global refers to
                        #All smokers need to be ready for the agent to smoke.
            time.sleep(1)

            with c_for_prd:#smart try catch to grab the lock# condition for producer
                if(n_smk == 3):
                    print " viiiiiiiiiiiiiiiiiisssiiinollllle "+ str(c_for_smk.acquire())
                    c_for_smk.release()
                    with c_for_smk:
                        self.getItemReady()
                        c_for_smk.notifyAll()
                        n_smk=0
                    c_for_prd.wait()
                    print "!!!Going to Reset Items!!!\n"
                else:
                    print ">>Waiting for Smokers to be ready<<"
    def getItemReady(self):
        i1=random.randrange(0,self.__rangeSet)
        i2=i1
        while(i1==i2):
            i2=random.randrange(0,self.__rangeSet)
        with c_for_m:
            global missing
            missing = filter(lambda x: x!=i1 and x!=i2, items)[0]
            print "Produced:",items.get(i1), items.get(i2)
            print "Missing:", items.get(missing)



class Smoker (Thread):
    def __init__(self,n,hI):
        Thread.__init__(self,name=n)
        self.haveI = hI
    def run(self):
      while True:
        with c_for_smk:
            global n_smk
            n_smk+=1
            print "{} READY".format(self.name)
            c_for_smk.wait()
            print "{} GOING TO TRY TO SMOKE".format(self.name)
            self.try_to_smoke()
    def try_to_smoke(self):
        with c_for_m:
            if(self.haveI == missing):
                print "{} is Smoking".format(self.name)
                time.sleep(2)
                with c_for_prd: c_for_prd.notify()
            else:
                print "{} do not have missing Item".format(self.name)

def driver():

    prd = Producer()
    smk1 = Smoker("Smk1",0)#Paper
    smk2 = Smoker("Smk2",1)#Tabaco
    smk3 = Smoker("Smk3",2)#Lighther
    smk1.start()
    smk2.start()
    smk3.start()
    prd.start()

if __name__ == '__main__':
    driver()