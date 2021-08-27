---
title: "Python: getting location through IP address"
description: "Python: getting location through IP address| 通过python 爬虫 获取IP地址和地理位置"
date: 2020/12/13
url: python_loc_get
toc: true
excerpt: "Python: getting location through IP address| 通过python 爬虫 获取IP地址和地理位置"
tags: [Python]
category: [Python]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Python: getting location through IP address

Target Website: https://my.ip.cn/

```python
import requests
import time

url = "https://my.ip.cn/api/index?ip=&type=0"

headers = {
  ":authority": "my.ip.cn",
  ":method": "GET",
  ":path": "/api/index?ip=&type=0",
  ":scheme": "https",
  "accept": "application/json, text/javascript, */*; q=0.01",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4",
  "cookie":"__cfduid=dfd9a8ad770a7d54ed934a6adb02390651607854807; INIT_IP_INFO=%E4%B8%AD%E5%9B%BD++%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81+%E5%93%88%E5%B0%94%E6%BB%A8%E5%B8%82+%E8%81%94%E9%80%9A",
  "referer": "https://my.ip.cn/",
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
  "x-requested-with": "XMLHttpRequest"
}
Result = requests.get(url).json()
## IP
print(Result['ip'])
## Address
print(Result['address'])
City = Result['address'].split(" ")[-2]
```
