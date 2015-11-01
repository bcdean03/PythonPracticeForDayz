__author__ = 'Dean'
__author__ = 'Dean'
from threading import *
from random import randint
from time import sleep
import time
smoke_materials_counter, smoke_materials, lock_smoking = [0,0,0],\
                                                         {0: "Tobacco", 1: "Papers", 2: "Matches"},\
                                                         RLock()



class Producer(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("Hello")
        global lock_smoking
        while True:
            lock_smoking.acquire()
            self.produce_smokes()
            print("Ive produced as much as I can, need to sleep for at least 35 seconds... Im exhausted...")
            print(smoke_materials_counter)
            lock_smoking.release()
            sleep(35)

    def produce_smokes(self):
        global smoke_materials_counter
        for i in range(0,40):
            s = randint(0,2)
            smoke_materials_counter[s] +=1


class Smoker(Thread):
    globals()
    def __init__(self,name, unlim_item):
        Thread.__init__(self)
        self.name = name
        self.unlimited_item = [i for i in smoke_materials if smoke_materials[i] == unlim_item] # If the string is passed in is equal
        # to the value in the dictionary then return the number in which it was into the objecys variable

    def run(self):
        print("Hi im a smoker. My name is {}".format(self.name))
        while True:
            lock_smoking.acquire()
            self.attemptToSmoke()
            if smoke_materials_counter[0] == 0 and smoke_materials_counter[1]  == 0 and smoke_materials_counter[2]== 0:
                lock_smoking.release()
                time.sleep(2)
            else:
                lock_smoking.release()




    def attemptToSmoke(self):
        #better way to do this, but wanted to play with nested if's
        global smoke_materials_counter
        #print(self.unlimited_item)

        if self.unlimited_item[0] == 0:
            if smoke_materials_counter[1] > 0 and smoke_materials_counter[2] > 0:
                print(self.name + " is going to smoke. ")
                sleep(1)
                print(self.name + " is taking " + str(smoke_materials[1]) + " and " +
                      smoke_materials[2] + " to smoke.")

                smoke_materials_counter[1]-=1
                smoke_materials_counter[2]-=1
                print(smoke_materials_counter)
        elif self.unlimited_item[0] == 1:
            if smoke_materials_counter[0] > 0 and smoke_materials_counter[2] > 0:
                print(self.name + " is going to smoke. ")
                sleep(1)
                print(self.name + " is taking " + smoke_materials[0] + " and " +
                      smoke_materials[2] + " to smoke.")

                smoke_materials_counter[0]-=1
                smoke_materials_counter[2]-=1
                print(smoke_materials_counter)
        elif self.unlimited_item[0] == 2:
            if smoke_materials_counter[0] > 0 and smoke_materials_counter[1] > 0:
                print(self.name + " is going to smoke. ")
                sleep(1)
                print(self.name + " is taking " + smoke_materials[0] + " and " +
                      smoke_materials[1] + " to smoke.")

                smoke_materials_counter[0]-=1
                smoke_materials_counter[1]-=1
                print(smoke_materials_counter)


def start():
    prod = Producer("Dean")
    smoker1 = Smoker("smoker1", "Tobacco")
    smoker2 = Smoker("smoker2", "Matches")
    smoker3 = Smoker("smoker3", "Papers")

    smoker1.start()
    smoker2.start()
    smoker3.start()
    prod.start()

if __name__ == '__main__':
    start()
