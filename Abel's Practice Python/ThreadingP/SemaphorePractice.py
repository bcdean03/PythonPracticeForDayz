__author__ = 'abelamadou'
from threading import *
import time, random
global semaphore,bounded_S
semaphore,bounded_S = Semaphore(2),BoundedSemaphore(2)

class Producer(Thread):
    def run(self):
        for _ in xrange(3):
            # time.sleep(random.randrange(5))
            with bounded_S:#semaphore:
                print "...Producer Begin"
                time.sleep(5)
                print "...Producer End"
        print("!!!!!Producer TERMINATED!!!!!")

class Smoker(Thread):
    def run(self):
        while True:
            # time.sleep(random.randrange(5))
            with bounded_S: #semaphore:
                print "...{} Begin".format(self.name)
                time.sleep(3)
                print "...{} End".format(self.name)
            # time.sleep(2)

def main():
    p = Producer().start()
    s1 = Smoker(name="Smk1").start()
    s2 = Smoker(name="Smk2").start()
    s3 = Smoker(name="Smk3").start()




if __name__ == '__main__':
    main()