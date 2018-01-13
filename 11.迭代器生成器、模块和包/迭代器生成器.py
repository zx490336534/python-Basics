#迭代器生成器、模块和包


#1迭代器和生成器

#补充
li = [0,2,4,6,8,10,12,14,16,18]
l2 = []
for i in range(20):
        if i%2 == 0:
                l2.append(i)
l3 = []
for i in range(0,20,20):
        l3.append(i)
l4 = list(range(0,20,2))
#列表推导式 优化 简单代码
l5 = [i for i in range(20)]#第一个i就是往列表中添加的对象
l6 = ['aa' for i in range(20)]#添加20个'aa'
l7 = [i for i in range(20) if i%2 == 0]
l8 = [i for i in range(20) if i%2 != 0]
#插入偶数，奇数->'a'
l9 = [i if i %2 == 0 else 'a' for i in range(20)]

#集合
s = [i for i in range(10)]
#字典
di = {i:'zz' for i in range(10)}




#迭代器
'迭代器协议就是实现对象的__iter__()和__next__()方法'
#可迭代对象__iter__()
#iter(xx) == xx.__iter__()    
li = iter(li)      #li变成了迭代器
type(li)#<class 'list_iterator'>
#next(x) == x.__next__() 迭代的取值
next(li)

#迭代器是用来干嘛的：
'''
for循环：
1.iter() ---> 对象变成了迭代器
2.next() --->迭代的取值

extend(iterable) ->iter() ->next() ->append()
'''
'''
for i in li:
        print(i)
# 输出2,4,6,8......
'''



#生成器 本质也是迭代器
def fun():
        i = 0
        while i <5:
                print('***')
                yield i #暂停 返回值
                i += 1
                print('+++',i)
a = fun()
#next(a)
next(fun())#每次调用，会新生成一个对象

#例子，菲波那切数列  1 1 2 3 5（f1+f2=f3）
def fib(num):
        n,a,b = 0,0,1
        while n < num:
                print(b)
                a,b=b,a+b
                n = n+1
#yield
def fib2(num):
        n,a,b = 0,0,1
        while n < num:
                print(b)
                if n%10 == 0:
                        yield
                a,b=b,a+b
                n = n+1                



#2.模块和包
#模块
#内置模块 python自带
#C:\Python3\Lib
import keyword
keyword.kwlist
from random import randint #指定导入，节省内存
from random import * #导入全部内容不会导入带一个下划线的内容
from random import _cos


#第三方模块 别人写的 不是python自带的
#同路径下
import test
test.test() #调用方法
test.test1#调用属性
#__name__我自己调用才会执行

#不同路径
#import test2
import os,sys
sys.path #以列表的形式返回放包的路径
sys.path.append(r'C:\Users\Administrator\Desktop\笔记\第十一课\zx')


#包 一个文件夹里面放了很多模块。文件夹就叫包
import xml
import xml.dom
import xml.dom.domreg

#不是系统的包就添加路径

#补充
sys.argv

