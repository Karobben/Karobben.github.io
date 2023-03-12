---
title: "wordcloud"
description: "wordcloud"
url: wordcloud2
date: 2020/06/23
toc: true
excerpt: "Wordcloud is a data visualization technique used to represent text data in a graphical format. In Python, the wordcloud library is used to generate wordclouds. It takes a text file or a string of text as input, and generates an image where the size of each word is proportional to its frequency in the input text. <a title='GhatGPT'>Who said this?</a>"
tags: [Python, WordCloud, Plot]
category: [Python, Plot]
cover: 'https://s1.ax1x.com/2020/06/22/NY0CDS.png'
thumbnail: 'https://s1.ax1x.com/2020/06/22/NY0CDS.png'
priority: 10000
covercopy: © Karobben
---


The color palette from the R package `worldcloud2` is very awesome. But it has some bugs. I can not set the mask for the world cloud. In python, this package is much user-friendly.

To be notice, the mask picture is very important. You can only use the rgb format. The picture has "0, 0, 0" for the background, "255, 255, 255" for the background. rgbi format is not supported even if it is very similar to rgb.

```python
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

## Read the whole text.
text = open('tmp.txt').read()

## read the mask image
## taken from
## http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open("/home/ken/Downloads/cloud.png"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white",
               max_words=512, mask=alice_mask,
               max_font_size=10, # 根据你的图片大小定义
               stopwords=stopwords)
## generate word cloud
wc.generate(text)

## store to file
wc.to_file("alice.png")

## show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()


## remove punctuation
Special = "”"
TT = text.translate(str.maketrans(' ', ' ', string.punctuation))
TT = TT.translate(str.maketrans('', '', string.whitespace[1:]))
TT = TT.translate(str.maketrans('', '', string.digits))
TT = TT.lower()
TT = TT.split(" ")
TT = list(set(TT))
for i in string.ascii_lowercase:
    try:
        TT.remove(i)
    except:
        print(i)

f = open("list",'a')
for i in TT:
    f.write(i+'\n')
f.close()
```


[https://amueller.github.io/word_cloud/auto_examples/colored.html#colored-py](https://amueller.github.io/word_cloud/auto_examples/colored.html#colored-py)
