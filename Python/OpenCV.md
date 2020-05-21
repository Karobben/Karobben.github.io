---
url: opencv2
---

# OpenCV

<a name="Y6vHH"></a>
# Install


```bash
pip3 install --upgrade setuptools
pip3 install numpy Matplotlib
pip3 install opencv-python
```


<a name="o64ZD"></a>
# 1. Img Read and Show
<a name="THijk"></a>
##
<a name="Qs3gR"></a>
## 1.1 Load an color image in grayscale
```python
import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
```


<a name="sShM1"></a>
### 1.12 img read from Camera


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


<a name="efUCs"></a>
#### Resolution of the img


```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
```


<a name="PjfCy"></a>
## 1.2 img show and close
<br />
```python
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


<a name="Fvpyi"></a>
### 1.21 resize


```python
 cv2.resize(img, (10,10), interpolation = cv2.INTER_AREA)
```

<br />

<a name="TIAdj"></a>
## 1.3 img wirte


```python
cv2.imwrite('messigray.png',img)
```


<a name="LpucV"></a>
## 1.4 Screen shot


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

<br />
<br />

<a name="smIPT"></a>
## 1.5 Some Tricks for img


```python
# Blur
img = cv2.medianBlur(img,5)

# Grey
cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
```


<a name="FS5Nj"></a>
# 2 Vedio


<a name="8FPmZ"></a>
## 2.1 Vedio read


```python
cap=cv2.VideoCapture("test")
while (True):
   ret,frame=cap.read()
   cv2.imshow("video",frame)
   # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
   if cv2.waitKey(25)&0xFF==ord('q'):
       cv2.destroyAllWindows()
       break

# fps of this vedio
fps_c = cap.get(cv2.CAP_PROP_FPS)
Vedio_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
Vedio_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
```


<a name="DG9Xm"></a>
## 2.2 play Vedio and audio


```python
#https://stackoverflow.com/questions/46864915/python-add-audio-to-video-opencv
import cv2
import numpy as np
#ffpyplayer for playing audio
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


<a name="dw94w"></a>
## 2.3 Vedio write


```python
# for normal output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while true:
 out.write(frame)
# For Gray outpu
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter("outfilename.mp4", fourcc, 15, (640,480), 0)
```

<br />

<a name="4DtIF"></a>
## 2.4 Img to Video


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


<a name="U6CwD"></a>
## 2.5 Vedio capture


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:43
# @Author  : HaoWANG
# @Site    :
# @File    : VideoWrite.py
# @Software: PyCharm

# 加载包
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
# end main()

if __name__ == "__main__":
	main()
```


<a name="fVJmV"></a>
# Training your personal model


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

# 探测图片中的人脸

detector = cv2.CascadeClassifier("models/params.xml") # absolute !!!

faces = detector.detectMultiScale(img)
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
```

<br />

<a name="pTmnX"></a>
# Matlibplot


```python
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : panjq
# @E-mail : pan_jinquan@163.com
# @Date   : 2020-02-05 11:01:49
# --------------------------------------------------------
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
