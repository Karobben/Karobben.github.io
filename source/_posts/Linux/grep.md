---
title: "grep 搜索"
description: "grep 搜索"
url: grep2
date: 2020/06/26
toc: true
excerpt: "grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p, which has the same effect."
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, Bash, awk/grep/sed]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## grep 搜索


```bash
grep
##Usage: grep [OPTION]... PATTERN [FILE]...
##Try 'grep --help' for more information.
```
**
<a name="90laC"></a>
## 1. 快速上手

```bash
## 创建测试文件
echo -e "ab\na\nb\nc\nd\ne\nf\ng\nA\nB\nC" > test.txt
## 搜索存在'a'的内容
grep a test.txt
```

![NseFc8.png](https://s1.ax1x.com/2020/06/26/NseFc8.png)


<a name="HflCw"></a>
## 2. 常用
$gr
```bash
## "."模糊匹配
grep a. test.txt

```
![Nse9ht.png](https://s1.ax1x.com/2020/06/26/Nse9ht.png)


```bash
## 显示所在行
grep -n a test.txt
```
![Nsei1f.png](https://s1.ax1x.com/2020/06/26/Nsei1f.png)

```bash
## 输出匹配次数(多少行)
grep -c a test.txt
```
![NsZv0H.png](https://s1.ax1x.com/2020/06/26/NsZv0H.png)


```bash
## 忽略大小写
grep -i a test.txt
```
![NseSAA.png](https://s1.ax1x.com/2020/06/26/NseSAA.png)

```bash
##多项匹配: "|" 分隔开多选必配项。注意，如果我没记错的话，最多可同时匹配1000项
grep -E 'a|b' test.txt
```
![NseP9P.png](https://s1.ax1x.com/2020/06/26/NseP9P.png)

```bash
##打印匹配项的上下一行或多行
grep -nA 1 A test.txt # 等同于 grep -n -A 1  A test.txt， -n 用于显示行数
grep -nB 1  A test.txt # 显示匹配的上一行
grep -nA 1 -B 1  A test.txt # 同时显示匹配的上下两行
```
![NseVBQ.png](https://s1.ax1x.com/2020/06/26/NseVBQ.png)
<a name="pFQtn"></a>
## 3. 快速应用：

抓取fasta序列：<br />测试文件：[test.fa.txt](https://www.yuque.com/attachments/yuque/0/2020/txt/691897/1581071887664-9edb6585-1fc9-4bf3-b5b4-181123b53c33.txt?_lake_card=%7B%22uid%22%3A%221577264129011-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Ftxt%2F691897%2F1581071887664-9edb6585-1fc9-4bf3-b5b4-181123b53c33.txt%22%2C%22name%22%3A%22test.fa.txt%22%2C%22size%22%3A6581%2C%22type%22%3A%22text%2Fplain%22%2C%22ext%22%3A%22txt%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22FBFrY%22%2C%22card%22%3A%22file%22%7D)<br />首先，把fasta文件规整成一行ID，一行序列格式。

```bash
##通过一系列骚操作，把多行序列转换成单行
cat test.fa.txt | tr '\n' '#'| sed 's/#>/\n>/g'|sed 's/#/\n/;s/#//g' > test.fa
```

<a name="PfuOk"></a>
### 3.1，获取所有的fasta ID
```bash
grep ">" test.fa
```
![NseptI.png](https://s1.ax1x.com/2020/06/26/NseptI.png)

<a name="B2a92"></a>
### 3.2，获取杠内ID
```bash
grep ">" test.fa| awk -F\| '{print $2}'
```
![NsZx7d.png](https://s1.ax1x.com/2020/06/26/NsZx7d.png)


<a name="frpmZ"></a>
### 3.3，通过grep 多项匹配，获取前两个ID及其序列
```bash
grep -EA 1 $(grep ">" test.fa| awk -F\| '{print $2}'|head -n 2| tr '\n' '|'|sed 's/^/"|/;s/$/"/') test.fa
##or
grep -EA 1 $(grep ">" test.fa|\
awk -F\| '{print $2}'|\
head -n 2|\
tr '\n' '|'|\
sed 's/^/"|/;s/$/"/') test.fa

'''
其中，$(grep ">" test.fa| awk -F\| '{print $2}'|head -n 2| tr '\n' '|'|sed 's/^/"|/;s/$/"/') 的结果为
的结果为：
"|Q6GZX4|Q6GZX3|"
因此可以直接被 grep -E 参数识别
'''
```

![NseEng.png](https://s1.ax1x.com/2020/06/26/NseEng.png)

<a name="t84Jr"></a>
## 4. 其他详细请看：
参数解释：[https://www.runoob.com/linux/linux-comm-grep.html](https://www.runoob.com/linux/linux-comm-grep.html)<br />复杂正则匹配：[https://www.cnblogs.com/keithtt/p/6820540.html](https://www.cnblogs.com/keithtt/p/6820540.html)





## Multi-words/strings grep

Shell can only 1000 args and if you exceeded it, you would end as error. For doing large number or words/strings match, we need to input words/strings in a file and grep it later. But the consuming time is raising largely after 1000.

| Number or words | time     |
| :------------- | :------------- |
|  1000      | 0m1.954s       |
|2000 | 0m4.825s |
|5000 | 0m26.232s |

Though, you can match thousands of words in a time, but you don't have too or it doesn't deserve it. In this time, a loop would much faster than single threads grep.
