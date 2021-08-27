---
toc: true
url: kivy_tutorial
priority: 10000
date: 2021-05-31 17:53:04
title: "Kivy 新手入门避坑指南"
ytitle: "Kivy 新手入门避坑指南"
description: "Kivy 新手入门避坑指南"
excerpt: "Kivy 新手入门避坑指南"
tags: [Python, Kivy]
category: [Python, Kivy, Toolbox]
covercopy: <a herf="https://realpython.com/mobile-app-kivy-python/">© RealPython</a>
cover: 'https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/Kivy-Tutorial_Watermarked.11c2f9141907.jpg&w=960&sig=7ed0c7170ace6f5bc13eb9ae5900a15bb6a8fd30'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
---

## Kivy 新手入门避坑指南

个人说说使用kivy的原因： 不会java, 不会C， 不会。。。 简而言之， 除了python, 啥也不会。但是又想写点 android 的apk. 所以， kivy成了我唯一的选择了。。。 在此奉劝， 如果只是一开发安卓apk为主要目的， 还是不要用比较好。 虽然kivy的买点在跨平台， 但是实际上， 平台夸起来， 很吃力。

我说说我现在的进展吧： （针对安卓）
- requests 库基本没问题
- Opencv 不完美。 可以配合摄像头做人脸识别等
  但是无法读取视频。 可以输出视频，但是格式有限制。
- imageio 输出gif
- PIL 基本没什么问题
- numpy ok
- 可开启http服务
- 可调用android web浏览器（java）

目前来说， 其实已经可以做很多事情了。不过得自己注意，电脑和安卓之间的兼容问题。

## 开始前的避坑
1. python 版本
    - 都2021年了， 不会真的还有人在用python2吧？？ 不会吧不会吧不会吧？？？ 请赶紧退坑， 谢谢。
    - python3 也不能乱用。 之前我用的 3.7.6， 然后打包request之后， 能用， 但是再出结果之后， 就会崩溃闪退。 我也不知道为啥。最后更具stack overflow 的解释， 换上了3.7.5， 就完全没问题了。 真的很奇奇怪怪=  =
    - 但是- - 目前我还是用的， 3.7.6。。。为什么？ 俺也不知道。反正：==不要用最新的不要用3.9，更加不要用4==。 不听的老人言， 吃亏在眼前
2. kivy和kivymd版本
    - Kivy和kivymd版本倒是没这么多的肯。 但是，md的坑是真大。 如果用错了版本， 你就会发现， 官方文档好多是“错的”！！更不不能运行。 其实官方文档怎么会有问题呢？ 动动脚趾头嘛？当然不会啦！ 对一下版本号就知道了。 切换版本以后， 就好。所以， 版本可以瞎用， 自己明白就好
    - 另外， kivy和kivymd版本， 自己瞎用无所谓， 但请一定记得， 测试和打包的版本，保持一致。 不然， 到时候肯定会有问题的。 开始不会怎么样= = 东西多了复杂就会发现， 电脑和手机结果， 不一样， 甚至手机直接闪退 = =
3. 打包
    - buildozer 打包hello world, 还是很方便的， 尤其是环境准备好之后， 再次打包就简单快了。
    - 对于国内来说， 打包大部分失败的原因都是， 网络链接问题， 下载失败。所以， 没事的话， 先多重复几次， 然后盯一下卡在了哪里。 一般是先卡很久， 然后才会报错。
    - 更复杂的东西， 比如打包opencv, 需要自己给sdk, 这个就麻烦了。 不过也只是第一次麻烦， 会了以后， 其实蛮简单的。
    - 有些东西， 是真的没发打包= =（打包了也没法用）可能需要更特殊手段。 这就看大家大显神通了
4. 报错
    - 如果在电脑端运行的报错， 都看不懂的话， 那真的， 求你了， 放弃kivy吧。你大概适合换一个饭碗\兴趣。python的错误， 都是精确到具体哪一行哪一個函数的说- -
    - adb logcat 安卓报错
      adb 报错的话， 一般来说， 也是python的运行问题。 如果这样的话， 只要在日至里搜寻 `I python` 就好。 对于linux, 可以直接`adb logcat| grep "I python"`
      再复杂的话， 就可以看看 `I python` 前面的编号，然后抓去这一个ID, 就可以获得这个程序所有的 adb log 了。但是这个内容报错- - 就会比较复杂了 = = 反正我是看不懂的。 贴上 stack overflow 也从来没有被回答过- - 我贴的几个= = 好难呀。  
5. 路径
    - 安卓文件安装后， 会在/data目录下创建该app的文件夹。你在使用对应app的时候，是有读写权限的。 但是在其他地方， 比如自带的文件管理器， 对该app没有任何读写权限。 所以， 你的把想保存的东西放在别的地方。 用户自己有读写权限的根目录， 一般为`/storage/emulated/0`。
6. icon-font 消失
    - 请加入字体 `sdl2_ttf==2.0.15` 在 requirements那里
## kivy 及其打包环境快速配置

首先， 这是我的系统环境：

<pre>
██████████████████  ████████     ken@manjaro
██████████████████  ████████     OS: Manjaro 21.0.5 Ornara
██████████████████  ████████     Kernel: x86_64 Linux 5.4.118-1-MANJARO
██████████████████  ████████     Uptime: 20h 14m
████████            ████████     Packages: 1599
████████  ████████  ████████     Shell: zsh 5.8
████████  ████████  ████████     Resolution: 1920x1080
████████  ████████  ████████     DE: GNOME 3.38.5
████████  ████████  ████████     WM: Mutter
████████  ████████  ████████     WM Theme: Matcha-dark-sea
████████  ████████  ████████     GTK Theme: Matcha-sea [GTK2/3]
████████  ████████  ████████     Icon Theme: Papirus-Dark-Maia
████████  ████████  ████████     Font: Noto Sans 11
████████  ████████  ████████     Disk: 705G / 1.5T (50%)
                                 CPU: Intel Xeon E3-1535M v6 @ 8x 4.2GHz [77.0°C]
                                 GPU: Quadro M2200
                                 RAM: 4366MiB / 64042MiB
</pre>

这里， 根据 [john100 2021](https://archived.forum.manjaro.org/t/solved-how-to-install-kivy-on-manjaro/113849) 在 arch 论坛的建议， 直接先安装 python 3.7.6， 然后配置一个虚拟环境

### 安装 Python
```python
cd /usr/local
sudo wget http://python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz
sudo tar xf Python-3.7.6.tar.xz
cd Python-3.7.6
sudo ./configure --enable-optimizations
sudo make altinstall
sudo rm -rf ../Python*xz
```

### kivy 和buildozer

这里我用力清华镜像。 但是清华镜像好像不稳定。 有时候， 直接下载还快。

```python
python3.7 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --user --upgrade pip wheel setuptools virtualenv
cd ~
python3.7 -m virtualenv kivyven
source kivyven/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple kivy   
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cython
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple buildozer
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  https://github.com/kivymd/KivyMD/archive/master.zip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  encodings
```

关于 buildozer, 还有一些小东西要安装的, 比如说， java, android-tools. 不同平台安装不一样。 我的是manjaro
```bash
cd ~
# install adb
sudo pamac install android-tools, dpkg
# install java
sudo pacman -S jre8-openjdk-headless jre8-openjdk jdk8-openjdk openjdk8-doc openjdk8-src
# Make invironment for some python library
sudo pacman -S cmake
source kivyven/bin/activate
# enter the working directory then
buildozer android debug deploy run
```

然后就可以直接打包测试了。
找个hello world 的帖子， 然后直接打包
网络没啥问题的话， 就直接成功啦！

有些小问题， 记录在 [Karobben Blog](https://karobben.github.io/2021/05/13/Linux/manjaro/#buildozer-test/)了 关于安装 sdk为了打包opencv, 也放哪里了




## 其他

打包 opencv：[我的博客](https://karobben.github.io/2021/05/15/Python/kivy-inaction-tb-8/)

上手项目练习：[简单工具箱](https://karobben.github.io/categories/Python/Kivy/Toolbox/)

关于报错：[如何看kivy的报错](https://karobben.github.io/2021/05/01/Python/kivy_buildozer/)

所有的kivy 帖子： [Kivy 合集](https://karobben.github.io/categories/Python/Kivy/)

## 项目展示

[inclem.net](http://inclem.net/2016/01/15/kivy/kivy_android_app_showcase/) 介绍了3款完成度非常高的精美kivyapp（本人没有上手测试）， 分别为
- Boardz (滑雪游戏)
- Kognitivo (益智游戏)
- Barly (文字游戏)

本人在写一个完程度不高， bug很多的工具箱。 主要基于opencv
[Karobben GitHub](https://github.com/Karobben/Kivymd_toolbox.git)
手把手教程：[点击我](https://karobben.github.io/categories/Python/Kivy/Toolbox)

另外， 写了个垃圾爬虫程序，[百度统计](https://github.com/Karobben/BaiduStatistic_kivy.apk) 但是好像不能用了- -百度json格式改了， 我懒得更新
