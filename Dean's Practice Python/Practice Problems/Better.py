__author__ = 'abelamadou'


class Better:
    def __init__(self,**kvargs):
        self._attribute = kvargs
    def set_attributes(self,key,value):
        self._attribute[key] = value
    def get_attributes(self,key):
        return self._attribute.get(key,None)
    def get_couple_attributes(self,*args):
        if args:
            rV=[]
            for x in args:
                # print x,self._attribute.get(x,None)
                rV.append(self._attribute.get(x,None))
            # pass
            return rV
        else: print("Pass in arguments")
    def toString(self):
        sA=""
        for x in self._attribute:
            sA+="|<Key:{}; Value:{}>|".format(x,self._attribute[x])
        return sA




def main():
    b = Better(Mike=10, __Joe="14", __Abel=(1,"2",3,"4"))
    b.toString()
    print b._attribute
    print "Joe: " + str(b.get_attributes("__Joe"))
    print b.__class__
    # a,b= b.get_attributes('Mike'),b.get_attributes('__Abel')
    a = b.get_couple_attributes('Mike',"__Joe","__Abel")
    print(a)

def testing():
    pass

if __name__ == '__main__':
    main()
    #testing()