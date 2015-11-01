__author__ = 'Dean'
class Test(object):
    lets_test_class_var = []
    def __init__(self, num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

test1 = Test(1, 2, 3)
test2 = Test(2, 3, 4)

test1.lets_test_class_var.append(2)#mutable object changes both
print ("test2:", str(test2.lets_test_class_var))
'''
class Test(object):
    lets_test_class_var = 1
    def __init__(self, num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

test1 = Test(1, 2, 3)
test2 = Test(2, 3, 4)
print ("test1:", str(test1.lets_test_class_var))
print ("test2:", str(test2.lets_test_class_var))

test1.lets_test_class_var = 2
test2.lets_test_class_var = 1
print ("test1:", str(test1.lets_test_class_var))
print ("test2:", str(test2.lets_test_class_var))

Test.lets_test_class_var = 4 #Telling the class to change all
#doesnt work if you already changed it. My guess is it creates
#an instance method
print ("test1:", str(test1.lets_test_class_var))
print ("test2:", str(test2.lets_test_class_var))

Test.lets_test_class_var = 5
print ("test1:", str(test1.lets_test_class_var))
print ("test2:", str(test2.lets_test_class_var))
'''''