#coding: utf-8

import B

class A:

    def __init__(self, a1):
        self.a1 = a1
    def getA1(self):
        return self.a1
    def setA1(self, v):
        self.a1 = v
    def getB(self):
        return self.b
    a1= property(getA1, setA1)   