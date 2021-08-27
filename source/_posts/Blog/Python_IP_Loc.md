---
title: "Python- IP 地址转地址信息"
description: "Python- IP 地址转地址信息"
url: python_ip
date: 2020/10/25
toc: true
excerpt: "Python- IP 地址转地址信息"
tags: [Python]
category: [Python]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Python- IP 地址转地址信息

最近看看服務器的`/var/log/secure`文件發現, 每天居然都收到了好幾千的攻擊 .
抱着好奇的心態, 我想統計一下攻擊都來自哪裏. 因此寫一個跑一趟hon腳本, 畫個地圖.

## 1. 網站
"https://cn.bing.com/search?mkt=zh-cn&h_IpInput=ctxtb&q=59.173.18.251&submit=%E6%9F%A5%E8%AF%A2"
網站查詢方便, 不僅告訴你歸屬地, 還可以告訴你運營商.

```python
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

## Starting resuqest
def IP_get(IP):
  url = "https://ipchaxun.com/"+ IP +"/"
  Cookies = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
  "Connection": "keep-alive",
  "Cookie": "PHPSESSID=t9dsgluabl4hs1vnneog2fi91d; Hm_lvt_22d5503e9164951ac850495fe15447a7=1588438128; Hm_lpvt_22d5503e9164951ac850495fe15447a7=1588438769",
  "Host": "ipchaxun.com",
  "Referer": url,
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
  }
  res = requests.get(url, headers=Cookies, timeout=30)
      # 设置页面编码格式
  res.encoding = "utf-8"
  soup = BeautifulSoup(res.text, "html.parser")
  Location = soup.find_all("label")[-2].get_text().split("：")[-1].replace("\n","")
  Suplyer = soup.find_all("label")[-1].get_text().split("：")[-1].replace("\n","")
  return IP, Location, Suplyer

IPlist = open("TB_IP",'r').read().split("\n")[:-1]

Result = []
for i in IPlist:
  A,B,C = IP_get(i)
  print("\t".join([A,B,C]))
  Result += ["\t".join([A,B,C])]

F = open("IP_location","w")
F.write("\n".join(Result))
F.close()
```


