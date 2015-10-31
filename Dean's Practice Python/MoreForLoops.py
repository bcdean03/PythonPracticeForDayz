__author__ = 'Dean'
list1 = ['misty', 'mountains', 'cold']
list2 = ['misty', 'mountains', 'cod']
countForSame = 0
for i, x in zip(list1, list2):
    if i == x:
        countForSame+=1
else:
    if countForSame == len(list1):
        print "The lists are the same"
    else:
        print "The lists are not the same"



word = "hello"
for i in word: # i represents the actual item
    print i

for i in range(len(word)): # i represents the number
    print i