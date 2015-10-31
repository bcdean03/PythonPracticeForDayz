__author__ = 'Dean'
'''
the else block will execute anytime the loop condition is evaluated to False. This means
that it will execute if the loop is never entered or if the loop exits normally.
If the loop exits as the result of a break, the else will not be executed.
'''
count = 0
while count != 5:
    print count
    count += 1
else:
    print "hello"