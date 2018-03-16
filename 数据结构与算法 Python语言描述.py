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
class PersonTypeError(TypeError):
    pass

class Person:
    #内部函数使用，只在类中生效
    _num = 0
    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ('男', '女') and isinstance(ident, str)):
            raise PersonValueError(name, sex, ident)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('生日错误', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id
    def name(self):
        return self._name
    def sex(self):
        return self._sex
    def birthday(self):
        return self._birthday
    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError('改名字', name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._birthday > another._birthday

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return '-'.join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ', '.join(('编号：'+self._id, '姓名：'+self._name,'性别：'+self._sex,'出生日期'+str(self._birthday)))


p1 = Person('导导', '男', (1999, 2, 11), '9090233')
p1.set_name('导导2号')
p2 = Person('微微', '女', (1993, 12, 22), '9091202')
p3 = Person('九九', '女', (1999, 7, 31), '9091201')
p4 = Person('三九', '男', (1399, 5, 1), '9092301')




# print(p1, '\n', p1.details())

p = [p1, p2, p3, p4]
p.sort()
for pp in p:
    print(pp.details(), pp._num)



class Student(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}
    def set_course(self, course_name):
        self._course[course_name] = None   
    def set_score(self, course_name, score):
        if course_name not in self._course:
            raise PersonValueError('课程错误', course_name)
        self._courses['course_name'] = score
    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]


s1 = Student('小吴', '女', (1988, 2, 11), '数学系')
s2 = Student('小周', '男', (1989, 12, 31), '外语系')

print(s1.details(), s2.details())