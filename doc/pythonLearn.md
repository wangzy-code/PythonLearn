# **Python 安装及调试**
## **安装及使用**
> Cmd中进入python的命令不同，有的电脑是py ，有的是python。
>
>Cmd中的路径切换与git等其他dos命令不同
每一个磁盘（通常情况下就是指硬盘分区C:，D:，E:，F:等等）下都有一个工作目录，初始情况下就是根目录\。比如当前DOS提示符如下：c:\>；这个提示符的意思是当前工作磁盘是C盘，C盘当前工作目录为\（根目录）假如我们现在输入d:将工作磁盘切换到D盘：
c:\>d:
提示符将变成下面这样子：
d:\>
这个提示符的意思是当前工作磁盘是D盘，D盘当前工作目录为\（根目录）
假设我们现在希望从将工作磁盘跟工作目录从D盘的根目录（d:\)切换到C盘根目录下的windows目录(c:\windows)。
可能一开始我们会想到输入cd c:\windows
d:\>cd c:\windows
这时会发现dos提示符仍显示工作目录在D盘的根目录：
d:\>
其实cd c:\windows命令是把c盘的工作目录切换到\windows，但是并没有把工作磁盘从d盘切换到c盘，要切换工作磁盘，应使用命令 [盘符]冒号：
d:\>c:
切换工作磁盘后，dos提示符如下：
c:\windows>
可见，我们已经切换到c盘了，而且由于前面cd c:\windows命令已经将c盘的工作目录切换到\windows，所以切换到c盘的同时进入到了
c盘的工作目录\windows。
## **notepad++中使用python**
>notepad中编辑代码，然后F5运行，提示输入运行命令，输入下面的代码。即可正常运行python
>>cmd /k C:\Programs\Python\Python3\CPython\x64\Python35\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
## **python在vscode中的使用**
[安装指导参考链接](https://xin053.github.io/2016/06/11/VS%20Code%E6%90%AD%E5%BB%BAPython%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83/)
>
>1.安装python插件,打开VScode，Ctrl+p,输入 "ext install python"，搜索时间可能会比较长
>
>2.设置环境变量，将python的路径添加到环境变量path中。
>
>3.vscode加载文件夹。
>>&ensp;&ensp; vscode 加载文件夹，该文件夹就可以算是一个工作空间，VS Code会在该文件下新建<span style="color: red"><.vscode></span>文件夹
>>
>>&ensp;&ensp; 里面存放的是该工作空间的配置文件，所以以后在该工作空间下的任何代码都会使用该配置文件。
>>
>>&ensp;&ensp; 该文件夹可以再vscode中的资源管理其中看到。
>>
> 4.添加py文件，根据错误提示安装其他插件，更新插件等。既完成配置。
>
> 5.利用vscode工具实现断点调试等。
>
## **python与opencv在vscode中的使用**
>1.将Opencv3.0安装目录下opencv\build\python\2.7\x64\cv2.pyd复制到python安装目录Lib\site-packages下。
>
>2.新建一个py文件，在cmd中执行如下代码 pip install numpy 如果运行失败，就多运行几次，知道安装成功。过程中可能要更相关的软件，直接更新就好。
>
>3.运行如下程序：

```
import cv2  
	filename=u"E:\\图库\\abc.jpg"
	img = cv2.imread(filename.encode('gbk'))
	cv2.namedWindow("Image")  
	cv2.imshow("Image", img)  
	cv2.waitKey (0)  

```
如果提示dll load failer  则需要执行 pip install F:\IMAGEPROCESS\PythonLearn\softWare\opencv\opencv_python-3.0.0-cp35-none-win_amd64.whl安装whl文件
>
>4.pip install jedi 安装后可以自动补全cv2.内的函数。
>
## **python调试**
* help(print) 会输出print函数的帮助信息

# **Python 基础**

## **python中的输出Print：**
print函数输出的规则：

* 不同类型的值和变量等之间的共同输出用逗号 ， 隔开；

* 实际输入时，各值之间有一个空格隔开，如下所示。该空格由分隔符<span style="color: green">分隔  sep</span>决定

* 实际输出字符串末尾是会有个回车。可以用<span style="color: green">结束符seend</span>进行设置

* 可以值输出到文件中，利用固定open命令及<span style="color: green">file</span>file

```
print('age', age)

输出:   age 18

print('age', age, sep='')  # 去掉空格

输出:   age18
```

## **python中的list**

### **list 初始化**
> 1.利用range赋值  L = list(range(1，100)) 
>> 两个都是小括号
>>
>>range(1，100)上下限之间用逗号，小于等于1，大于100，没有等于100.
>
> 2.直接赋值 L=['A','B','C']  
>> 用中括号，而不是小括号
>
> 3.创建空的list，r=[],利用append赋值 r.append('a') 
>
### **list 访问**
> 与tuple类似，可以通过下标访问L[0]
>
> 通过小标切片，L[1:40] , L[-5,-2], L[:50],L[::50]
>>L[1:40] 取第2到第39个元素组成新的list
>>
>>L[-5,-2]取导数第2 到导数第5个元素
>>
>>L[:50] 取前49个元素
>>
>>L[::50]每个50个值取一次，取所有元素
### **list 遍历**
>1.用list变量名字遍历 for i in list:  
>> list 不是关键字,list没有关键字
>>
>>该访问的方式，i相当于list[0],list[1]...等其中一个。所以list[i]是有问题的
>>
>>输出该值用 print ("序号：%s   值：%s" % (list.index(i) + 1, i))
>>
>2.用list长度遍历 for i in range(len(list)):
>
>> 计算长度用len(list)
>>
>>计算长度后还要用range求上限,i在这个范围内
>>
>> print ("序号：%s   值：%s" % (i, list[i]))
>>
>3.列表生成式的方法  print ([x+1 for x in list])
>>对x进行循环，然后得到x+1构成的list，for 前面的变量必须在for后声明
>>
### **列表生成式**

> 生成列表

  如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？循环 或 列表生成式

```
 L =[]
 for x in range(1, 11):
     L.append(x * x)  --> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
```
[x * x for x in range(1, 11)] --> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

  这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。

  写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来，十分有用。

> 条件过滤

  如果我们只想要偶数的平方，不改动 range()的情况下，可以加上 if 来筛选：有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。
```
 [x * x for x in range(1, 11) if x % 2 == 0] --> [4, 16, 36, 64, 100]

```
> 多层表达式

  for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。对于字符串 'ABC' 和 '123'，
可以使用两层循环，生成全排列：
```
[m + n for m in 'ABC' for n in '123'] -->['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

```
# **Python 函数式编程**
函数式编程（请注意多了一个“式”字）Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

## **高阶函数**
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
>**变量可以指向函数**,并且可以用这个变量来调用这个函数。例如绝对值函数abs
```
f = abs
f(-10)
```
>**函数名也是变量**，如果把该变量指向其他变量，则该变量原来指向的函数则不可以通过这个变量调用。
```
abs = 10
abs(-10) --> Traceback (most recent call last):File "<stdin>", line 1, in <module>TypeError: 'int' object is not callable
```
以上只为了说明问题，实际不可以这么操作。由于abs函数定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用以下代码：
```
import builtins
builtins.abs = 10
```
>
>**传入函数**，一个函数可以接受另一个函数作为参数
```
def add(x, y, f):
    return f(x) + f(y)
```


# **Python 模块**
python中模块module是一个python文件，以.py结尾。模块能定义函数，变量，类等，可以对照.cpp理解，可以更好的

管理代码。将功能相近或相关的函数，类等放在一个py文件中。
## **collections模块**

### **1. Iterable 和iterator**
> Iterable 判断是否可以迭代。凡是可以for循环的，都是Iterable。

```
from collections import Iterable
isinstance({}, Iterable) --> True
isinstance((), Iterable) --> True
isinstance(100, Iterable) --> False
```
> Iterator 判断是不是迭代器。凡是可以next()的，都是Iterator。集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但通过iter()函数获得一个Iterator对象
```
from collections import Iterator
isinstance({}, Iterator)  --> False
isinstance((), Iterator) --> False
isinstance( (x for x in range(10)), Iterator)  --> True
isinstance(iter('abc'), Iterator)  --> True

```
>list 为什么不是迭代器。
>>Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的

## **sys模块**
导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。