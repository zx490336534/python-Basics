'''第二次作业'''


#1.定义一个列表,lis = [1,2]
#①用至少三种方法往列表里面插值。
#②用至少三种方法替换列表中的某个元素。
#①
lis = [1,2]
lis.append(3)#第一种
lis.extend([4])#第二种
lis.insert(4,5)#第三种
lis += [6] #a+=a不会改变id调用
lis = lis + [6]#a = a + a重新生成了新的对象
#②
lis = [1,2]
#第一种-参考作业一8种
lis[0] = 0
#第二种添加3*删除2=6种
lis.pop()
lis.append(3)
#第三种
del lis[1]
lis.append(3)


#2.s = 'hello python !'   如何把s 中的'python' 替换成'ladygaga'
s = 'hello python !'
s1 = s.replace('python','ladygaga')



#3.①将 s ='hello python !',转换成列表 li=['hello','python','!']
#  ②如何取出li列表里的‘hello’的最后一个字母'o'?
#①
s ='hello python !'
s1 = s.split()
#②
s1[0][-1]
s1[0].endswith('o')


#4有一个列表，列表里6个元素，要求将列表中的每个元素向左移动
#一个位置，第一个元素到列表的最后，然后输出这个列表。
'''test_li1 = [1,2,3,4,5,6]
运行代码后，输出后的列表为test_li2 = [2,3,4,5,6,1]'''
#请问运行的代码该如何写？写出这串代码。
test_li1 = [1,2,3,4,5,6]
test_li1.append(test_li1.pop(0))
test_li2 = test_li1
#5.现有一个列表，请完成下列要求：
list_1 = ['1',['2','nvzhuangdalao', 'Thailander'],
              ['2','Java', 'Python', 'Ruby', 'PHP', ['3','zhaoliying','guanxiaotong','Hi python']],
              ['2','Adam', 'Bart', 'Lisa', ['3','luhan','wuyifan','liyifeng','wangbaoqiang']]
]

# ①打印出Python
# print(?)
print(list_1[2][2])
# ②打印出guanxiaotong,luhan，并将他们添加到list_2
print(list_1[2][5][2])
print(list_1[3][4][1])
list_2 = []
list_2.append(list_1[2][5][2])
list_2.append(list_1[3][4][1])
# ③打印出nvzhuangdalao，并将nvzhuangdalao添加到到list_2.
print(list_1[1][1])
list_2.append(list_1[1][1])
# ④print(list_1[2][5][0])会打印出什么？
#打印出3
print(list_1[2][5][0])
