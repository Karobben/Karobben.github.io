---
url: qa88z1
---

# 在博客下面添加评论区gittack


![](https://cdn.nlark.com/yuque/__graphviz/7f121e2d20e14013cfb815e70a92580b.svg#lake_card_v2=eyJjb2RlIjoiZGlncmFwaCBGIHtcbiAgICByYW5rZGlyID0gTFI7XG4gICAgZWRnZSBbc3R5bGU9c29saWRdO1xuICAgIG5vZGUgW3N0eWxlPWZpbGxlZCwgZm9udD1Db3VyaWVyXTtcblxuICAgIHN1YmdyYXBoIEEge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgU3RhcnQgW2xhYmVsID0gXCLnmbvlvZVnaXRodWJcIiwgc2hhcGUgPSBib3gsIGZpbGxjb2xvciA9IFwiI0ZGMDAwMFwiIF07XG4gICAgICAgIEVuZCAgIFtsYWJlbCA9IFwi5a6M5oiQ77yB77yBRW5qb3nvvZ5cIiAgICAgICwgc2hhcGUgPSBib3gsIGNvbG9yID0gY29yYWxdO1xuXG4gICAgICAgIEEgW2xhYmVsID0gXCLmlrDlu7rkuIDkuKpSZXBvc3RvcnlcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxLCBzaXplID0gM107XG4gICAgICAgIEIgW2xhYmVsID0gXCLmiZPlvIDkuLvpobXorr7nva5cIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxLCBzaXplID0gM107XG4gICAgfVxuXG4gICAgc3ViZ3JhcGggQiB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBDIFtsYWJlbCA9IFwi6YCJ5oup5byA5Y-R6ICF6K6-572uXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMSwgc2l6ZSA9IDNdO1xuICAgICAgICBEIFtsYWJlbCA9IFwi5Yib5bu6T0F1dGggYXBwXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMSwgc2l6ZSA9IDNdO1xuICAgICAgICBFIFtsYWJlbCA9IFwi5re75Yqg5Luj56CBXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMSwgc2l6ZSA9IDNdO1xuICAgICAgICBGIFtsYWJlbCA9IFwi5Yid5aeL5YyW6K-E6K66772eXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMSwgc2l6ZSA9IDNdO1xuICAgIH1cblxuICAgIFN0YXJ0XHQtPiBBO1xuXHRcdEFcdC0-IEI7XG5cdFx0Qlx0LT4gQztcblx0XHRDXHQtPiBEO1xuXHRcdERcdC0-IEU7XG5cdFx0RVx0LT4gRjtcblx0XHRcblx0XHRGIC0-IEVuZFxufSIsInR5cGUiOiJncmFwaHZpeiIsImlkIjoiQldDRzYiLCJ1cmwiOiJodHRwczovL2Nkbi5ubGFyay5jb20veXVxdWUvX19ncmFwaHZpei83ZjEyMWUyZDIwZTE0MDEzY2ZiODE1ZTcwYTkyNTgwYi5zdmciLCJjYXJkIjoiZGlhZ3JhbSJ9)

主流程： [https://www.jianshu.com/p/4242bb065550](https://www.jianshu.com/p/4242bb065550)

如何注册一个Github Application：[https://blog.csdn.net/xingkaifan/article/details/81105352](https://blog.csdn.net/xingkaifan/article/details/81105352)

代码配置：[https://blog.csdn.net/Madridcrls7/article/details/80871596](https://blog.csdn.net/Madridcrls7/article/details/80871596)
```html
<!-- Link Gitalk 的支持文件  -->
<link rel="stylesheet" href="https://unpkg.com/gitalk/dist/gitalk.css">
<script src="https://unpkg.com/gitalk@latest/dist/gitalk.min.js"></script> 
<div id="gitalk-container"></div>     <script type="text/javascript">
    var gitalk = new Gitalk({

    // gitalk的主要参数
        clientID: '复制刚才生成的clientID',
        clientSecret: '复制刚才生成的clientSecret',
        repo: '用于存放的仓库',
        owner: 'GitHub的用户名',
        admin: ['Github的用户名'],
        id:window.location.pathname,

    });
    gitalk.render('gitalk-container');
</script> 
<!-- Gitalk end -->
```

配置成功后， 会显示<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581308158919-763bfd62-7827-4e3e-926c-b1b15486cba3.png#align=left&display=inline&height=103&name=image.png&originHeight=103&originWidth=424&size=9024&status=done&style=none&width=424)

这时候只要登录，留下评论，就可以初始化了～！！ <br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581307994597-77c5ed16-1ebd-4f05-8c4c-788a25f8e9db.png#align=left&display=inline&height=336&name=image.png&originHeight=336&originWidth=1318&size=30155&status=done&style=none&width=1318)


Enjoy!~





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
