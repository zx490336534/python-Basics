# python基础 函数

`教学监督热线：400-1567-315`
`20:30上课!!!`

#### 1.几个可能用到的内置函数

#### 2.lambda匿名函数

#### 3.函数内变量的作用域

#### 4.内嵌函数和闭包

#### 5.递归函数和回调函数



##### 1.常见的内置函数

```python
常见的内置函数:
    查看内置函数：
        print(dir(__builtins__))
    常见函数
    len 求长度
    min 求最小值
    max 求最大值
    sorted  排序
    reversed 反向
    sum  求和

进制转换函数:
    bin()  转换为二进制
    oct()  转换为八进制
    hex() 转换为十六进制
    ord() 将字符转换成对应的ASCII码值
    chr() 将ASCII码值转换成对应的字符
补充：
1.enumerate()   #返回一个可以枚举的对象
2.eval()    #1.将字符串str当成有效的表达式来求值并返回计算结果2.取出字符串中内容
3.exec()    #执行字符串或complie方法编译过的字符串，没有返回值
4.filter() #过滤器
5.map() #对于参数iterable中的每个元素都应用fuction函数，并将结果作为列表返回
6.zip() #将对象逐一配对
```

##### 2.lambda匿名函数

```python
没有函数名的函数
g = lambda x:x+1
lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解  
```

##### 3.函数内变量的作用域     

```python
变量的作用域与其定义的方式有关：
    如果变量在函数内部定义，则变量的作用域在函数内部
    如果变量在具有全局变量的作用域定义，则变量的作用域是全局，全局变量可以在函数内部访问，但是不能改变

    定义在函数内部的变量称为局部变量
    如果在函数内部想修改全局变量，可以用 global 来修饰变量

    nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量  （python3中新增关键字）
```

##### 4.内嵌函数和闭包

    内嵌函数： 在函数内部定义函数，只能在函数内部调用

    闭包：一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量
#####5.递归函数

    函数调用自己本身
#####6.回调函数

    回调函数就是一个通过函数指针调用的函数。如果你把函数的指针（地址）作为参数传递给另一个函数，当这个指针被用来调用其所指向的函数时，
    我们就说这是回调函数。回调函数不是由该函数的实现方直接调用，而是在特定的事件或条件发生时由另外的一方调用的，用于对该事件或条件进行响应。
### 第七次作业

```
1.把老师上课例子都敲一遍（不需要截图，但是一定要做）

2.定义一个函数，输入一个序列(序列元素是同种类型)，判断序列是顺序还是逆序，顺序输出UP，逆序输出DOWN，否则输出None

3.写一个函数，对列表li = [9,8,3,2,6,4,5,7,1]，进行从小到大的排序。最后返回li
```

