---
title: "kivy-Buildozer: packed to android apk"
ytitle: "Kivy 打包成安卓apk"
description: "kivy-Buildozer, pack your python codes to android apk"
url: buildozer2
date: 2021/01/01
toc: true
excerpt: "Buildozer install and android APK packaging"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.dpHEt6VNif2n2c4ULEqQ7gHaDJ'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '© dotmodus'
---



## Prerequisite: Java Home
Download **openJDK 8** from [here](https://adoptopenjdk.net).
```bash
sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev

sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

sudo apt install cython
```
## 1 install Buildozer

```bash
## install python
sudo apt install python3.7
## install pip
sudo apt install python3-pip
##
sudo python3.7 -m pip install --user --upgrade Cython==0.29.19 virtualenv

sudo python3.7 -m pip  install -i https://pypi.tuna.tsinghua.edu.cn/simple buildozer


sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

or you can go and Check: [kivy-buildozer-installer.sh](https://github.com/zaemiel/kivy-buildozer-installer/blob/master/kivy-buildozer-installer.sh)
## add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/
```
If you come with error `buildozer debug error "[WARNING]" when i run buildozer andriod debug`, please install lib below
```
sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev
```
链接安卓手机, 开启USB debug模式;<br />进入 kivy 项目目录<br />测试项目:[https://github.com/sevvalbrt/Todolist](https://github.com/sevvalbrt/Todolist)
```bash
buildozer init
buildozer android debug deploy run
```
手机有什么提示, 记得选择

可能会下一些东西. 等一下就好了<br/>

![NYV7mF.png](https://s1.ax1x.com/2020/06/22/NYV7mF.png)

<br />更多参考:<br />[https://cycleuser.gitbooks.io/kivy-guide-chinese/content/15-Kivy-Pack-Android.html](https://cycleuser.gitbooks.io/kivy-guide-chinese/content/15-Kivy-Pack-Android.html)

## Quick Test

### Download a Kivy example
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
## Buildozer failed to execute the last command
## The error might be hidden in the log above this error
## Please read the full log, and search for it before
## raising an issue with buildozer itself.
## In case of a bug report, please add a full log with log_level = 2
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

## Success
When the code shows as below, it means everything is down and you can upload apk file from bin to your Android phone:
<pre>
WARNING: Received a --sdk argument, but this argument is deprecated and does nothing.
No setup.py/pyproject.toml used, copying full private data into .apk.
Applying Java source code patches...
Applying patch: src/patches/SDLActivity.java.patch
Warning: failed to apply patch (exit code 1), assuming it is already applied:  src/patches/SDLActivity.java.patch
## Android packaging done!
## APK myapp-0.1-armeabi-v7a-debug.apk available in the bin directory
</pre>

ummmm... I fail to open this app in Huawei p30 pro. But I tried another more simple app and it succeed.



---
```bash
sudo apt install install python3-dev
```

## Erros

<pre>
RAN: /bin/tar xf /media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/packages/cython/0.29.15.tar.gz

STDOUT:


STDERR:
/bin/tar: This does not look like a tar archive

gzip: stdin: unexpected end of file
/bin/tar: Child returned status 1
/bin/tar: Error is not recoverable: exiting now
</pre>

cypython file is damaged. Delete `.buildozer/android/platform/build-armeabi-v7a/packages/cython` to download it again



```python
def Seq_clean():
F = open("clusttmp/result.aln-clustal_num.clustal_num").read()
F  = F.replace("\n\n\n","\n\n")
F  = F.split("\n\n")[1:]
Result = ""
Num = 0

for head in F[0].split("\n"):
  for Seq in F:
    tmp = Seq.split("\n")[Num].split("\t")[0]
    if head !=Seq.split("\n")[Num]:
      tmp = tmp.split(" ")[-1]
    Result +=  tmp
  Result += "\n"
  Num +=1

print(Result)

Mark_list = []
for i in Result.split('\n'):
  Mark_list += [i.split(" ")[-1]]

while "" in Mark_list:
  Mark_list.remove("")

Marked_list = []
for seq in Mark_list:
  Marked_list += [MarkDown(seq)]

for i, ii in zip(Mark_list, Marked_list):
  Result= Result.replace(i, ii)
return Result

def MarkDown(Text):
  Result = ""
  for i in list(Text):
      if i == "a" or i == "A":
          i = "[color=#fa937f]A[/color]"
      if i == "t" or i == "T":
          i = "[color=#1193ee]T[/color]"
      if i == "c" or i == "C":
          i = "[color=#51d673]C[/color]"
      if i == "g" or i == "G":
          i = "[color=#edcf1d]G[/color]"
      if i == "-" or i == " ":
          i = "[color=#ffffff]G[/color]"
      Result += i
  return Result
```
