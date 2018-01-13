#条件语句
'''
if（如果） A :

	就 B（当A为True）

elif（或者） C :

	就 D（当A为False并且C为True）

else（否则） :
	就E（当A和C都为False）
'''
'''
需求：1、年龄大于12买成人票
          2、4-12儿童票
          3、0-3不需要买票
          4、年龄大于60岁不需要买票

'''
#输入年龄进行判断
b = input('请输入') #接收的内容会变成字符串
b = int(b)
a = b
if a>=12:
        if a >=60:
                print('您好，您的年龄 %s岁，不需要买票' % a)
        print('你好先生，你需要购买成人票')
elif a>=4 and a<12:
        print('你好小朋友，你需要购买儿童票')
else:
        print('你好baby，你不需要买票')

#随机生成年龄进行判断
import random
r = random.randint(0,100) #输出一个0~100之间的随机数
print('随机数:',r)
a = r
if a>=12:
        if a >=60:
                print('您好，您的年龄 %s岁，不需要买票' % a)
        print('你好先生，你的年龄 %s岁，你需要购买成人票' % a)
elif a>=4 and a<12:
        print('你好小朋友，你的年龄 %s岁，你需要购买儿童票' % a)
else:
        print('你好baby，你的年龄 %s岁，你不需要买票' %a)

##pass 占位，什么都不干
a = 1
b = 2
if a>b:
        pass
elif a<b:
        pass
else:
        pass
if a>b:
        print('a大于b')
elif a<b:
        print('a小于b')
else:
        print('a等于b')

#循环语句 while for
#while
'''
while 判断语句A:
    执行语句B
'''
'''
死循环：
while True:
        print('hello')
'''
a = 1
while a < 5:    #写while循环的时候一定要有终止条件
        print('hello',a)
        a += 1
print('='*10,'break','='*10)
#break 强行终止循环 相当于ctrl + c
b = 0
while True:
        print('hello',b)
        if b > 5:
                break
        b += 1
print('='*10,'continue','='*10)
#continue 跳过本次循环，进入下一个循环
#打印处10以内的奇数
m = 0
while m < 10:
        m += 1
        if m % 2 == 0:
                continue
        print(m)



#for 循环
range(10)#表示一个范围，左闭右开0-9
list(range(10))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(5,10))#[5, 6, 7, 8, 9]
list(range(5,10,2))#[5, 7, 9]
print('='*10,'for','='*10)
for i in range(10):
        print(i)
print('='*10,'列表','='*10)
#列表
li = ['a', 'b', 'c']
for f in li:
        print(f)
print('='*10,'字符串','='*10)
#字符串
for s in 'abcdefghijk':
        print(s)
#字典
print('='*10,'字典','='*10)
di = {'ai':1,'bi':2,'ci':3}
for d in di:
        print(d)
        print(di[d])
print('='*10,'10以内的奇数','='*10)
#for 10以内的奇数
for i in range(1,11):
        if i %2 == 0:
                continue
        print(i)

#嵌套循环 5小组，每个8位同学
print('='*10,'for+for','='*10)
for i in range(5):
        print('第%s个小组' % (i+1))
        for j in range(8):
                print('第%s小组,第%s位同学' % ((i+1),(j+1)))

print('='*10,'for+while','='*10)
for i in range(5):
        print('第%s个小组' % (i+1))
        n = 1
        while n <= 8:
                print('第%s小组,第%s位同学' % ((i+1),(j+1)))
                n += 1

##else   只有正常结束的循环，非break结束的循环才会执行else部分
a = 0
while a < 10:
        print(a)
        a += 1
else:
        print('while 循环正常退出')

b = 0
while b < 10:
        print(b)
        b+= 1
        if b > 5:
                break    
else:
        print('while 循环正常退出')


for i in range(10):
        print(i)
else:
        print('for 循环正常结束')

for j in range(10):
        print(j)
        if j > 5:
                break
else:
        print('for 循环正常结束')
