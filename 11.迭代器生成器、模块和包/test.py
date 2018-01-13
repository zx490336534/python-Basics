#test 模块
import sys
def test():
        print('this is test')
        a = 'test'
        return a

test1 = 'this is test1'

if __name__ == '__main__': #我自己调用才会执行
        print('main')
        sys.argv
        print(sys.argv)
        print(sys.argv[1])
        print(sys.argv[2])
        test()
