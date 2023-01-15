---
toc: true
url: khal
covercopy: © Karobben
priority: 10000
date: 2022-05-02 20:54:34
title: "khal, a fancy calendar app in your terminal"
ytitle: "khal, terminal 里面的一款帅气的日历程序"
description: "If you need a fancy but elegant calendar live in your terminal, khal would be an awesome choice."
excerpt: "If you need a fancy but elegant calendar live in your terminal, khal would be an awesome choice."
tags: [Software, Linux, Tools]
category: [others, Blog, Sharing]
cover: "https://camo.githubusercontent.com/71bb6f25021a0b056fbeb9587194858c4b62f5265cceec003b09094e6573c795/687474703a2f2f6c6f73747061636b6574732e64652f696d616765732f6b68616c2e706e67"
thumbnail: "https://camo.githubusercontent.com/71bb6f25021a0b056fbeb9587194858c4b62f5265cceec003b09094e6573c795/687474703a2f2f6c6f73747061636b6574732e64652f696d616765732f6b68616c2e706e67"
---

## khal calendar

The store begins I find I had a very terrible memory and forget the schedules again and again. I really need a calendar to stick on the wall and remind me again and again. I considered some online services like outlook calendar or google calendar but they are not fancy. I think it could be cool that I can show it in the terminal, for one thing, is that I can make the background dark to save the bower. On the other hand, I can use the old tablet or android phone to display the calendar for a whole day in the "termux". It could also be my small server for running some programs.

According to some posts, it can also sync your online calendars like google calendar or outlook calendar. I tried to use `vdirsyncer` to synchronize the Google calendar but failed. I applied the Client ID but it tell me that I had `uri_redirect_mistake`. Annoying.

But anyway, I still like to use it in local, synchronize them through the local network with some stupid bash scrip. So, I'll introduce the basic use of the `khal` to build your local calendar. Cheers!

## vdirsyncer

```bash
sudo apt install vdirsyncer
mkdir /home/ken/.config/vdirsyncer
touch /home/ken/.config/vdirsyncer/config
vdirsyncer discover personal_sync
```


## khal

```bash
sudo apt install khal
# Creat a configure file
khal configure
```

How the initiated configure file looks like:

<pre>
[calendars]

[[private]]
path = /home/ken/.local/share/khal/calendars/private
type = calendar

[locale]
timeformat = %H:%M
dateformat = %Y-%m-%d
longdateformat = %Y-%m-%d
datetimeformat = %Y-%m-%d %H:%M
longdatetimeformat = %Y-%m-%d %H:%M
</pre>

Detailed configuration paremeters could be find at: [Documentation](https://khal.readthedocs.io/en/latest/configure.html)

More information:
- [Documentation](https://lostpackets.de/khal/configure.html)
Maybe check this: https://opensource.com/article/20/1/open-source-calendar
https://vdirsyncer.pimutils.org/en/stable/config.html#google
https://arwebhosting.com/blog/set-up-and-sync-your-calendar-with-khal-and-vdirsyncer/
http://manpages.ubuntu.com/manpages/bionic/man1/vdirsyncer.1.html



## Bugs in Termux

<pre>
File "/data/data/com.termux/files/usr/lib/python3.9/site-packages/atomicwrites/__init__.py", line 59, in _move_atomic
	os.link(src, dst)
AttributeError: module 'os' has no attribute 'link'
</pre>

`vim /data/data/com.termux/files/usr/lib/python3.9/site-packages/atomicwrites/__init__.py
`
```bash

def link(src, dest):
    shutil.copyfile(src, dest)

def unlink(src):
    os.remove(src)

os.link = link
os.unlink = unlink
```
