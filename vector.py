#!/usr/bin/env python3
import math
class Vector(object):
    def __init__(self, components=[]):
        self.__components = list(components)

    def set(self, components):
        if len(components) > 0:
            self.__components = list(components)
        else:
            raise Exception("please give any vection")

    def __str__(self):
        return "(" + ",".join(map(str, self.__components)) + ")" 

    def component(self, i):
        if type(i) is int and -len(self.__components) <= i <len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def changeCpmponent(self, pos, value):
        assert (-len(self.__components) <= i <len(self.__components))
        self.__component[pos] = value

    def __len__(self):
        return len(self.__components)

    def eulidlength(self):
        summe = 0
        for i in self.__components:
            summe += (i**2)
        return math.sqrt(summe)

    def __add__(self,other):
        size = len(self)
        if size == len(other):
            result = [self.__components[i] +
                      other.component(i) for i in range(size)]
            return Vector(result)
        else: Exception("must have the same size")

    def __sub__(self,other):
        size = len(self)
        if size == len(other):
            result = [self.__components[i] -
                      other.component(i) for i in range(size)]
            return Vector(result)
        else: Exception("must have the same size")

    def __mul__(self,other):
        if isinstance(other,int) or isinstance(other,float):
            ans = [self.__components[i]*other for i in self.__components]
            return ans
        elif (isinstance(other, Vector) and (len(self) == len(other))):
            size = len(self)
            summe = 0
            for i in range(size):
                summe += self.__components[i] * other.components(i)
            return summe
        else:
            raise Exception("invalide operand!")

    def zeroVector(dimension):
        assert(isinstance(dimension,int))
        return Vector([0]*dimension)

    def unitBasisVector(dimension, pos):
        assert(isinstance(dimension,int) and isinstance(pos,int))
        ans = [0]*dimension
        ans[pos] = 1
        return Vector(ans)
