---
url: ew3wen
---

# Python 爬虫 -- 新闻爬取


<a name="KzDXU"></a>
# 1. 科技快讯

网址:[http://www.citreport.com/](http://www.citreport.com/)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579693172404-2969e30c-a408-40e0-8b1e-5ec74e325d14.png#align=left&display=inline&height=805&name=image.png&originHeight=805&originWidth=1120&size=613850&status=done&style=none&width=1120)

以科技快报为目标

<a name="mQNML"></a>
## 1. 首先, 获取整个页面信息
```bash
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

# Starting resuqest
html = urlopen("http://www.citreport.com/").read()
soup = BeautifulSoup(html, features='lxml')
```


<a name="wtYUI"></a>
## 2. 查看网页源码
ctrl+shit+c 查看网页源码

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579693464963-77ccd62f-f574-4ed8-bfd0-44c9f8321327.png#align=left&display=inline&height=548&name=image.png&originHeight=729&originWidth=857&size=233323&status=done&style=none&width=644)

<a name="SK2Oq"></a>
## 3. 复制框内的信息, 匹配一下:
```bash
Paper = soup.find('div',{'class':"right-item news-flash-box"})

# 检查一下
print(Paper.get_text())
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579693742028-d1c13075-75ef-4526-8092-633bd9a7c966.png#align=left&display=inline&height=315&name=image.png&originHeight=315&originWidth=553&size=110552&status=done&style=none&width=553)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579694243921-39cbf8e5-e900-431e-997f-a04591d7c1a7.png#align=left&display=inline&height=333&name=image.png&originHeight=333&originWidth=600&size=51687&status=done&style=none&width=600)<br />就这么简单2333

<a name="7gtdC"></a>
## 4. 获取快讯文字链接
```bash
# 检查一下
print(soup.find('div',{'class':"right-item news-flash-box"}).get_text())

#获得快讯文字的链接
Links = Paper.find_all("a", {"href": re.compile('http://..*?\.html')})
for link in Links:
    print(link['href']) # pic locationg
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579694659974-de2bbf0d-a29a-4606-a9ee-7199e0ad27aa.png#align=left&display=inline&height=342&name=image.png&originHeight=342&originWidth=412&size=41509&status=done&style=none&width=412)

成功获得快讯文字的链接

<a name="hfWrS"></a>
## 5. 以第一篇为模板进行文章抓取

```bash
url = Links[1]['href']
html = urlopen(url).read()
soup = BeautifulSoup(html, features='lxml')
```

<a name="EbG2t"></a>
## 6. 继续查看码源, 获取标题和文字格式

发现,标题的标签为:<br /><h1 class="ph"><br />文章主题标签为:<br /><div class="d"><br />则,代码如下
```bash
P_title = soup.find('div',{"class":"h hm cl"}).get_text()
P_body	= soup.find('td',{"id":"article_content"}).get_text()
```
这就成功啦<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579695490393-8a71e7e4-412c-4fc8-92c7-5d60893edf63.png#align=left&display=inline&height=461&name=image.png&originHeight=461&originWidth=791&size=244688&status=done&style=none&width=791)<br />

<a name="pmjx3"></a>
## 7. 整合一下,并且, 循环抓取本小模块的所有paper

```bash
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

# Starting resuqest
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
  P_body	= soup.find('td',{"id":"article_content"}).get_text()
  Paper += P_title + P_body

print(Paper)
```

<a name="BXq7e"></a>
# 2 NPR News Head Line

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
# 3. 爬取B站空间主页信息

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

<a name="qdYiN"></a>
# 更多, 见博客: [**BiliBili API**](https://www.yuque.com/liuwenkan/blog/pn5boe)



Enjoy ~




<br />--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
