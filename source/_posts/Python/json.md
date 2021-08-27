---
title: "json data in python | read, write, and transfer"
ytitle: "Python 處理json數據， 讀寫轉化"
description: "json"
url: gde4da
date: 2020/12/16
toc: true
excerpt: "manipulate json date with python"
tags: [Python, HTML]
category: [Python]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---



```python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print json



jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print text


Config = json.load(open('config.json'))
```
