---
title: "Python- IP 地址转地址信息"
description: "Python- IP 地址转地址信息"
url: python_ip
---

# Python- IP 地址转地址信息

最近看看服務器的`/var/log/secure`文件發現, 每天居然都收到了好幾千的攻擊 .
抱着好奇的心態, 我想統計一下攻擊都來自哪裏. 因此寫一個跑一趟hon腳本, 畫個地圖.

# 1. 網站
"https://cn.bing.com/search?mkt=zh-cn&h_IpInput=ctxtb&q=59.173.18.251&submit=%E6%9F%A5%E8%AF%A2"
網站查詢方便, 不僅告訴你歸屬地, 還可以告訴你運營商.

```python
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Starting resuqest
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

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
