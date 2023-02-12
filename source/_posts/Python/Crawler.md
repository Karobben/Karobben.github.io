---
title: "Crawler (爬虫)"
ytitle: "Python 網絡爬蟲"
description: "Crawler Examples, Webpage Crawling"
url: crawler2
date: 2020/01/22
toc: true
excerpt: "codes example for reading crawlers"
tags: [Python, Crawler]
category: [Python, Crawler]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---


## Crawler (爬虫)

<a name="4xYVn"></a>
## 1. Quick Start
Crawler img location sites from National Geographic web site & downloading them. 
```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

## Starting resuqest
html = urlopen("http://www.nationalgeographic.com.cn/animals/").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('http://image..*?\.jpg')})
for link in img_links:
    print(link['src']) # pic locationg
```

![NYEsa9.png](https://s1.ax1x.com/2020/06/22/NYEsa9.png)

```python
## With adding this
## mkdir img # 创建一个img文件夹

for link in img_links:
    print(link['src'])
    if link['src'][0:4] == 'http':
        url = link['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)

```

Running result:

![Python Crawler](https://s1.ax1x.com/2020/06/22/NYEy5R.gif)



<a name="FmNuL"></a>
## 实战案例:
<a name="zWSme"></a>
### [科技快讯](https://www.yuque.com/liuwenkan/tza8ge/ew3wen)
