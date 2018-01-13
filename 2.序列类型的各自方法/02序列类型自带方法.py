'''
1.基本数据类型 int float bool complex
2.+ = * / // % **
3.序列类型 str list tupe
4.索引 切片 步长
5.赋值运算、成员运算符in 、not in
6.list可变 str、tupe不可变
'''
#列表
li = ['a', 'b', 'c', 'd', 'e']
dir(li)#查看变量内的属性和方法
#带下划线的是属性，不带下划线的是方法
help(li.append)#查看方法的用法

li.append('s') #追加的方式，添加到list最后
#li.clear() #清空list
li.copy() #复制，但是生成了一个新的对象
li.count('a')#统计li中'a'的出现次数
#iterable 可迭代的 有'__iter__'属性即为可迭代
#str list tupe字符串，列表，元祖都为可迭代
li.extend('666')#传入可迭代对象，追加到list
li.index('b')#索引，'b'第一个出现的位置
li.insert(1,'aaa')#L.insert(index, object)在1号位置插入'aaa'
li.pop()#默认弹出最后一个元素
li.pop(0)#弹出下标为0的元素
li.remove('6')#移除找到的第一个指定元素
li.reverse()#列表翻转abc->cba

li.sort() #默认按ascii排序 L.sort(key=None, reverse=False)默认参数
li.sort(key=len) #把li中内容逐个调用len方法后返回值从小到大排序
#key 是指定，按照某一种方法进行排序
#li.sort(key = max) li.sort(key = min)
li.sort(reverse=True)#倒叙





#元祖
tu = ('a','b','c','d')
tu2 = 'a','b'
tu3 = (1,)

dir(tu)
tu.count('a')#统计tu中'a'的出现次数
tu.index('a')#索引，'a'第一个出现的位置
tu.index('d',1,4)#指定范围1:4检索（左闭右开）
tu = list(tu)
tu.pop()
tu = tuple(tu)


#字符串
s = 'I love python'
l1=dir(s)
l2=l1[l1.index('capitalize'):]
len(l2)#44个方法

s.count('o') #o的个数
s.endswith('n')#字符串是否以n结尾，返回True
s.startswith('I')#字符串是否以I结尾，返回True
s.find('I')#返回I索引值，不存在返回-1
s.index('I')#返回I索引值，不存在报错：ValueError
s.isalpha()#全字母返回True，否则False
s.isdigit()#全数字
s.islower()#全小写
s.isupper()#全大写
s.lower()#转换小写
s.upper()#转换大写
s.replace('I','zhong')#替换所有
s.split()#默认以空格分割
s.split('l')#以l进行分割
