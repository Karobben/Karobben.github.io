---
title: "PIL image to np.array"
description: "PIL, np.array"
url: lb1xtn2
date: 2020/01/22
toc: true
excerpt: "The maintainers of Pillow and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use."
tags: [Python, Image]
category: [Python, Scripting, Practice]
cover: 'https://miro.medium.com/v2/resize:fit:720/format:webp/1*PIpjPTlcrDyXLl2fDv34bA.png'
covercopy: '<a href="https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64">© Claire D. Costa</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## PIL, np.array

<a name="F4075"></a>
#### PIL.Image转换成OpenCV格式


```python
##reference https://blog.csdn.net/dcrmg/java/article/details/78147219
import cv2
from PIL import Image
import numpy

image = Image.open("plane.jpg")
image.show()
img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV",img)
cv2.waitKey()
```
