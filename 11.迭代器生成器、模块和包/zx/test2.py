#test 模块
def test():
        print('this is test')
        a = 'test'
        return a

test1 = 'this is test1'

if __name__ == '__main__': #我自己调用才会执行
        print('main')
        test()
