#正则、re模块
#回忆
'''
1、列表推导式li = [i for i in range(10)]
2、迭代器、生成器
迭代器：__iter__  __next__
生成器：yield next() __next__()
3、模块、包
py文件    import      from xxx import xxx
第三方模块：同目录下：import
                    不同目录下：import sys
                    sys.path.append()
包：装有很多py文件的文件夹
'''

#正则（不是python特有的）匹配字符串
#需求：输入字符串，判断字符串中有没有python这个单词
'''
a = input('输入：')
b = 'python'
if b in a:
        print('OK')
else:
        print('NO')

import re
a = input('输入：')
b = re.search('python',a)#搜索匹配，匹配到第一个
#<_sre.SRE_Match object; span=(6, 12), match='python'>
#如果没有匹配到返回None
if b:
        print('OK')
else:
        print('NO')
'''

#需求：判断是否是QQ号（5-11）
import re
qq = input('输入QQ：')
b = re.search('[0-9]{5,11}',qq)
if qq:
        print('OK')
else:
        print('NO')


#元字符(有了特殊的意义)
'.   ^   $   *   +   ?   {}  []   \   |   ()'
#大多数字母和字符会匹配它们自身，有少数特殊字符不能匹配自身称为元字符

#子组匹配和模式重复次数等
#.    匹配除换行符之外的所有的字符
re.search('.','asfa')#<_sre.SRE_Match object; span=(0, 1), match='a'>
re.search('.','\nbs')#<_sre.SRE_Match object; span=(1, 2), match='b'>
#\d   匹配0~9的数字
re.search('\d','asf1')#<_sre.SRE_Match object; span=(3, 4), match='1'>
re.findall('\d','aa1asd1234')#查询所有，返回列表['1', '1', '2', '3', '4']
#\s    匹配任意的空白符，包括空格，制表符(Tab)，换行符等
re.findall('\s','     \n\n\tasa')#[' ', ' ', ' ', ' ', ' ', '\n', '\n', '\t']
#\w  匹配字母或数字或下划线或汉字等 
re.findall('\w','ad我__65!@#$%^&*()_+')#['a', 'd', '我', '_', '_', '6', '5', '_']
#\b   表示单词的边界 边界：特殊字符 空格 末尾
re.findall('\bapple\b','apple apple')#不会匹配
re.findall(r'\bapple\b','apple apple')#需要加r取消字符串转义
re.findall(r'apple\b','apple apple 555apple')#['apple', 'apple', 'apple']
re.findall(r'\bapple','apple apple 555apple')#['apple', 'apple']
#\.     表示匹配点号本身 正则里面如何取消转义
re.findall('\.','asf...')#['.', '.', '.']#取消元字符的转义
re.findall(r'\\b',r'apple++\b')#['\\b']
#\D、\S、\W、\B     是与小写的相反的作用
#\D 不匹配数字
#\S 不匹配任意的空白符，包括空格，制表符(Tab)，换行符等
#\W  不匹配字母或数字或下划线或汉字等
#\B   表示单词的边界
re.findall(r'\Baa\B',' daad') #['aa']
#^   脱字符，匹配输入字符串的开始的位置
re.findall(r'^abc','abcd')#['abc']
re.findall(r'^abc','bcd')#[]
#$    匹配输入字符串的结束位置，解除元字符的特殊功能例
re.findall(r'gc$','agc')#['gc']
re.findall(r'gc$','agcd')#[]



#匹配次数
#{M,N}    M和N 为非负整数，其中M<=N 表示前面的匹配M~N次
re.findall(r'\d{1,3}','22bvc33sf556asf1111')#['22', '33', '556', '111', '1']
#{M，}    表示需要匹配M次
re.findall(r'\d{3,}','22bvc33sf556asf1111')#['556', '1111']
#{，N}    等价于{0~N}
re.findall(r'\d{,2}','22b4sf1')#['22', '', '4', '', '', '1', ''] 匹配次数为0的时候末尾加空格
#{N}      表示需要匹配N次
re.findall(r'\d{2}','22b44sf111')#['22', '44', '11']
#*      匹配前面的子表达式零次或多次，等价于{0，}
re.findall(r'\d*','22b4sf1')#['22', '', '4', '', '', '1', '']
#+     匹配前面的子表达式一次或多次，等价于{1，}
re.findall(r'\d+','22b4sf1')#['22', '4', '1']
#?      匹配前面的子表达式零次或一次，等价于{0,1}
re.findall(r'\d?','22b4sf1')#['2', '2', '', '4', '', '', '1', '']
 #注：*？、+？、{n,m}?  贪婪与懒惰
re.findall(r'\d*?','22b4sf1')#['', '', '', '', '', '', '', '']
re.findall(r'\d+?','22b4sf1')#['2', '2', '4', '1']
re.findall(r'\d{2,4}?','22b4sf1')#['22']取小值



#子组匹配
# [ ]      字符类，将要匹配的一类字符集放在[]里面
re.findall(r'[0-9]','22b4sf1')#['2', '2', '4', '1']
re.findall(r'[a-zA-Z]','22b4sf1AD')#['b', 's', 'f', 'A', 'D']
re.findall(r'[a-zA-Z0-9]','22b4sf1AD')#同下
re.findall(r'[a-zA-Z\d]','22b4sf1AD')#['2', '2', 'b', '4', 's', 'f', '1', 'A', 'D']
re.findall(r'[a-zA-Z\d]{2}','22b4sf1AD')#['22', 'b4', 'sf', '1A']
re.findall(r'[a-zA-Z]{2}','22b4sf1AD')#['sf', 'AD']
re.findall(r'[^a]','abc')#['b', 'c'] 代表取反，返回非a
# | 或
re.findall(r'b|a','abc')#['a', 'b']
re.findall(r'[ba]','abc')#同上等价


#分组 ()
re.findall(r'(abc)','abc bac kkk') #['abc']
re.findall(r'(abc)*','abc bac abcabckkk')#['abc', '', '', '', '', '', 'abc', '', '', '', '']




#re模块
#re模块的常用方法
#re.compile()   编译正则表达式为模式对象
a = re.compile(r'\d')#re.compile('\\d')
a.findall('asd123')#['1', '2', '3']
#match()        判断一个正则表达式是否从开始处匹配字符串
#相当于^脱字符
re.match(r'\d','123adc')#<_sre.SRE_Match object; span=(0, 1), match='1'>
re.match(r'\d','abc123')#None
#search()       遍历字符串，找到正则表达式匹配的第一个位置  
#findall()       遍历字符串，找到正则表达式匹配的所有位置并以列表的形式返回
#sub()            替换 类似于字符串中 split() 方法  
re.sub('i','o','pyiii')#'pyooo'默认替换所有 可以指定
re.sub('i','o','pyiii',1)#只替换1个


#查看匹配对象中的信息  
# group()        返回匹配到的字符串
c = re.search(r'\d','b35f3')#<_sre.SRE_Match object; span=(1, 2), match='3'>
c.group()#'3'
c.start()#1--返回开始位置
c.end()#2--返回结束位置
c.span()#(1, 2) 索引位置
