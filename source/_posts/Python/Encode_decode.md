---
title: "Encode & decode in Python"
ytitle: "Python 的文字加密和解碼"
description: "Encode & decode in Python"
url: decode2
date: 2020/01/22
toc: true
excerpt: "Encode and decode in python"
tags: [Python]
category: [Python, others]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---


## Encode&decode

<a name="GkAZZ"></a>
## gb2312
=?gb2312?b?1cq7p9Lss6O1x8K8u+62rw==?=
```python
base64.b64decode("1cq7p9Lss6O1x8K8u+62rw==").decode("GBK")
```
 结果： '帐户异常登录活动'
