# 1  判断1 - 100 内能够被 3 和 5 整除的数，用while和for循环来做
i = 1
while i < 100:
    i = i + 1
    if i % 3 == 0 and i % 5 == 0:
        print(i)
print('*' * 10)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 2.定义一个函数，必须包含4种参数形式，然后打印这4个参数，最后返回'OK'。
def fun(*args, a, b=1, **kwargs):
    print('args:', args)
    print('a:', a)
    print('b:', b)
    print('kwargs:', kwargs)
    return 'OK'


fun(1, 2, 3, 4, 5, a=6, b=7, c=1)
print(fun(1, 2, 3, 4, 5, a=6, b=7, c=1))


# 3.定义一个函数，能够输入字典和元组。将字典的值(value) 和 元组的值交换，
#  交换结束后，打印并且返回 字典和元祖。
def fun1(*args, **kwargs):
    print(args, kwargs)
    n = len(args)
    li = []
    for i in range(0, n):
        li.append(kwargs[list(kwargs.keys())[i]])
        kwargs[list(kwargs.keys())[i]] = args[i]
    args = tuple(li)
    print(args, kwargs)


fun1(1, 2, 3, a=4, b=5, c=6)
#fun1(1,2,3,4,a=5,b=6,d=7) 会报错！需要判断元祖和字典的长度



