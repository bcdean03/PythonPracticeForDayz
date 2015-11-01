__author__ = 'Dean'
my_dict = {'dean':25, 'Abel': 21, 'Jordan':22}
print my_dict.items()
print my_dict.keys()
print my_dict.values()

#   items() returns an array of tuples with
#each tuple consisting of a key/value pair from the dictionary:

#The keys() function returns an array of the dictionary's keys

#The values() function returns an array of the dictionary's values.

#   You can think of a tuple as an immutable (that is, unchangeable) list
#though this is an oversimplification); tuples are surrounded by
#()s and can contain any data type.
for key in my_dict:
    print key, my_dict[key]


prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill
'''
parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    print 'Parent {}'.format(parents)
    parents, babies = (babies, parents + babies)
    '''
weird, dollars, dean = (sum(i + i for i in range(0,4)),
                 sum(i+1 for i in range(0,4)),
                 "HEllo")
print dollars
print weird
print dean
