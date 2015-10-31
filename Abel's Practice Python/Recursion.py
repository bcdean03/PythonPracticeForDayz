__author__ = 'abelamadou'
def add_number(stng):
    if stng == 1:return 1
    else:return stng + add_number(stng-1)
print(add_number(5))