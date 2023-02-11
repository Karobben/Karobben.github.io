---
title: "在博客下面添加评论区gittack"
description: "在博客下面添加评论区gittack"
url: qa88z1
date: 2020/06/26
toc: true
excerpt: "在博客下面添加评论区gittack"
tags: [Hexo, Hexo Plugin, HTML]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---

## 在博客下面添加评论区gittack

```flow
st=>start: 登录GitHub
op1=>operation: 新建一个Repository
op2=>operation: 打开主页设置
op3=>operation: 选择开发者设置
op4=>operation: 创建OAuth app
op5=>operation: 添加代码
op5=>operation: 初始化评论
e=>end: 完成!! Enjoy！


st->op1(right);
op1->op2
op2(right)->op3
op3->op4
op4(right)->op5
op5->e
```

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


配置成功后， 会显示
![Nrj7WR.png](https://s1.ax1x.com/2020/06/26/Nrj7WR.png)

这时候只要登录，留下评论，就可以初始化了～！！
![NrjbS1.png](https://s1.ax1x.com/2020/06/26/NrjbS1.png)



Enjoy!~
