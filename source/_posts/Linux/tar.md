---
title: "Compress and Decompress"
url: compress_linux
description: "How to compress and decompress files and directories in linux command lines"
date: 2020/06/26
toc: true
excerpt: "Compress and Decompress in linux command lines."
tags: [Linux, tar, bash]
category: [Linux, Bash, More]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## tar

##reference:[https://man.linuxde.net/tar](https://man.linuxde.net/tar)


- Compress:
  `tar -zcvf File.tar.gz File`
- Decompress:
  `tar - zxvf File.tar.gz`

|Format|Decompress|compress|
|:-|:-|:-|
|.tar|xvf|cvf|
|.tar.gz|zxvf|zcvf|
|.tar.bz2|jxvf|jcvf|
|.tar.bz|jxvf|
|.tar.Z|.tar.Z|.tar.Z|
