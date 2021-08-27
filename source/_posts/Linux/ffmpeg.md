---
title: "ffmpeg"
description: "ffmpeg"
url: ffmpeg
date: 2020/06/23
toc: true
excerpt: "FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the FFmpeg program itself, designed for command-line-based processing o…"
tags: [Linux, Software, Multimedia, bash]
category: [Linux, Software]
cover: 'https://cn.bing.com/th?id=AMMS_f767fc15742ef6a9b129e406618c0ef3&w=410&h=110'
thumbnail: 'https://cn.bing.com/th?id=AMMS_f767fc15742ef6a9b129e406618c0ef3&w=110&h=110'
priority: 10000
---

## ffmpeg

![](https://cn.bing.com/th?id=AMMS_f767fc15742ef6a9b129e406618c0ef3&w=410&h=110)

## Mp4
```bash
ffmpeg -re -i "1.mp4" -vcodec copy -acodec aac -b:a 192k -f flv "你的rtmp地址/你的直播码"
```


<a name="Ctdka"></a>
## Camera


```python
sudo raspivid -o - -t 0 -w 1280 -h 720 -fps 24 -b 1000000 |
    ffmpeg -f h264 -i - -vcodec copy -acodec aac -b:a 192k \
        \\\-f flv "你的rtmp地址/你的直播码"
```


<a name="9vrdi"></a>
## Add an audio


```bash
sudo raspivid -o - -t 0 -w 1280 -h 720 -fps 24 -b 1000000 |
        ffmpeg  -re -stream_loop -1 -i  "/home/pi/scrpt/Blive/StarBucks_BGN.mp3" \
        -f h264 -i - -vcodec copy -r 30 -acodec aac -b:a 100k -preset ultrafast \
        -tune zerolatency -f flv "rtmp://"
```


<a name="TqqYA"></a>
## Camera＆　Mircrophone
```bash
## https://blog.csdn.net/word_joke/article/details/96978138
ffmpeg  -f dshow -i video="USB2.0 PC CAMERA"
                 -f dshow -i audio="麦克风 (2- USB2.0 MIC)"
                 -vcodec libx264 -preset:v ultrafast -tune:v zerolatency
                 -f flv rtmp://127.0.0.1:1935/live/123

## https://blog.csdn.net/HuiShouDeZaiLai/article/details/97373878
ffmpeg  -f alsa -thread_queue_size 1024  -i "$MIC_DEV_NAME" \
        -f video4linux2   -r 10  -s 640x480 -i "$CAMERA_DEV_NAME" \
        -vcodec h264  -ac 1  -b:a 128k -ar 44100 -acodec aac   \
        -strict -2  -tune zerolatency  -preset medium -b:v 1500k -f pcm   \
        -f  flv    rtmp://XXX:1935/live/livestream
```

<br />

<a name="Bi3mX"></a>
## 拉流


```bash
##https://blog.csdn.net/hdg745979749/article/details/103000160

ffmpeg -i rtmp://58.200.131.2:1935/livetv/hunantv -c copy dump.flv
## 地址为 湖南卫视
## 可直接下载保存为flv 视频
```
