#coding: utf-8
import math
from itertools import cycle

class D:
    d1 = 2034.2334
    float(d1)
    a = 1
    d1t = [1,2,3,4]
    s =""
    ddddd = 20.29
    
    def __init__(self, d1):
        self.d1 = d1
    def getD1(self):
        return self.d1
    def setD1(self,v):
        self.d1 = v
    def addA(self, d1t):
        a = True
        d1t.append(a)
        return d1t
    def removeA(self, d1t):
        a = 1
        d1t.remove(a)
        return d1t
    def iteratorA(self, d1t):
        d1t=iter(d1t)
        return next(d1t)
    def SizeOfA (self,a):
        a = '493049494'
        return len(a)
    def ddddd(self, ddddd):
        s = D.d1 
        multiA = []   
        for a in multiA:
            s+= a.getB()+C.bbbbb()
        return s
class B:
    index = []
    bb = 203034.23
    def __init__(self, b1=False, newb=False):
        self.b1 = b1
        if newb!=False:
            self.index.append(newb)
           
    def getB1(self):
        return self.b1
    def setB1(self, v):
        self.b1 = v
    def getproximoB(self):
        if self.index:
            proximoB = cycle(self.index).next()
            return proximoB
    def setproximoB (self,v):
        b = B(False, v)
        if b:
            return True
        else:
            return False 
         
class C(B):
    def __init__(self, c1):
        self.c1 = c1
    def getC1(self):
        return self.c1
    def setC1(self, v):
        self.c1 = v
    def getD1(self):
        return self.d1
    def bbbbb(self):
        if not (B.getproximoB) == 0:
            return str(C.c1) + str(B.bbbbb)
        else:
            return str(C.c1)    
class A:
    b = B(1)
    def __init__(self, a1):
        self.a1 = a1
    def getA1(self):
        return self.a1
    def setA1(self, v):
        self.a1 = v
    def getB(self):
        return self.b
    a1= property(getA1, setA1)    
 
# class Teste(object):
#     a = A('Matheus') 
#     b = B(1, False)
# 
#     print "b1", b.getB1()
#     b.setB1(2)
#     b2 = B(3, False)
#     b.setproximoB(b2)
#     print "Proximo de B1", b.getproximoB()
    
#===============================================================================
# print 'Teste Classe D\n'
# a = D(5)
# print D.addA(a,D.d1t) , "/----> Adiciona o Elemento (5) na lista d1t"
# b = D(3)
# print D.iteratorA(b, D.d1t), "/----> Iterações da Lista D.d1t"
# c = D(1)
# print D.removeA(c, D.d1t) , "/----> Remove ELemento (1) da Lista d1t"
# d = D(493049494)
# print D.SizeOfA(d, b) , "/----> Tamanho do item"
# e = D(5)
# print D.ddddd(e, D.ddddd), "/----> Verificação de ddddd"
# print D.s ,"/---> teste for\n"
#===============================================================================
    
    