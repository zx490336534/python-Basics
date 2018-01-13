#01类的概念、定义、属性、继承
#回顾
'''
1.内置函数：enumerate  filter map zip
2.变量的作用域：global nonlocal
3.闭包：函数中嵌套函数
4.递归：终止条件 递归推导式
'''
#面向对象
'''
图书管理系统：
1.图书：10000本
2.管理员：50个
3.读者：1000个
'''
#类的定义：类是对现实生活中，具有共同特征的事物的抽象
class Animal(object):
        '''定义一个动物类'''
        pass

#object:基类，任何类都要继承object
#python3中继承object类可写可不写
class Animal:
        pass
dog = Animal()
cat = Animal()

#构造方法 __init__()        self参数
class Animal:
        def __init__(self):#在实例化对象时调用
                print('正在实例化一个类')
        def test(self):
                print('aaa')

#当我们没有写__init__(),默认调用父类__init__
class Animal:
        def test(self):
                print('aaa')

#self 实例化对象本身
#self可以替换成别的参数名，但是最好别改
class TestSelf:#书写规范：方法testSelf 类TestSelf
        def __init__(self):#在初始化的时候，默认往构造方法传入一个值
                print('正在实例化一个类')
        def test():
                print('bbb')
        def test2():#只能被类调用TestSelf.test2()
                print('ccc')


#属性：变量
'''
1.实例化属性
2.类属性（共有属性）
'''

#1.实例化属性----自己独有的属性就放到实例化中
class Animal:
        def __init__(self,name,food):
                print('正在实例化')
                self.name = name#self.namesss 实例化属性中新增形参namesss
                self.food = food
        def get_name(self):
                print(self.name)

dog = Animal('大黄','骨头')
dir(dog)
dog.get_name()

#2.类属性（共有属性）----共有的放到外部
class Animal:
        eye = 2
        leg = 4
        def __init__(self,name,food):
                print('正在实例化')
                self.name = name
                self.food = food
        def get_name(self):
                print(self.name)

#私有化
'''
单下划线_'：模块私有化
from moduleName import * 不会引入单下划线开热的变量、函数
'''
#'_'和'__'是一种规范和约定，没有真正达到限制的目的
import random #全部导入
from random import *#单下划线内容不会导入
class Animal:
        _eye = 2
        __leg = 4
        def __init__(self,name,food):
                print('正在实例化')
                self.name = name
                self.food = food
        def get_name(self):
                print(self.name)
                
dog = Animal('大黄','骨头')
dog._eye = 3
dog._Animal__leg #__默认加一个类名，用来警告


#面向对象的三个特征：封装、继承、多态
#封装
class Animal:
        eye = 2
        leg = 4
        def __init__(self,name,food):
                print('正在实例化')
                self.name = name
                self.food = food
        def get_name(self):
                print(self.name)
        def get_food(self):
                print(self.food)

#继承--代码的重用
class People(Animal):
        leg = 2
        def __init__(self,name,food,sex):
                self.name = name
                self.food = food
                self.sex = sex
        def get_sex(self):
                print(self.sex)
        def speak(self):
                print('asfasfasfasfas')
        def eat(self):
                print('果子')

zx = People('zx','饭','男')

#多态--子类重写父类的方法--继承

class Chinese(People):
        def speak(self):
                print('你好')
        def eat(self):
                print('大米')

class American(People):
        def speak(self):
                print('hello')
        def eat(self):
                print('面包')     

class Thailand(People):
        def speak(self):
                print('萨瓦迪卡')
        def eat(self):
                print('香蕉') 

xiaoming = Chinese('小明','大米','男')
jack = American('Jack','面包','男')
lala = Thailand('lala','咖喱','女')



'''
总结：
1.类的定义
2.__init__()构造方法
3.self 参数---实例对象本身
4.类属性（共有属性），实例化属性
5.'_'和'__' 类中的私有化
6.面向对象的三大特征：封装、继承、多态

'''









