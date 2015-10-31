__author__ = 'abelamadou'
def FirstReverse(str):
    a = ""
  # code goes here
    for x in xrange (len(str)):
        a+=str[(len(str)-1)-x]

    return a
# keep this function call here
# to see how to enter arguments in Python scroll down
print (FirstReverse("I Love Coding"))