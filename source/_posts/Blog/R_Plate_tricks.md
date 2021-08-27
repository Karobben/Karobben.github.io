---
title: "用R语言来指导实验"
description: "我居然用R语言来指导点样顺序和位置"
date: 2020/09/03
url: r_tricks
toc: true
excerpt: "我居然用R语言来指导点样顺序和位置"
tags: [R, Sanger Sequencing, Plot]
category: [R, others]
cover: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Microtiter_plate.JPG/400px-Microtiter_plate.jpg'
thumbnail: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Microtiter_plate.JPG/400px-Microtiter_plate.jpg'
covercopy: '© wikipedia.org'
priority: 10000
---

## 我居然用R语言来指导实验点样顺序和位置

96孔板大家都熟悉吧,

如果样孔都一样量, 用排枪, 刷刷刷的, 就结束了, 超级方便.
可是就怕, <span style="background:salmon">不同孔, 不同样本, 还不同的量</span>. 这就, 非常恼火了.
加的慢不说, 还容易搞错, 加到, 怀疑人生


## 事情是这样子的。
入职了一家测序公司, 在测序之前, BDT反应要根据客户模板的个人情况点样.
可是, 客户多, 且杂, 所以我就要
1. 不同客户模板
2. 引物浓度不一样
3. 有的单个样本重复使用, 用不同引物测
4. 有很多通用引物, 前后都用
5. 更具不同引物, 加不同浓度对应的水

一开始, 我想象着, 一个高级的, AR交互软件, 告诉你哪个孔加哪个样, 加多少, 然后判断是否已完成.

算了, 还是想想把... 那, 普通交互软件, 开始加水, 点一软件, 同浓度水的样孔, 高亮显示? 可是我不会呀, 用QT? TK? 好像可以, 可是没有项目经验呀...

最后, 好吧, 用R语言画图吧. 96孔板是吧, 热图正好.
(理想很丰满, 显示很骨感 = =)

公司的系统还是不错的, 点样可以直接导出excel表格. 因此, 直接用`library(readxl)` 读取excel.
画图, 就用`pheatmap`, 简单方便.
中文字体库, 用 `library(showtext)`

格式由于涉密, 就不展示出来了.
看看处理结果把:

## 让我们来看图吧

### 第一步, 加水:
像这样, 根据对应高亮孔, 加2ul水, 就好
![Water](https://s1.ax1x.com/2020/09/03/wC0mNj.png)

### 第二步, 引物:
最开始就用觉得引物太麻烦, 想这个样子, 前面用了, 后面还要用. 对照打印的表格来看, 就太麻烦了. 现在, 在加 B9 的时候, 就可以很明显的发现, C 也需要也需要加, 并且, D 也需要. 这就减少了, 重复找一个通用引物的麻烦
![Primers](https://s1.ax1x.com/2020/09/03/wC0wgx.png)

### 第三步, 模板:
有时候, 模板前后都得加, 比如第一个在 A 行, 第二次加就跳到 E 行, 有这个图, 就会方便很多
![Samples](https://s1.ax1x.com/2020/09/03/wC0oqS.png)

## 总结:
**优点**: 清楚明了, 防止前后重复找一个东西.
还是蛮有意思的. 有了这个小脚本, 我的加样时间, 大大缩短了.
**缺点**: 一次生成图片太多... 样本乱的时候, 可以生成上百张图片. 每次手动翻下一张图片, 还是不方便的.
