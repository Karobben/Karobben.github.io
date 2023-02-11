---
title: "Kivy: debug, understand adblog| adb log"
ytitle: "Kivy: debug, 安卓 adblog| adb log"
description: "A quick way to understand the adblog"
date: 2021/04/30 15:03:00
url: kivy_adblog
toc: true
excerpt: "A quick way to understand the adblog"
tags: [Python, Kivy]
category: [Python, Kivy]
cover: 'https://i.stack.imgur.com/y6Hmq.png'
thumbnail: 'https://kivy.org/logos/kivy-logo-black-64.png'
priority: 10000
covercopy: '<a href="https://stackoverflow.com/questions/29928496/kivy-look-and-feel">© Malik Brahimi</a>'
---


## Adblog cat

A standard adblog catout is `adb logcat`. But I do not suggest you do this since there is too much unrelated information

If you have are familiar with adb, you may add a filter-args like `adb logcat *:W`. But this is not the case for Kivy because most of the information is in `*:I` level.

As a result, pipeline adblog with `grep` is the best choice which could solve most of your problem. Here is my advice:


```python
# it could cover 99% cases
adb logcat| grep -i python

# it could help you access a more elegant result which cover the most of errors.
adb logcat| grep -w "I python"
```

`adb logcat| grep -i python` could access all information containing python.
`grep -w "I python"` should more focus on the running log of python-android.


## Python for Android Ended

This piece of information always one line a heading before the code `Python for android ended`. So, you can find it very easily with:

```python
adb logcat| grep -B 1 -w "Python for android ended"
```

### ModuleNotFoundError

<pre>
  04-27 23:19:06.229 25804 25854 I python  : [INFO   ] [Logger      ] Record log in /data/user/0/org.sirfanas.filechooser.filechooser/files/app/.kivy/logs/kivy_21-04-27_3.txt
  04-27 23:19:06.229 25804 25854 I python  : [INFO   ] [Kivy        ] v1.11.1
  04-27 23:19:06.229 25804 25854 I python  : [INFO   ] [Kivy        ] Installed at "/data/user/0/org.sirfanas.filechooser.filechooser/files/app/_python_bundle/site-packages/kivy/__init__.pyc"
  04-27 23:19:06.229 25804 25854 I python  : [INFO   ] [Python      ] v3.7.5 (default, Apr 21 2021, 11:10:26)
  04-27 23:19:06.229 25804 25854 I python  : [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
  04-27 23:19:06.229 25804 25854 I python  : [INFO   ] [Python      ] Interpreter at "android_python"
  04-27 23:19:06.287  2208  2469 I WindowManager: Removing Window{8e822e1 u0 Splash Screen org.sirfanas.filechooser.filechooser} from AppWindowToken{8ef4121 token=Token{7fb7980 ActivityRecord{8ef4191 u0 org.sirfanas.filechooser.filechooser/org.kivy.android.PythonActivity t13316}}}
  04-27 23:19:06.390  2208  4223 I WindowManager: Animation done in AppWindowToken{8ef4121 token=Token{7fb7980 ActivityRecord{8ef4191 u0 org.sirfanas.filechooser.filechooser/org.kivy.android.PythonActivity t13316}}} isHidden:false hiddenRequested:false
  04-27 23:19:06.587 25804 25854 I python  : [INFO   ] [Factory     ] 184 symbols loaded
  04-27 23:19:06.730 25804 25854 I python  : [INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_pil, img_gif (img_ffpyplayer ignored)
  04-27 23:19:06.745 25804 25854 I python  : [INFO   ] [Text        ] Provider: sdl2
  04-27 23:19:06.761 25804 25854 I python  : [INFO   ] [Window      ] Provider: sdl2
  04-27 23:19:06.776 25804 25854 I python  : [INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] Backend used <sdl2>
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] OpenGL version <b'OpenGL ES 3.2 v1.r18p0-01rel0.c9f554cb2d312e725c77b822a0503b07'>
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] OpenGL vendor <b'ARM'>
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] OpenGL renderer <b'Mali-G76'>
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] OpenGL parsed version: 3, 2
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] Texture max size <8192>
  04-27 23:19:06.777 25804 25854 I python  : [INFO   ] [GL          ] Texture max units <16>
  04-27 23:19:06.780  2208  4460 I DebugKeepScreenOn: Acquiring screen wakelock due to Window{888d929 u0 org.sirfanas.filechooser.filechooser/org.kivy.android.PythonActivity}
  04-27 23:19:06.787 25804 25854 I python  : [INFO   ] [Window      ] auto add sdl2 input provider
  04-27 23:19:06.788 25804 25854 I python  : [INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
  04-27 23:19:06.848 25804 25854 I python  : [INFO   ] [Video       ] Provider: null(['video_ffmpeg', 'video_ffpyplayer'] ignored)
  04-27 23:19:06.849 25804 25854 I python  :  Traceback (most recent call last):
  04-27 23:19:06.849 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/app/main.py", line 64, in <module>
  04-27 23:19:06.849 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/app.py", line 828, in run
  04-27 23:19:06.849 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/app.py", line 599, in load_kv
  04-27 23:19:06.849 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/lang/builder.py", line 301, in load_file
  04-27 23:19:06.849 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/lang/builder.py", line 405, in load_string
  04-27 23:19:06.850 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/lang/builder.py", line 659, in _apply_rule
  04-27 23:19:06.850 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/lang/builder.py", line 659, in _apply_rule
  04-27 23:19:06.850 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/lang/builder.py", line 616, in _apply_rule
  04-27 23:19:06.850 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/factory.py", line 142, in __getattr__
  04-27 23:19:06.850 25804 25854 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/uix/rst.py", line 81, in <module>
  <span style="color:red">04-27 23:19:06.850 25804 25854 I python  :    ModuleNotFoundError: No module named 'docutils'</span>
  04-27 23:19:06.850 25804 25854 I python  : Python for android ended.
  04-27 23:19:06.943  2208  2664 W InputDispatcher: channel '888d929 org.sirfanas.filechooser.filechooser/org.kivy.android.PythonActivity (server)' ~ Consumer closed input channel or an error occurred.  events=0x9
  04-27 23:19:06.943  2208  2664 E InputDispatcher: channel '888d929 org.sirfanas.filechooser.filechooser/org.kivy.android.PythonActivity (server)' ~ Channel is unrecoverably broken and will be disposed!
</pre>

What you want to know is this:  `ModuleNotFoundError: No module named 'docutils'`

As it's who below, we can get the info by:


## AttributeError

<pre>
  04-30 16:22:14.236  6326  6417 I python  : [INFO   ] [Base        ] Start application main loop
  04-30 16:22:14.236  6326  6417 I python  : [INFO   ] [Base        ] Leaving application in progress...
  04-30 16:22:14.237  6326  6417 I python  :  Traceback (most recent call last):
  04-30 16:22:14.237  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/app/main.py", line 111, in <module>
  04-30 16:22:14.237  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/app.py", line 855, in run
  04-30 16:22:14.237  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/base.py", line 504, in runTouchApp
  04-30 16:22:14.237  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/core/window/window_sdl2.py", line 747, in mainloop
  04-30 16:22:14.237  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/core/window/window_sdl2.py", line 479, in _mainloop
  04-30 16:22:14.237  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/base.py", line 339, in idle
  04-30 16:22:14.238  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/clock.py", line 591, in tick
  04-30 16:22:14.238  6326  6417 I python  :    File "kivy/_clock.pyx", line 384, in kivy._clock.CyClockBase._process_events
  04-30 16:22:14.238  6326  6417 I python  :    File "kivy/_clock.pyx", line 414, in kivy._clock.CyClockBase._process_events
  04-30 16:22:14.238  6326  6417 I python  :    File "kivy/_clock.pyx", line 412, in kivy._clock.CyClockBase._process_events
  04-30 16:22:14.238  6326  6417 I python  :    File "kivy/_clock.pyx", line 154, in kivy._clock.ClockEvent.tick
  04-30 16:22:14.238  6326  6417 I python  :    File "kivy/_clock.pyx", line 88, in kivy._clock.ClockEvent.get_callback
  04-30 16:22:14.239  6326  6417 I python  :    File "/media/ken/Data/Kivy/.buildozer/android/platform/build-armeabi-v7a/build/python-installs/filechooser/kivy/weakmethod.py", line 47, in __call__
  04-30 16:22:14.239  6326  6417 I python  :  <span style="color:red">AttributeError: 'WebviewLauncher' object has no attribute 'f2'</span>
  04-30 16:22:14.239  6326  6417 I python  : Python for android ended.
</pre>

Check the class WebviewLauncher and figure out what is `f2` in it.



## Buildozer Error
<pre>
  Non-user install due to --prefix or --target option
  Created temporary directory: /tmp/pip-target-nnpo4wye
  Created temporary directory: /tmp/pip-ephem-wheel-cache-hjzhdyqg
  Created temporary directory: /tmp/pip-req-tracker-nryx6lee
  Initialized build tracking at /tmp/pip-req-tracker-nryx6lee
  Created build tracker: /tmp/pip-req-tracker-nryx6lee
  Entered build tracker: /tmp/pip-req-tracker-nryx6lee
  Created temporary directory: /tmp/pip-install-xivbs0bw
  Collecting https://github.com/kivymd/kivymd/archive/master.zip (from -r requirements.txt (line 1))
    Created temporary directory: /tmp/pip-req-build-6lx7kxss
    Created temporary directory: /tmp/pip-unpack-cr7m7azt
    Looking up "https://github.com/kivymd/kivymd/archive/master.zip" in the cache
    No cache entry available
    Starting new HTTPS connection (1): github.com:443
    Incremented Retry for (url='/kivymd/kivymd/archive/master.zip'): Retry(total=4, connect=None, read=None, redirect=None, status=None)
    WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='github.com', port=443): Read timed out. (read timeout=15)")': /kivymd/kivymd/archive/master.zip
    Starting new HTTPS connection (2): github.com:443
    Incremented Retry for (url='/kivymd/kivymd/archive/master.zip'): Retry(total=3, connect=None, read=None, redirect=None, status=None)
    WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f0c4b98ccd0>, 'Connection to github.com timed out. (connect timeout=15)')': /kivymd/kivymd/archive/master.zip
    Starting new HTTPS connection (3): github.com:443
    Incremented Retry for (url='/kivymd/kivymd/archive/master.zip'): Retry(total=2, connect=None, read=None, redirect=None, status=None)
    WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f0c4b98ce50>, 'Connection to github.com timed out. (connect timeout=15)')': /kivymd/kivymd/archive/master.zip
    Starting new HTTPS connection (4): github.com:443
    Incremented Retry for (url='/kivymd/kivymd/archive/master.zip'): Retry(total=1, connect=None, read=None, redirect=None, status=None)
    WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))': /kivymd/kivymd/archive/master.zip
    Starting new HTTPS connection (5): github.com:443
    Incremented Retry for (url='/kivymd/kivymd/archive/master.zip'): Retry(total=0, connect=None, read=None, redirect=None, status=None)
    WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f0c4b722190>, 'Connection to github.com timed out. (connect timeout=15)')': /kivymd/kivymd/archive/master.zip
    Starting new HTTPS connection (6): github.com:443
  ERROR: Could not install packages due to an OSError.
  Traceback (most recent call last):
    File "/media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/build/venv/lib/python3.8/site-packages/pip/_vendor/urllib3/connection.py", line 169, in _new_conn
      conn = connection.create_connection(
    File "/media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/build/venv/lib/python3.8/site-packages/pip/_vendor/urllib3/util/connection.py", line 96, in create_connection
      raise err
    File "/media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/platform/build-armeabi-v7a/build/venv/lib/python3.8/site-packages/pip/_vendor/urllib3/util/connection.py", line 86, in create_connection
      sock.connect(sa)
  socket.timeout: timed out

  During handling of the above exception, another exception occurred:
</pre>

Key error: `Starting new HTTPS connection (5): github.com:443`
Reason: Github didn't response.
Resolution: Try `builder` again or connect your terminal to VPN.



## Errors

`requests`
Found by `adb logcat| grep -i python`
Resolution:
```kv buildozer.spec
requirements =  openssl, requests, Urllib3, chardet, certifi, idna
```
<pre>
  05-09 19:24:20.139 23571 23629 I python  :    File "kivy/_event.pyx", line 709, in kivy._event.EventDispatcher.dispatch
  05-09 19:24:20.140 23571 23629 I python  :    File "/media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/app/libWidget/Seq.py", line 25, in align
  05-09 19:24:20.141 23571 23629 I python  :    File "/media/ken/Data/Kivy_env/Kivy2Py3.8.1MD0.104.2.dev0/.buildozer/android/app/bin/clustalo.py", line 35, in <module>
  05-09 19:24:20.141 23571 23629 I python  :  ModuleNotFoundError: No module named 'requests'
  05-09 19:24:20.141 23571 23629 I python  : Python for android ended.
</pre>


```py
def fasta_read(FA):
fasta = {}
with open("clusttmp/result.aln-fasta.fasta") as file_one:
    for line in file_one:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            print(line)
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                fasta[active_sequence_name] = []
            continue
        sequence = line
        fasta[active_sequence_name].append(sequence)

print(fasta)
      return fasta

from collections import defaultdict #this will make your life simpler
f = open("clusttmp/result.aln-fasta.fasta",'r')
list=defaultdict(str)
name = ''
for line in f:
    #if your line starts with a > then it is the name of the following sequence
    if line.startswith('>'):
        name = line[1:-1]
        continue #this means skips to the next line
    #This code is only executed if it is a sequence of bases and not a name.
    list[name]+=line.strip()


d = {}

with open("clusttmp/result.aln-fasta.fasta") as f:
    for line in f:
        if len(line) > 1:
            if '%Labelinf' in line:
                key = line.strip()
                d[key] = ""
            else:
                d[key] += line.strip() + "+"

d = {key: d[key][:-1] for key in d}
print d
```
