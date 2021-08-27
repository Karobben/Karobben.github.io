---
title: "Python 爬虫 -- 新闻爬取"
description: "Python 爬虫 -- 新闻爬取"
url: ew3wen
date: 2020/12/13
toc: true
excerpt: "Python 爬虫 -- 新闻爬取"
tags: [Python, Crawler]
category: [Python, Crawler]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Python 爬虫 -- 新闻爬取


<a name="KzDXU"></a>
## 1. 科技快讯

网址:[http://www.citreport.com/](http://www.citreport.com/)

![Nsi6fS.png](https://s1.ax1x.com/2020/06/26/Nsi6fS.png)

以科技快报为目标

<a name="mQNML"></a>
### 1. 首先, 获取整个页面信息
```bash
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

## Starting resuqest
html = urlopen("http://www.citreport.com/").read()
soup = BeautifulSoup(html, features='lxml')
```


<a name="wtYUI"></a>
### 2. 查看网页源码
ctrl+shit+c 查看网页源码

![NsisFf.png](https://s1.ax1x.com/2020/06/26/NsisFf.png)

<a name="SK2Oq"></a>
### 3. 复制框内的信息, 匹配一下:
```bash
Paper = soup.find('div',{'class':"right-item news-flash-box"})

## 检查一下
print(Paper.get_text())
```

![NsiBwt.png](https://s1.ax1x.com/2020/06/26/NsiBwt.png)
就这么简单2333

<a name="7gtdC"></a>
### 4. 获取快讯文字链接
```python
## 检查一下
print(soup.find('div',{'class':"right-item news-flash-box"}).get_text())

##获得快讯文字的链接
Links = Paper.find_all("a", {"href": re.compile('http://..*?\.html')})
for link in Links:
    print(link['href']) # pic locationg
```
![NsiDTP.png](https://s1.ax1x.com/2020/06/26/NsiDTP.png)



成功获得快讯文字的链接

<a name="hfWrS"></a>
### 5. 以第一篇为模板进行文章抓取

```python
url = Links[1]['href']
html = urlopen(url).read()
soup = BeautifulSoup(html, features='lxml')
```

<a name="EbG2t"></a>
### 6. 继续查看码源, 获取标题和文字格式

发现,标题的标签为:
`<br /><h1 class="ph"`

文章主题标签为:
`<br /><div class="d">`

则,代码如下
```python
P_title = soup.find('div',{"class":"h hm cl"}).get_text()
P_body  = soup.find('td',{"id":"article_content"}).get_text()
```
这就成功啦
![NsiyY8.png](https://s1.ax1x.com/2020/06/26/NsiyY8.png)


<a name="pmjx3"></a>
### 7. 整合一下,并且, 循环抓取本小模块的所有paper

```bash
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

## Starting resuqest
html = urlopen("http://www.citreport.com/").read()
soup = BeautifulSoup(html, features='lxml')
Paper = soup.find('div',{'class':"right-item news-flash-box"})

Links = Paper.find_all("a", {"href": re.compile('http://..*?\.html')})

Paper = Paper.get_text()
for link in Links:
  url = link['href']
  html = urlopen(url).read()
  soup = BeautifulSoup(html, features='lxml')
  P_title = soup.find('div',{"class":"h hm cl"}).get_text()
  P_body  = soup.find('td',{"id":"article_content"}).get_text()
  Paper += P_title + P_body

print(Paper)
```

<a name="BXq7e"></a>
## 2 NPR News Head Line

```bash
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import time


url= "https://www.npr.org/"
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

story_today = soup.find_all('div',{"class":"story-wrap"})

HeadLine =""
for i in story_today:
    HeadLine += i.get_text()
```


<a name="3z1ri"></a>
## 3. 爬取B站空间主页信息

参考: [https://zhuanlan.zhihu.com/p/34716924](https://zhuanlan.zhihu.com/p/34716924)

```python
import ast
from urllib.request import urlopen
import time


ID = "86328254"
url = "http://api.bilibili.com/archive_stat/stat?aid=" + ID
html = urlopen(url).read().decode('utf-8')
d = ast.literal_eval(html)
Cont = d['data']
View    = "观看量: " + str(Cont['view'])
Like    = "点赞: " + str(Cont['like'])
Reply   = "回复: " + str(Cont['reply'])
Coin    = "硬币: " + str(Cont['coin'])
Result = "\n".join([View, Like, Reply, Coin])
print(Result)

```
