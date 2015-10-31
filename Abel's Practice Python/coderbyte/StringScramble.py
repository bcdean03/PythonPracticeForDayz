__author__ = 'abelamadou'

def StringScramble(str1,str2):
    can = False
    for x in str2:
        can = x in str1
        if can==False:
            break
        else:str1 = str1.replace(x,"")
    return can

print(StringScramble("cdore","coder"), StringScramble("rkqodlw","world"))
# s = "Howdy"
# print("J"in s)
# a=raw_input("Entr name: ")
# print(a)