---
title: "terminal 不走代理加速"
description: "terminal 不走代理加速"
url: wdda8g2
---

# terminal 不走代理加速

系统: deepin 15.11

明明都开了全局模式, 但是terminal 下载还是很慢<br />解决方法:


![Nse4v8.png](https://s1.ax1x.com/2020/06/26/Nse4v8.png)

```bash
export http_proxy="http://127.0.0.1:12333"
export https_proxy="http://127.0.0.1:12333"
```
然后就好啦~

参考:[https://blog.csdn.net/weixin_43377336/article/details/87249688](https://blog.csdn.net/weixin_43377336/article/details/87249688)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
