#第十次 作业：
'''

'''

#1.打开文件，修改内容，写入另一个文件。
#  把文件reform.txt中的名人名言改成“某某说：......”的形式保存到另一个文件中。
'例：雨果说：大胆是取得进步所付出的代价。'
f1 = open('reform.txt','r')
f2 = open('zx.txt','w+')
li = f1.readlines()
li_1 = []
##n = 1
##while n:
##      try:
##            li.remove('\n')
##      except Exception:
##            n = 0
##for i in range(0,len(li)):
##      li_1.append(li[i].split('——'))
##      t = li_1[i][1]
##      li_1[i][1] = li_1[i][1][:len(t)-1]
##for j in range(0,len(li_1)):
##      f2.write('%s说：%s\n\n' % (li_1[j][1],li_1[j][0]))
li =li[::2]
for i in li:
      said,who = i.split('——')
      who = who.replace('\n','')#拿掉\n
      f2.write(who+'说：'+said+'\n\n')
     
f1.close()
f2.flush()
f2.close()
      
#2.针对实例化矩行类时，输入字符串等错误参数，写一个提示异常。
#第一种方法
class Rectangle1:
    def __init__(self,length,width):
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
        #if ( type(length) == int or  type(length) == float )  and (type(width) ==int or type(widh) == float):
            self.length = length
            self.width = width
        else:
            raise TypeError('666')
    def area(self):
        return self.length * self.width


def f(rr):
      if rr < 1:
            raise Exception('zzzzz',rr)#抛出异常
#第二种方法
class Rectangle2:
    def __init__(self,length,width):
      assert isinstance(length,(int,float)) and isinstance(width,(int,float)),'非int float类型'
      self.length = length
      self.width = width

    def area(self):
        return self.length * self.width


def asse(s):
      assert s != 0, 's is zero'#s为非0数字则True，不报错，s=0False报错
      return 10/s
#第三种方法
class Rectangle3:
      def __init__(self,length,width):
            try:
                  if isinstance(length,(int,float)) and isinstance(width,(int,float)):
                        self.length = length
                        self.width = width
                  else:
                        raise TypeError
            except Exception:
                  print('not ok')
      def area(self):
            return self.length * self.width
