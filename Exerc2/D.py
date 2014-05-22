#coding: utf-8

import A, C
from itertools import cycle
class D:

    a = 1
    s =""
    multiA = []   
    d1 = ""
    
    def __init__(self, d1):
        self.d1 = d1
    def getD1(self):
        return self.d1
    def setD1(self,v):
        self.d1 = v
    def addA(self, a):
        if isinstance(a,type(A)):
            self.multiA.append(a)
            return True
        else:
            return False
    def removeA(self,a):
        return self.multiA.remove(a)
        
    def iteratorA(self):
        if self.multiA:
            iteratorA = cycle(self.multiA)
            return iteratorA
    def SizeOfA (self,a):
        a = '493049494'
        return len(a)
    def ddddd(self, ddddd):
        s = D.d1 
        for a in self.multiA:
            s+= a.getB()+C.bbbbb()
        return s

class Teste(object):
    teste = D(10)
    teste.ddddd(ddddd=20.32)
