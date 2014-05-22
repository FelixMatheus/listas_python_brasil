#coding: utf-8
import math
from itertools import cycle

class B(object):
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
