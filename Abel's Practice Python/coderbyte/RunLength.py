__author__ = 'abelamadou'

def RunLength(strg):
    print("Original word: {}".format(strg))
    D = {}
    for x in strg:
        if D.has_key(x):
            D[x]=D[x]+1
        else:
            D.update({x:1})
            # D[x]=1
    P=""
    for x in D:
        P+= str(D.get(x)) + x    #http://www.pitt.edu/~naraehan/python2/data_types_conversion.html
    return "RunLength: {}".format(P)

print RunLength("jjjssiikkk")

