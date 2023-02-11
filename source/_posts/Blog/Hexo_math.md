---
title: "Hexo: Math Function"
url: hexo_math
date: "2020-06-30"
description: "hexo, how to render letex math function in hexo"
toc: true
excerpt: '
Insert Math function in hexo post:
$$
P(t)= \frac{KP_{0}e^{rt}}{K + P_0(e^{rt} - 1)}
$$
'
tags: [Hexo, Hexo Plugin, MarkDown]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---
## Hexo: Make a Post

## For the theme NexT user
Scripts and engines are embedded already. You can enable it by altering the parameters at `_config.yml` by following the instructor post by [醉渔  2019](https://blog.zuiyu1818.cn/posts/hexo_math.html)

## Insert the script
reference: [Guohua Wu 2013](https://wugh.github.io/posts/2013/11/hexo-math-equation/)[^1]

[^1]: Guohua Wu; hexo数学公式; Gitpage; 2013; [link](https://wugh.github.io/posts/2013/11/hexo-math-equation/)

Insert the codes below at `themes/landscape/layout/_partial/head.ejs` in your hexo directory. (At here, my theme is "landscape")
```html
<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```

According from the original post[^1], we are supposed to make some modifications on a few other files. But I just found it is fine without a further alteration. So, I stopped at this steps. If you can have a visitation on the post if you want to check out by yourselves.

$$
P(t)= \frac{KP_{0}e^{rt}}{K + P_0(e^{rt} - 1)}
$$
