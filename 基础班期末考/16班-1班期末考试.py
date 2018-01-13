#16班期末考试
#注意事项：
'''
1.11月3日18点之前，发送到林泷老师的邮箱(3002742285@qq.com)。

2.标注好第几题，一题一个截图，包含这个题的代码和运行结果,必须是截图，别发附件。

3.所有题目都可以已学知识解答，想到多少写多少。

4.最后重申：必须在11月3日18点之前以截图的形式发送到林泷老师的邮箱。
'''



#题1
'''
在这一个月，我们学了python基础，简单总结下，有六种数据类型，函数以及类。
(1)请从str，list,dict,set选出 1 种数据类型，进行归纳总结。
(2)请选择函数和类其中 1 种，进行归纳总结。
'''

#例  元组(tuple)
#1.可变不可变对象？序列还是非序列？
#2.操作元祖的方法有多少种，其中哪几个方法使用频率高，并选择1-3个方法进行代码展示
#3.是否可迭代
#4.索引和步长简单展示
#5.特殊的骚操作及用法
#开放题，想到多少写多少，可以通过回顾视频以及查资料的方法完成此题。
#以元祖为例，完成1.2.3即可拿到70%的分数。

#列表list
#1.可变对象，序列类型
#2.11种，append remove reverse的使用频率比较高
li_list = dir(list)
print(len(li_list) - li_list.index('append'))
li_1 = [1,2,3]
li_1.append(4)
print(li_1)
li_1.remove(4)
print(li_1)
#3.可迭代含有'__iter__'
#4.输出第一个元素，第二个元素，间隔一个步长取出[1, 3, 5, 7]
li_2 = [1,2,3,4,5,6,7,8]
print(li_2[1],li_2[2],li_2[::2])
#5
#(1)将列表转化为字符串--->''.join
#(2)列表推导式
li_3 = ['aaa','bbb','ccc']
li_4 = [i for i in range(1,10)]
print(''.join(li_3),li_4)

#函数
#1.函数如何定义
def fun():
        pass
#2.①不传参②必备参数③默认参数④可选参数
#①
def fun2():
        print('hello python')
#②
def fun3(a):
        print('必备参数:',a)
#③
def fun4(a=3):
        print('默认参数:',a)
#④
def fun5(*arg): #将传入的参数包装成元祖
        print('arg:',arg)
def fun6(**kwarg): #将传入的参数包装成字典
        print('kwarg:',kwarg)
#3传参混合使用
#①默认参数，必备参数
def fun7(b,m=2):#必须必备参数在前，默认参数在后
        print('必备参数:',b)
        print('默认参数:',m)
fun7(1,3)
fun7(m=10,b=5)#带上参数名，进行指定传参
#②*arg，默认参数，必备参数
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
#③*arg，**kwarg
def fun11(*arg,**kwarg): #**kwarg必须放到最后
        print('arg:',arg)
        print('kwarg:',kwarg)
fun11() #arg: () kwarg: {}
fun11(1,2,3,4,5)#arg: (1, 2, 3, 4, 5) kwarg: {}
fun11(1,2,3,4,a=1,b=2)#arg: (1, 2, 3, 4) kwarg: {'a': 1, 'b': 2}
#4.return
'如果函数中没有写return其实函数结束的时候，默认执行了return None'
#5.return和print的区别
'''
return ：返回函数运行的结果
print   ：打印输出，只是用来看的
'''
#6.lambda匿名函数
print((lambda x:x+1)(5)) #6




#题2
'''
今天学习了正则表达式，请以所学的知识完成以下要求：
(1)请写出python的变量命名规则    
(2)'00\d'可以匹配 001,002,003等等，
   '\d\d\d'可以匹配010,999,998,666等三位数
    请写出一个正则表达式，它可以匹配python合法的变量名

'''
'''
1.由字母，数字，下划线组成
2.不能以数字开头
3.不能使用关键字
可以使用中文但是不建议使用
'''
import re
import keyword
keys = keyword.kwlist
def check():
        n = input('输入内容')
        if n in keys:
                print('不符合python的变量命名规则 ')
        else:
                m = re.findall(r'^[_a-zA-Z]\w*$',n)
                if m:
                        print('符合python的变量命名规则')
                else:
                        print('不符合python的变量命名规则 ')



#题3
'''
请定义一个类(class),满足以下要求：
    1.这个类，必须含有字符串所有的方法。
    2.这个类有一个统计方法：
        统计输入字符串里，英文字母、空格、数字和其他字符分别出现次数，
        返回值为包含元祖的列表，格式如下：
        参数'delete'
        返回值：[('d',1),('e',3),('l',1),('t',1)]
        (对返回值列表中元祖的顺序无要求)

'''
class ZX(str):
        def statistics(self):
                li_s = []
                li_a = []
                for i in self:
                        li_s.append(i)
                it = iter(set(li_s))
                for j in it:
                        tu = j,li_s.count(j)
                        li_a.append(tu)
                print(sorted(li_a))
zx = ZX('aaabbc13`_!@$     ')
zx.statistics()


#题4
'''
猴子第一天摘下N个桃子，当时就吃了一半，还不过瘾，就又多吃了一个。第二天又将剩下的桃子吃掉一半，又多吃了一个。
以后每天都吃前一天剩下的一半零一个。
到第10天在想吃的时候就剩一个桃子了,
问第一天共摘下来多少个桃子？
(提示:递归函数)
'''
def eat(day):
        if day == 10:
                return 1
        else:
                return (eat(day+1)+1)*2
                
print('一共'+str(eat(1))+'个桃子')


#题5
'''
请定义一个名为titles的函数：
    1.接收一句英文(字符串)作为参数
    2.将这个英文的每个单词转换成有且只有首字母大写的形式
    3.返回转换后的英文句
    4.str.title具有这个功能，但在此题不可使用str.title，请用自己的代码完成。
例如：
>>> titles('this is python.')
'This Is Python.'
>>> titles('i love python')
'I Love Python'
>>> 

'''
def titles(sentence):
        li = sentence.split()
        title = []
        for i in li:
                i = i.capitalize()
                title.append(i)
        title = ' '.join(title)
        return title

def titles_1(strs):
        return ' '.join(i.capitalize() for i in strs.split())

def titles_2(strs):
        a1 = strs.split(' ')
        a2 = list(map(lambda x:x.capitalize(),a1))
        return ' '.join(a2)

#题6
'''
现有一个列表，其中有10个元素，元素均为int类型，列表内的数据是无序。
现在要求我们通过编程将这列表变成一个从小到大排序的列表
请用自己的代码完成。
'''
li = [1,3,2,7,4,8,12,9,35,6]
for i in range(10):
        for j in range(9):
                if li[j] > li[j+1]:
                        li[j],li[j+1] = li[j+1],li[j]
                        
print(li)


#题7
'''
1.写一个猜数字的游戏，要求：系统生成一个随机数（1-10），用户输入数字去猜。
如果输入数 小了 或者 大了，都给于相应提示。如果输入数 与 随机数相等，就提示“ 恭喜您猜对了!”
'''
import random
num = random.randint(1,10)
num_i = int(input('输入你想到的数字：'))
while 1:
        if num_i > num:
                print('大了')
                num_i = int(input('再次输入你想到的数字：'))
        elif num_i < num:
                print('小了')
                num_i = int(input('再次输入你想到的数字：'))
        elif num_i == num:
                print('恭喜您猜对了!')
                break


