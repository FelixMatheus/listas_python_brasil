#coding: utf-8
import math

class A:
    a1 = 'Rafael'
    def __init__(self, a1):
        self.a1 = a1
    def getA1(self):
        return self.a1
    def setA1(self, v):
        return self.a1 == v
        print "New String a1"
    def getB(self):
        return B
    print "Exercicio 1\n"
    
print 'Teste da Classe A'        
a = A('Rafael')
print a.setA1('Rafael')
print a.getA1()
print '\n'

class B:
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
    b1 = property(getB1, setB1)

print 'Teste Classe B'
b = B(3)
BB = B(4)
bbb = B(3)
print b.setB1(3)
print b.getB1()
print BB.setproximoB(4)
print BB.getproximoB()
print BB.bbbb(4)
print '\n'

class C(B):
    c1 = 0.2
    float(c1)
    
    def __init__(self, c1):
        self.c1 = c1
    def getC1(self):
        return self.c1
    def setC1(self, v):
        return self.c1 == v
    def getD1(self):
        return D
    def bbbb(self, bbbb):
        self.bbbb = bbbb
    
    if not (B.getproximoB) == "":
        str(c1) + str(bbbb)
    else:
        c1

print 'Teste Classe C'
cc = C(1)
print cc.getC1(), "\n"


class D:
    d1 = 203.2334
    float(d1)
    a = 1
    d1t = [1,2,3,4]
    s =""
    
    def __init__(self, d1):
        self.d1 = d1
    def getD1(self):
        return self.d1
    def setD1(self,v):
        return self.d1 == v
    def addA(self, d1t):
        a = 5
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
        return self.ddddd == ddddd
    s = d1 
    multiA = []   
    for a in multiA:
        s+= a.getB()+C.bbbb()
    

print 'Teste Classe D\n'
a = D(5)
print D.addA(a,D.d1t) , "/----> Adiciona o Elemento (5) na lista d1t"
b = D(3)
print D.iteratorA(b, D.d1t), "/----> Iterações da Lista D.d1t"
c = D(1)
print D.removeA(c, D.d1t) , "/----> Remove ELemento (1) da Lista d1t"
d = D(493049494)
print D.SizeOfA(d, b) , "/----> Tamanho do item"
e = D(5)
print D.ddddd(e, D.ddddd), "/----> Verificação de ddddd"
print D.s ,"/---> teste for\n"
    
    