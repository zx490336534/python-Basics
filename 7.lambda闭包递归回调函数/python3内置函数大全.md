# python3函数大全

```python
#1.abs()	绝对值或复数的模
abs(-1)		>>> 1

#2.all()	接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False
all([1,2,3])	>>> True 

#3.any()	接受一个迭代器，如果迭代器里有一个元素为真，那么返回True,否则返回False
any([0,0])	>>> False

#4.ascii()	调用对象的__repr__()方法，获得该方法的返回值
ascii('ab')   >>> "'ab'"

#5.bin()	将十进制转换为二进制
bin(10)		>>> '0b1010'

#6.bool()	测试一个对象是True还是False
bool([])	>>> False

#7.bytearray()   字节数组 字节是计算机的语言，字符串是人类语言，它们之间通过编码表形成一一对应的关系  
a = 'python'
>>> bytearray(a,'utf8')
bytearray(b'python')
>>> list(bytearray(a,'utf8'))
[112, 121, 116, 104, 111, 110]
>>> b'python'[0]
112

#8.bytes()	将一个字符串转换成字节类型
st = 'python'
a = bytes(st,encoding='utf-8')
>>> a
b'python'

#9.callable()	判断对象是否可以被调用，能被调用的对象就是一个callables对象，比如函数
callable(str)		>>> True

#10.chr()	查看十进制数对应的ASCII字符
chr(10)		>>> '\n'

#11.classmethod()	用来指定一个方法为类的方法，由类直接调用执行，只有一个cls参数,执行类的方法时，自动将调用该方法的类赋值给cls.没有此参数指定的类的方法为实例方法

#12.compile()	将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
'''
将source编译为代码或者AST对象。代码对象能过通过exec语句来执行或者eval()进行求值。
参数source：字符串或者AST（abstract syntax trees）对象。
参数filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
参数model：指定编译代码的种类。可以指定'exec', 'eval', 'single'。
参数flag和dont_inherit：这两个参数为可选参数
'''
st = 'python'
r = compile(st,'<string>','exec')
>>> r	<code object <module> at 0x000001841735E810, file "<string>", line 1>

#13.complex()	创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数是字符串，则不需要指定第二个参数
complex(1,2)	>>> (1+2j)
complex('12')	>>> (12+0j)

#14.copyright()	版权

#15.credits()  支持

#16.delattr()	删除对象的属性

#17.dict()	创建数据字典
dict(a=1)	>>> {'a': 1}

#18.dir()	不带参数时返回当前范围内的变量，方法和定义的类型列表，带参数时返回参数的属性，方法列表

#19.divmod()	分别取商和余数
divmod(5,2)		>>> (2, 1)

#20.enumerate()	返回一个可以枚举的对象，该对象的next()方法将返回一个元组
li = ['a','b','c']
>>> enumerate(li)
<enumerate object at 0x0000018417402558>
>>> list(enumerate(li))
[(0, 'a'), (1, 'b'), (2, 'c')]

#21.eval()	1.将字符串str当成有效的表达式来求值并返回计算结果2.取出字符串中内容
>>> eval("{'a':1}")
{'a': 1}
>>> eval('1 + 2 + 3')
6

#22.exec()	执行字符串或complie方法编译过的字符串，没有返回值
>>> st = '''
z = 4
a = x + y + z
print(a)
'''
>>> exec(st,{'x':0,'y':0},{'y':10,'z':10})
14
>>> st = '''
a = x + y + z
print(a)
'''
>>> exec(st,{'x':0,'y':0},{'y':10,'z':10})
20

#23.exit()  退出

#24.filter()	过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据
'''
filter(function or None, iterable) --> filter object
参数function：返回值为True或False的函数，可以为None
参数iterable：序列或可迭代对象
'''
>>> filter(lambda x:x+1,[1,2])
<filter object at 0x00000184173EAD30>
>>> list(filter(lambda x:x+1,[1,2]))
[1, 2]

>>> filter(lambda x:x>10,[9,12])
<filter object at 0x00000184173EAC88>
>>> list(filter(lambda x:x>10,[9,12]))
[12]

#25.float()	讲一个字符串或整数转换为浮点数
>>> float(11)
11.0

#26.format()	格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法
>>> format(12)
'12'
>>> format(12,'5d')
'   12'

#27.frozenset()	创建一个不可修改的集合
'''
frozenset([iterable])
set和frozenset最本质的区别是前者是可变的，后者是不可变的。当集合对象会被改变时（例如删除，添加元素），只能使用set，
一般来说使用fronzet的地方都可以使用set
'''
>>> frozenset([1,2,3])
frozenset({1, 2, 3})

#28.getattr()	获取对象的属性
'''
getattr(object, name[, default]) -> value
获取对象object名为name的特性，如果object不包含名为name的特性，将会抛出AttributeError异常；如果不包含名为name的特性
且提供default参数，将返回default。
参数object：对象
参数name：对象的特性名
参数default：缺省返回值
'''

#29.globals()	返回一个描述当前全局变量的字典
>>> st = 'python'
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': b'python', 'li': ['a', 'b', 'c'], 'i': 'zip', 'st': 'python', 'r': <code object <module> at 0x000001841735E810, file "<string>", line 1>}

#30.hasattr()	hasattr(object，name)判断对象object是否包含名为name的特性（hasattr是通过调用getattr(object，name)）是否抛出异常来实现的
>>> hasattr(list,'pop')
True

#31.hash()	哈希值hash(object)注意：可哈希的即不可变数据类型，不可哈希即可变数据类型
'''
如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数，在字典查找中，哈希值用于快递比价字典的键。
两个数值如果相等，则哈希值也相等
'''
>>> hash('ab')
2766084925433962145
>>> hash(12)
12

#32.help() 返回对象的帮助文档
'''
调用内建的帮助系统，如果不包含参数，交互式帮助系统将在控制台启动。如果参数为字串，则可以是模块，类，方法等名称，并且帮助页面将会在控制台打印。参数也可以         为任意对象
'''

#33.hex() 将十进制转换为十六进制
hex(16)		>>> '0x10'

#34.id()	返回对象的内存地址
>>> id(1)
1726850144

#35.input()	获取用户输入内容
>>> input('请输入：')
请输入：abc
'abc'

#36.int()	将一个字符串或数值转换为一个普通整数
'''
int(x=0) -> integer
int(x, base=10) -> integer
如果参数是字符串，那么它可能包含符号和小数点。参数base表示转换的基数（默认是10进制）。
它可以是[2,36]范围内的值，或者0。如果是0，系统将根据字符串内容来解析。
如果提供了参数base，但参数x并不是一个字符串，将抛出TypeError异常；
否则，参数x必须是数值（普通整数，长整数，浮点数）。通过舍去小数点来转换浮点数。
如果超出了普通整数的表示范围，一个长整数被返回。
如果没有提供参数，函数返回0
'''
>>> int('12')
12

#37.isinstance()	检查对象是否是类的对象，返回True或False
>>> isinstance('a',str)
True

#38.issubclass()	检查一个类是否是另一个类的子类。返回True或False issubclass(sub, super)
>>> issubclass(str,object)
True

#39.iter()	 返回一个iterator对象
'''
iter(iterable) -> iterator
iter(callable, sentinel) -> iterator
'''
>>> a = iter([1,2,3])
>>> next(a)
1
>>> a = iter([1,2,3,4,5])
>>> b = iter(a.__next__,3)
>>> next(b)
1
>>> next(b)
2
>>> next(b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    next(b)
StopIteration

#40.len()	返回对象长度，参数可以是序列类型（字符串，元组或列表）或映射类型（如字典）
>>> len([1,2,3])
3

#41.license()	软件的历史

#42.list()	列表构造函数
>>> list('abc')
['a', 'b', 'c']

#43.locals()	打印当前可用的局部变量的字典
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': <list_iterator object at 0x00000185CCC2C4E0>, 'b': <callable_iterator object at 0x00000185CCCC8860>}

#44.map()	对于参数iterable中的每个元素都应用fuction函数，并将结果作为列表返回
'''
如果有多个iterable参数，那么fuction函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function函数的参数。
如果一个iterable中元素的个数比其他少，那么将用None来扩展改iterable使元素个数一致。
如果有多个iterable且function为None，map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。
'''
>>> li = [1,2,3]
>>> a = map(str,li)
>>> a
<map object at 0x00000185CCCC8F60>
>>> list(a)
['1', '2', '3']

#45.max()	返回给定元素里最大值
>>> max(1,2,3,4)
4

#46.memoryview()	本函数是返回对象obj的内存查看对象。所谓内存查看对象，就是对象符合缓冲区协议的对象，为了给别的代码使用缓冲区里的数据，而不必拷贝，就可以直接使用
>>> memoryview(b'aabc')
<memory at 0x00000185CCC95408>
>>> list(memoryview(b'abc'))
[97, 98, 99]

#47.min()	返回给定元素里最小值  具体用法跟max()相同
>>> min([1,2,3,4])
1

#48.next()	返回一个可迭代数据结构（如列表）中的下一项
>>> a = iter([1,2,3,4])
>>> next(a)
1

#49.object()	获取一个新的，无特性(geatureless)对象。Object是所有类的基类。它提供的方法将在所有的类型实例中共享

#50.oct() 将十进制转换为八进制
oct(8)		>>> '0o10'

#51.open()	打开文件	open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

#52.ord()	查看某个ascii对应的十进制数
ord('a')	>>> 97

#53.pow()	幂函数pow(x, y, z=None, /)	幂函数,表示取x得y次幂，如果存在第三个参数z，则表示乘方结果对第三个参数取余
>>> pow(2,8)
256
>>> pow(2,8,3)
1

#54.print()	输出函数

#55.property()  类方法可以当作属性调用

#56.quit()	退出

#57.range() 根据需要生成一个指定范围的数字，可以提供你需要的控制来迭代指定的次数
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#58.repr()	将任意值转换为字符串，供计时器读取的形式  

#59.reversed()	反转，逆序对象

#60.round()	四舍五入
>>> round(1.556,2)
1.56

#61.set()	将对象转换成集合

#62.setattr()	与getattr()相对应

#63.slice()	切片功能
>>> li = [1,2,3,4,5,6]
>>> slice(1,3,li)
slice(1, 3, [1, 2, 3, 4, 5, 6])

#64.sorted()	排序
>>> li
[1, 2, 3, 4, 5, 6]
>>> sorted(li,key = int,reverse = True)
[6, 5, 4, 3, 2, 1]

#65.staticmethod()	方便将外部函数集成到类体中,美化代码结构,重点在不需要类实例化的情况下调用方法

#66.str() 将字符类型/数值类型等转换为字符串类型
>>> str(12)
'12'

#67.sum()	求和
>>> sum([1,2])
3

#68.super()	调用父类的方法

#69.tuple()	元组构造函数
>>> tuple([1,2,3])
(1, 2, 3)

#70.type()	显示对象所属的类型
>>> type(1)
<class 'int'>

#71.vars()	本函数是实现返回对象object的属性和属性值的字典对象。如果默认不输入参数，就打印当前调用位置的属性和属性值，相当于locals()的功能。如果有参数输入，就只打印这个参数相应的属性和属性值
>>> class ob:
	i = 1
>>> vars(ob)
mappingproxy({'__module__': '__main__', 'i': 1, '__dict__': <attribute '__dict__' of 'ob' objects>, '__weakref__': <attribute '__weakref__' of 'ob' objects>, '__doc__': None})
>>> a = ob()
>>> vars(a)
{}

#72.zip()	将对象逐一配对
>>> li = [1,2,3]
>>> tu = ('a','b','c')
>>> zip(tu,li)
<zip object at 0x00000185CCD04548>
>>> list(zip(tu,li))
[('a', 1), ('b', 2), ('c', 3)]
>>> dict(zip(tu,li))
{'a': 1, 'b': 2, 'c': 3}
```



*如何获取的：*

```python
>>> li = dir(__builtins__)
>>> li = li[li.index('abs'):]
>>> for i in range(len(li)):
	print('#%s.%s()'%(i+1,li[i]))
```

