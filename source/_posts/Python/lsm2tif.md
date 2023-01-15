---
toc: true
url: librosa
covercopy: © Dhana Design
priority: 10000
date: 2021-09-18 16:56:59
title: "Python: lsm image to tif image"
ytitle: "Python: lsm image to tif image"
description: "Conver the image from lsm into tif format"
excerpt: "Conver the image from lsm into tif format"
tags: [Python]
category: [Python]
cover: "https://image.shutterstock.com/image-vector/modern-sound-wave-equalizer-vector-600w-1711177093.jpg"
thumbnail: "https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA"
---

```python
import tifffile, cv2, os
List_dir = "lsm/"
out_dir = "out/"
LSM_list = [i for i in os.listdir(List_dir) if ".lsm" in i]
LSM_list[0]

for i in LSM_list:
    A = tifffile.imread(List_dir + i)
    #fig, ax = plt.subplots(figsize=(10, 10))
    for ch_id in range(A.shape[1]):
        Pic = A[:,ch_id,:,:]
        tifffile.imsave(out_dir + i+str(ch_id)+".tif", Pic)
```
