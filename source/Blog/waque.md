---
title: "为什么我要使用瓦雀| markdown 语法大全"
description: "为什么我要使用瓦雀| markdown 语法大全介绍"
url: waque
---

# 为什么我要使用瓦雀

# 爲什麼使用瓦雀
瓦雀是[官方又推薦](https://www.yuque.com/yuque/help/third-party-tools#waque)的一個，三方[開源程序](https://github.com/yesmeck/waque)。方便本地管理，編輯，下載，上傳markdown語法的文件
具體可以看[官方文檔](https://www.yuque.com/waquehq/docs/getting-started)
# 哪些人適合使用瓦雀
- 想要在本地直接備份，想類似git一樣管理自己的筆記
- 希望在本地用markdown語法編輯記錄
- 希望用自己喜歡的編輯器的人
- 希望自由插入html語法(部分)的人
- 希望可以方便存入其他庫備份的人(比如, 百度雲, github)
- 喜歡用代碼畫流程圖的人

# 不適合人羣
- 不熟悉markdown語法的人
- 不會用代碼畫流程圖/腦圖
- 討厭命令行的人

Markdown 語法雖然輕量, 但是足夠強大. 不過, 語雀, GIthub等, <b>並不是就能完美支持</b>markdown和html的所有語法. 因此, 還請<span style="color:salmon;">跟具自己的實際情況</span>來選擇個人所需.

# 使用方式
<font s><a scr="https://www.yuque.com/waquehq/docs/getting-started">詳情點擊</a></font>

## 安裝
```bash
sudo npm i -g waque
```
## 登錄
```bash
waque login
```
這個時候彈出一張網頁, 掃碼登錄授權就好
## 初始化配置
創建一個文件夾(倉庫), 進入後,初始化
```bash
waque init
```
選擇一個 Repository

## 使用
然後就可以通過`waque export`下載本倉庫所有的文本
通過`waque export ***.md` 便可以上傳同步筆記了!
<p style="color:salmon;">注意:</p> 直接編輯文檔並上傳, 會出現:

```bash
✖  error     更新 安卓手机 Turmux 搭建博客[is3vdm]
{ status: 400,
  message: '抱歉，语雀不允许通过 API 修改 Lake 格式文档，请到语雀进行操作。' }
```

只需要去網頁上, 把該文檔刪除, 然後就可以上傳了.




# 已知問題

大部分和簡書顯示類似: [择势勤 2019](https://www.jianshu.com/p/ebe52d2d468f)[^A]

[^A]: 择势勤; Markdown语法大全(超级版); 简书; 2019.05.02 16:37:47.


### 在语雀無法使用(hexo 可以):
- 腦圖;流程圖等語法
- `<details>`或region 摺疊標籤
- html 的 height 屬性
- `<font-size="100px">` style font-size 無效
- `<font></font>` font 屬性標籤
- `<i>`
- `<p style="...">`
- 代碼摺疊



### 可

#### 文字
- 註釋`[\\]:#` `<div style='display: none'>`
- `<img>` 標籤
- `<div align=right>` 排版標籤
- `这是*倾斜*的文字` 这是*倾斜*的文字
- `这是**加粗**的文字` 这是**加粗**的文字
- `这是 ***斜体加粗*** 的文字` 这是 ***斜体加粗*** 的文字
- `这是文字^右上角^` 这是文字^右上角^
- `这是文字~右下角~` 这是文字~右下角~
- `这是==高亮==文字` 这是==高亮==文字 (**hexo 失效**)
- `这是加~~删除线~~的文字` 这是加~~删除线~~的文字
- ``![图片alt](图片地址 ''图片title'')``
- ```<s><sub><sup><u><b>```
- `flow`
- `mermaid`

#### 缩写

```
convert to HTML
*[HTML]: HyperText Markup Language
```
convert to HTML
*[HTML]: HyperText Markup Language

#### 待办事项 (**hexo 失效**)
`- [ ] item`
- [ ] item

`- [x] item2`
- [x] item2

#### 公式 (**hexo 失效**)
解决办法： [链接](http://Karobben.github.io/Blog/Hexo_math.html)
```md
$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt
$$
```

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt
$$

#### 表格

|表头1|表头2|表头3|表头4|5|
|--|---------|:--|--:|:--:|
|普通|加宽|靠左对齐|靠右对齐|居中|
|普普通通|宽|我从左边开始|我向右看齐|我在中间|

更多: [复杂表格 aladdin_sun 2018](https://blog.csdn.net/sunbocong/article/details/81033915)

```bash
#flow codes for below
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: 这啥啊|invalid
cond=>condition: Yes or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|request

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2(right)->op1
```
```flow
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: 这啥啊|invalid
cond=>condition: Yes or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|request

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2(right)->op1
```

```bash
#mermaid codes for below
graph LR;
　　Portal-->|发布/更新配置|Apollo配置中心;
　　Apollo配置中心-->|实时推送|App;
　　App-->|实时查询|Apollo配置中心;
```
Citation: [cicero 2018](https://www.cnblogs.com/nanqiang/p/8244309.html)
```mermaid
graph LR;
　　Portal-->|发布/更新配置|Apollo配置中心;
　　Apollo配置中心-->|实时推送|App;
　　App-->|实时查询|Apollo配置中心;
```
更多mermaid例子：
[道隐无名 2015](https://www.cnblogs.com/dao0/p/4489837.html)
[七适散人 2018](https://cloud.tencent.com/developer/article/1334691)

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
