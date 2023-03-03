---
toc: true
url: opencv_edge_detect
covercopy: © Karobben
priority: 10000
date: 2022-06-13 10:14:24
title: "Python:Opencv Edge Detection"
ytitle: "Pyhton:Opencv 边缘检测"
description: "Detect the edge of the image by using python opencv"
excerpt: "Detect the edge of the image by using python opencv"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: "https://s1.ax1x.com/2022/06/22/jpCvRJ.png"
thumbnail: "https://s1.ax1x.com/2022/06/22/jpCvRJ.png"
---

## Python:Opencv Edge Detection

Reference:
- [LearnOpenCV](https://learnopencv.com/edge-detection-using-opencv/)
- [Morphological Transformations](https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html)

Example Image:
|![](https://images.theconversation.com/files/22985/original/kk8g8b9t-1367209604.jpg?ixlib=rb-1.1.0&rect=0%2C197%2C968%2C470&q=45&auto=format&w=1356&h=668&fit=crop)|
|:-:|
|[© Joe Jimbo](https://theconversation.com/animals-in-research-drosophila-the-fruit-fly-13571)|

```python
import cv2
import numpy as np

# Read the original image
img = cv2.imread('test.jpg')
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
'''
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
'''

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=70, threshold2=70) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

![](https://s1.ax1x.com/2022/06/22/jpCjG4.png)

```python

edges = cv2.Canny(image=img_blur, threshold1=70, threshold2=70) # Canny Edge Detection
edges[edges!=0]= 100
edges[edges==0]= 255
edges[edges==100]= 0

#img2 = cv2.dilate(edges,kernel,iterations = 1)

cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(edges,kernel,iterations = 1)
img = cv2.cvtColor(erosion, cv2.COLOR_GRAY2RGB)
#img[np.all(img == (0, 0, 0), axis=-1)] = (128, 114, 250)

cv2.imshow('Canny Edge Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("result2.png", img)
```

![](https://s1.ax1x.com/2022/06/22/jpCvRJ.png)
