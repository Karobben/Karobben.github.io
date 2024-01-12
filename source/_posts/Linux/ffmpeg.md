---
title: "ffmpeg"
description: "ffmpeg"
url: ffmpeg
date: 2020/06/23
toc: true
excerpt: "FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the FFmpeg program itself, designed for command-line-based processing o…"
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, Software]
cover: 'https://user-images.githubusercontent.com/88981/194717684-9919353b-8d51-4920-9980-3193fd895390.png'
thumbnail: 'https://user-images.githubusercontent.com/88981/194717684-9919353b-8d51-4920-9980-3193fd895390.png'
priority: 10000
covercopy: <a href='https://blog.miniasp.com/post/2022/10/08/Useful-tool-FFmpeg'>© Will Huang</a>
---


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

- American SCCTV: rtmp://media3.scctv.net/live/scctv_800

## Video Editer

```bash
ffmpeg -i test.MP4  \
    -r 30 -b 1000k -s "1920*1080"  \
    -an output.mp4
```
- `-i`: Input Video
- `-r`: Frame
- `-b`: bit rate for video
- `-s`: size for each frame
- `-an`: mute video

## Crop the Video

This example, we could crop the Video, Zoom in, and finally fit it in an new size of the video

```bash
ffmpeg -i test.avi -vf "crop=300:300:814:396,scale=1080:1080,scale=-1:1080,pad=1920:1080:(1920-iw)/2:0:black"   -acodec aac -vcodec h264 out.mp4
```

- `-i`: Input video
- `-vf`: filter graph, Different kinds of filter you can do with your video.
  - `crop`: crop peremeter: width:height:x:y. The x and y means the left up point you started to crop the video. All units are work as pixels.
  - `scale`: rescale the image. Here is from 300 to 1080.
  - `pad`: Not very clear. It seams like adding an black pad on the backgorund. We can use this feature to turn vertical-laied video into horizontal-laied video and filld with black in empty.



```bash
ffmpeg -i VideoBefore.mp4 -i MainVideo.mp4 -i VideoAfter.mp4 -i Audio.mp3 -filter_complex [1:v]scale=-2:480,setsar=sar=1[Scaled];[0:v][Scaled][2:v]concat=n=3:v=1:a=0[Merged] -map [Merged] -map 3:a OUTPUT.mp4


MOVE1=/mnt/8A26661926660713/Vlog/PubData/Courtship/hyper/movie1/movie1.mp4
MOVE2=/mnt/8A26661926660713/Vlog/PubData/Courtship/hyper/movie2/movie2.mp4
MOVE3=/mnt/8A26661926660713/Vlog/PubData/Courtship/hyper/movie3/movie3.mp4
MOVE4=/mnt/8A26661926660713/Vlog/PubData/Courtship/hyper/movie4/movie4.mp4
ffmpeg -i $MOVE1 -i $MOVE2 -i $MOVE3 -i $MOVE4 -filter_complex "[1:v]scale=-2:480,setsar=sar=1[Scaled];[0:v][Scaled][2:v]concat=n=3:v=1:a=0[Merged]" -map "[Merged]" -map 3:a OUTPUT.mp4


ffmpeg -i $MOVE1 -i $MOVE2 -i $MOVE3 -i $MOVE4 \
-f lavfi -t 0.1 -i anullsrc \
-filter_complex  \
  "[0:v]trim=0:138,setpts=PTS-STARTPTS[v0]; \
   [0:a]atrim=0:138,asetpts=PTS-STARTPTS[a0]; \
   [v0]scale='gte(iw/ih\,600/480)*600+lt(iw/ih\,600/480)*((480*iw)/ih):lte(iw/ih\,600/480)*480+gt(iw/ih\,600/480)*((600*ih)/iw)',pad='600:480:(600-gte(iw/ih\,600/480)*600-lt(iw/ih\,600/480)*((480*iw)/ih))/2:(480-lte(iw/ih\,600/480)*480-gt(iw/ih\,600/480)*((600*ih)/iw))/2:black'[x];[1:v]scale=600:480[y];[x][y]overlay=0:0[z];[2:v]scale=600:480,setsar=1:1[x0];[3:v]scale=600:480,setsar=1:1[x1];[x0][4:a][z][a0][x1][4:a]concat=n=3:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -shortest out.mp4









ffmpeg -y -i $MOVE1 -i $MOVE2 -filter_complex  "[0]scale=90:90;[1]scale=90:90;[0:0][1:0]concat=n=2:v=1:a=0" output.mp4


ffmpeg -y -i $MOVE1 -i $MOVE2 -filter_complex
 "[0]scale=720:576:force_original_aspect_ratio=decrease,pad=720:576:(ow-iw)/2:(oh-ih)/2,setsar=1[v0];[1]scale=720:576:force_original_aspect_ratio=decrease,pad=720:576:(ow-iw)/2:(oh-ih)/2,setsar=1[v1];[v0][0:a:0][v1][1:a:0]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" out.mp4
```
