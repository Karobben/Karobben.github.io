---
toc: true
url: opencv-similarity
covercopy: © Karobben
priority: 10000
date: 2023-05-12 15:27:11
title: Compare the similar of two images
ytitle: Compare the similar of two images
description: Compare the similar of two images
excerpt: Compare the similar of two images
tags: [Python, Image]
category: [Python, Data]
cover: "https://s1.ax1x.com/2023/05/13/p96k0NF.png"
thumbnail: "https://s1.ax1x.com/2023/05/13/p96k0NF.png"
---

## Picture similarities a

Image from: [© Chun-Guang Shan; 2019](https://cancerci.biomedcentral.com/articles/10.1186/s12935-019-0924-9#auth-Chun_Guang-Shan)

|![Fig. 5E](https://s1.ax1x.com/2023/05/13/p96k8pj.png)|![Fig. 3D](https://s1.ax1x.com/2023/05/13/p96k1hQ.png)|
|-:|:-|

Why this example: 
- Youtube: [736778E78A9F9447776A74287756D7](https://www.youtube.com/watch?v=QKOmaQ8bnO8)
- Twitter: [Elisabeth Bik](https://twitter.com/MicrobiomDigest)

```python
import cv2

img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')
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

![Similarities between two images](https://s1.ax1x.com/2023/05/13/p96k0NF.png)

From this results, we can find that event though the elements of the images are complicated and the color is transferred, this algorithm could still do an awesome job.

Here we are using the RootSIFT rather then standard SIFT which requires `cv2.xfeatures2d` module. What's the difference between them?

> SIFT (Scale-Invariant Feature Transform) is an algorithm used to detect and describe local features in images. It was developed by David Lowe in 1999 and is widely used in computer vision applications, such as image matching, object recognition, and stitching. The key advantages of SIFT are its scale and rotation invariance, as well as its robustness to changes in illumination and viewpoint.
> 
> RootSIFT is an extension of SIFT proposed by Arandjelović and Zisserman in 2012. The main idea behind RootSIFT is to improve the performance of the original SIFT descriptor by applying a simple element-wise square root normalization to the descriptor values. This normalization helps to better differentiate between descriptors and improves matching performance, especially in scenarios where the distribution of descriptor distances is heavily skewed.
>
> The best scenarios for each method:
> **Standard SIFT**:
> General-purpose feature detection and description
> Applications where scale and rotation invariance are required
> Object recognition, image stitching, and 3D reconstruction
> **RootSIFT**:
> Improved performance in scenarios with skewed descriptor distance distributions
> Better differentiation between descriptors for more accurate matching
> Applications where a more discriminative descriptor is needed
>
> In summary, RootSIFT is an improvement over standard SIFT in terms of descriptor matching performance. It is especially useful in scenarios where the distribution of descriptor distances is heavily skewed, and a more discriminative descriptor is required. However, for general-purpose feature detection and description, the standard SIFT algorithm is still widely applicable.
> © ChatGPT4

## Similarity by machine learning model

```python
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def extract_features(img_array, model):
    return model.predict(img_array)

def calculate_similarity(feature_vector1, feature_vector2):
    return cosine_similarity(feature_vector1, feature_vector2)

# Load the pre-trained VGG16 model
model = VGG16(weights='imagenet', include_top=False, pooling='avg')

# Load and preprocess the images
image1_path = '1.png'
image2_path = '2.png'

image1 = load_and_preprocess_image(image1_path)
image2 = load_and_preprocess_image(image2_path)

# Extract high-level features from both images
feature_vector1 = extract_features(image1, model)
feature_vector2 = extract_features(image2, model)

# Calculate the cosine similarity between the feature vectors
similarity_score = calculate_similarity(feature_vector1, feature_vector2)

print('Similarity score:', similarity_score[0][0])
```

<pre>
Similarity score: 0.9361447
</pre>

### How it work?

It compare the similarities of the images is by using a pre-trained deep learning model `VGG16` to extract high-level features from both images and then calculate the cosine similarity between these features. Here's an example of how you can do this using Keras with TensorFlow backend:


#### What is VGG16 (From ChatGPT4)

VGG16 is a deep convolutional neural network architecture proposed by the Visual Geometry Group (VGG) at the University of Oxford. It was introduced by Karen Simonyan and Andrew Zisserman in their 2014 paper, "[Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556.pdf)" VGG16 contains 16 weight layers, including 13 convolutional layers and 3 fully connected layers. It was trained on the ImageNet dataset, which contains over 14 million images belonging to 1,000 different classes.

The primary purpose of VGG16 is for image classification, where it has achieved top performance in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC). However, its learned features can also be used for various other tasks, such as object detection, segmentation, and image similarity comparison, as demonstrated in the previous code example.

**Merits of using VGG16 for image similarity comparison:**

1. Pre-trained models: VGG16 is pre-trained on a large dataset (ImageNet), so it has already learned high-level features that can be useful for a wide range of tasks, including image similarity comparison.
2. Transfer learning: Since VGG16 has already learned high-level features, you can use it as a feature extractor for your images without having to train the model from scratch.
3. Robustness: VGG16 can extract features that are robust to variations in scale, rotation, and translation, making it suitable for comparing images with different sizes and orientations.

**Disadvantages of using VGG16 for image similarity comparison:**

1. Computational complexity: VGG16 has a large number of parameters, which can make it computationally expensive to use, especially on devices with limited computational resources. This can be a concern if you need to process a large number of images or require real-time processing.
2. Model size: The model size of VGG16 is relatively large (around 528 MB), which can be a concern if you have limited storage or need to deploy the model on edge devices.
3. Newer models available: Since the introduction of VGG16, several more advanced architectures have been proposed, such as ResNet, Inception, and EfficientNet, which can achieve better performance with less computational complexity and smaller model sizes.

In summary, while VGG16 can be used effectively for image similarity comparison, its computational complexity and model size might be a concern for certain applications or devices. In such cases, you may consider using more recent and efficient architectures like ResNet or EfficientNet for feature extraction.



```python
import cv2
import numpy as np

def align_images(image1, image2):
    h1, w1, _ = image1.shape
    h2, w2, _ = image2.shape
    aligned_image = np.zeros((max(h1, h2), w1 + w2, 3), dtype=np.uint8)
    aligned_image[:h1, :w1] = image1
    aligned_image[:h2, w1:] = image2
    return aligned_image

def draw_matching_lines(image1, image2, num_matches=50):
    akaze = cv2.AKAZE_create()
    keypoints1, descriptors1 = akaze.detectAndCompute(image1, None)
    keypoints2, descriptors2 = akaze.detectAndCompute(image2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)[:num_matches]

    aligned_image = align_images(image1, image2)

    for m in matches:
        pt1 = tuple(np.round(keypoints1[m.queryIdx].pt).astype(int))
        pt2 = tuple(np.round(keypoints2[m.trainIdx].pt).astype(int))
        pt2 = (pt2[0] + image1.shape[1], pt2[1])
        cv2.line(aligned_image, pt1, pt2, (0, 255, 0), 1)

    return aligned_image

# Load the images
image1_path = '1.png'
image2_path = '2.png'

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Draw lines between matching keypoints
aligned_image = draw_matching_lines(image1, image2, num_matches=50)

# Show the aligned images with matching lines
cv2.imshow('Aligned Images with Similar Regions', aligned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

= = I am not quirt accept this results 

![Image Similarities check ](https://s1.ax1x.com/2023/05/14/p9cYeyt.png)


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>









```python
import cv2
import os 
import itertools

Img_lst = os.listdir('Test')
pairs = list(itertools.combinations(Img_lst, 2))

for i in pairs:
  img1 = cv2.imread('Test/' + i[0])
  img2 = cv2.imread('Test/' + i[1])
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

  cv2.imwrite("Result/" + i[0] + '_' + i[1], result)
```
