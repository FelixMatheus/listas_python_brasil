#coding: utf-8

from B import *

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