---
title: "ImageAI"
ytitle: "ImageAI"
description: "ImageAI"
url: imageai
date: 2020/01/22
toc: true
excerpt: "ImageAI"
tags: [Python, HTML]
category: [Python]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---
## Create an virtual environment for ImageAI

```bash
python3 -m pip install  --upgrade pip wheel setuptools virtualenv

python3 -m virtualenv Python_ev_image
source Python_ev_image/bin/activate
```

## Install

```bash
pip install tensorflow==2.4.0
pip install tensorflow-gpu==2.4.0

pip install keras==2.4.3 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1 h5py==2.10.0 matplotlib==3.3.2 opencv-python keras-resnet==0.2.0
pip install imageai --upgrade
```

## Download Models

- <a class="reference external" href="https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/mobilenet_v2.h5/">Download MobileNetV2 Model</a>
- <a class="reference external" href="https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_imagenet_tf.2.0.h5/">Download ResNet50 Model</a>
- <a class="reference external" href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/inception_v3_weights_tf_dim_ordering_tf_kernels.h5/">Download InceptionV3 Model</a>
- <a class="reference external" href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/DenseNet-BC-121-32.h5/">Download DenseNet121 Model</a>


After downloaded, move it to your directory

```bash
mkdir Python_ev_image/image_Models
mv *.h5 Python_ev_image/image_Models
```


## test

```python
from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "Python_ev_image/image_Models/resnet50_imagenet_tf.2.0.h5"))
prediction.loadModel()

Pic_test  ="/home/ken/Downloads/test_car.jpeg"

predictions, probabilities = prediction.classifyImage(Pic_test, result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
```

<pre style="background-color:rgb(65,65,65);color:salmon">
cab  :  70.75855731964111
sports_car  :  16.99793189764023
forklift  :  2.3407679051160812
pickup  :  2.0892834290862083
car_wheel  :  1.97103600949049
</pre>

|![car example](https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8MjAyMCUyMGNhcnN8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80)|
|:-:|
|[© unsplash.com](https://unsplash.com/s/photos/2020-cars)|


## Test 2, Video detact

Download the models:
<li><strong><a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5">RetinaNet</a></strong> <em>(Size = 145 mb, high performance and accuracy, with longer detection time)</em></li>
<li><strong><a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5">YOLOv3</a></strong> <em>(Size = 237 mb, moderate performance and accuracy, with a moderate detection time)</em></li>
<li><strong><a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5">TinyYOLOv3</a></strong> <em>(Size = 34 mb, optimized for speed and moderate performance, with fast detection time)</em></li>

After download the models, move them to the same directory as above.

```python
from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( "./Python_ev_image/image_Models/hololens-ex-60--loss-2.76.h5")
detector.loadModel()

Video_test = "Github/FliesDetect/Behavior_movie/promE.mp4"
video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, Video_test),
                                output_file_path=os.path.join(execution_path, "traffic_detected")
                                , frames_per_second=20, log_progress=True)
print(video_path)
```

==I failed==

## build custom video object detaction

### FirstCustomVideoObjectDetection.py

```python
from imageai.Detection.Custom import CustomVideoObjectDetection
import os

execution_path = os.getcwd()

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("hololens-ex-60--loss-2.76.h5")
video_detector.setJsonPath("detection_config.json")
video_detector.loadModel()

Video_test = "/media/ken/Data/Github/FliesDetect/Behavior_movie/promE.mp4"
video_detector.detectObjectsFromVideo(input_file_path=Video_test,
                                          output_file_path=os.path.join(execution_path, "holo1-detected3"),
                                          frames_per_second=20,
                                          minimum_percentage_probability=40,
                                          log_progress=True)
```


```python
import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if __name__ == '__main__' :
    # Set up tracker.
    # Instead of MIL, you can also use
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[2]
    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv2.TrackerCSRT_create()
    # Read video
    video = cv2.VideoCapture("/media/ken/Data/Github/FliesDetect/Behavior_movie/promE.mp4")
    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print ('Cannot read video file')
        sys.exit()
    # Define an initial bounding box
    bbox = (287, 23, 86, 320)
    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        # Start timer
        timer = cv2.getTickCount()
        # Update tracker'Cannot read video file'
        ok, bbox = tracker.update(frame)
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
```
