---
title: "R 语言报错集"
description: "R 语言报错集"
url: error_codes2
date: 2020/06/20
toc: true
excerpt: "heatmap is fun!"
tags: [R, Plot, Interoperable Plot]
category: [R, others]
cover: 'https://s1.ax1x.com/2020/08/15/dFpkUH.png'
thumbnail: 'https://s1.ax1x.com/2020/08/15/dFpkUH.png'
priority: 10000
---

## R 语言报错集

<a name="YqNpC"></a>
## 写R包

<a name="ll1lF"></a>
### 打包错误
```bash
R CMD build  hello

* checking for file ‘hello/DESCRIPTION’ ... OK
* preparing ‘hello’:
* checking DESCRIPTION meta-information ... OK
* installing the package to process help pages
      -----------------------------------
* installing *source* package ‘hello’ ...
** using staged installation
** R
** byte-compile and prepare package for lazy loading
** help
Warning: /tmp/Rtmp9IseJR/Rbuild799a14248b2f/hello/man/hello-package.Rd:26: All text must be in a section
*** installing help indices
Error in Rd_info(db[[i]]) :
  missing/empty \title field in '/tmp/Rtmp9IseJR/Rbuild799a14248b2f/hello/man/hello.Rd'
Rd files must have a non-empty \title.
See chapter 'Writing R documentation' in manual 'Writing R Extensions'.
* removing ‘/tmp/Rtmp9IseJR/Rinst799a2d1feb80/hello’
      -----------------------------------
ERROR: package installation failed

```

错原： “missing/empty \title fiel”， 没有改title<br />解决： sed -i 's/%%  ~~function to do ... ~~/喵喵喵？/' hello/man/hello.Rd

<a name="rGBi1"></a>
### 上传至github后安装报错
```r
devtools::install_github("Karobben/Test")

Downloading GitHub repo Karobben/Test@master
✔  checking for file ‘/tmp/Rtmp3HTrN3/remotes225241f0c918/Karobben-Test-252c791/DESCRIPTION’ ...
─  preparing ‘hello’:
✔  checking DESCRIPTION meta-information
─  installing the package to process help pages
─  saving partial Rd database (688ms)
─  checking for LF line-endings in source and make files and shell scripts
─  checking for empty or unneeded directories
─  building ‘hello_1.0.tar.gz’

Installing package into ‘/home/ken/R/x86_64-pc-linux-gnu-library/3.6’
(as ‘lib’ is unspecified)
* installing *source* package ‘hello’ ...
** using staged installation
** R
** byte-compile and prepare package for lazy loading
** help
Error : (converted from warning) /tmp/RtmpixBxlB/Rbuild2ccc35a25d23/hello/man/hello-package.Rd:26: All text must be in a section
ERROR: installing Rd objects failed for package ‘hello’
* removing ‘/home/ken/R/x86_64-pc-linux-gnu-library/3.6/hello’
```

错原：Error : (converted from warning) /tmp/RtmpixBxlB/Rbuild2ccc35a25d23/hello/man/hello-package.Rd:26: All text must be in a section<br />解决： 删除 man/hello-package.Rd 的 第 26 行
