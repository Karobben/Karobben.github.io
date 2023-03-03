---
title: "pip"
description: "pip"
url: pip2
date: 2020/01/22
toc: true
excerpt: "pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes."
tags: [Python]
category: [Python, Beginner]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## pip

```bash
## 清华
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
## 豆瓣
pip install -i http://pypi.douban.com/simple/ --upgrade numpy
```

```bash
pip install -t /usr/local/lib/python2.7/site-packages/ xlrd
```

```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## list


```bash
pip list
```

```bash
Package              Version    
-------------------- -----------
absl-py              0.9.0      
aiohttp              3.6.2      
allow                0.0.3      
alot                 0.9        
appdirs              1.4.3     
```


<a name="n0A8A"></a>
## show


```bash
pip show opencv-python
'''
Name: opencv-python
Version: 4.1.2.30
Summary: Wrapper package for OpenCV python bindings.
Home-page: https://github.com/skvark/opencv-python
Author: None
Author-email: None
License: MIT
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy
Required-by:
'''
```

