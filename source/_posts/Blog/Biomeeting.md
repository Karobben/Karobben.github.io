---
toc: true
url: Biomeeting
covercopy: © Karobben
priority: 10000
date: 2021-07-13 18:02:38
title: "Biology meetings information"
ytitle: "生物学相关会议"
description: "Biology meetings"
excerpt: "Biology meetings"
tags:
category:
cover: ""
thumbnail: ""
---

## Meetings

[科学网会议系统](http://meeting.sciencenet.cn/index.php?s=/Category/index&cid=2)

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

source = "http://meeting.sciencenet.cn/index.php?s=/Category/mth_meeting&mth=2021-07"
html = urlopen(source).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
Meeting_list = soup.find_all("div",{"class":"col-md-6"})

Num_m = len(Title)

for Meeting in Meeting_list:
  Tmp, Date = Get_Inf(Meeting)
  print(Date, Tmp)

def Get_Inf(Meeting):
  try:
    Title = Meeting.find("span",{"class" : "aa"}).get_text()
  except:
    Title = "404"
  #
  try:
    Tail = Meeting.find("a").get('href')
    #
    html = urlopen(source+"/"+Tail).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    Text = soup.get_text()
    #
    date_pattern="(\d{1,4}年)((([0?][1-9])月)|(([1?][0-2])月)|([1-9]月)?)(([0?][1-9]日)|([1?][0-9]日)|([2?][1-9]日)|([3][0-1]日)?)"
    res=re.search(date_pattern,Text)
    Date = res.group()
  except:
    Date = "404"
  #
  return Title, Date

"会议时间：" in Text
```
