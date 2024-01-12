---
title: "如何在deepin上安装scrcpy"
description: "如何在deepin上安装scrcpy"
url: scrcpy2
date: 2020/06/26
toc: true
excerpt: "This application provides display and control of Android devices connected on USB (or over TCP/IP). It does not require any root access. It works on GNU/Linux, Windows and macOS."
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, Software]
cover: 'https://s1.ax1x.com/2020/06/26/NsEzKe.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsEzKe.png'
priority: 10000
---

## 如何在deepin上安装scrcpy

source: [https://www.linuxuprising.com/2019/03/control-android-devices-from-your.html](https://www.linuxuprising.com/2019/03/control-android-devices-from-your.html)

scrcpy 作为一个良心开源投屏加控制软件，真是太强大了。 不需要手机安装额外垃圾东西，比自带的手机投屏到电脑功能要稳定很多， 不容易崩溃(某win)。稳定好， 高清画面也不容易掉帧，真是太舒服了。

| <br /><br />**本来**这个软件非常友好啊, 但是却应为deepin 系统的关系, apt源没有, snap在上国又很鸡肋,完全不能用, 只能自己编译。<br /><br /><br />编译就编译吧， 偏偏又有很多的坑要填 = = 我是被虐的不要不要的反正。<br />对于小白来说， configure + make， 还是很友好的， 报错清晰，debug简单。 但是第一次接触mason 和nijia 来说- -有点噩梦了。<br /><br />最开始想着直接下最新的1.12.1， 然后直接编译， 一堆错误。 后面终于通过googel 到了一个全能贴， 发现需要安装服务。按照要求，安装服务器后，又出现了，ninjia 报错说没有找到1.11.1 的服务器。。？？？ 好吧，去下好了1.11.1的， 总算是没有报错了， 输入scrcpy 也成功了， 没有报错。<br />并且和成功运行的画面一样， 手机收到了确认。 但是- - 就是半天不显示画面。。。 没反应了。<br /><br />瞎折腾了几下， 抱着实时心态， 既然报错说1.11.1， 可能是版本对不上 == ？ 索性干脆安装1.11.1的包， 删掉重来。 终于- -唉， 成功了 - - 撒花！！！<br /><br />下面是详细教程： |![NsEzKe.png](https://s1.ax1x.com/2020/06/26/NsEzKe.png)|
|---|:---:|



<a name="ss2DJ"></a>
## 1. 各种依赖：

```bash
sudo apt install adb ffmpeg libsdl2-2.0.0 make gcc pkg-config meson ninja-build \
    libavcodec-dev libavformat-dev libavutil-dev libsdl2-dev
```

<a name="T1Pew"></a>
## 2. 下载 
**<br />地址：[https://github.com/Genymobile/scrcpy/releases/tag/v1.11](https://github.com/Genymobile/scrcpy/releases/tag/v1.11)


![NsEvvD.png](https://s1.ax1x.com/2020/06/26/NsEvvD.png)

现在圈内两个， 代码：<br />第一个加尾坠“.jar”<br />第二个解压
```bash
wget -c https://github.com/Genymobile/scrcpy/releases/download/v1.11/scrcpy-server-v1.11
wget -c https://github.com/Genymobile/scrcpy/archive/v1.11.tar.gz

mv scrcpy-server-v1.11 scrcpy-server-v1.11.jar
tar -zxvf v1.11.tar.gz
```

<a name="Aqkr0"></a>
## 3. 安装

<a name="Tgac6"></a>
### 安装服务
```bash
sudo install scrcpy-server-v1.11.jar /usr/local/bin/scrcpy-server.jar
```

<a name="fMc6q"></a>
### 编译

```bash
cd scrcpy-1.11
meson build --buildtype release --strip -Db_lto=true  -Dprebuilt_server=../scrcpy-server-v1.11.jar

cd build
ninja

sudo ninja install
```

这一步可能出现错误：

<pre>
ninja: error: '/home/ken/Soft/scrcpy-server-v1.11.jar',
needed by 'server/scrcpy-server', missing and no known rule to make it
</pre>

因为没有找到server 的路径， 因此只需要把那前面下载的文件， 拷贝或者移动到这个路径就好了， 然后重新ninjia


## 最后
插入数据线， 打开USB调试模式，输入scrcpy后手机勾选确认
```bash
adb tcpip 5555
scrcpy
```

terminal可能会出现如下代码：

<pre>
INFO: scrcpy 1.11 <https://github.com/Genymobile/scrcpy>
[100%] /data/local/tmp/scrcpy-server
bind: Address already in use
ERROR: Could not listen on port 27183
</pre>

端口被占用或无法使用， 我们换一个端口：<br />输入 scrcpy -p 1234<br />
```bash
scrcpy -p 1234
INFO: scrcpy 1.11 <https://github.com/Genymobile/scrcpy>
[100%] /data/local/tmp/scrcpy-server
INFO: Initial texture: 1080x2336
INFO: Device clipboard copied
[server] WARN: Could not inject char u+5509
[server] WARN: Could not inject char u+ff0c
[server] WARN: Could not inject char u+5509
```

等待一下就好啦！

安装成功的环境：
Ubuntu 18
Deepin 15.1
Manjaro 21.0.4 Ornara

Enjoy~
