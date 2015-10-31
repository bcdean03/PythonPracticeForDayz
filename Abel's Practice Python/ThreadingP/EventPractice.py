__author__ = 'abelamadou'
from threading import *
import time
global event
event = Event()
j = RLock()

class Producer(Thread):
    def run(self):
        while True:
            print "Going to set it"
            # time.sleep(1)
            event.set()
            event.clear()
            print "Cleared it"
            time.sleep(5)
            # event.set()

class Smoker(Thread):
    def run(self):
        while True:
            print "Waiting for Produce to notify me "
            event.wait()
            print "Done waiting"
            time.sleep(2)

def main():
    s = Smoker().start()
    p = Producer().start()




if __name__ == '__main__':
    main()