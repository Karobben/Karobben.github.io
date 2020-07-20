---
title: "Lightening Img"
description: "Lightening Img"
url: pwx66f
---

# Lightening Img



```python
def contrast_img(img1, c, b):
    #https://blog.csdn.net/wsp_1138886114/article/details/82624534
    # 亮度就是每个像素所有通道都加上b
    rows, cols, channels = img1.shape
    # 新建全零(黑色)图片数组:np.zeros(img1.shape, dtype=uint8)
    blank = np.zeros([rows, cols, channels], img1.dtype)
    dst = cv2.addWeighted(img1, c, blank, 1-c, b)
    return dst

frame2=contrast_img( frame, Config['Lighten_R'], Config['Lighten_B'])
```

<br />More: [https://blog.csdn.net/weixin_38342946/article/details/100071255](https://blog.csdn.net/weixin_38342946/article/details/100071255)
 
