__author__ = 'Dean'
'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for i in word:
        for key in score:
            if i == key:
                total+= score[key]
    return total

print(str(scrabble_score("Dean")))
'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
'''
def scrabble_Score(word):
    total = 0
    for i in word:
        if (i.lower() in score)== True:
            total+= score[i.lower()]
    return total

def scrabble_score(word):
    total = 0
    for i in word:
            total+= score[i.lower()] if (i.lower() in score)== True else 0
    return total

def censor(text, word):
    return text.replace(word,"*"*len(word))

print censor("you fuck", "fuck")


def purify(lst):
    counter = 0
    while(counter != len(lst)):
        if lst[counter] % 2 != 0:
            lst.remove(lst[counter])
            counter = 0
        else:
            counter += 1
    return lst

lst = [1, 2, 3, 4, 5, 6]
print pop_out_lists(lst)


def product(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst.pop() * product(lst)

lst = [1, 2, 3, 4]
print product(lst)
'''''
'''
def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    new_lst.sort()
    return new_lst

lst = [3, 4, 2, 1, 1, 2, 2, 3, 3, 4,  4, 5, 5,6, 6]
print remove_duplicates(lst)

'''
'''
def purify(list):
    l =[]
    for x in range(len(list)):
        l.append(list[x]) if (list[x]%2 == 0) else 0
    return l

def purify(lst):
    counter = 0
    while(counter != len(lst)):
        if lst[counter] % 2 != 0:
            lst.remove(lst[counter])
            counter = 0
        else:
            counter += 1
    return lst

lst = [1, 2, 3, 4, 5, 6]
print(purify(lst))
'''
from math import ceil
def median(lst):
    median = len(lst) / float(2)
    print("median: " + str(median))

    if median - int(median) != 0:
        return lst[int(median)]
    else:
        return (lst[int(median)] + lst[int(median)-1])/float(2)

def create_list(*arg):
    lst = list(arg)
    lst.sort()
    print("lst: " + str(lst))
    return lst


print median(create_list(6, 8, 12, 2, 23))
#print create_list(1, 2, 3, 4, 5)


