---
toc: true
url: manjaro
covercopy: <a herf="https://forum.manjaro.org/t/manjaro-20-1-mikah-got-released/24173">© philm</a>
priority: 10000
date: 2021-05-13 14:31:08
title: "To start with manjaro"
ytitle: "Manjaro 环境配置"
description: "Started with Manjaro"
excerpt: "Started with Manjaro"
tags:  [Linux]
category: [Linux]
cover: "https://forum.manjaro.org/uploads/default/optimized/2X/6/63c8d1ff720cfb682ed046dd8e67c37d7083ed1b_2_690x388.jpeg"
thumbnail: "https://forum.manjaro.org/uploads/default/optimized/2X/6/63c8d1ff720cfb682ed046dd8e67c37d7083ed1b_2_690x388.jpeg"
---

## Manjaro

- May 13
  - [x] [R](#R)
  - [x] [hexo](#hexo)
  - [x] [Chinese input](##Chinese-input)
  - [x] [QQ & wechat](#Wechat)
  - [x] [kivy](#Kivy)
  - [x] [buildozer](#Kivy)
- May 15
  - [x] [Graphic Manager](#Graphic-Manager)
  - [X] [OBS bug](#Graphic-Manager)
- May 17
  - [x] [SSR](#SSR)
- [x] Biology Environment(#Biology-environment)
- Others
  - [x] [zoom](#Zoom)
  - [x] [Slack](#Slack)
  - [ ] [Atom]


## update

```bash
pacman -Syyu
```

## Graphic Manager
I strongly recommend Settle GPU driver first if you are using dual GPU and one of them is Nvidia. Because one of my systems can't be open again after following a set of processes for installing an Nvidia driver. As it said by Linus Torvalds: F**K YOU, NVIDIA! After you switched to the Nvidia driver, your ==OBS could work== ~~fluently~~.

This [post](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-manjaro-linux) from linuxconfig could help you install driver appropriately.

The trick is you need to switch into ==an old kernel== (exp: 5.4.116). I even failed to install it on kernel `5.4.106_rt54-1`.

```bash
sudo mhwd -a pci nonfree 0300
sudo reboot
```

<pre style="color:dodgerblue">
██████████████████  ████████     ken@manjaro
██████████████████  ████████     OS: Manjaro 21.0.4 Ornara
██████████████████  ████████     Kernel: x86_64 Linux 5.4.116-1-MANJARO
██████████████████  ████████     Uptime: 2h 55m
████████            ████████     Packages: 1390
████████  ████████  ████████     Shell: zsh 5.8
████████  ████████  ████████     Resolution: 1920x1080
████████  ████████  ████████     DE: GNOME 3.38.5
████████  ████████  ████████     WM: Mutter
████████  ████████  ████████     WM Theme: Matcha-dark-sea
████████  ████████  ████████     GTK Theme: Matcha-sea [GTK2/3]
████████  ████████  ████████     Icon Theme: Papirus-Dark-Maia
████████  ████████  ████████     Font: Noto Sans 11
████████  ████████  ████████     Disk: 868G / 1.8T (48%)
                                 CPU: Intel Xeon E3-1535M v6 @ 8x 4.2GHz [82.0°C]
                                 GPU: <span style="color:red">Quadro M2200</span>
                                 RAM: 5644MiB / 64042MiB
</pre>

## Terminal failed to open after update

Try this: [Yochanan](https://forum.manjaro.org/t/root-tip-troubleshooting-locale-errors/21008)

```bash
sudo sed -i '/en_US.UTF-8/s/^#//g' /etc/locale.gen
sudo sed -i '/fr_FR.UTF-8/s/^#//g' /etc/locale.gen
sudo locale-gen
```

## R

```bash
sudo pacman -S yaourt
sudo pacman -S r
# an R execute terminal environment
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple radian
```

some common libraries of R:[Karobben](Karobben.github.io/2020/02/14/R/library/)


<p id="manjaro_hexo"></p>

## hexo

```bash
# Switch the mirror into TaoBao
npm --registry https://registry.npm.taobao.org install express
sudo npm install hexo-cli -g
```

<p id="manjaro_cn"></p>


## Chinese input
[Neutionwei 2020](https://blog.csdn.net/Neutionwei/article/details/108500946)

```bash
# installs
sudo pacman -S fcitx
sudo pacman -S fcitx-im
sudo pacman -S fcitx-configtool
sudo pacman -S fcitx-googlepinyin
sudo pacman -S fcitx-sunpinyin
# config
sudo vim  ~/.xprofile
```

<pre>
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
</pre>


==reboot needed==
```bash
reboot
```
undo-check `Only Show Current Language` selection and you can find the Google Pinyin you just installed

### fcix5

I failed to setup Chinese input, so I try 5

[DotIN13 2020](https://www.wannaexpresso.com/2020/03/26/fcitx5/)
```bash
pacman -Rs $(pacman -Qsq fcitx) #卸载fcitx4
pacman -S fcitx5-chinese-addons fcitx5 fcitx5-gtk fcitx5-qt #安装community源的fcitx5
#你也可以选择用下面的命令安装archlinuxcn源的fcitx5
sudo pacman -S fcitx5-chinese-addons-git fcitx5-git fcitx5-gtk-git fcitx5-qt5-git

# config
mkdir ~/.config/fcitx5/
vim ~/.config/fcitx5/profile
```


```bash
# Activate
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"

# reboot your computer to activate it.
reboot
```
run
```bash

fcitx5 &
```

==Error==
<pre>
You're currently running Fcitx with GUI, but fcitx5-config-qt couldn't be found. Now it will open config directory.
</pre>
reference: [](https://www.cnblogs.com/yellowgg/p/11113442.html)

```bash
sudo pacman -S fcitx5-config-qt
```

### themes
downloads the themes from github [hosxy](https://github.com/hosxy/Fcitx5-Material-Color)

```bash
pacman -S fcitx5-material-color
```

## Japanese Impute  

```bash
sudo pacman -S  fcitx5-mozc
```



## Wechat

[JontyShaw 2020](https://blog.csdn.net/qq_37284020/article/details/107116065)
```bash
sudo pacman -S yay
sudo pacman -S base-devel

yay -S deepin-wine-wechat

#yay -S deepin-wine-qq # I failed to install QQ
```

### QQ

[link 1](https://blog.csdn.net/qq_37284020/article/details/107116065)
[link 2](https://blog.csdn.net/qq_41050631/article/details/102538649)
```bash
sudo pacman -S yay

yay -S adobe-source-han-sans-cn-fonts
yay -S xdotool
yay -S com.qq.im.deepin
```

### other packages

## nmp
```bash
npm i -g waque
```

## apps from Add/Remove Software

atom: `sudo pacman -Sy atom`
obs: `sudo pacman -Sy obs`
wps: `yay -S wps-office`

## Scrcyp

prerequisite:
```bash
sudo pacman -S meson ninja
```
Who to install [Scrcyp](karobben.github.io/2020/06/26/Linux/Deepin_scrcpy/)

## Kivy

[john100 2021](https://archived.forum.manjaro.org/t/solved-how-to-install-kivy-on-manjaro/113849)

```bash
cd /usr/local
sudo wget http://python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz
sudo tar xf Python-3.7.6.tar.xz
cd Python-3.7.6
sudo ./configure --enable-optimizations
sudo make altinstall
sudo rm -rf ../Python*xz
```

```
python3.7 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --user --upgrade pip wheel setuptools virtualenv
cd ~
python3.7 -m virtualenv kivyven
source kivyven/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple kivy   
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cython
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple buildozer
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  https://github.com/kivymd/KivyMD/archive/master.zip
```

### buildozer test

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

<pre>
RAN: /run/media/karobben/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3 setup.py build_ext -v

STDOUT:
Could not find platform independent libraries <prefix>
Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
Python path configuration:
.
.
.
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'
</pre>


```bash
rm -r /run/media/karobben/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/hostpython3
```


<pre>
STDOUT:
Traceback (most recent call last):
File "setup.py", line 20, in <module>
  from setuptools import Extension, setup
ModuleNotFoundError: No module named 'setuptools'
</pre>


```
rm -r /run/media/karobben/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer
```

<pre>
CMake Error at cmake/android/OpenCVDetectAndroidSDK.cmake:176 (message):
  Android SDK Tools: OpenCV requires Android SDK Tools revision 14 or newer.

  Use BUILD_ANDROID_PROJECTS=OFF to prepare Android project files without
  building them
Call Stack (most recent call first):
  CMakeLists.txt:780 (include)
</pre>

[git issue](https://github.com/opencv/opencv/commit/6abfc6761e5a58c12ef69d7f6efca3c8a96b9184)
[issue](https://github.com/kivy/python-for-android/pull/2419)


### Debug info for oepncv

The problem of building fail for opencv is the SDK tool was changes. But we could settle our own sdk too by setting `android.sdk_path=` in buildozer file.

<pre>
  [DEBUG]:   -> running gradlew assembleDebug
  [DEBUG]:   	
  [DEBUG]:   	> Task :compileDebugJavaWithJavac
  [DEBUG]:   	Note: Some input files use or override a deprecated API.
  [DEBUG]:   	Note: Recompile with -Xlint:deprecation for details.
  [DEBUG]:   	Note: Some input files use unchecked or unsafe operations.
  [DEBUG]:   	Note: Recompile with -Xlint:unchecked for details.
  [DEBUG]:   	
  [DEBUG]:   	> Task :transformNativeLibsWithStripDebugSymbolForDebug
  [DEBUG]:   	/home/karobben/.buildozer/android/platform/android-ndk-r19c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-strip:/run/media/karobben/Data/Kivy2.0MD0.104.2.dP3.7.5/.buildozer/android/platform/build-armeabi-v7a/dists/opencvtest__armeabi-v7a/build/intermediates/transforms/mergeJniLibs/debug/0/lib/armeabi-v7a/gdb.setup: File format not recognized
  [DEBUG]:   	
  [DEBUG]:   	Unable to strip library '1' due to error /home/karobben/.buildozer/android/platform/android-ndk-r19c/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-strip returned from '/run/media/karobben/Data/Kivy2.0MD0.104.2.dP3.7.5/.buildozer/android/platform/build-armeabi-v7a/dists/opencvtest__armeabi-v7a/build/intermediates/transforms/mergeJniLibs/debug/0/lib/armeabi-v7a/gdb.setup', packaging it as is.
  [DEBUG]:   	
  [DEBUG]:   	Deprecated Gradle features were used in this build, making it incompatible with Gradle 7.0.
  [DEBUG]:   	Use '--warning-mode all' to show the individual deprecation warnings.
  [DEBUG]:   	See https://docs.gradle.org/6.4.1/userguide/command_line_interface.html#sec:command_line_warnings
  [DEBUG]:   	
  [DEBUG]:   	BUILD SUCCESSFUL in 5s
  [DEBUG]:   	27 actionable tasks: 27 executed

  [INFO]:    <- directory context /run/media/karobben/Data/Kivy2.0MD0.104.2.dP3.7.5/.buildozer/android/platform/python-for-android  	
  [INFO]:    Of the existing distributions, the following meet the given requirements:
  [INFO]:    	opencvtest: min API 21, includes recipes (freetype, hostpython3, jpeg, libffi, librt, libshine, libx264, libxml2, openssl, png, sdl2_image, sdl2_mixer, sdl2_ttf, sqlite3, ffpyplayer_codecs, libxslt, python3, sdl2, cymunk, ffmpeg, setuptools, cppy, cython, decorator, ffpyplayer, lxml, pillow, six, zope_interface, kiwisolver, numpy, pyjnius, twisted, android, audiostream, kivy, matplotlib, , pygments, imageio, docutils, opencc-python-reimplemented, urllib3, plyer, constantly, plumbing, cycler, python-dateutil, idna, imageio_ffmpeg, pypinyin, biopython, pyparsing, https://github.com/kivymd/kivymd/archive/master.zip, certifi, chardet, tqdm, requests, moviepy, autopaths, incremental), built for archs (armeabi-v7a)
  [INFO]:    opencvtest has compatible recipes, using this one
  [INFO]:    # Copying android package to current directory
  [INFO]:    # Android package filename not found in build output. Guessing...
  [INFO]:    # Found android package file: /run/media/karobben/Data/Kivy2.0MD0.104.2.dP3.7.5/.buildozer/android/platform/build-armeabi-v7a/dists/opencvtest__armeabi-v7a/build/outputs/apk/debug/opencvtest__armeabi-v7a-debug.apk
  [INFO]:    # Add version number to android package
  [INFO]:    # Android package renamed to opencvtest__armeabi-v7a-debug-0.1-.apk
  [DEBUG]:   -> running cp /run/media/karobben/Data/Kivy2.0MD0.104.2.dP3.7.5/.buildozer/android/platform/build-armeabi-v7a/dists/opencvtest__armeabi-v7a/build/outputs/apk/debug/opencvtest__armeabi-v7a-debug.apk opencvtest__armeabi-v7a-debug-0.1-.apk
  WARNING: Received a --sdk argument, but this argument is deprecated and does nothing.
  No setup.py/pyproject.toml used, copying full private data into .apk.
  Applying Java source code patches...
  Applying patch: src/patches/SDLActivity.java.patch
</pre>



[franslott](https://github.com/kivy/buildozer/issues/1144)

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


## SSR

[Awk.BLOG 2021](https://www.buptstu.cn/2021/02/07/Manjaro%E9%85%8D%E7%BD%AEQv2ray-SSR/)

1. Download [Qv2ray](https://github.com/Qv2ray/Qv2ray) and (AppImage) [SSR plugin](https://github.com/Qv2ray/QvPlugin-SSR/releases)
2. `chmod +x *.AppInage`
3. mv SSR plugin to `/home/$USER/.config/qv2ray/plugins/`
4. Click `AppImage`, Click group, add your links.


## Biology environment

## bioconda
```bash
## miniconda


# download miniconda
wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
# export your Miniconda/bin to path

# Douban mirror
conda config --add channels https://pypi.douban.com/anaconda/cloud/conda-forge/
conda config --add channels https://pypi.douban.com/anaconda/cloud/msys2/
conda config --add channels https://pypi.douban.com/anaconda/cloud/bioconda/
conda config --add channels https://pypi.douban.com/anaconda/cloud/menpo/
conda config --add channels https://pypi.douban.com/anaconda/cloud/pytorch/
```

### qinhua mirro

```bash
#Anaconda Python 免费仓库
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
# for legacy win-64
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/peterjc123/
conda config --set show_channel_urls yes
```

### beida mirror

```bash
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.bfsu.edu.cn/miniconda/cloud/bioconda/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/peterjc123/
conda config --set show_channel_urls yes
```


### Zoom

Source: [Zoom for linux](https://support.zoom.us/hc/en-us/articles/204206269-Installing-or-updating-Zoom-on-Linux)

```bash
sudo pacman -U zoom_x86_64.pkg.tar.xz
```

### Slack

Slack is a chatting channel which for sharing your ideas proficiently.sla

```bash
sudo pacman -S slack-desktop
```
