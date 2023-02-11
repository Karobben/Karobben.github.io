---
title: "Blive with RasperryPi"
description: "Blive with RasperryPi"
url: blive2
date: 2020/06/23
toc: true
excerpt: "A script for Blive stream in RasperryPi.python + openCVC + ffmpeg"
tags: [Linux, RasperryPi, bash, Python]
category: [Linux, RasperryPi]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## Blive with RasperryPi

Reference: [Bilibili: 五维谐振子 ](https://www.bilibili.com/read/cv791252/)

<a name="Aypwi"></a>
## Qick Start
```bash
sudo apt upgrade
sudo apt update
sudo apt install ffmpeg

sudo raspivid -o - -t 0 -w 1280 -h 720 -fps 24 -b 1000000 | ffmpeg -f h264 -i - -vcodec copy -acodec aac -b:a 192k -f flv "你的rtmp地址/你的直播码"
```

<a name="Zgaim"></a>
### 降低延迟:
[CSDN: 北雨南萍](https://blog.csdn.net/fireroll/article/details/51902018)

```bash
sudo raspivid -o - -t 0 -w 1280 -h 720 -fps 24 -b 1000000 |
    ffmpeg -f h264 -i - -vcodec copy -r 30 -acodec aac -b:a 100k -preset ultrafast -tune zerolatency -f flv "你的rtmp地址/你的直播码"
```

<a name="3NazO"></a>
## raspivid
[树莓派实验室: Spoony](https://shumeipai.nxez.com/2014/09/21/raspicam-documentation.html)
```bash
"raspivid" Camera App (commit 06bc6daa0213 Tainted)

Display camera output to display, and optionally saves an H264 capture at requested bitrate


usage: raspivid [options]

Image parameter commands

-b, --bitrate  : Set bitrate. Use bits per second (e.g. 10MBits/s would be -b 10000000)
-t, --timeout  : Time (in ms) to capture for. If not specified, set to 5s. Zero to disable
-d, --demo  : Run a demo mode (cycle through range of camera options, no capture)
-fps, --framerate  : Specify the frames per second to record
-e, --penc  : Display preview image *after* encoding (shows compression artifacts)
-g, --intra  : Specify the intra refresh period (key frame rate/GoP size). Zero to produce an initial I-frame and then just P-frames.
-pf, --profile  : Specify H264 profile to use for encoding
-td, --timed  : Cycle between capture and pause. -cycle on,off where on is record time and off is pause time in ms
-s, --signal  : Cycle between capture and pause on Signal
-k, --keypress  : Cycle between capture and pause on ENTER
-i, --initial  : Initial state. Use 'record' or 'pause'. Default 'record'
-qp, --qp  : Quantisation parameter. Use approximately 10-40. Default 0 (off)
-ih, --inline  : Insert inline headers (SPS, PPS) to stream
-sg, --segment  : Segment output file in to multiple files at specified interval <ms>
-wr, --wrap  : In segment mode, wrap any numbered filename back to 1 when reach number
-sn, --start  : In segment mode, start with specified segment number
-sp, --split  : In wait mode, create new output file for each start event
-c, --circular  : Run encoded data through circular buffer until triggered then save
-x, --vectors  : Output filename <filename> for inline motion vectors
-if, --irefresh  : Set intra refresh type
-fl, --flush  : Flush buffers in order to decrease latency
-pts, --save-pts  : Save Timestamps to file for mkvmerge
-cd, --codec  : Specify the codec to use - H264 (default) or MJPEG
-lev, --level  : Specify H264 level to use for encoding
-r, --raw  : Output filename <filename> for raw video
-rf, --raw-format  : Specify output format for raw video. Default is yuv
-l, --listen  : Listen on a TCP socket
-stm, --spstimings  : Add in h.264 sps timings
-sl, --slices  : Horizontal slices per frame. Default 1 (off)


H264 Profile options :
baseline,main,high

H264 Level options :
4,4.1,4.2

H264 Intra refresh options :
cyclic,adaptive,both,cyclicrows

Raw output format options :
yuv,rgb,gray

Raspivid allows output to a remote IPv4 host e.g. -o tcp://192.168.1.2:1234or -o udp://192.168.1.2:1234
To listen on a TCP port (IPv4) and wait for an incoming connection use the -l option
e.g. raspivid -l -o tcp://0.0.0.0:3333 -> bind to all network interfaces,
raspivid -l -o tcp://192.168.1.1:3333 -> bind to a certain local IPv4 port

Common Settings commands

-?, --help  : This help information
-w, --width  : Set image width <size>
-h, --height  : Set image height <size>
-o, --output  : Output filename <filename> (to write to stdout, use '-o -'). If not specified, no file is saved
-v, --verbose  : Output verbose information during run
-cs, --camselect  : Select camera <number>. Default 0
-md, --mode  : Force sensor mode. 0=auto. See docs for other modes available
-gps, --gpsdexif  : Apply real-time GPS information to output (e.g. EXIF in JPG, annotation in video (requires libgps.so.23)

Preview parameter commands

-p, --preview  : Preview window settings <'x,y,w,h'>
-f, --fullscreen  : Fullscreen preview mode
-op, --opacity  : Preview window opacity (0-255)
-n, --nopreview  : Do not display a preview window
-dn, --dispnum  : Display on which to display the preview window (dispmanx/tvservice numbering)

Image parameter commands

-sh, --sharpness  : Set image sharpness (-100 to 100)
-co, --contrast  : Set image contrast (-100 to 100)
-br, --brightness  : Set image brightness (0 to 100)
-sa, --saturation  : Set image saturation (-100 to 100)
-ISO, --ISO  : Set capture ISO
-vs, --vstab  : Turn on video stabilisation
-ev, --ev  : Set EV compensation - steps of 1/6 stop
-ex, --exposure  : Set exposure mode (see Notes)
-fli, --flicker  : Set flicker avoid mode (see Notes)
-awb, --awb  : Set AWB mode (see Notes)
-ifx, --imxfx  : Set image effect (see Notes)
-cfx, --colfx  : Set colour effect (U:V)
-mm, --metering  : Set metering mode (see Notes)
-rot, --rotation  : Set image rotation (0-359)
-hf, --hflip  : Set horizontal flip
-vf, --vflip  : Set vertical flip
-roi, --roi  : Set region of interest (x,y,w,d as normalised coordinates [0.0-1.0])
-ss, --shutter  : Set shutter speed in microseconds
-awbg, --awbgains  : Set AWB gains - AWB mode must be off
-drc, --drc  : Set DRC Level (see Notes)
-st, --stats  : Force recomputation of statistics on stills capture pass
-a, --annotate  : Enable/Set annotate flags or text
-3d, --stereo  : Select stereoscopic mode
-dec, --decimate  : Half width/height of stereo image
-3dswap, --3dswap  : Swap camera order for stereoscopic
-ae, --annotateex  : Set extra annotation parameters (text size, text colour(hex YUV), bg colour(hex YUV), justify, x, y)
-ag, --analoggain  : Set the analog gain (floating point)
-dg, --digitalgain  : Set the digital gain (floating point)
-set, --settings  : Retrieve camera settings and write to stdout
```


<a name="7wvaM"></a>
## python + openCVC + ffmpeg
more: [CSDN: mind_programmonkey](https://blog.csdn.net/Mind_programmonkey/article/details/102732555)

基本框架
```python
import cv2 as cv
import subprocess as sp

rtmpUrl = "你的rtmp地址/你的直播码"
camera_path = "/dev/video0"
cap = cv.VideoCapture(camera_path)

## Get video information
fps = 30 #int(cap.get(cv.CAP_PROP_FPS))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

## ffmpeg command
command = ['ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "{}x{}".format(width, height),
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        rtmpUrl]

## 管道配置
p = sp.Popen(command, stdin=sp.PIPE)

## read webcamera
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break

    # process frame
    # your code
    # process frame

    # write to pipe
    p.stdin.write(frame.tostring())
```
