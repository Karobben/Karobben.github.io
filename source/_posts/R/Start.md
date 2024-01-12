---
title: "How to Start With R"
description: "How to Started With R"
url: start_r
date: 2020/06/03
toc: true
excerpt: "几个在线自学R的平台"
tags: [R]
category: [R, Beginner]
cover: 'https://s1.ax1x.com/2020/06/03/taYsKI.md.png'
thumbnail: 'https://s1.ax1x.com/2020/06/03/taYsKI.md.png'
priority: 10000
---
## How to Started With R
R语言新手快速入门起步

## 实验楼

國內網站， 所以全是中文， 並且速度快。 新手超級友好！
缺點： 免費課程較少（5個，鏈接列在後面了）
不過， 免費的， 對與新手入門來說， 還是夠了。！（反正都是， 從入門，到放棄 23333）
並且基礎的， 機器學習入門，也有。所以還是蠻OK的，首推

### 界面

實驗樓界面比較簡潔。
左邊是介紹， 和練習用的代碼
右邊是一個完全的， linux 圖形虛擬桌面。
好處就是， 他是一個完全的linux圖形界面系統
壞處就是， 應爲是基於瀏覽器，所以是有些快捷鍵無法使用。
此外，就是比較浪費，網絡， 計算機的性能， 反應較慢。
並且無法檢測代碼對錯進行打分評價。
不過因此， 看見太簡單的教程也可以直接跳過，避免冗餘的重複練習。
![taB2CV.png](https://s1.ax1x.com/2020/06/03/taB2CV.png)

免费课程列表：
1. [R 语言基础入门](https://www.shiyanlou.com/courses/855)
2. [R 语言高级数据管理](https://www.shiyanlou.com/courses/867)
3. [R 语言英国房屋价格建模预测](https://www.shiyanlou.com/courses/882)
4. [R 语言序列数据挖掘](https://www.shiyanlou.com/courses/887)
5. [R 语言进行商业问卷分析](https://www.shiyanlou.com/courses/873)

## DataCampe

虽然是英文界面， 国外服务器， 但是速度还是挺快的。 比之后测试的 CodaAcademy 要好很多。 而且输入界面，更像Rstudio


[首页](https://campus.datacamp.com/)
![taYsKI.md.png](https://s1.ax1x.com/2020/06/03/taYsKI.md.png)

### 练习界面
分区如下图所示， 输入代码后， 按输入区的submit 提交即可下一题
![tat8Jg.png](https://s1.ax1x.com/2020/06/03/tat8Jg.png)

### 下一题
![taY6qP.md.png](https://s1.ax1x.com/2020/06/03/taY6qP.md.png)

## code academy
Website: [CodeAcademy](https://www.codecademy.com/courses/learn-r)
### 主页
![ta3YtJ.png](https://s1.ax1x.com/2020/06/03/ta3YtJ.png)

### 第一页
![ta3th9.md.png](https://s1.ax1x.com/2020/06/03/ta3th9.md.png)
### 学习界面
![ta3UpR.png](https://s1.ax1x.com/2020/06/03/ta3UpR.png)

```r
12+3
```

网速略慢。

## swirl
Learn R in R

```r
install.packages("swirl")
library(swirl)
swirl()
```
```
| Welcome to swirl! Please sign in. If you've been here before, use the same
| name as you did then. If you are new, call yourself something unique.

What shall I call you?
```
我很皮的输入`papa` /滑稽
```
| Thanks, papa. Let's cover a couple of quick housekeeping items before we
| begin our first lesson. First of all, you should know that when you see
| '...', that means you should press Enter when you are done reading and ready
| to continue.

...  <-- That's your cue to press Enter to continue
```

更具指引， 你將開始下一個課程， 然後選擇他：
### 開始學習！
####　一大波文字說明即將到來， 2333
```
|                                                                      |   0%

| The simplest and most common data structure in R is the vector.

...

 |==                                                                    |   3%
| Vectors come in two different flavors: atomic vectors and lists. An atomic
| vector contains exactly one data type, whereas a list may contain multiple
| data types. We'll explore atomic vectors further before we get to lists.

...

 |====                                                                  |   5%
| In previous lessons, we dealt entirely with numeric vectors, which are one
| type of atomic vector. Other types of atomic vectors include logical,
| character, integer, and complex. In this lesson, we'll take a closer look at
| logical and character vectors.
```
#### 終於開始了，2333
```R
| First, create a numeric vector num_vect that contains the values 0.5, 55,
| -10, and 6.
```
輸入 `0.5`
```
[1] 0.5

| You almost had it, but not quite. Try again. Or, type info() for more
| options.

| Recall that the c() function is used for creating a vector. If you forget how
| to use it, use ?c to access the help file. Don't forget to assign the result
| to a new variable called num_vect.

>
```

ummm， 我覺得相對於來學R， 這個更適合用來學英語， 哈哈哈哈哈
