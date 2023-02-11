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
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
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
