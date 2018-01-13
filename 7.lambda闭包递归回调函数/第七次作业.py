#python基础   第七次作业


#1.把老师上课例子都敲一遍（不需要截图，但是一定要做)
'''
|<<   >>|      鹏保宝播放器这两个按钮可以倍速播放  
'''


#2.定义一个函数，输入一个序列(序列元素是同种类型)，
#判断序列是顺序还是逆序，顺序输出UP，逆序输出DOWN，否则输出None

def order(li):
    li = list(li)
    print(li)
    if li == sorted(li,reverse = False) or li == sorted(li,reverse = True):
        if li[0] > li[len(li)-1]:
            print('DOWN')
        else:
            print('UP')
    else:
        print('None')

#正确答案
def judge_seq(seq): #seq代表序列
    se = list(seq)
    print(se)
    if sorted(se) == se:
        return 'UP'
    elif sorted(se,reverse=True) == se:
        return 'DOWN'
    else:
        return 'None'

#3.写一个函数，对列表li2 = [9,8,3,2,6,4,5,7,1]，进行从小到大的排序。最后返回排序后的列表
li2 = [9,8,3,2,6,4,5,7,1]

def li_sort(li):
    li.sort()
    return li

def order2():
    print(sorted(li2))

def order3():
    len_li = len(li2)
    for i in range(0,len_li):
        for j in range(0,len_li-1):
            if li2[j] > li2[j+1]:
                li2[j],li2[j+1] = li2[j+1],li2[j]
            else:
                pass
    print(li2)

def order_f(li):
    result = []
    for i in range(len(li)):
        result.append(min(li))
        li.remove(min(li))
    print (result)

#4一个列表，有4个由数字组成的长度为4的元组，对这四个元组，
#按每个元组的第2个数字大小排序
li3 = [(1,2,3,4),(3,4,5,6),(1,6,2,3),(7,5,4,2)]
#正确答案！！！！！！！
print(li3)
li3.sort(key=lambda a:a[1])
print(li3)
#麻烦答案！！！！！
def order4():
    for i in range(0,4):
        for j in range(0,3):
            if list(li3[j])[1] > list(li3[j+1])[1]:
                list(li3[j])[1],list(li3[j+1])[1] = list(li3[j+1])[1],list(li3[j])[1]
                li3[j],li3[j+1] = li3[j+1],li3[j]
            else:
                pass
    print(li3)
    

#5思考题：有一个名为list_apd的函数，
#如下所示，请你多次调用这个函数，对比返回值，是否与你预期的一致？
#想到什么写什么，可以空着
def list_apd(b,a=[]):
    a.append(b)
    return a
list_apd(2)
list_apd(4)
list_apd(6)#如果不写上a的值那么就会一直往list中append
#[2,4,6]
list_apd(1,[2,3,4])#如果写上a的值那么就会清空list并往里面append一个b的值
#[2,3,4,1]
list_apd(5)#结果是[2,4,6,5]
list_apd(1,[2,3,4])#[2,3,4,1]
list_apd(5)#[2,4,6,5,5]



















