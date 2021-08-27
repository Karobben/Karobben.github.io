---
title: "Hexo: Make a Post"
url: hexo_post
date: "2020-06-30"
description: "hexo 發佈新文檔"
toc: true
excerpt: "hexo 發佈新文檔"
tags: [Hexo]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---

## Hexo: Make a Post

Date: 30 June 2020

```bash
hexo new page post
```
It will make `source/post` and `source/post/index.md`

```bash
hexo new test
```
`source/_posts/test.md` is build

## Customize Front-matter Format

Front-matter is the head in your post
```yml
title: {{ title }}
date: {{ date }}
toc: true
description:
url:
excerpt:
tags:
category:
cover:
thumbnail:
priority: 10000
covercopy: '© Karobben'
```

We can alter the default value of it by recording it in `{Hexo}/scaffolds/post.md` [^luckyforefforts_2020]

[^luckyforefforts_2020]: luckyforefforts; 2020; CSDN; [hexo博客front-matter格式](https://blog.csdn.net/qq_38747027/article/details/107967518);
