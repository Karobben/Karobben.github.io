---
title: "kivy-Buildozer"
description: "kivy-Buildozer"
url: buildozer2
---

# kivy-Buildozer


<a name="Z0CZY"></a>
# 1 install Buildozer

```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple buildozer


sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/
```

链接安卓手机, 开启USB debug模式;<br />进入 kivy 项目目录<br />测试项目:[https://github.com/sevvalbrt/Todolist](https://github.com/sevvalbrt/Todolist)
```bash
buildozer init
buildozer android deploy run
```
手机有什么提示, 记得选择

可能会下一些东西. 等一下就好了<br/>

![NYV7mF.png](https://s1.ax1x.com/2020/06/22/NYV7mF.png)

<br />更多参考:<br />[https://cycleuser.gitbooks.io/kivy-guide-chinese/content/15-Kivy-Pack-Android.html](https://cycleuser.gitbooks.io/kivy-guide-chinese/content/15-Kivy-Pack-Android.html)

# Quick Test

## Download a Kivy example
```bash
git clone https://github.com/sevvalbrt/Todolist.git

cd ToDolist
buildozer init
buildozer android debug deploy run
```
![NYV7mF.png](https://s1.ax1x.com/2020/06/22/NYV7mF.png)
As this photo above, it'll take a while...

The problem is you'll download a bunch of libs and you'll fail if one of the packages download fail.
['hostpython3', 'libffi', 'openssl', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'sqlite3', 'python3', 'sdl2', 'setuptools', 'six', 'pyjnius', 'android', 'kivy']
- android-ndk-r19c-linux-x86_64.zip

<pre>
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2
</pre>
I got an error and it says I need to read the error code in full log file...

<pre>
Exception in thread "main" java.lang.NoClassDefFoundError: javax/xml/bind/annotation/XmlSchema
</pre>

reference: [lplj717 2019](https://blog.csdn.net/lplj717/article/details/103126209)
It seems like I got a wrong version of jave.
So, I removed the new version and keep the jdk8.

And then, a new error arise:
<pre>
WARNING: Received a --sdk argument, but this argument is deprecated and does nothing.
BUILD FAILURE: No main.py(o) found in your app directory. This
file must exist to act as the entry point for you app. If your app is
started by a file with a different name, rename it to main.py or add a
main.py that loads it.
</pre>

So... mv `Main.py` to `main.py`

and then:
<pre>
Could not find tools.jar. Please check that /home/ken/Soft/jre1.8.0_231 contains a valid JDK installation
</pre>
reference: [CUFFS 2017](https://www.jianshu.com/p/1ed02fb2726d)
So, there are some thing wrong with my JAVA environment, I download it from https://adoptopenjdk.net and export them in `~/.bashrc`

# Success
When the code shows as below, it means everything is down and you can upload apk file from bin to your Android phone:
<pre>
WARNING: Received a --sdk argument, but this argument is deprecated and does nothing.
No setup.py/pyproject.toml used, copying full private data into .apk.
Applying Java source code patches...
Applying patch: src/patches/SDLActivity.java.patch
Warning: failed to apply patch (exit code 1), assuming it is already applied:  src/patches/SDLActivity.java.patch
# Android packaging done!
# APK myapp-0.1-armeabi-v7a-debug.apk available in the bin directory
</pre>

ummmm... I fail to open this app in Huawei p30 pro. But I tried another more simple app and it succeed.
