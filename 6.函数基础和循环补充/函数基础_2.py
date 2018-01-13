#return

#1
#如果函数中没有写return
#其实函数结束的时候，默认执行了return None

def test_return(a,b):
        if a>b:
                return a
        elif a<b:
                return b
        else:
                return '一样大'
        print('比较结束') #不会输出，return处就结束
#return print区别:
#return ：返回函数运行的结果
#print   ：打印输出，只是用来看的
def test_return2(a,b):
        if a>b:
                print(a)
        elif a<b:
                print(b)
        else:
                print('一样大')
        print('比较结束')


#lambda匿名函数，没有名字的函数
def fun_name():
        print('函数内容')

f = fun_name
f()
#lambda定义
#lambda x(参数):x+1(return x+1)
lambda x:x+1 #返回函数体
(lambda x:x+1)(5) #6
g = lambda x:x+1
g(5) #6

add = lambda x,y:x+y
add(1,2) #3
judge = lambda x:bool(x%2==0) #判断是否偶数
