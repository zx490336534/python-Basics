#内置函数 python自带
'''
dir(__builtins__)
type()
max()
min()
print()
len()
sorted()#排序
reversed()
help()
id()
range()
sum()
'''
li = dir(__builtins__)
len(li[li.index('abs'):])

l1 = [1,2,3,4]
sum(l1)

abs(-12)#绝对值
round(1.9)#四舍五入
round(1.145,2)#保留两位小数四舍五入1.15

bin(2)#二进制
oct(8)#八进制
hex(16)#十六进制
ord('a')#字符转换为ascii码
chr(65)#将ascii码转换为字符

l2 = ['a','b','c']
enumerate(l2)#返回一个可以枚举的对象（index,value）
list(enumerate(l2))#[(0, 'a'), (1, 'b'), (2, 'c')]
di = {'a':1,'b':2}
dict(enumerate(l2))#可以转换成字典
#注意，集合字典是无序的没有索引,返回（伪索引，values）
se = {1,2,3,'asd',5}
list(enumerate(se))

#filter()过滤器
l3 = [1,2,3,4,5,6,7,8]
def test(x):
        return x > 5
list(filter(test,l3)) #[6, 7, 8]
list(filter(lambda x:x>5,l3))
#lambda 凡是可以用到函数的地方都可以使用lambda

#map() 加工
l4 = [1,2,3,4]
list(map(str,l4))#['1', '2', '3', '4']转换成字符串
list(map(lambda x:x+1,l4)) #[2, 3, 4, 5]每个元素+1


#zip()将对象逐一配对
l5 = [1,2,3]
tu = ('a','b','c')
list(zip(l5,tu))#[(1, 'a'), (2, 'b'), (3, 'c')]
dict(zip(l5,tu)) #{1: 'a', 2: 'b', 3: 'c'}

'''
全局变量可以在函数内部访问，但是不能修改
如果在函数内部想修改全局变量，可以用global来修饰变量
'''
#2.函数内变量的作用域
a = 10 #全局变量
def test1():
        b = 5 #局部变量
        print('局部访问全部变量 a:',a)#局部可以访问全局变量
        #a += 1 #全局变量可以在函数内部访问，但是不能改变

def test2():
        global a#全局变量
        a += 1
        print('局部访问全部变量 a:',a)

def test3(): #global只对当前函数起作用
        #global a        
        a += 1
        print('test3修改全部变量 a:',a)

'''
局部变量只能在局部内进行访问和修改
如果在函数外部想要访问局部变量，也可以用global，将局部变量声明为全局变量
'''

def test4():
        global b
        b = 4
        b += 1
        print('局部变量b:',b)


#使用nonlocal的情况
#内嵌函数
def test5():
        c = 2
        print('局部外层 c:',c)
        def test6():
                d = 5
                print('局部里层 d:',d)
        #test6()#在test5中调用则会运行test6，不然不输出
#nonlocal
def test7():
        c = 2
        print('局部外层 c:',c)#声明外层（非全局）变量
        def test8():
                d = 5
                print('局部里层 d:',d)
                nonlocal c
                #global c 函数外部没有定义c
                c += 1#当里层局部,需要修改外层局部
                print('当里层局部,需要修改外层局部c:',c)
        test8()




#闭包

def test9(name):
        def test10(age):
                print('name:',name,',age',age)
        return test10

f = test9('zx')
f(23)#name: zx ,age 23

#装饰圈 本身就是一个闭包


#递归函数

#for 循环
def age(n):
        age = 10
        for i in range(1,n):
                age += 2
        print('最后一个人%s岁'% age)

#递归
def age2(n):
        if n == 1:
                return 10
        else:
                return age2(n-1)+2

#阶层
#1！=1
#2！=1*2
#3！=1*2*3
#4！=1*2*3*4
def fun(n):
        n = int(n)
        if n==1:
                return 1
        elif n <= 0:
                print('请输入大于1的整数')
        else:
                return fun(n-1) * n
