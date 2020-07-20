---
title: "wordcloud"
description: "wordcloud"
url: wordcloud2
---
# wordcloud

![NY0CDS.png](https://s1.ax1x.com/2020/06/22/NY0CDS.png)

```python
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

# Read the whole text.
text = open('alice.txt').read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open("alice_mask.png"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white",
               max_words=200, mask=alice_mask,
               max_font_size=200, # 根据你的图片大小定义
               stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file("alice.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()


# remove punctuation
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
