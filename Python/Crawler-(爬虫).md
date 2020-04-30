---
url: crawler
---

# Crawler (爬虫)

<a name="4xYVn"></a>
# 1. Quick Start
Crawler img location sites from National Geographic web site & downloading them. 
```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests

# Starting resuqest
html = urlopen("http://www.nationalgeographic.com.cn/animals/").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('http://image..*?\.jpg')})
for link in img_links:
    print(link['src']) # pic locationg
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579662530841-1686d08e-9b0c-4ae5-b004-fddf1aa54e60.png#align=left&display=inline&height=181&name=image.png&originHeight=181&originWidth=663&size=53517&status=done&style=none&width=663)<br />

```python
# With adding this
# mkdir img # 创建一个img文件夹

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

![deepin-screen-recorder_nautilus_20200122111508.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1579662953089-51c2e01a-808c-4251-a500-f6df2fe0a7c3.gif#align=left&display=inline&height=384&name=deepin-screen-recorder_nautilus_20200122111508.gif&originHeight=591&originWidth=890&size=730944&status=done&style=none&width=579)<br />




<a name="FmNuL"></a>
# 实战案例:
<a name="zWSme"></a>
## [科技快讯](https://www.yuque.com/liuwenkan/tza8ge/ew3wen)
