---
title: "3分钟写一个R包"
description: "3分钟写一个R包"
url: rpackage2
date: 2020/06/22
toc: true
excerpt: "快速打包一个简单的R包"
tags: [R]
category: [R, Pack your pack]
cover: 'https://s1.ax1x.com/2020/06/22/NJkJnH.jpg'
thumbnail: 'https://s1.ax1x.com/2020/06/22/NJkJnH.jpg'
priority: 10000
---

## 3分钟写一个R包

主要参考：[https://blog.csdn.net/jiyang_1/article/details/53283504](https://blog.csdn.net/jiyang_1/article/details/53283504)

<a name="VITLM"></a>
## 3分钟写个R包
<a name="CCkEd"></a>
### 1. 新建目录，快速写一个函数 
```bash
mkdir R_package

echo '
hello <- function() {
  print(paste("Hellow World"))
}' > hello.R
##这里的 hello.R 就是所有的需要放在包里面的函数了
```

<a name="b8zup"></a>
### 2. 在R中创建骨架
```r
##该目录打开R
package.skeleton(name="hello",code_files="hello.R")
```

<a name="G7sG0"></a>
### 3. 根据需要添加相关相关信息
为了赶上3min，我只改了两个必须改的地方。
```bash
## 在title 下面加一行，不然本地安装报错
sed -i 's/%%  ~~function to do ... ~~/喵喵喵？/' hello/man/hello.Rd

##删除此行，不然github远程安装的时候报错
sed -i '/~~ Optionally other standard keywords, one per line, from file KEYWORDS in the R documentation directory ~~/d' hello/man/hello-package.Rd

R CMD build  hello
##R CMD check hello_1.0.tar.gz
##可以不check 应为有错误也能安装，一般只要能打包
##但是上Cran就一定要check了

```

不run第3部分第二行代码的结果（改title）<br />
![NJk8je.png](https://s1.ax1x.com/2020/06/22/NJk8je.png)




<a name="gJ2cL"></a>
### 4. 开始安装
进入R安装。注意**路径**。
```r
install.packages("hello_1.0.tar.gz", type="source", repos=NULL)
```

成果！ 撒花<br />
![NJkYBd.md.png](https://s1.ax1x.com/2020/06/22/NJkYBd.md.png)


<a name="zPzeB"></a>
### 5. 运行测试
```r
library(hello)                                                                                                                
hello()

##输出结果
##Hellow World

?hello#查看函数信息
packageDescription('hello') # 查看信息和安装地址

##最后删除我们的包
remove.packages('hello' )
```
Details:<br />

Indexofhelptopics:<br />
![NJkJnH.jpg](https://s1.ax1x.com/2020/06/22/NJkJnH.jpg)






  <br />
<a name="3Q8gZ"></a>
### 6. 完成！
接下来可以认真的写一个自己的包啦！<br />可以和大众分享，也可以是储存几个自己习惯的函数<br />看看表，有没有超过3min！
![NJkUAI.md.png](https://s1.ax1x.com/2020/06/22/NJkUAI.md.png)



<a name="I7vyG"></a>
## 最后
上传到github吧

<a name="Wx9L4"></a>
### Github
新建目录后，直接吧hello下的文件，全部上传即可，安装

```r
devtools::install_github("Karobben/Test")
```

不进行第3部分第5航代码的结果：
![NJktHA.md.jpg](https://s1.ax1x.com/2020/06/22/NJktHA.md.jpg)

统统上传～～<br />
![NJkaNt.md.png](https://s1.ax1x.com/2020/06/22/NJkaNt.md.png)
