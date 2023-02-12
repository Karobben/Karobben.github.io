---
title: "python ftp"
ytitle: "python 操作ftp服務器"
description: "Connect FTP server with python"
url: ftp
date: 2020/01/22
toc: true
excerpt: "open a ftp server with python"
tags: [Python, FTP]
category: [Python, Scripting, Module]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---


Reference soruce: [jihite, 2015](https://www.cnblogs.com/kaituorensheng/p/4480512.html)

## Quick start

```python
from ftplib import FTP            # Loading the lib
ftp=FTP()       									# Assign to ftp
ftp.connect("IP","port")					# Connected it
ftp.login("user","password")			# Login
ftp.cwd("xxx/xxx")								# cd command
ftp.nlst()												# read the items in directory as list
```
