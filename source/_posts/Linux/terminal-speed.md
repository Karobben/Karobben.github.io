---
title: "terminal 不走代理加速"
description: "terminal 不走代理加速"
url: wdda8g2
date: 2020/06/26
toc: true
excerpt: "明明浏览器等软件连国外仓库OK的, 为什么terminal就是连不上去呢?"
tags: [Linux]
category: [Linux, others]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## terminal 不走代理加速

系统: deepin 15.11

明明都开了全局模式, 但是terminal 下载还是很慢<br />解决方法:


![Nse4v8.png](https://s1.ax1x.com/2020/06/26/Nse4v8.png)

```bash
export http_proxy="http://127.0.0.1:12333"
export https_proxy="http://127.0.0.1:12333"
```
然后就好啦~

参考:[https://blog.csdn.net/weixin_43377336/article/details/87249688](https://blog.csdn.net/weixin_43377336/article/details/87249688)
