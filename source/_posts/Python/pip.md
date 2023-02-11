---
title: "pip"
description: "pip"
url: pip2
date: 2020/01/22
toc: true
excerpt: "pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes."
tags: [Python, pip]
category: [Python]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
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

<br />

```bash
pip install -t /usr/local/lib/python2.7/site-packages/ xlrd
```

<br />

```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple
```

<br />

<a name="Wo9ga"></a>
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

