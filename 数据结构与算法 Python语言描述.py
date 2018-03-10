# -*- coding: utf-8 -*-

"""
    作者:     王导导
    版本:     1.0
    日期:     2018/03/08
    项目名称： 数据结构与算法 Python语言描述
    项目参考地址：无

"""




#类静态的使用方法

class Rational0:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den

    def plus(self,another):
        den = self.den * another.den 
        num = (self.num * another.den + self.den * another.num)
        return Rational0(num, den)

    def print(self):
        print(str(self.num) + '/' +str(self.den))


r1 = Rational0(3)
print(r1)
r1.print()
r2 = r1.plus(Rational0(7))
r2.print()

class Rational:
    #静态方法函数，在一个类里使用的普通函授，没有self，不参加实例
    @staticmethod
    def _gcd(m, n):
        #带_的函授名,非实例方法，表示只在类里面使用，不应该在类之外使用
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n
    def __init__(self, num, den=1):
        sign = 1
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)

        self._num = sign *(num//g)
        self._den = den//g



x = Rational('44', 0)
print(x._num, x._den)