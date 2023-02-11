---
title: "How to Using Python to Acquire Websites' Responding Time"
description: "How to Using Python to Acquire Websites' Responding Time"
url: py_requesttime
date: 2020/10/25
toc: true
excerpt: "How to Using Python to Acquire Websites' Responding Time"
tags: [Python]
category: [Python]
cover: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
thumbnail: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
priority: 10000
---

## How to Using Python to Acquire Websites' Responding Time

## 1. Acquiring Responding Time
reference:[子黍](https://blog.csdn.net/weixin_41787887/article/details/82660467)
```Python
import requests
r = requests.get("http://www.cnblogs.com/yoyoketang/")
print(r.elapsed.total_seconds())
```

## 2. Multiprocessing

```python
import multiprocessing as mp
import time, re
import requests

List = ["www.baidu.com", "https://tongji.baidu.com/web/10000138058/overview/index?siteId=14350939","https://karobben.github.io/","https://space.bilibili.com/393056819","https://github.com/Karobben","https://www.yuque.com/dashboard/books","haishdiashdiahsdiuhsaiudha"]

def RespTime(url):
  # Page is exist or not
  try:
    r = requests.get(url, timeout=20)
    print("("+url+")(Update:"+time.strftime("%D")+ " "+ str(r.elapsed.total_seconds())+"s)"
)
  except:
    print(url+"\tFailed")


def multicore(List, Pool=10):
  pool = mp.Pool(processes=Pool)
  for i in List:
    multi_res = [pool.apply_async(RespTime,(i,))]
  pool.close()
  pool.join()
```

## 3. Extract urls from Markdonw File

### 1. Extract and Calculates Responding Time
Using this Script to test the links in Markdonw file
reference: [张土豆](https://www.jb51.net/article/153432.htm)
```python
import multiprocessing as mp
import time, re
import requests


Input = "/media/ken/Data/Github/Yuque/Bioinfor/test2.md"
F = open(Input,'r')
File = F.read()

pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\)') # 匹配模式
List = pattern.findall(File)

def RespTime(url,return_dict):
  # Page is exist or not
  url = url.replace('(','').replace(")","")
  try:
    r = requests.get(url, timeout=20)
    Result = url+"\t"+str(r.elapsed.total_seconds())
  except:
    Result = url+"\tFailed"
  return_dict[Result] = Result

if __name__ == '__main__':
    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in List:
        p = mp.Process(target=RespTime, args=(i,return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()

for i in return_dict.values():
  print(i)
```
It backs to:
```
http://www.kazusa.or.jp/codon/  0.721183
http://wwwmgs.bionet.nsc.ru/mgs/gnw/trrd/  1.616894
http://www.ncbi.nlm.nih.gov/dbSTS/  1.460668
...
```
### 2. Update the Markdonw File
#### 1. Format your markdown file url as:
```
[Title](https://www.baidu.com) (Oct; 0.888888s)
```
You can format your file with codes below:


```python
import re

Input = "/media/ken/Data/Github/Yuque/Bioinfor/test2.md"
F = open(Input,'r')
File = F.read()

pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\)') # 匹配模式
List = pattern.findall(File)


for i in List:
  i2 = i.replace(")",'').replace("(",'')
  File = re.sub(i, i2+") (test", File)

F = open(Input,'w')
F.write(File)
F.close()
```
As a result, your url will look like:
[Title](http://www.sssss.com)(test)

#### 2. Replace

##### Basic rule of substitude
```python
import re
url = 'https://113.215.20.136:9011/113.215.6.77/c3pr90ntcya0/youku/6981496DC9913B8321BFE4A4E73/0300010E0C51F10D86F80703BAF2B1ADC67C80-E0F6-4FF8-B570-7DC5603F9F40.flv'
pattern = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
print pattern.findall(url)
out = re.sub(pattern, '127.0.0.1', url)
print out
```
Cite: [那年花开月正圆](https://www.cnblogs.com/prometheus-python-xshell/p/7646965.html)

##### Replace
```python
import multiprocessing as mp
import time, re
import requests


Input = "/media/ken/Data/Github/Yuque/Bioinfor/test2.md"
F = open(Input,'r')
File = F.read()

pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\) \((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])| )+'+"\)") # 匹配模式
List = pattern.findall(File)

def RespTime(url,return_dict):
  # Page is exist or not
  url = url.split(')')[0].replace("(","")
  try:
    try:
      r = requests.get(url, timeout=20)
      rtime = str(r.elapsed.total_seconds())+"s)"
    except:
      rtime = "OutOfTime)"
    Result = "("+url+") (Update:"+time.strftime("%D")+ "; "+ rtime
  except:
    Result = "("+url+") (Update:"+time.strftime("%D")+ "; Failed)"
  return_dict[Result] = Result

if __name__ == '__main__':
    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in List:
        p = mp.Process(target=RespTime, args=(i,return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()

DB="\n".join(return_dict.values())


for i in List:
  Str = i.split(")")[0].replace("(",'')
  #pattern = re.compile(Str+r"\)[ ]\((?:[a-zA-Z]|[0-9]|[:/|\.]|;)+[ ][0-9]|[a-zA-Z]|\.?+")
  pattern = re.compile(Str+"\) \(.+")
  i2 = "("+pattern.findall(DB)[0]
  print(i,i2,sep='\n')
  File = File[:File.find(i)] + i2+ File[File.find(i)+len(i):]

F = open(Input,'w')
F.write(File)
F.close()
```

## 4. Final Script

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-U','--output')     #输入文件

##获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output

import multiprocessing as mp
import time, re
import requests


F = open(INPUT,'r')
File = F.read()

pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\) \((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])| )+'+"\)") # 匹配模式
List = pattern.findall(File)

def RespTime(url,return_dict):
  # Page is exist or not
  url = url.split(')')[0].replace("(","")
  try:
    try:
      r = requests.get(url, timeout=20)
      rtime = str(r.elapsed.total_seconds())+"s)"
    except:
      rtime = "OutOfTime)"
    Result = "("+url+") (Update:"+time.strftime("%D")+ "; "+ rtime
  except:
    Result = "("+url+") (Update:"+time.strftime("%D")+ "; Failed)"
  return_dict[Result] = Result

if __name__ == '__main__':
    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in List:
        p = mp.Process(target=RespTime, args=(i,return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()

DB="\n".join(return_dict.values())


for i in List:
  Str = i.split(")")[0].replace("(",'')
  #pattern = re.compile(Str+r"\)[ ]\((?:[a-zA-Z]|[0-9]|[:/|\.]|;)+[ ][0-9]|[a-zA-Z]|\.?+")
  pattern = re.compile(Str+"\) \(.+")
  i2 = "("+pattern.findall(DB)[0]
  print(i,i2,sep='\n')
  File = File[:File.find(i)] + i2+ File[File.find(i)+len(i):]

F = open(OUTPUT,'w')
F.write(File)
F.close()
```
