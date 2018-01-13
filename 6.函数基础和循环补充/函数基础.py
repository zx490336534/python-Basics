#python函数基础

'''
1.条件语句：if elif else，pass占位
2.循环语句：1.while，终止条件
                     2.for ，迭代对象
3.三种通用操作：break，强制结束循环
                           continue，跳出本次循环
                           else，当前循环正常结束，就会执行else
'''

def sel_for(iterable):
        for i in iterable:
                print(i)
                
##定义函数
def fun1(a):
        print('hello',a)

#传参

#不需要传参
def fun2():
        print('hello python')
        print('人生苦短，我用python')
#必备参数
def fun3(a):
        print('必备参数:',a)
#默认参数
def fun4(a=3):
        print('默认参数:',a)


#可选参数 0个~多个
#*arg
#**kwarg


#*arg
def fun5(*arg): #默认将我们传入的参数包装成元祖
        print('arg:',arg)
fun5(1,2,3,4,5) #arg: 1 2 3 4 5
tu = (1,2,3,4)
li = [1,2,3]
fun5(tu) #arg: ((1, 2, 3, 4),)
fun5(*tu)#arg: (1, 2, 3, 4)
fun5(li)#arg: ([1, 2, 3],)
fun5(*li)#arg: (1, 2, 3)
fun5(*'asfasf')#arg: ('a', 's', 'f', 'a', 's', 'f')

#**kwarg 传值的时候，必须要满足字典的定义
def fun6(**kwarg): #默认将我们传入的参数包装成字典
        print('kwarg:',kwarg)
#空集合 se = set()
#空字典 {}
di = dict(a=1)
fun6(a=1,b=2,c=3)#kwarg: {'a': 1, 'b': 2, 'c': 3}
fun6(**di)#kwarg: {'a': 1}

#五种传参，混合用时，需要注意的事项：
'''
1.默认参数，必备参数
2.*arg，默认参数，必备参数
3.*arg，**kwarg
'''
#1默认参数，必备参数
def fun7(b,m=2):#必须必备参数在前，默认参数在后
        print('必备参数:',b)
        print('默认参数:',m)
fun7(1,3)
fun7(m=10,b=5)#带上参数名，进行指定传参

#2*arg，默认参数，必备参数
def fun8(b,m=2,*arg):
        print('必备参数:',b)
        print('默认参数:',m)
        print('arg:',arg)
fun8(1,2,3,4,5) #必备参数: 1;默认参数: 2;arg: (3, 4, 5)
def fun9(*arg,b,m=2):
        print('必备参数:',b)
        print('默认参数:',m)
        print('arg:',arg)
fun9(1,2,3,4,b=3)#必备参数: 3;默认参数: 2;arg: (1, 2, 3, 4)

def fun10(*arg,m=2,b):
        print('必备参数:',b)
        print('默认参数:',m)
        print('arg:',arg)
fun10(1,2,3,4,b=5)#必备参数: 5;默认参数: 2;arg: (1, 2, 3, 4)

#3*arg，**kwarg
def fun11(*arg,**kwarg): #**kwarg必须放到最后
        print('arg:',arg)
        print('kwarg:',kwarg)
fun11() #arg: () kwarg: {}
fun11(1,2,3,4,5)#arg: (1, 2, 3, 4, 5) kwarg: {}
fun11(1,2,3,4,a=1,b=2)#arg: (1, 2, 3, 4) kwarg: {'a': 1, 'b': 2}


