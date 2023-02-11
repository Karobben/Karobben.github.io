---
toc: true
url: ocr
covercopy: <a href="https://mariam123.medium.com/overview-of-ocr-c00699caa2f4">© Mariam Y</a>
priority: 10000
date: 2022-08-02 10:06:23
title: "Pytessaract: OCR Tool in Python"
ytitle: ""
description: "Extract texts from img"
excerpt: "Extract texts from img"
tags: [Python, orc]
category: [Python]
cover: "https://miro.medium.com/max/700/1*CBkz7f_KjNh_wVuqLp-m0A.png"
thumbnail: "https://miro.medium.com/max/700/1*CBkz7f_KjNh_wVuqLp-m0A.png"
---

## Pytessaract: ORC Tool in Python

### Prepare: Tesseract

[Tesseract install manual](https://tesseract-ocr.github.io/tessdoc/Compiling.html#android)

In Linux

```bash
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

# usage:
tesseract 123.pmg 123.txt
```

### Pytessaract

Reference: [© Sandun Amarathunga](https://medium.com/@sandun.amarathunga/extract-text-from-files-and-images-using-pytessaract-and-opencv-aa26b615a7fb)
```bash
pip install Pytessaract
```

```python
import cv2
import pytesseract

img = cv2.imread(“images/002.png”) # read an image

text = pytesseract.image_to_string(img) # extract text
print(text)
```

## Other languages support

[Github](https://github.com/tesseract-ocr/tessdata/)

When you don't have the language model:
```bash
tesseract -l chi_sim test.png  test.txt
```

<pre>
Error opening data file /usr/share/tesseract-ocr/4.00/tessdata/chi_sim.traineddata
Please make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory.
Failed loading language 'chi_sim'
Tesseract couldn't load any languages!
Could not initialize tesseract.
</pre>

```bash
cd /usr/share/tesseract-ocr/4.00/
mv tessdata tessdata_bc
git clone https://github.com/tesseract-ocr/tessdata.git
```
