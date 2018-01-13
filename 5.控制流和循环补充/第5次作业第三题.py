#3.流量套餐订购小程序：1.运行程序后，提示输入你现有的话费余额。
#                      2.输入余额后打印套餐列表，列表使用第二题的prd_l1。
#                      3.用户可以根据套餐编号订购套餐，如果余额足够则打印出扣款金额和话费余额，余额不够则提示用户余额不够。
#                      4.在输入套餐编号阶段，用户可以通过输入e退出订购程序，退出时，打印出已订购套餐和余额。
prd_l1 = [
    ('小时包流量1G/小时',5),
    ('日包流量1G/日',10),
    ('月末嗨翻天10天10G',20),
    ('闲时流量1G/月',10),
    ('30元5个G',30),
    ('50元50个G',50),
]
shopping_l2 = []
phone_fare = input('请输入你现有的话费余额')
phone_fare = int(phone_fare)
for i,info in enumerate(prd_l1):
        print('编号',(i),'\t',info[0],'\t',info[1],'元')
print('退出请按e')
while 1:
        user_want = input('请输入想要订购的套餐编号')#用户选择
        if user_want.isdigit():
                user_want = int(user_want)
                if user_want >=0 and user_want < len(prd_l1):
                        prd = prd_l1[user_want]
                        if phone_fare >= prd[1]:
                                shopping_l2.append(prd)
                                phone_fare -= prd[1]
                                print('套餐订购成功，已支付金额%s元，当前话费余额%s'%(prd[1],phone_fare))
                        else:
                                print('余额不足,退出请按e')
                else:
                        print('编号不存在，请输入正确商品编号')
        elif user_want == 'e':
                for p in shopping_l2:
                        print(p)
                print('当前话费余额是：',phone_fare)
                exit()
        else:
                print('输入不合法,退出请按e')
