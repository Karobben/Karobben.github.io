---
title: "Hexo: Footnotes"
date: 2020/08/04
description: "hexo: footnotes| hexo: 脚注插件"
url: hexo_footnotes
toc: true
excerpt: "hexo: footnotes plugin install| hexo: 脚注插件"
tags: [Hexo, MarkDown]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---
## Hexo: Footnotes

Reference: [张慕晖 2018](https://zhanghuimeng.github.io/post/add-footnote-plugin-for-hexo-blog/)

We can using `hexo-renderer-markdown-it` to achieve this.
But before we install it, we need to remove the default widget `hexo-renderer-marked`. Besides `hexo-render-markdwon-it` doesn't have checkbox plugin. So, you'd like to downloads `markdown-it-task-checkbox`, too.

```bash
npm un hexo-renderer-marked --save
npm i hexo-renderer-markdown-it --save
npm install markdown-it-task-checkbox  --save
```

Codes for `_config.yml`
```yml
## Markdown-it config
### Docs: https://github.com/celsomiranda/hexo-renderer-markdown-it/wiki
markdown:
  # 渲染设置
  render:
    # 置为true时，html内容保持不变；置为false时，html内容将被转义成普通字符串
    html: true
    # 是否生成与XHTML完全兼容的标签（虽然我不懂是什么意思）
    xhtmlOut: false
    # 置为true时，每个换行符都被渲染成一个<br>（即Hexo的默认表现）；置为false时，只有空行才会被渲染为<br>（GFM的默认表现）
    breaks: true
    # 是否自动识别链接并把它渲染成链接
    linkify: true
    # 是否自动识别印刷格式（意思是把(c)渲染为©这样的）
    typographer: true
    # 如果typographer被设置为true，则该选项用于设置将dumb quotes（""）自动替换为smart quotes
    quotes: '“”‘’'
  # 设置所需插件
  plugins:
    - markdown-it-abbr
    - markdown-it-footnote
    - markdown-it-ins
    - markdown-it-sub
    - markdown-it-sup
    - markdown-it-task-checkbox
  # 锚点设置（因为我没有尝试相关内容，所以就不翻译相关说明了）
  anchors:
    level: 2
    collisionSuffix: 'v'
    permalink: true
    permalinkClass: header-anchor
    permalinkSymbol: ¶
```

## Grammar for Footnotes
```md
As you can see[^2], the order of the footnotes is doesn't matter[^1].

[^2]: Word: see
[^1]: Word: matter
```

## Result

### Before:

![aBejnU.md.png](https://s1.ax1x.com/2020/08/04/aBejnU.md.png)

### Now:

( You can see the codes at above)
As you can see[^2], the order of the footnotes is doesn't matter[^1].

[^2]: Word: see
[^1]: Word: matter
