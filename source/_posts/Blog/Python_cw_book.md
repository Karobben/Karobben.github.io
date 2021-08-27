---
title: "用Python下载高中教材"
description: "用python爬蟲下載高中人教版教材"
url: python_cl_book
date: 2020/07/17
toc: true
excerpt: "用python爬蟲下載高中人教版教材"
tags: [Python, Crawler]
category: [Python, Crawler]
cover: 'https://s1.ax1x.com/2020/07/17/Uy4W4g.png'
thumbnail: 'https://s1.ax1x.com/2020/07/17/Uy4W4g.png'
priority: 10000
---

## 如何用python爬蟲獲取高中教材

目標網頁: `http://www.100.com/article/309299.html`(已失效)
![Uy4W4g.png](https://s1.ax1x.com/2020/07/17/Uy4W4g.png)

點擊網頁， 可知， 目標圖片的結構爲:
```html
<p style="text-align:center">
  <img id="99770" src="http://edu_img.bs2.100.com/b31c5369425c1c5203b2437.jpg" alt="bb09f673355c1c4ff92c54c.jpg" />
</p>
```
```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

## Function for downloading
def page_download(image_name,r):
  try:
    with open('./img/%s' % image_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)  
  except:
    print("missing")

## Starting resuqest
ulr = "http://www.100.com/article/309299.html?&display=w&fd=wap"

html = urlopen(ulr).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

Book_list = soup.findAll('p',{"style":"text-align:center"})

Num = 0
for link in Book_list:
  try:
    Num += 1
    url = link.find('img')['src']
    r = requests.get(url, stream=True)
    image_name = str(Num)+'.jpg'
    page_download(image_name,r)
    print('Saved %s' % image_name)
  except:
    print("Missing")
```

## 壓縮成單個pdf

```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple img2pdf

img2pdf $(ls | sort -n) -o ../Biology1.pdf
```

![Uy4B3d.md.jpg](https://s1.ax1x.com/2020/07/17/Uy4B3d.md.jpg)

完成～

注: 有的網頁， 可能不一樣。 比如生物必修二就在匹配的時候， 多了一個分號， 因此， 要改成：`Book_list = soup.findAll('p',{"style":"text-align:center;"})`

enjoy~
