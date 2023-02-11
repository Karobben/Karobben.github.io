---
toc: true
url: opencv_img_trans
covercopy: <a href="https://www.pexels.com/photo/low-angle-view-of-lighting-equipment-on-shelf-257904/">© Pixabay</a>
priority: 10000
date: 2021-11-13 16:19:31
title: "Opencv, Flip, noise, mask, etc"
ytitle: "Opencv, Flip, noise, mask, etc"
description: "Opencv, Flip, noise, mask, etc"
excerpt: "Stich two or more images to one with opencv"
tags: [Python, OpenCV]
category: [Python, OpenCV]
cover: "https://images.pexels.com/photos/257904/pexels-photo-257904.jpeg"
thumbnail: "https://images.pexels.com/photos/257904/pexels-photo-257904.jpeg?cs=srgb&dl=pexels-pixabay-257904.jpg"
---

## Image Transfor

Sometimes, we'd like to transfer image's color, temperature, or something for getting more trainning data.

There are few way's could help you argument your photos to generate a considerable training data set.

## Flip

```python
img2 = cv2.flip(img, 0) ## img would flip vertically
img2 = cv2.flip(img, 1) ## img would flip horizontally
```

## Temperature

source code: [Packt](https://subscription.packtpub.com/book/application-development/9781785282690/1/ch01lvl1sec11/generating-a-warming-cooling-filter)

### Lighter
```python
import cv2
import numpy as np

x = [0, 128, 255]
y = [0, 192, 255]
myLUT = _create_LUT_8UC1(x, y)
img_curved = cv2.LUT(img_gray, myLUT).astype(np.uint8)
```

### Warming filter

Strangely enough, those codes doesn't work = =
```python
class WarmingFilter:

  def __init__(self):
    self.incr_ch_lut = _create_LUT_8UC1([0, 64, 128, 192, 256],
      [0, 70, 140, 210, 256])
    self.decr_ch_lut = _create_LUT_8UC1([0, 64, 128, 192, 256],
      [0, 30,  80, 120, 192])

	def render(self, img_rgb):
	    c_r, c_g, c_b = cv2.split(img_rgb)
	    c_r = cv2.LUT(c_r, self.incr_ch_lut).astype(np.uint8)
	    c_b = cv2.LUT(c_b, self.decr_ch_lut).astype(np.uint8)
	    img_rgb = cv2.merge((c_r, c_g, c_b))
			c_b = cv2.LUT(c_b, decrChLUT).astype(np.uint8)

			# increase color saturation
	c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_rgb,
	    cv2.COLOR_RGB2HSV))
	c_s = cv2.LUT(c_s, self.incr_ch_lut).astype(np.uint8)
	return cv2.cvtColor(cv2.merge((c_h, c_s, c_v)),
	    cv2.COLOR_HSV2RGB)
```

### Colder Filter

```python
class CoolingFilter:

    def render(self, img_rgb):

        c_r, c_g, c_b = cv2.split(img_rgb)
        c_r = cv2.LUT(c_r, self.decr_ch_lut).astype(np.uint8)
        c_b = cv2.LUT(c_b, self.incr_ch_lut).astype(np.uint8)
        img_rgb = cv2.merge((c_r, c_g, c_b))

        # decrease color saturation
        c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV))
        c_s = cv2.LUT(c_s, self.decr_ch_lut).astype(np.uint8)
        return cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)
```

## Add a transbarent mask

source code: [Pyimagesearch](https://www.pyimagesearch.com/2016/03/07/transparent-overlays-with-opencv/)


```python
from __future__ import print_function
import numpy as np
import cv2
# load the image
image = cv2.imread("mexico.jpg")

for alpha in np.arange(0, 1.1, 0.1)[::-1]:
	# create two copies of the original image -- one for
	# the overlay and one for the final output image
	overlay = image.copy()
	output = image.copy()
	# draw a red rectangle surrounding Adrian in the image
	# along with the text "PyImageSearch" at the top-left
	# corner
	cv2.rectangle(overlay, (420, 205), (595, 385),
		(0, 0, 255), -1)
	cv2.putText(overlay, "PyImageSearch: alpha={}".format(alpha),
		(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
	# apply the overlay
	cv2.addWeighted(overlay, alpha, output, 1 - alpha,
		0, output)
		# show the output image
	print("alpha={}, beta={}".format(alpha, 1 - alpha))
	cv2.imshow("Output", output)
	cv2.waitKey(0)
```

## Add noises

Source: [Shubham Pachori, from stackoverflow](https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv)
```python

import numpy as np
import os
import cv2

def noisy(noise_typ,image):
  if noise_typ == "gauss":
    row,col,ch= image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy
  elif noise_typ == "s&p":
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out
  elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
  elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      return noisy
```


Source: [ppk28, from stackoverflow](https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv)
```python
import numpy as np
import random
import cv2

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('image.jpg',0) # Only for grayscale image
noise_img = sp_noise(image,0.05)
cv2.imwrite('sp_noise.jpg', noise_img)
```

## Filter from PIL

Sorce: [www.tutorialspoint.com](https://www.tutorialspoint.com/python_pillow/python_pillow_adding_filters_to_an_image.htm)

```python
from PIL import Image, ImageFilter

im = Image.open('123.png')
im1 = im.filter(ImageFilter.BLUR)
im1.show()
```
