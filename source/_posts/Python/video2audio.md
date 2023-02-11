---
toc: true
url: video2audio
covercopy: <a href="http://doc.moviepy.com.cn/index.html#document-2_MoviePy%E5%85%A5%E9%97%A8/index">© moviepy</a>
priority: 10000
date: 2021-04-23 11:30:11
title: "Video to audio | Python |mp4 to mp3"
ytitle: "视频转音频 Python| MP4 转 MP3"
description: "Python script for extract the soundtrack from videos; moviepy, ffmpy3"
excerpt: "Python script for extract the soundtrack from videos: moviepy, ffmpy3"
tags: [Video, Audio]
category: [Python, Scripting, Practice]
cover: "http://zulko.github.io/moviepy/_images/explanations.jpeg"
thumbnail: "http://zulko.github.io/moviepy/_images/explanations.jpeg"
---

## Quick Start: moviepy

Cite: [taoquns 2019](https://www.cnblogs.com/taoquns/p/11936800.html)

```python
# pip install moviepy
from moviepy.editor import *

video = VideoFileClip('test.mp4')
audio = video.audio
audio.write_audiofile('test.mp3')
```

### Requirement

<pre>
moviepy
decorator
tqdm
requests
numpy
imageio
pillow
imageio_ffmpeg
</pre>


## ffmpy3

Cite: [(c) Jumping boy;  2019](https://blog.csdn.net/qq_40962368/article/details/91355429)

```python

from ffmpy3 import FFmpeg
ff = FFmpeg(inputs={'周笔畅-最美的期待(伴奏版).mp4': None},
            outputs={'output.mp3': None})
print(ff.cmd)
ff.run()
```
