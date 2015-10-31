__author__ = 'Dean'
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
'''
def average():#can be above or below doesnt matter like c++
    return grades_sum(grades)

def grades_sum(scores):
    return sum(grades)

def average():#can be above or below doesnt matter like c++
    return grades_sum(grades)

#print grades_sum(grades)
print average()


def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score)**2
    return variance/float(len(scores))

def grades_std_deviation(variance):
    return variance ** 0.5
print grades_variance(grades)

#list comprehension
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
print doubles_by_3

even_squares = [x**2 for x in range(1, 12) if x % 2 == 0]
print even_squares
'''''
'''
List slicing allows us to access elements of a list in a concise
manner. The syntax looks like this:
[start:end:stride]
Where start describes where the slice starts (inclusive), end is
where it ends (exclusive), and stride describes the space between
items in the sliced list.
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E']

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

my_list = range(1, 11)

# Add your code below!
backwards = my_list[-1:-11:-1]
print backwards

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

my_list = range(16)
my_list = filter(lambda x: x % 3 == 0, my_list) #My list doesnt change, returns a list
print my_list


languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python",languages)
print languages
#didnt change it, Read api it constructs a new list

cubes = [x**3 for x in range(1, 11)]
print cubes
print filter(lambda x: x % 3 == 0, cubes)

squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <=70, squares)

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[-1: -len(garbled)-1:-2]
print message

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x!='X' and x!='x', garbled)
print message

'''''