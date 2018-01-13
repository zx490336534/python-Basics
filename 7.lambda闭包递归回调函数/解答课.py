#函数的命名规范
#pep8
#1.和变量命名规则一样
#a.只能由字母、数字、下划线组成
#b.不能以数字开头
#c.不能使用关键字作为变量（import keyword \keyword.kwlist）
#2.命名需要见名知义，user_want，this_is_a_func

#命名关键字参数
def f(a,b=1,*args,**kwargs):
        print(a)
        print(b)
        print(args)
        print(kwargs)
#默认参数不能放到必备参数前面
def f1(**kwargs):#0-任意多个参数，字典 传入的数量，以及传入的建名
        print(kwargs)

#学籍注册 姓名，年龄，国籍，城市。
def f2(name,*,country,city):
        print(name)
        print(country)
        print(city)

f2('zx',country='CN',city='zhejiang')
#作用，限制传入的参数的数量，限制变量名

#sort与sorted 区别
#sort是list的一个方法，它的作用对象只能是列表
#sorted是内置函数，对象为可迭代对象

#可迭代对象：
        #1.所有的序列类型 list tuple str
        #2.一些非序列类型 dict set
        #3.定义任何包含 __iter__() 或者 __getitem__()类的对象
li = [9,6,2,1,4]


