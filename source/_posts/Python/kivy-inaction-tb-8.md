---
toc: true
url: kivy_inaction_tb_8
priority: 10000
date: 2021-05-15 23:26:53
title: "Kivy for android in action: pack OpenCV with buildozer"
ytitle: "Kivy安卓实战:8 |安卓打包OpenCV| 寫個工具箱把8"
excerpt: "Write a kivy toolbox for yourselves."
description: "Write a kivy toolbox for yourselves."
tags: [Python, Kivy]
category: [Python, Kivy, Toolbox]
cover: 'https://kivy.org/static/images/kivy-colorwheel-examples.jpg'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
covercopy: '<a href="https://kivy.org/">© kivy</a>'
---

```
CryptoWatch-Kivy          1.13
Kivy                      2.0.0
Kivy-Garden               0.1.4
kivy-garden.wordcloud     1.0.0
kivymd                    0.104.2.dev0
```

## Build OpenCV for kivy

The resolution is from [franslott](https://github.com/kivy/buildozer/issues/1144) in github issue.

It seems the new version of buildozer updated the SDK tools and no longer supports packing the OpenCV with the default setting. So, we should settle the SDK by ourselves.


==What can we do with OpenCV in Android==:
- loading/writing images
- writing videos (some formats like avi)
- facial detection with the camera opened by kivy

What we can't do:
- loading videos
- open cameras
- update images under threading (display)

Abilities of OpenCV were limited in android. Hope someone could solve the problems above soon.


```bash
#mv tools old-tools
# mv lib/external/com/android/tools lib/external/com/android/old-tools

# 1. Download [cmdlines-tools from google](https://developer.android.com/studio#cmdline-tools)

# 2. prepare the sdk by yourself
# export the path you'd like to place it
export PREFIX=/run/media/karobben/Data/Kivy2.0MD0.104.2.dP3.7.5
mkdir $PREFIX/.buildozer/android/platform/android-sdk
cd $PREFIX/.buildozer/android/platform/android-sdk/

cp ~/Downloads/commandlinetools-linux-7302050_latest.zip  .
unzip commandlinetools-linux-7302050_latest.zip

# mv tools old-tools

cd cmdline-tools/bin

sudo ./sdkmanager --sdk_root=$PREFIX/.buildozer/android/platform/android-sdk/ --install "tools"
sudo ./sdkmanager --sdk_root=$PREFIX/.buildozer/android/platform/android-sdk/ --install "build-tools;29.0.0-rc3"
sudo ./sdkmanager --sdk_root=$PREFIX/.buildozer/android/platform/android-sdk/ --install "platforms;android-27"
sudo ./sdkmanager --sdk_root=$PREFIX/.buildozer/android/platform/android-sdk/ --install "platform-tools"
sudo ./sdkmanager --sdk_root=$PREFIX/.buildozer/android/platform/android-sdk/ --install "patcher;v4"
sudo ./sdkmanager --sdk_root=$PREFIX/.buildozer/android/platform/android-sdk/ --install "emulator"

sudo ./sdkmanager --sdk_root=$PREFIX/android-sdk/ --install "tools"
sudo ./sdkmanager --sdk_root=$PREFIX/android-sdk/ --install "build-tools;29.0.0-rc3"
sudo ./sdkmanager --sdk_root=$PREFIX/android-sdk/ --install "platforms;android-27"
sudo ./sdkmanager --sdk_root=$PREFIX/android-sdk/ --install "platform-tools"
sudo ./sdkmanager --sdk_root=$PREFIX/android-sdk/ --install "patcher;v4"
sudo ./sdkmanager --sdk_root=$PREFIX/android-sdk/ --install "emulator"

```

adding the path into `buildozer.spc`:
```kv buildozer.spc
android.sdk_path = /run/media/ken/Data/Kivy2.0MD0.104.2.dP3.7.5/android-sdk/
```


```bash
# delete ANT, NDK again
buildozer android clean
buildozer distclean
buildozer -v android debug
# or  buildozer android debug deploy run
```
