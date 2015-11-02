__author__ = 'abelamadou'
from threading import *
from time import sleep
import random


smph,items,c_Agent,l_m,evt,missing,found_s = BoundedSemaphore(3),{0:"Paper",1:"Tabacco",2:"Lighter"},Condition(RLock()),RLock(),Event(),-1,False
rangeSet = 3
class Agent (Thread):

    def run(self):
        while True:
            with c_Agent:
                self.getItemReady()
                evt.set()
                c_Agent.wait()
                print "!!Found a Smocker!! Going to reset"
                sleep(3)

    def getItemReady(self):
        i1=random.randrange(rangeSet)
        i2=i1
        while(i1==i2):
            i2=random.randrange(rangeSet)
        with l_m:
            global missing,found_s
            found_s=False
            missing = filter(lambda x: x!=i1 and x!=i2, items)[0]
            print "Produced:",items.get(i1), items.get(i2)
            print "Missing:", items.get(missing)


class Smoker (Thread):
    def __init__(self,n,mItem):
        Thread.__init__(self,name=n)
        self.m_item=mItem

    def run(self):
        while True:
            with smph:
                print "{}[{}] going to wait for Producer to be ready".format(self.name,items[self.m_item])
                evt.wait()
                self.try_to_smoke()
            sleep(10)
    def try_to_smoke(self):
        with l_m:
            global found_s
            if(self.m_item == missing and not found_s):
                # with lock_print:
                print "{}[{}] is Smoking>>>>".format(self.name,items[self.m_item])
                evt.clear()
                found_s = True
                sleep(5)
                with c_Agent: c_Agent.notify()
            elif found_s==True:
                print "Already found a Smoker sorry:{}[{}]" .format(self.name,items[self.m_item])
            else:
                # print missing
                print "{}[{}] do not have missing Item".format(self.name,items[self.m_item])



def main():
    # smk1 = Smoker("Smk1",0).start()#Paper
    # smk2 = Smoker("Smk2",1).start()#Tabaco
    # smk3 = Smoker("Smk3",2).start()#Lighther
    # agt = Agent().start()
    # smk4 = Smoker("Smk4",0).start()#Paper
    # smk5 = Smoker("Smk5",1).start()#Tabaco
    # smk6 = Smoker("Smk6",2).start()#Lighther
    agt = Agent().start()
    i = 0
    while True:
        i+=1
        a = Smoker("SMK"+str(i),random.randrange(rangeSet)).start()
        sleep(random.randrange(10))





if __name__ == '__main__':
    main()