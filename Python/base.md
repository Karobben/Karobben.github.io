---
url: base2
---
# base


```python
#########print##########

pi = 3.141592653
print('%10.3f' % pi) #字段宽10，精度3
# 3.142
print("pi = %.*f" % (3,pi)) #用*从后面的元组中读取字段宽度或精度
# pi = 3.142
print('%010.3f' % pi) #用0填充空白
# 000003.142
print('%-10.3f' % pi) #左对齐
# 3.142
print('%+f' % pi) #显示正负号
# +3.141593

for x in range(0,10):
  print (x,end = '')
# 0123456789

##read file
f = open("demofile.txt", "r")
print(f.read())

with open(fname) as f:
    content = f.readlines()

## write to file
fo = open("foo.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")

fo.close()
# wirte at the end of the file
with open('something.txt', 'a') as f:
    f.write('text to be appended')


# duplicats removing
A = [1,1,1,2,3,4,3]
list(set(A))

######################
######### caculating #
######################
Operator 	Description 	Example
+ 	Addition operator 	100 + 45 = 145
- 	Subtraction operator 	500 - 65 = 435
* 	Multiplication operator 	25 * 4 = 100
/ 	Float Division Operator 	10 / 2 = 5.0
// 	Integer Division Operator 	10 / 2 = 5
** 	Exponentiation Operator 	5 ** 3 = 125
% 	Remainder Operator 	10 % 3 = 1  #  10 / 3 = 3 ... 1

```

# print


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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579675315341-8baaaabd-65cc-411c-8c8b-0b3232f9018c.png#align=left&display=inline&height=79&name=image.png&originHeight=79&originWidth=443&size=9295&status=done&style=none&width=443)


# List

int list to str list
```python
[str(x) for x in int_list]
```


<br />int list to str list<br />

```python
a_list = ["1", "2", "3"]
#int list to str list
list(map(str, a_list))
#str list to int list
list(map(int, a_list))


# 逐个相减
c = [b[i] - a[i] for i in range(len(a))]
```


## Compare Two list


```python
l = [1, 2, 3, 5]
l_one = [2, 8, 6, 10]
print set(l) & set(l_one)
```


<a name="F7DeQ"></a>
# path

```python
import pathlib
pathlib.Path(__file__).parent.absolute()

import pathlib
pathlib.Path().absolute()

import os
sys.path[0]

# Chage Workind Director
import os
os.chdir("../")
```

<a name="5ixt3"></a>
# import

```python
# import from the same directory
import XXX

# import from the directories in the same directory
from Directory import xxx

# import from .. directory
import sys
sys.path.append("..")
import xxx　
```

<a name="0wVAH"></a>
# str to var

```python
for i in range(4):
    name='v'+str(i)
    locals()['v'+str(i)]=i

print v1,v2,v3
```

--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](https://karobben.github.io/) <br />R 语言画图索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
