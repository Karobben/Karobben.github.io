---
url: wdda8g2
---

# terminal 不走代理加速

系统: deepin 15.11

明明都开了全局模式, 但是terminal 下载还是很慢<br />解决方法:


| ![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1584010079703-3369009e-e68d-45d6-b9df-0ce7252ec80f.png#align=left&display=inline&height=321&name=image.png&originHeight=321&originWidth=171&size=23242&status=done&style=none&width=171) |  |
| --- | --- |


```bash
export http_proxy="http://127.0.0.1:12333"
export https_proxy="http://127.0.0.1:12333"
```
然后就好啦~

参考:[https://blog.csdn.net/weixin_43377336/article/details/87249688](https://blog.csdn.net/weixin_43377336/article/details/87249688)




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](https://karobben.github.io/) <br />R 语言画图索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
