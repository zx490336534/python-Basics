#强制类型转换
a = int(1.1)
b = float(1)

c1 = bool(0)
c2 = bool(1)

d = complex(2)

li = [1,2,3]
tu = (1,2,3)
s = 'abc'

li =list(tu)
li = list(s)
#li = list(1) 必须是可迭代对象

tu = tuple(li)
tu = tuple(s)
#tu = tuple(1) 必须是可迭代对象

s = str(li) #"['a', 'b', 'c']"
s = str(tu)#"('a', 'b', 'c')"
s = str(1) #'1'



#字典     键值对 key - values
'''
1.无序-------没有索引
#di[0]
2.key 唯一，不可变
唯一:
di5 = {'a' : 2, 'b' : 3, 'c' : 4, 'a' : 1}
'a' : 2, 'a' : 1->'a' : 1
不可变:
li = [1,2,3]
di6 = {li:55 ,'a' :1}
3.字典可变
'''
#两种定义方式：
#1
di = {'a' : 1}
di3 = {1:2}
type(di) #<class 'dict'>
#2
di2 = dict(a=1)
#di4 = dict(1 = 2)
#SyntaxError: keyword can't be an expression

#字典取值,通过key
di = {'a':1, 'b':2,'c':3}
di['a'] #1
#字典中的添加、修改
di['a'] = 4
di['z'] = 'zx'
di['z'] = 'zx1'
#字典的自带方法
#di.clear()#清空
di2 = di.copy() #复制
id(di2),id(di)#(2398744412096, 2398744917264)生成了一个新的对象
di.fromkeys('asd') #{'a': None, 's': None, 'd': None}
di.get('a')#取值，当key不存在返回空
di.get('b','not found')#当key不存在返回'not found'
di.items() #返回每一个键值对dict_items([('a', 4), ('b', 2), ('c', 3), ('z', 'zx1')])
list(di.items())#[('a', 4), ('b', 2), ('c', 3), ('z', 'zx1')]
di.keys()#dict_keys(['a', 'b', 'c', 'z'])
list(di.keys())#['a', 'b', 'c', 'z']
di.pop('a')#指定弹出key='a'的values
di.pop('w','not found') #弹出key='w'的values如果没有'w'则输出'not found'
di.popitem()#随机弹出一个键值对
di.setdefault('b',12)#key=b的时候如果有values则输出values，没有则添加并返回添加的值
di.update({'a':10,'666':666})#原来存在则更新，没有则添加
di.values()#dict_values([2, 3, 10, 666])
list(di.values())#[2, 3, 10, 666]

#可变对象：list set dict 
#不可变对象：str tuple


#运算符
'''
算术运算符 + ，- ， *， /， %， **，//
赋值运算符：= ，+=，-=， *=，/=，%=， **=
比较运算符：==，!=， >， <， >=，<=
成员运算符：in , not in
身份运算符：is , is not
a = 1
b = a
a is b #True
判断两个名字是否指向同一个对象，当id相同时返回True(==比较运算是判断的值)
    逻辑运算符：and，or，not，优先级 not>and>or
        and(与) 两个条件都满足时才返回True
        or(或)  有一个条件满足了就返回True
        not(非) 取反

 计算顺序：默认地，运算符优先级表决定了哪个运算符在别的运算符之前计算。然而，如果你想要改变它们的计算顺序，你得使用圆括号
    结合规律：运算符通常由左向右结合，即具有相同优先级的运算符按照从左向右的顺序计算
'''
#运算优先级
'''
**                            #幂运算
+   -                         #一元运算符  正负号
*   /   %                     #算术运算符
+  -                          #算术运算符
<  >  <=  >=                  #比较运算符
==  !=                        #比较运算符
=  %=  /=  -=  +=  *=  **=    #赋值运算符
is    is not                  #身份运算符
in    not in                  #成员运算符
not  >  and  > or             #逻辑运算符
'''
