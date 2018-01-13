#多继承、类的特殊方法、装饰器
#回顾
'''
1.类的定义class
2.__init__构造方法
3.self参数，实例本身
4.属性，类属性（共有属性） 实例化属性
5.私有化  '_' '__'
6.封装、继承（object）、多态（子类重写父类方法）
'''
#1.多继承
class Base:
        def play(self):
                print('这是Base')

class A(Base):
        def play(self):
                print('这是A')        

class B(Base):
        def play(self):
                print('这是B')  

class C(A,B):
        #子类调用父类方法
        def play(self):
                '''
                #第一种方法
                A.play(self)
                B.play(self)
                '''
                #super().play()#第二种方法 默认调用第一个父类的方法（A）
                #super(C,self).play() = super().play() #括号不写，默认(C,self)
                super(A,self).play()#这是B
                super(B,self).play()#这是Base
                super(Base,self).play()
                print('这是C')  

c = C()
C().__class__.mro() #C->A->B->Base->object
'''
super=上一层
1.super() = super(自己的类名,self) <->（自己的类名，自己的实例化方法）
2.谁调用我，我就以谁为基准，建立一张调用顺序表C().__class__.mro()
'''



#2.类的特殊方法 （魔法方法）
'''
不仅仅是属性，更多的是方法
'''
class Rectangle:
        '''
        这是一个矩形类，可以计算面积
        '''
        aaa = 1
        def __init__(self,length,width):
                if isinstance(length,(int,float)) and isinstance(width,(int,float)):
                        self.length = length
                        self.width = width
                else:
                        print('请输入int or float')
        def area(self):
                return self.length * self.width
        
        def __str__(self):
                return '这个长方形的面积%s' % self.area()

        def __repr__(self):
                return '长：%s  宽： %s' %(self.length, self.width)

        def __call__(self):
                return '我这是一个Rectangle类，你要干嘛'

        def __add__(self,other):
                return self.area() + other.area()

        def __sub__(self,other):
                return '不可以相减'
                
r  = Rectangle(2,3)
#类属性

#__dict__
r.__dict__ #打印实例里面的属性 {'length': 2, 'width': 3}
#注意共有属性，当不修改的时候默认引用源类
        #修改后就会定义在实例里面
r.aaa = 22
r.__dict__ #{'length': 2, 'width': 3, 'aaa': 22}

#__doc__ 只能打印出句首的文档
r.__doc__


#类方法
#__str__           %s调用__str__
print(r)#这个长方形的面积6

#__repr__         %r调用__repr__ 
r#长：2  宽： 3

#print默认调用__str__，没有时__repr__


#__call__
r()#'我这是一个Rectangle类，你要干嘛'


r1 = Rectangle(2,4)
r2  = Rectangle(3,5)

#__add__(self,other)     #x+y
r1+r2#23
# __sub__(self,other)     #x-y 
#__mul__(self,other)     #x*y 
#__mod__(self,other)     #x%y
#  __iadd__(self,other)    #x+=y
#__isub__(self,other)    #x-=y 
#__radd__(self,other)    #y+x
#__rsub__(self,other)    #y-x 
#__imul__(self,other)    #x*=y
#__imod__(self,other)    #x%=y 

'''
#和类有关的几个函数  
delattr()		# 删除对象属性
getattr()		# 得到修行的某个属性值
setattr()		# 给对象添加某个属性值
hasattr()  		# 判断对象object是否包含名为name的特性
isinstance()  	# 检查对象是否是类的对象，返回True或False
issubclass()  	# 检查一个类是否是另一个类的子类。返回True或False	
'''



#3.装饰器 添加附加功能

#闭包
def fx(x):
        x += 1
        def fy(y):
                return x * y
        return fy

fx(1)(2)

def f1(func):
        print('f1 running')
        def f2(y):
                print('f2 running')
                return func(y) + 1
        return f2

def gun(m):
        print('gum runing')
        return m*m
'''
f1(gun)
temp = f1(gun)
temp(5)
'''

@f1#f1(gun2)
def gun2(m):
        print('gun running')
        return m*m
'''
1.@f1 -> f1(gun2) -> f2
2.f2 等待调用
3.gun2(5) -> 当参数5传入时gun2没有拿到 -->f2(5)
4.f2(5)开始运行 ->print('f2 running')->func(y) : y = 5 func = gun2
5.gun2(5)开始运行 ->print('gum runing')->m*m=25 
6.25 + 1 -> 26
'''


import time
def run_time(func):
        def new_fun(*args,**kwargs):
                t0 = time.time()
                print('start time:%s' % (time.strftime('%x',time.localtime())))
                back = func(*args,**kwargs)
                print('end time:%s' % (time.strftime('%x',time.localtime())))
                print('run time:%s' % (time.time() - t0))
                return back
        return new_fun

@run_time
def test():
        for i in range(1,10):
                for j in range(1, i+1):
                        print('%dx%d=%2s' %(i,j,i*j),end =' ')
                print()


#类装饰器

class Test_Class:
        def __init__(self,func):
                self.func = func
        def __call__(self):
                print('类')
                return self.func

@Test_Class
def fun_test():
        print ('这是一个测试')

fun_test()#类
fun_test()()
#类
#这是一个测试


#python 自带 类的内置装饰器
class Rectangle:
        '''
        这是一个矩形类，可以计算面积
        '''
        aaa = 1
        def __init__(self,length,width):
                if isinstance(length,(int,float)) and isinstance(width,(int,float)):
                        self.length = length
                        self.width = width
                else:
                        print('请输入int or float')
        @property#r.area 不需要加括号=可以把方法当成属性一样访问
        def area(self):
                return self.length * self.width
        @staticmethod#定义成静态方法 不用self，实例可以直接调用
        def func():
                print('可以调用吗？')
        @classmethod#将实例还原成了类
        def show(self):
                print(self)
                print('show fun')
        
r = Rectangle(2,3)
r.area
