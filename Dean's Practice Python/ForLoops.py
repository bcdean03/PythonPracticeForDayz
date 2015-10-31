__author__ = 'Dean'
'''
from random import randint

list = [1, 2, 3, 4, 5, 6]
for i in list:
    print i
print
for i in range(len(list)):
    print list[i]
print
for i in range(20):
    print(i)
'''
'''
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:#This one iterates through the two sublists
        for num in numbers:#This one iterates through the sublist because numbers referes to the those two sublists
            results.append(num)
    return results

print flatten(n)


int() to convert the string to an integer.
'''
'''
board = []
for i in range(5):
    board.append(["O"]*5)
for i in board:
    print i

letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)
'''
'''
enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go
through the loop, index will be one greater, and item will be the next item in the sequence.

choices = ['pizza', 'pasta', 'salad', 'nachos']
moreChoices = ['pizza', 'pasta', 'salad', 'breakdsticks']
print 'Your choices are:'


zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

for i, x in zip(choices, moreChoices):
    if x == i:
        print("choices and more choices both want: " + x)

for index, item in enumerate(choices):
    print index+1, item

n this case, the else statement is executed after the for, but only if the
for ends normally—that is, not with a break.
'''

word = "hello"
for i in word:
    print i

for i in range(len(word)):
    print i

