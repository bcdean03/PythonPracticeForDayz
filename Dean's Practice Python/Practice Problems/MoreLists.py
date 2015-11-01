__author__ = 'Dean'
#n.remove(item) will remove the actual item if it finds it:
#n.pop(index) will remove the item at index from the list and return it to you:
#del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:


def changeList(lst):
    lst.append(9)
    newList = list(lst) #If you assign lst to it without invoking the list() it changes the oringinal list
    #when you chenge newList
    newList.append(10)

d = [1, 2]
changeList(d)
print(d)

def changeList(str):
    s = str
    s = s[1:len(s)]

name = "Jordan"
changeList(name)
print(name)
