# -*- coding: utf-8 -*-
import datetime


"""
    作者:     王导导
    版本:     1.0
    日期:     2018/03/08
    项目名称： 数据结构与算法 Python语言描述
    项目参考地址：无

"""
from collections import Counter

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


# r1 = Rational0(3)
# print(r1)
# r1.print()
# r2 = r1.plus(Rational0(7))
# r2.print()

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
# print(x._num, x._den)


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
# print(Countable.get_count())


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

print(p3.age())
print(p2)


# print(p1, '\n', p1.details())

# p = [p1, p2, p3, p4]
# p.sort()
# for pp in p:
#     print(pp.details(), pp._num)



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
    def details(self):
        return ', '.join(('编号：'+self._id, '姓名：'+self._name,'性别：'+self._sex,'出生日期'+str(self._birthday),'院系:'+self._department))



s1 = Student('导导', '男', (1988, 6, 22), '化学系')
s2 = Student('彤彤', '女', (1991, 11, 2), '管理系')

<<<<<<< HEAD
aa = '''<meta property="og:description" content="步骤： 1. 下载Git客户端 2. 配置环境变量 3. 设置vscode与Git的关联 4. 重启 步骤一： 该网址，下载即可。 https://git scm.com/downloads 步骤二：" />
<link type="text/css" rel="stylesheet" href="/bundles/blog-common.css?v=giTNza-Of-PEt5UsELhFQAR7G6-bfaSa4oolcq7i9-o1"/>
<link id="MainCss" type="text/css" rel="stylesheet" href="/skins/SimpleMemory/bundle-SimpleMemory.css?v=EanP3quXYv9G0oFCmz4BNBHvmK7M_Si1iD1EpUHL_441"/>
<link id="mobile-style" media="only screen and (max-width: 767px)" type="text/css" rel="stylesheet" href="/skins/SimpleMemory/bundle-SimpleMemory-mobile.css?v=XGOE8_i3XCsAIQHcgl5c_8VAMMKRkj0W3Eckyc8qbso1"/>
<link title="RSS" type="application/rss+xml" rel="alternate" href="https://www.cnblogs.com/geekfeier/rss"/>
<link title="RSD" type="application/rsd+xml" rel="EditURI" href="https://www.cnblogs.com/geekfeier/rsd.xml"/>
<link type="application/wlwmanifest+xml" rel="wlwmanifest" href="https://www.cnblogs.com/geekfeier/wlwmanifest.xml"/>
<script src="//common.cnblogs.com/scripts/jquery-2.2.0.min.js"></script>
<script type="text/javascript">var currentBlogApp = 'geekfeier', cb_enable_mathjax=false;var isLogined=false;</script>
<script src="/bundles/blog-common.js?v=yRkjgN2sBQkB4hX-wirHxPomeBT9sB5dawr6ob7KIvg1" type="text/javascript"></script>
</head>
<body>
<a name="top"></a>
'''
print(Counter(aa))


=======
print(s1.details(),'\n', s2.details())
>>>>>>> dbb1ab0e9d3c629c7877df73589d3ccaa780494b
