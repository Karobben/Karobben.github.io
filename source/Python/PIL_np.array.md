---
title: "PIL, np.array"
description: "PIL, np.array"
url: lb1xtn2
---

# PIL, np.array

<a name="F4075"></a>
### PIL.Image转换成OpenCV格式


```python
#reference https://blog.csdn.net/dcrmg/java/article/details/78147219
import cv2
from PIL import Image
import numpy

image = Image.open("plane.jpg")
image.show()
img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV",img)
cv2.waitKey()
```
