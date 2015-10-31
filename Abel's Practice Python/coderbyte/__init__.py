__author__ = 'abelamadou'
# from RunLength import RunLength
# print(RunLength("gggghhhh hdd  uuuaihhh h"))
# # http://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html

# self https://www.youtube.com/watch?v=M1BAlDufqao&index=33&list=PLFD32AF85033E6DDC
# def reverse_string(text):
#     newString = ""
#     for i in xrange(1,len(text)+1):
#         newString += text[-i]
#     return newString
#
# print reverse_string("hello abel")
#
# b = "23 L 1hello abel J"
# print(b[-len(b)])
#
# def reverse_string(text):
#     newString = ""
#     for i in range(-1, -len(text)-1, -1):
#         newString += text[i]
#     return newString
# print reverse_string("hello abel")

# l = [1,2,3,4,5,6,7,8,9,10]
# print l[0:len(l):2]
#
# def anti_vowel(text):
#     anti_vowel = ""
#     for i in range(len(text)):
#         if text[i].lower() != 'a' \
#             and text[i].lower() != 'e' \
#             and text[i].lower() != 'i' \
#             and text[i].lower() != 'o' \
#             and text[i].lower() != 'u':
#                 anti_vowel+= text[i]
#     return anti_vowel
# print(anti_vowel("aeiou"))

# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def scrabble_score(word):
#     total = 0
#     for i in word:
#         # if (i.lower() in score)== True:
#             total+= score[i.lower()] if (i.lower() in score) == True else 0
#     return total
#
# print(str(scrabble_score("Dean")))

# def censor(text, word):
#     return text.replace(word,"*"*len(word))
#
# print censor("you fuck", "fuck")


# def purify(list):
#     l =[]
#     for x in range(len(list)):
#         # if (list[x]%2 == 0):
#         l.append(list[x]) if (list[x]%2 == 0) else 0
#     return l
#
# lst = [1, 2, 3, 4, 5, 6]
# print(purify(lst))

# def purify(lst):
#     counter = 0
#     while(counter != len(lst)):
#         if lst[counter] % 2 != 0:
#             lst.remove(lst[counter])
#             counter = 0
#         else:
#             counter += 1
#     return lst
# lst = [1, 2, 3, 4, 5, 6]
# print(purify(lst))

# anonymous functions
# http://www.secnetix.de/olli/Python/lambda_functions.hawk
# cubes = range(3)#range(1,6,2) #[x*1 for x in range(1, 6)]
# m={"a":10,"b":23,}
# print cubes
# print filter(lambda x: x % 3 == 0, cubes)
# print reduce(lambda x, y: x + y, cubes)
# print(map(lambda x: m[x] + 10, m))
# def make_incrementor (n): return lambda x: x + n
# f = make_incrementor(2)
# g = make_incrementor(6)
# print f(42), g(42)
# print make_incrementor(22)(33)

# garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# message = filter(lambda x: x!='X' and x!='x', garbled)
# print message
# a = lambda x,y,z: x+y+z
# print(a(10,2,5) )


# def reverse_strings(x):
#      for i in reversed(x):
#         print (i + "\r")
#         print("Hdsdf")
#
#
# reverse_strings("hello abel")