---
title: "OpenCV examples for beginners| Python"
ytitle: "OpenCV 简单入门| Python"
description: "OpenCV tutorials: basic grammar for OpenCV"
url: opencv2
date: 2020/09/12
toc: true
excerpt: "The Python library cv2 is an open-source computer vision library used for real-time image processing and analysis. It provides a variety of image processing functions, including object detection, face recognition, and video analysis. It is often used in fields such as robotics, self-driving cars, and augmented reality. <a title='ChatGPT'>Who said this?</a>"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
thumbnail: 'https://opencv.org/wp-content/uploads/2021/01/OpenCV-logo.png'
covercopy: "© OpenCV"
priority: 10000
---
## Install


```bash
pip3 install --upgrade setuptools
pip3 install numpy Matplotlib
pip3 install opencv-contrib-python
```

==Notice:== Don't ever install other versions opencv, exp: python2-opencv, opencv-python


## Img Read and Show


### Load an color image in grayscale
```python
import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
```


### img read from Camera


```python
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

cap = cv2.VideoCapture(0)
while(True):
   ret, frame = cap.read()
   cv2.imshow('image',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
```


### Resolution of the img


```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
```


### img show and close

```python
cv2.imshow('image',img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
```


### resize

```python
 cv2.resize(img, (10,10), interpolation = cv2.INTER_AREA)
```


### Slice

Slice the image based on the center, width, and height
```python
import cv2
import numpy as np

# Load the image
img = cv2.imread('example.jpg')

# Get the center point of the rectangular region
center_x, center_y = 100, 100
# Get the width and height of the rectangular region
width, height = 50, 80

def img_slice(center_x, center_y, width, height):
  # Calculate the coordinates of the top-left and bottom-right corners of the rectangular region
  x1 = int(center_x - (width / 2))
  y1 = int(center_y - (height / 2))
  x2 = int(center_x + (width / 2))
  y2 = int(center_y + (height / 2))

  # Slice the rectangular region from the original image
  return img[y1:y2, x1:x2]
```


### rotate

Cite: [geeksforgeeks.org, 2023](https://www.geeksforgeeks.org/python-opencv-cv2-rotate-method/)

```python
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
```

### img wirte

```python
cv2.imwrite('messigray.png',img)
```

### img to gif

Original Webpage:
- [PHILOS_THU, 2017](https://blog.csdn.net/guduruyu/article/details/77540445)
- [执笔论英雄, 2018](https://blog.csdn.net/qq_38662930/article/details/83832455)

```python
import cv2
import imageio
List = ['./yang1.jpg', './yang2.jpg', './yang3.jpg']

frames = []

for img in List:
  img = cv2.imread(img, 1)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img = cv2.resize(img, (460,360))
  frames.append(img)

gif=imageio.mimsave('yang.gif',frames,'GIF',duration=0.4)
```

### Screen shot


```python
import cv2
import numpy as np
from mss import mss
cords = {'top':40 , 'left': 0 , 'width': 800, 'height': 640 }
while(True):
   with mss() as sct :
       img = np.array(sct.grab(cords)) #sct.grab(cords/monitor)
   #cimg = cv2.cvtColor(img , cv2.COLOR_BGRA2GRAY)
   cv2.imshow('image',img)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
cv2.destroyAllWindows()
```
### Draw on Img


#### Draw a Rectangle
reference: [AlanWang4523 2018](https://blog.csdn.net/u011520181/java/article/details/84036425)

With know top-left and bottom-right:

```python
## 绘制一个红色矩形
ptLeftTop = (120, 100)
ptRightBottom = (200, 150)

def Draw_rect(img, ptLeftTop, ptRightBottom,
  point_color = (0, 0, 255), # BGR
  thickness = 1,
  lineType = 8):
  return cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
```

With know center, width, and height

```python
def Draw_rect(img, Ccenter_x, center_y, width, height,
  point_color = (0, 0, 255), # BGR)
  thickness = 2,
  lineType = 8):
  ptLeftTop = (int(center_x - (width / 2)), int(center_y - (height / 2)))
  ptRightBottom = (int(center_x + (width / 2)), int(center_y + (height / 2)))
  # Draw the rectangle on the image
  return cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
```

#### Draw a oval / ellipse

Source: [geeksforgeeks.org](https://www.geeksforgeeks.org/python-opencv-cv2-ellipse-method/)

```python
center_coordinates = (120, 100)
axesLength = (100, 50)
angle = 30
startAngle = 0
endAngle = 360
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of -1 px
thickness = -1
# Using cv2.ellipse() method
# Draw a ellipse with blue line borders of thickness of -1 px
image = cv2.ellipse(image, center_coordinates,
                    axesLength, angle, startAngle,
                    endAngle, color, thickness)
# Displaying the image
cv2.imshow("Ellipse", image)
```
#### Draw an arrow

Source: [geeksforgeeks.org](https://www.geeksforgeeks.org/python-opencv-cv2-arrowedline-method/)

```python
start_point = (225, 0)
# End coordinate
end_point = (0, 90)
# Red color in BGR
color = (0, 0, 255)
# Line thickness of 9 px
thickness = 9
# Using cv2.arrowedLine() method
# Draw a red arrow line
# with thickness of 9 px and tipLength = 0.5
image = cv2.arrowedLine(image, start_point, end_point,
                    color, thickness, tipLength = 0.5)
# Displaying the image
cv2.imshow("arrow", image)
```

#### Write on the image
```python
img = cv2.imread('messi5.jpg',0)
cv2.putText(img, "Hello World" ,(200, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
```

### Other Tricks for image

```python
## Blur
img = cv2.medianBlur(img,5)

## Grey
cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
```


## Video

### Video read

```python
cap=cv2.VideoCapture("test")
while (True):
   ret,frame=cap.read()
   cv2.imshow("video",frame)
   # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
   if cv2.waitKey(25)&0xFF==ord('q'):
       cv2.destroyAllWindows()
       break
```

### Reading Video information

```python
## fps of this Video
fps_c = cap.get(cv2.CAP_PROP_FPS)
frame_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
Video_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
Video_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
```


<a name="DG9Xm"></a>
### play Video and audio


```python
##https://stackoverflow.com/questions/46864915/python-add-audio-to-video-opencv
import cv2
import numpy as np
##ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
video_path="../L1/images/Godwin.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)
```


### Video write

```python
import cv2, os

File = "Up"
OUTPUT = "Egg_Day1.avi"
List = os.popen('ls '+File).read().split('\n')[:-1]

img = cv2.imread(File +"/"+List[0])
fps = 24
size = (len(img[0]),len(img))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps,size)
for i in List:
    img = cv2.imread(File +"/"+i)
    videowriter.write(img)
videowriter.release()
```

`cv2.VideoWriter_fourcc('M','J','P','G')`: It creates a VideoWriter fourcc object in OpenCV, which is used to specify the codec to be used for writing video files.

The `cv2.VideoWriter_fourcc()` function takes four characters as input to create a fourcc code. In this case, the four characters are `'M', 'J', 'P', and 'G'`, which correspond to the MPEG-1 codec.

So the `fourcc` variable will hold the fourcc code for the MPEG-1 codec, which will be used when writing the video file.


### Grey iamge to video

```python
import cv2
import numpy as np

# Create a list of grayscale images
img_list = [...]  # insert your list of images here

# Define the video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (img_list[0].shape[1], img_list[0].shape[0]), False)

# Write each image to the video
for img in img_list:
    # Convert to grayscale if not already
    if len(img.shape) == 3 and img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Write to video
    out.write(img)

# Release the video writer
out.release()
```

In this code, `img_list` is the list of grayscale images you want to output as a video. The code first defines the `VideoWriter` object with the desired filename, codec, frame rate, and frame size. Then, it iterates through each image in `img_list`, converts it to grayscale (if it isn't already), and `writes` it to the video using the write method of the `VideoWriter` object. Finally, it releases the `VideoWriter` object to close the video file.


### vedio to gif


```python
from cv2 import cv2
import imageio
import numpy
# Collection of the imgs
frames_list = []

# Tossed frames per FPS. When FPS = 1, all frame are saved.
FPS = 1

cap=cv2.VideoCapture("test_1.mp4")
while (True):
  ret,frame=cap.read()
  #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  img = cv2.resize(frame, (460,360))
  frames_list.append(img)


frames = []

Num =0
for img in frames_list:
  Num +=1
  if Num %3 == 0:
    frames.append(img)

gif=imageio.mimsave('test_3.gif',frames,'GIF',duration=1/8)
```



### Video capture


```python
##!/usr/bin/env python
## -*- coding: utf-8 -*-
## @Time    : 2019/3/7 11:43
## @Author  : HaoWANG
## @Site    :
## @File    : VideoWrite.py
## @Software: PyCharm

## 加载包
import math
import sys
import cv2

def main():
  # 初始化摄像头
  keep_processing = True;
  camera_to_use = 0;  # 0 if you have one camera, 1 or > 1 otherwise
  cap = cv2.VideoCapture(0)  # 定义视频捕获类cap
  windowName = "Live Video Capture and Write"  # 窗口名

  # opencv中视频录制需要借助VideoWriter对象， 将从VideoCapture 中读入图片，不断地写入到VideoWrite的数据流中。
  # 指定视频编解码方式为MJPG
  codec = cv2.VideoWriter_fourcc(*'MJPG')
  fps = 25.0  # 指定写入帧率为25
  frameSize = (640, 480)  # 指定窗口大小
  # # 创建 VideoWriter对象
  output = cv2.VideoWriter('VideoRecord.avi', codec, fps, frameSize)

  # 摄像头开启检测
  # error detection #
  if not (((len(sys.argv) == 2) and (cap.open(str(sys.argv[1]))))
          or (cap.open(camera_to_use))):
    print("ERROR：No video file specified or camera connected.")
    return -1

  # Camera Is Open
  # create window by name (note flags for resizable or not)
  cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
  print("按键Q-结束视频录制")

  while (cap.isOpened()):

    # 00 if video file successfully open then read frame from video
    if (keep_processing):

      ret, frame = cap.read()  # 定义read对象ret和frame帧
      # start a timer (to see how long processing and display takes)
      start_t = cv2.getTickCount()

      # 不断的从VideoCapture 中读入图片，然后写入到VideoWrite的数据流中。
      output.write(frame)

      cv2.imshow(windowName, frame)  # display image

      # stop the timer and convert to ms. (to see how long processing and display takes)
      stop_t = ((cv2.getTickCount() - start_t) / cv2.getTickFrequency()) * 1000

      # 接收键盘停止指令
      # start the event loop - essential
      # wait 40ms or less depending on processing time taken (i.e. 1000ms / 25 fps = 40 ms)

      key = cv2.waitKey(max(2, 40 - int(math.ceil(stop_t)))) & 0xFF

      # It can also be set to detect specific key strokes by recording which key is pressed
      # e.g. if user presses "q" then exit

      if (key == ord('q')):
        print("Quit Process ")
        keep_processing = False
    else:
      break

  print("The display and video write tasks take {} ms".format(stop_t))

  # release the camera and close all windows
  # 资源释放,在录制结束后，我们要释放资源：
  # # 释放资源
  cap.release()
  output.release()
  cv2.destroyAllWindows()
## end main()

if __name__ == "__main__":
  main()
```


## Training your personal model


```python
'''
positive list:
Pics in Me director, 55*110
Background Pics are in BG file
'''
for i in $(ls Me/);do echo Me/$i 1 0 0 55 110;done > pos.list

for i in $(ls BG/);do echo BG/$i;done > bg.list

rm models/*
opencv_createsamples  -info pos.list -vec pos.vec -bg bg.list -num 12 -w 20 -h 40
opencv_traincascade -data models/ -vec pos.vec -bg bg.list -numPos 12 -numNeg 27 -numStages 2 -featureType HAAR -w 20 -h 40

'''
s
'''

import cv2

## 探测图片中的人脸

detector = cv2.CascadeClassifier("models/params.xml") # absolute !!!

faces = detector.detectMultiScale(img)
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
```

<br />

<a name="pTmnX"></a>
## Matlibplot


```python
## -*- coding: utf-8 -*-
"""
## --------------------------------------------------------
## @Author : panjq
## @E-mail : pan_jinquan@163.com
## @Date   : 2020-02-05 11:01:49
## --------------------------------------------------------
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2


def fig2data(fig):
    """
    fig = plt.figure()
    image = fig2data(fig)
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    import PIL.Image as Image
    # draw the renderer
    fig.canvas.draw()
    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = np.asarray(image)
    return image


if __name__ == "__main__":
    # Generate a figure with matplotlib</font>
    figure = plt.figure()
    plot = figure.add_subplot(111)
    # draw a cardinal sine plot
    x = np.arange(1, 100, 0.1)
    y = np.sin(x) / x
    plot.plot(x, y)
    plt.show()
    ##
    image = fig2data(figure)
    cv2.imshow("image", image)
    cv2.waitKey(0)
```




```python

img1 = Overed_fly.copy()
img2 = ID_lay_img.copy()
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Find keypoints and descriptors for both images
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# Initialize brute-force matcher
bf = cv2.BFMatcher()

# Match descriptors from both images
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test to remove false matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Draw the matched keypoints
result = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None)

cv2.imshow("video",result)
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyAllWindows()

```