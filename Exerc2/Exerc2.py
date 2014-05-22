#coding: utf-8
import math

class A(object):
    a1 = ""
    def __init__(self, a1):
        self.a1 = a1
    def getA1(self):
        return self.a1
    def setA1(self, v):
        return self.a1 == v
        print "New String a1"
#    a1 = property(getA1, setA1)
        
a = A('Rafael')
print a.setA1('Rafael')
print a.getA1()

class B(object):
    b1 = 2
    int(b1)
    B = ""
    bbbb = ""
    def __init__(self, b1):
        self.b1 = b1
    def getB1(self):
        return self.b1
    def setB1(self, v):
        return self.b1 == v
        print "New int b1"
    def getproximoB(self):
        return self.B
    def setproximoB (self,v):
        return self.B == v
    def bbbb(self, bbbb):
        self.bbbb = bbbb
#    b1 = property(getB1, setB1)

b = B(3)
BB = B(4)
bbb = B(3)
print b.setB1(3)
print b.getB1()
print BB.setproximoB(4)
print BB.getproximoB()
print bbb.bbbb(0.2)


class C(B):
    c1 = 0.2
    float(c1)
    
    def __init__(self, c1):
        self.c1 = c1
    def getC1(self):
        return self.c1
    def setC1(self, v):
        return self.c1 == v
    def bbbb(self, bbbb):
        self.bbbb = bbbb
    
    if not (B.getproximoB) == "":
        str(c1) + str(bbbb)
    else:
        c1
class D:
    d1 = 0
    int(d1)
    
    def __init__(self, d1):
        self.d1 = d1
        
#agregação de A com B

#herança de B para C

#composição de D com C