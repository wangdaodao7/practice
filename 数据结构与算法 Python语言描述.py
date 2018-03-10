# -*- coding: utf-8 -*-
import datetime


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
        self._den = den// num



x = Rational(9, 9)
print(x._num, x._den)


#静态方法
class Countable:
    counter = 0
    def __init__(self):
        Countable.counter += 1
    @classmethod
    #不参与实例化，表示类本身特性的一些方法，比如实例的计量
    def get_count(cls):
        return Countable.counter

x = Countable()
y = Countable()
print(Countable.get_count())





class PersonValueError(TypeError):
    pass


class Person:
    #内部函数使用，只在类中生效
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ('男', '女')):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('生日错误', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1





p = Person('导导', '女', (1999, 12, 22), 9090200)