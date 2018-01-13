#第五次作业    控制流程



#1.用本节课学过的知识，输出9*9 乘法口诀表。
print('='*20,'#1','='*20)
for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d ' %(i,j,(i*j)),end=" ")
    print()



#2.输入help(enumerate)学习怎么使用enumerate.试着对prd_l1使用enumerate()这个内置函数。（提示：使用for
# 循环）
b = [1,2,3,4]
c = enumerate(b) #|(0,1),(1,1),(2,3),(3,4)|
print('='*20,'#2','='*20)
prd_l1 = [
    ('小时包流量1G/小时',5),
    ('日包流量1G/日',10),
    ('月末嗨翻天10天10G',20),
    ('闲时流量1G/月',10),
    ('30元5个G',30),
    ('50元50个G',50),
]

for i,info in enumerate(prd_l1):
    print('编号',(i+1),'\t',info[0],'\t',info[1],'元')




#3.流量套餐订购小程序：1.运行程序后，提示输入你现有的话费余额。
#                      2.输入余额后打印套餐列表，列表使用第二题的prd_l1。
#                      3.用户可以根据套餐编号订购套餐，如果余额足够则打印出扣款金额和话费余额，余额不够则提示用户余额不够。
#                      4.在输入套餐编号阶段，用户可以通过输入e退出订购程序，退出时，打印出已订购套餐和余额。
print('='*20,'#3','='*20)
money = input('输入你现有的话费余额')
money =int(money)
for i,info in enumerate(prd_l1):
    print('编号',(i+1),'\t',info[0],'\t',info[1],'元')
choice = input('请输入套餐编号订购套餐')
choice = int(choice)
need = 0
while choice:
    if choice == 1:
        need = 5
        choice = input('输入e退出订购程序，输入非e重新选择套餐')
        if choice == 'e':
            break
        else:
            choice = input('重新选择套餐')
        choice = int(choice)
        continue
    elif choice == 2:
        need = 10
        choice = input('输入e退出订购程序，输入非e重新选择套餐')
        if choice == 'e':
            break
        else:
            choice = input('重新选择套餐')
        choice = int(choice)
        continue
    elif choice == 3:
        need = 20
        choice = input('输入e退出订购程序，输入非e重新选择套餐')
        if choice == 'e':
            break
        else:
            choice = input('重新选择套餐')
        choice = int(choice)
        continue
    elif choice == 4:
        need = 10
        choice = input('输入e退出订购程序，输入非e重新选择套餐')
        if choice == 'e':
            break
        else:
            choice = input('重新选择套餐')
        choice = int(choice)
        continue
    elif choice == 5:
        need = 30
        choice = input('输入e退出订购程序，输入非e重新选择套餐')
        if choice == 'e':
            break
        else:
            choice = input('重新选择套餐')
        choice = int(choice)
        continue
    elif choice == 6:
        need = 50
        choice = input('输入e退出订购程序，输入非e重新选择套餐')
        if choice == 'e':
            break
        else:
            choice = input('重新选择套餐')
        choice = int(choice)
        continue
    elif str(choice) == 'e':
        break
    else:
        print('请输入正确的套餐号，或者输入e退出订购程序')
        continue
if money - need > 0:
    print('扣款金额%d,话费余额%d' % (need,(money-need)))
elif money - need < 0:
    print('您的余额不足')


