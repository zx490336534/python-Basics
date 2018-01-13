#Os模块
import os

#环境变量函数
os.name #如果是windows操作系统返回’nt’，如果是其他系统则返回‘posix’
os.environ#返回系统的环境变量，以字典dict形式显示

#文件操作函数
os.getcwd()#返回当前工作目录
os.chdir('E:\\')#改变工作目录os.getcwd()=='C:\\'

##列举指定目录中的文件名
os.listdir(path='.')#‘.’表示当前目录
os.listdir(path='..')#’..’代表上一级目录

##创建文件夹
os.mkdir('zx')#在当前工作目录创建一个zx文件夹，如果文件夹存在则报错
os.makedirs(r'666\777\888\999')#递归创建多层目录，如果该目录已经存在则抛出异常

##删除
os.remove('zx.png')#删除文件
os.rmdir('666')#删除单层目录，如改目录非空则抛出异常
os.removedirs(r'666\777\888\999')#递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常。
os.rename('zx','zx111')#将文件old 重命名为new，文件和目录都使用这条命令

#os.path
os.path#<module 'ntpath' from 'C:\\Python3\\lib\\ntpath.py'>
os.path.basename('C:\\Python3\\lib\\ntpath.py')#返回文件名'ntpath.py'
os.path.dirname('C:\\Python3\\lib\\ntpath.py')#返回路径'C:\\Python3\\lib'
os.path.join('C:\\Python3\\lib','ntpath.py')#'C:\\Python3\\lib\\ntpath.py'
os.path.split('C:\\Python3\\lib\\ntpath.py')#('C:\\Python3\\lib', 'ntpath.py')
os.path.getsize('zx.png')#返回指定文件的尺寸，单位是字节
os.path.getatime('zx.png')#1504760575.9185095返回指定文件最近的访问时间
os.path.getctime('zx.png')#返回指定文件创建时间
os.path.getmtime('zx.png')#返回指定文件最新的修改时间

#返回True或False的函数
os.path.exists('zx.png')#判断指定路径（目录或文件）是否存在
os.path.isabs('zx.png')#False
os.path.isabs('C:\\')#True    判断指定路径是否为绝对路径
os.path.isdir('C:\\')#判断指定路径是否存在且是一个目录
os.path.isfile('zx.png')#判断指定路径是否存在且是一个文件



#shutil模块
import shutil

#复制文件
shutil.copyfile('zx.png','aa.png')
shutil.copy('zx.png','aa.png')
shutil.copy('zx.png','zx')#前者必须为文件，后者可以为文件、目标目录
shutil.copytree('zx','zzzzz')#复制文件夹，后者必须不存在
shutil.move('zx','\zzzzz')#移动前者到后者里面
shutil.rmtree('\zzzzz')#删除非空目录，空目录


#sys模块
import sys
sys.argv#['C:/Users/zhongxin/Desktop/模块笔记.py']
#用来向python解释器传递参数，名曰“命令行参数”
sys.exit()#退出当前程序
sys.stdout#<idlelib.run.PseudoOutputFile object at 0x0305B3D0>
sys.path#列表返回python目录下所有.pth路径文件下的内容集系统默认设置。
#可以通过列表的操作对其进行修改，不过这种更改只对当前的程序起作用。



#time模块
import time
time.localtime()
#time.struct_time(tm_year=2017, tm_mon=11, tm_mday=3, tm_hour=16, tm_min=41, tm_sec=55, tm_wday=4, tm_yday=307, tm_isdst=0)
for i in range(len(time.localtime())):
      print(str(i)+'     '+str(time.localtime()[i]))
'''
0     2017年
1     11月
2     3日
3     16时
4     45分
5     2秒
6     4星期几0~6(0代表星期一)
7     307一年中的第几天
8     0 是否为夏令0，1，-1(-1代表夏令时)
'''
time.asctime(time.localtime())#返回一个可读的时间格式'Fri Nov  3 16:47:41 2017'
time.clock()#用以浮点数计算的秒数返回当前的cpu时间,用来衡量不同程序的耗时
time.time()#返回当前时间的时间戳
#时间戳(timestamp)表示的是从1970年1月1日00：00：00开始按秒计算的偏移量
time.asctime(time.gmtime(0))#'Thu Jan  1 00:00:00 1970'
time.sleep(2)#推迟调用线程的运行，secs的单位是秒

