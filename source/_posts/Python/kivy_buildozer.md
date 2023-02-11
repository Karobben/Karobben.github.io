---
title: "Kivy: debug, understand adblog| adb log"
ytitle: "Kivy: Structure of Buildozer"
description: "A quick way to understand the adblog"
date: 2021/05/01 15:03:00
url: kivy_buildozer
toc: true
excerpt: "A quick way to understand the adblog"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://i.stack.imgur.com/y6Hmq.png'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '<a href="https://stackoverflow.com/questions/29928496/kivy-look-and-feel">© Malik Brahimi</a>'
---

## tar files for packaging

This is where `tar.gz` filers stored. By storing files where, we needn't downloads them again next time.

`.buildozer/android/platform/build-armeabi-v7a/packages/`

<pre style="color:green">
├── cython
│   └── 0.29.15.tar.gz
├── decorator
│   └── 4.2.1.tar.gz
├── ffmpeg
│   └── 007e03348dbd8d3de3eb09022d72c734a8608144.zip
├── freetype
│   └── freetype-2.10.1.tar.gz
├── hostpython3
│   ├── Python-3.7.5.tgz
│   └── Python-3.8.1.tgz
├── jpeg
│   └── 2.0.1.tar.gz
├── kivy
│   ├── 1.11.1.zip
│   └── 2.0.0.zip
├── libbz2
│   └── bzip2-1.0.8.tar.gz
</pre>

## File for packaging

This is the place of environment for packaged apk.
The name of it is from `buildozer.spec`: `package.name = KarobbenTB`

`.buildozer/android/platform/build-armeabi-v7a/build/python-installs/`

<pre>
.buildozer/android/platform/build-armeabi-v7a/build/python-installs/
├── BaiduStat
├── CSVD
├── filechooser
├── Icons
├── KarobbenTB
├── Kivyv2a
└── opencvdemo
</pre>

==PS==:

## packaged apk

### Place 1
`/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/dists/{package.name}__armeabi-v7a/build/outputs/apk/debug/{package.name}__armeabi-v7a-debug.apk`

Exp:

`/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/dists/filechooser__armeabi-v7a/build/outputs/apk/debug/filechooser__armeabi-v7a-debug.apk`

### Place 2
`/media/ken/Data/Kivy/.buildozer/android/platform/python-for-android/`


## Download packages by yourself

according to the error code:
<pre>
INFO]:    Downloading cython
[INFO]:    -> running mkdir -p /media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/packages/cython
[INFO]:    -> directory context /media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/packages/cython
[INFO]:    -> running basename https://github.com/cython/cython/archive/0.29.15.tar.gz
[INFO]:    -> running rm -f .mark-0.29.15.tar.gz
[INFO]:    Downloading cython from https://github.com/cython/cython/archive/0.29.15.tar.gz
</pre>

```bash
wget -c https://github.com/cython/cython/archive/0.29.15.tar.gz
cp 0.29.15.tar.gz .buildozer/android/platform/build-armeabi-v7a/packages/cython/.mark-0.29.15.tar.gz
```
