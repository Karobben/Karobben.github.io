---
title: "Python hello world"
description: "Really fundamental codes for python"
url: base2
date: 2020/01/22
toc: true
excerpt: "Basic grammar of python"
tags: [Python, Script]
category: [Python, Beginner]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Integer/Float calculation

```python
#######################
########## caculating #
#######################
Operator   Description   Example
+   Addition operator   100 + 45 = 145
-   Subtraction operator   500 - 65 = 435
*   Multiplication operator   25 * 4 = 100
/   Float Division Operator   10 / 2 = 5.0
//   Integer Division Operator   10 / 2 = 5
**   Exponentiation Operator   5 ** 3 = 125
%   Remainder Operator   10 % 3 = 1  #  10 / 3 = 3 ... 1
```
### Float formate
```python
##########print##########

pi = 3.141592653
print('%10.3f' % pi) #字段宽10，精度3
## 3.142
print("pi = %.*f" % (3,pi)) #用*从后面的元组中读取字段宽度或精度
## pi = 3.142
print('%010.3f' % pi) #用0填充空白
## 000003.142
print('%-10.3f' % pi) #左对齐
## 3.142
print('%+f' % pi) #显示正负号
## +3.141593
```

## List
```python
## duplicats removing
A = [1,1,1,2,3,4,3]
print(A)
```

### Remove duplicates from list
```python
list(set(A))
```

## int list to str list
```python
[str(x) for x in int_list]
```
or
```python
a_list = ["1", "2", "3"]
##int list to str list
list(map(str, a_list))
##str list to int list
list(map(int, a_list))
```
### 逐个相减
```python
c = [b[i] - a[i] for i in range(len(a))]
```

### Compare Two list

```python
l = [1, 2, 3, 5]
l_one = [2, 8, 6, 10]
print set(l) & set(l_one)
```


## Time

```python
import time
print(time.time())
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
```

### Date caculating

[zhengxiangwen 2017](https://blog.csdn.net/zhengxiangwen/article/details/55157697)
```python
import datetime #导入日期时间模块
today = datetime.date.today() #获得今天的日期
print today #输出今天日期
2016-01-25
yesterday = today - datetime.timedelta(days=1) #用今天日期减掉时间差，参数为1天，获得昨天的日期
print yesterday
2016-01-25
tomorrow = today + datetime.timedelta(days=1) #用今天日期加上时间差，参数为1天，获得明天的日期
print tomorrow
2016-01-25
print "昨天:%s， 今天:%s， 明天：%s" % (yesterday, today, tomorrow) #
```

## For loop
```python
for x in range(0,10):
  print (x,end = '')
```

## Read/Write a file
```python
###read file
f = open("demofile.txt", "r")
print(f.read())

with open(fname) as f:
    content = f.readlines()

### write to file
fo = open("foo.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")

fo.close()
## wirte at the end of the file
with open('something.txt', 'a') as f:
    f.write('text to be appended')

```


## print


```python
A =" "
B =u"\u2581"
C =u"\u2582"
D =u"\u2583"
E =u"\u2584"
F =u"\u2585"
G =u"\u2586"
H =u"\u2587"
I =u"\u2588"

for i in A,B,C,D,E,F,G,H,I:
  print("\x1b[3;45;6m%s\x1b[0m"%(i),end='')
```

![NYE1bQ.png](https://s1.ax1x.com/2020/06/22/NYE1bQ.png)



<a name="F7DeQ"></a>
## path

```python
import pathlib
pathlib.Path(__file__).parent.absolute()

import pathlib
pathlib.Path().absolute()

import os
sys.path[0]

## Chage Workind Director
import os
os.chdir("../")
```

<a name="5ixt3"></a>
## import

```python
## import from the same directory
import XXX

## import from the directories in the same directory
from Directory import xxx

## import from .. directory
import sys
sys.path.append("..")
import xxx　
```

<a name="0wVAH"></a>
## str to var

```python
for i in range(4):
    name='v'+str(i)
    locals()['v'+str(i)]=i

print v1,v2,v3
```


## Dictionary

Find the max value from a dictionary

```python
d = {'a': 10, 'b': 5, 'c': 20}
max_value = max(d, key=d.get)
print(max_value)
```

<pre>
c
</pre>