#面向对象作业2



#1.把老师上课例子都敲一遍（不需要截图，但是一定要做）



#2.测试type 和 isinstance 那个的速度更快
#高阶函数 嵌套函数
#嵌套函数：
def a(txt):
      def b(txtb):
            def c(txtc):
                  print(txt,txtb,txtc)
            return c
      return b
a(1)(2)(3)
#高阶函数1可以接受函数作为参数 2可以将函数作为返回值
def f(aa):
      aa()
      aa()
def lin():
      print('高阶函数')

f(lin)

def log(fun):
      def wrapper():
            print('我叫装饰器')
            fun()
      return wrapper

def ff():
      print('这是一个被装饰的函数')

@log # f = log(fff) --> wrapper
def fff(): #fff() --> wrapper()
      print('我也被装饰了')



import time
def run_time(func):
      def new_fun(*args,**kwargs):
            t0 = time.time()
            print('star time: %s'%(time.strftime('%x',time.localtime())) )
            back = func(*args,**kwargs)
            print('end time: %s'%(time.strftime('%x',time.localtime())) )
            print('run time: %s'%(time.time() - t0))
            return back
      return new_fun

@run_time
def test_1():
      type(1)

@run_time
def test_2():
      isinstance(1,int)

test_1()
test_2()
#isinstance更快


#3.实现一个正方形类的加减乘除(就那些装B的魔术方法，能写多少写多少)
class Square:
      def __init__(self,length):
            self.length = length
      def area(self):
            return self.length * self.length
      def __add__(self,other):
            return self.area() + other.area()
      def __sub__(self,other):
            return self.area() - other.area()
      def __mul__(self,other):
            return  self.area() * other.area()
      def __truediv__(self,other):
            return self.area() / other.area()
      
s1 = Square(2)
s2 = Square(3)
