__author__ = 'abelamadou'
from threading import *
import time
global event
event = Event()

class Producer(Thread):
    def run(self):
        for _ in xrange(2):
            print "Producer Going to set it"
            # time.sleep(1)
            event.set()
            event.clear()
            print "Producer Cleared it"
            time.sleep(3)
            # event.set()
        print("!!!Producer TERMINATING!!!")

class Smoker(Thread):
    def run(self):
        while True:
            print "{} Waiting for Producer to notify me".format(self.name)
            event.wait()
            print "{} Done waiting".format(self.name)
            time.sleep(2)

def main():
    s1 = Smoker(name="Smk1").start()
    s2 = Smoker(name="Smk2").start()
    p = Producer().start()




if __name__ == '__main__':
    main()