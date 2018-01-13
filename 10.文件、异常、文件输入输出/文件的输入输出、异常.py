#文件的输入输出、异常
#回顾
'''
1.多继承：1：类名调用 2：supper
2.魔法方法
3.装饰器@
4.类的装饰器，property  staticmethod classmethod
'''

#1.文件

#打开文件对象
#open()
'''
#只读模式，文件不存在的时候报错
f = open('text.txt','r')
#写入模式，文件存在清空内容，不存在则创建文件
f = open('text.txt','w')
#写入模式，文件存在报错，不存在则创建文件
f = open('text.txt','x')
#追加写入模式，不清空文件，直接写入后面
f = open('text.txt','a')
#以二进制模式读写文件，wb,rb,ab。
f = open('text.txt','wb')
#可读写模式，r+,w+,x+,a+,这几种模式还遵循了r,w,x,a的基本原则。
f = open('text.txt','r+')
'''
#默认建立在当前目录
#绝对路径 C:\Users\Administrator\Desktop\笔记\第十课\zx
#加入转义字符r或者在有\的地方变成\\
#f = open(r'C:\Users\Administrator\Desktop\笔记\第十课\zx\test.txt','w')
path = r'C:\Users\Administrator\Desktop\笔记\第十课\zx\test.txt'
f = open(path,'w')
#相对路径...\zx
path_1 = r'..第十课\zx\z.txt'
f = open(path,'w')
type(f)#<class '_io.TextIOWrapper'> 文件类 / 流类
#操作
'''
打开  写入 读取 关闭
'''
f = open('test.txt','w')#以写的方式打开
#f.read()会报错
f.close()
# + 可读写，在原有的基础上多加了读写功能
f = open('test.txt','w+')#可读写模式

#read 读的操作
#光标------文件指针
'''
f.tell()#返回光标在文件中的位置
f.seek(offset,from)#移动光标f.seek(0)=f.seek(0,0)返回起始位置
'''
f.read()#将文件所有内容以一个字符串返回,光标移到最后
f.readline()#读出当前光标所在的一行
f.readlines()#以列表形式读出光标后的全部内容
#汉字占两个字节
'''
编码问题：
        cp936 = GBK（中文编码） 2字节
        IBM在发明Code Page的时候将GBK放在第936页,所以叫CP936
        UTF-8 国际编码 3字节
'''


#写入 write
f = open('test.txt','w+')
f.write('人生苦短，我用python')#缓存
f.flush()#将缓存写入硬盘
li = ['\n123\n','456\n','789\n','101112\n']
f.writelines(li)
f.flush()

#文件 属性
f.closed#文件是否关闭
f.name#文件名
f.mode#文件打开方式
f.encoding#编码
#with形式打开文件，运行完文件自动写入硬盘并关闭
with open('test.txt','w+') as f:
        f.write('555')
print(f.closed)





#2.异常语法  为了让错误不影响程序运行
try:
        b = 3
        d = 2
        b %d
except NameError:
        print('没有定义')
except TypeError:
        print('你的类型错误')
except ValueError:
        print('值错误')
except Exception:
        print('b % d,报错了')
else:#当try里面没报错则执行else
        print('没有问题')
finally:
        print('不管你报不报错，我都要执行')


try:
        f = open('test.txt','w')
        f.read()
except Exception:
        print('文件操作有误')
finally:
        f.close()

print(f.closed)
        
a = 1


#raise 故意报错 显性的引发异常
try:
        a = input('输入数字：')
        if a.isdigit():
                print('输入成功',a)
        else:
                raise TypeError
except Exception:
        print('您输入有误')

#assert 返回False就弹出异常
assert 1>2#False ---- AssertionError
assert isinstance(1,str)#False ---- AssertionError
assert isinstance(1,(str,int))#True ---- 没有返回值
