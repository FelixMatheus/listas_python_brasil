#coding: utf-8

from B import *

class C(B):

    def __init__(self, c1):
        B.__init__(self, b1=False, newb=False)
        self.c1 = c1
    def getC1(self):
        return self.c1
    def setC1(self, v):
        self.c1 = v
    def getD1(self):
        return self.d1
    def bbbbb(self):
        if not (B.getproximoB) == 0:
            return str(C.c1) + str(C.bbbbb)
        else:
            return str(C.c1)
        