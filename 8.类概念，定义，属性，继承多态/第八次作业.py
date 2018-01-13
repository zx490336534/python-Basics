#python面向对象作业1


#1.把老师上课例子都敲一遍（不需要截图，但是一定要做）




#2.定义一个矩形的类：
#    要求：1.有长和宽的属性
#          2.有一个计算面积的方法
#isinstance
class Rectangle:
      def __init__(self,length,width):
            if isinstance(length,(int,float)) and isinstance(width,(int,float)):
                  self.length = length
                  self.width = width
            else:
                  print('实例化失败')
                  return
            print('矩形的长为%s,宽为%s'%(self.length,self.width))
      def area(self):
            print('面积为:',(self.length*self.width))


rect = Rectangle(2,4)
rect.area()
rect = Rectangle('aaa','bbb')

#如何判断self就是实例化对象
class test:
      def __init__(self):
            if isinstance(self,test):
                  print('True')
      def isin(self):
            if type(self) == type(test):
                  print('z_True')      
            else:
                  print('z_False')
                  print(type(self))#<class '__main__.test'>
                  print(type(test))#<class 'type'>元类 metaclass




#3.写一个正方形的类，继承矩形类
#    要求：有一个判断是不是正方形的方法

class Square(Rectangle):
      def is_square(self):
            if self.length == self.width:
                  print('是正方形')
            else:
                  print('不是正方形')


square = Square(2,2)
square.is_square()






















