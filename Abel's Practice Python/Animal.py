__author__ = 'abelamadou'
class Aninals(object):
    # __name=""  '''Don't need it'''
    # __sound=""
    # __owner=""
    # __age=0

    def __init__(self,n,s,o,a):
        self.__name=n
        self.__sound=s
        self.__owner=o
        self.__age=a
    def get_name(self):
        return self.__name
    def get_sound(self):
        return self.__sound
    def get_owner(self):
        return self.__owner
    def get_age(self):
        return self.__age
    def make_sound(self, amount):
        return self.__sound *amount
    def toString(self):
        return "{} is {} year old and say {}, owner is {}".format(self.__name,
                                                             self.__age,
                                                             self.__sound,
                                                             self.__owner)
