__author__ = 'Dean'
class GrandFather(object):
    def poop(self):
        print "poop"

class Father(GrandFather):
    def hello_world(self):
        print "hello"

class Child(Father):
    def lets_try(self):
        print "trying"

child = Child()
child.lets_try()
# child inherits from Grandfather and father and object
# no overloading in python, but there is overriding in inheritnace