---
title: "python ftp"
description: "Connect FTP server with python"
url: ftp
---

# FTP lib for python

Reference soruce: [jihite, 2015](https://www.cnblogs.com/kaituorensheng/p/4480512.html)

# Quick start

```python
from ftplib import FTP            # Loading the lib
ftp=FTP()       									# Assign to ftp
ftp.connect("IP","port")					# Connected it
ftp.login("user","password")			# Login
ftp.cwd("xxx/xxx")								# cd command
ftp.nlst()												# read the items in directory as list
```
