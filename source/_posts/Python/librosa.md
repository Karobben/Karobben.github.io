---
toc: true
url: librosa
covercopy: © Dhana Design
priority: 10000
date: 2021-09-18 16:56:59
title: "librosa for sound track| Python"
ytitle: "libroa 库来做声音处理"
description: "librosa library for sound track processing in python"
excerpt: "librosa library for sound track processing in python"
tags: [Python]
category: [Python]
cover: "https://image.shutterstock.com/image-vector/modern-sound-wave-equalizer-vector-600w-1711177093.jpg"
thumbnail: "https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA"
---

## python
Cite: [叁公子KCN; 2019](http://nladuo.github.io/2019/08/31/%E4%BD%BF%E7%94%A8Python%E5%AF%B9%E9%9F%B3%E9%A2%91%E8%BF%9B%E8%A1%8C%E7%89%B9%E5%BE%81%E6%8F%90%E5%8F%96/)

```python
import librosa

import matplotlib.pyplot as plt
import librosa.display

File = "input.mkv"

x , sr = librosa.load(File, sr=8000)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x[:10000], sr=sr)
plt.show()
```


## ffmpeg

Cite: [dennyyoung](https://zhuanlan.zhihu.com/p/97914917)

```bash
# Video split
ffmpeg -y -ss 0 -t 3 -i Function.mkv -c:v libx264 -c:a copy  123.mkv

# Video merge
ffmpeg -y -i filename -i filename2 -vcode copy -acodec copy
```
