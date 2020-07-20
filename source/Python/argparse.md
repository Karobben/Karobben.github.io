---
title: "argparse (参数库)"
description: "argparse (参数库)"
url: argparse2
---

# argparse (参数库)

<a name="wrCHD"></a>
# 1. sys


```python
 sys.argv[1]
```


<a name="JyBOw"></a>
# 2. argparse
<a name="A41Zh"></a>
## 1. Quick Start


```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-U','--output')     #输入文件

#获取参数
args = parser.parse_args()
INPUT = args.input
RANGE = args.output




```

<br />run as <br />
```bash
python3 test.py -i inputfile -o outpufile
```


<a name="WGl76"></a>
## 2. Important arguments
```python
####
with type and default
parser.add_argument(
  '--width',
  dest='num_hands',
  type = int,
  default = 80,
  help='Max number of hands to detect.')
```


<a name="V1ygH"></a>
## 3. Reading *.png


<a name="ECaCU"></a>
### 3.1 nargs="+" (One/More)
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',nargs='+')    #输入文件

args = parser.parse_args()
INPUT = args.input

print(INPUT)
```


```bash
$ python3.7 test.py  -i Ms*
['Msg', 'Msg2']
```

<br />

<a name="VDzdW"></a>
### 3.2 nargs="?" (None/One)


```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',  default='a', nargs='?')    #输入文件

args = parser.parse_args()
INPUT = args.input

print(INPUT)
```


```bash
$ python3.7 test.py
a
$ python3.7 test.py -i
None
$ python3.7 test.py -i b
b
```
