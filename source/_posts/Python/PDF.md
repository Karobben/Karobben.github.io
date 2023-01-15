---
title: "PDF"
description: "PDF"
url: pdf2
date: 2020/01/22
toc: true
excerpt: "Manipulate PDF with Python"
tags: [Python, PDF]
category: [Python, Scripting, Module]
cover: 'https://res.cloudinary.com/practicaldev/image/fetch/s--I4vwWL5a--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/biqym5siaf3o80dzetie.png'
covercopy: '<a href="https://dev.to/stokry/add-watermark-to-your-pdf-file-with-python-3ijo">© Stokry</a>'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## PYPDF2


### Read & Write

```python
from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = 'read.pdf'
writeFile = 'write.pdf'

pdfReader = PdfFileReader(open(readFile, 'rb'))
pdfWriter.write(open(writeFile, 'wb'))
```

### Pick First two Page

```python
from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2

readFile = 'SA.pdf'
writeFile = 'write.pdf'

pdfWriter = PyPDF2.PdfFileWriter()

pdfReader = PdfFileReader(open(readFile, 'rb'))
pdfWriter.write(open(writeFile, 'wb'))

for page in range(2):
        pageObj = pdfReader.getPage(page)
        pdfWriter.addPage(pageObj)

newFile = open(writeFile,'wb')
pdfWriter.write(newFile)

newFile.close()

```


#### 2.1 Double the Pages

```python
from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2

readFile = 'SA.pdf'
writeFile = 'write.pdf'

pdfWriter = PyPDF2.PdfFileWriter()

pdfReader = PdfFileReader(open(readFile, 'rb'))
pdfWriter.write(open(writeFile, 'wb'))

for page in range(2):
        pageObj = pdfReader.getPage(page)
        pdfWriter.addPage(pageObj)
        pageObj = pdfReader.getPage(page)
        pdfWriter.addPage(pageObj)

newFile = open(writeFile,'wb')
pdfWriter.write(newFile)

newFile.close()
```


![NYakNR.jpg](https://s1.ax1x.com/2020/06/22/NYakNR.jpg)<br />

### 3. Water Mark

```python
cm =1
def create_watermark(content):
    #默认大小为21cm*29.7cm
    c = canvas.Canvas('mark.pdf', pagesize = (30*cm, 30*cm))   
    c.translate(10*cm, 10*cm) #移动坐标原点(坐标系左下为(0,0)))                                                                                                                             
    #c.setFont('song',22)#设置字体为宋体，大小22号
    c.setFillColorRGB(0.5,0.5,0.5)#灰色                                                                                                                         
    c.rotate(45)#旋转45度，坐标系被旋转
    c.drawString(-7*cm, 0*cm, content)
    c.drawString(7*cm, 0*cm, content)
    c.drawString(0*cm, 7*cm, content)
    c.drawString(0*cm, -7*cm, content)                                                                                                                              
    c.save()#关闭并保存pdf文件
```

![NYaFE9.jpg](https://s1.ax1x.com/2020/06/22/NYaFE9.jpg)
```python
from reportlab.pdfgen import canvas

cm =1
def create_watermark(W, H):
    #默认大小为21cm*29.7cm
    c = canvas.Canvas('mark.pdf', pagesize = (W, H))   
    c.translate(10*cm, 10*cm) #移动坐标原点(坐标系左下为(0,0)))                                                                                                                             
    #c.setFont('song',22)#设置字体为宋体，大小22号
    #c.setFillColorRGB(0.5,0.5,0.5)#灰色                                                                                                                         
    #c.rotate(45)#旋转45度，坐标系被旋转
    #c.drawString(-7*cm, 0*cm, content)
    #c.drawString(7*cm, 0*cm, content)
    #c.drawString(0*cm, 7*cm, content)
    #c.drawString(0*cm, -7*cm, content)
    #指定描边的颜色
    #c.setStrokeColorRGB(0, 1, 0)
    #指定填充颜色
    c.setFillColorRGB(255, 255, 255)
    #画一个矩形
    c.rect(0, 0, W, H/2 -10 , fill=1)
    c.save()#关闭并保存pdf文件

create_watermark(580,820)
add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
```

```python
##encoding=utf-8
##author: walker
##date: 2014-03-18
##function:给pdf添加水印
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
##所有路径为绝对路径


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(pdf_file_in)                                                                                
    # PDF文件被加密了
    if pdf_input.getIsEncrypted():
        print( '该PDF文件被加密了.')
        # 尝试用空密码解密
        try:
            pdf_input.decrypt('')
        except Exception or e:
            print( '尝试用空密码解密失败.')
            return False
        else:
            print( '用空密码解密成功.')
    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()
    #读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'))
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()   #压缩内容
        pdf_output.addPage(page)
    return pdf_output


PDF1 = add_watermark("GRE阅读白皮书.pdf", pdf_file_mark, pdf_file_out)
PDF2 = add_watermark("GRE阅读白皮书.pdf", pdf_file_mark2, pdf_file_out)

pdf_output = PdfFileWriter()
for i in range(PDF2.getNumPages()):
    page = PDF1.getPage(i)
    pdf_output.addPage(page)
    page = PDF2.getPage(i)
    pdf_output.addPage(page)

newFile = open(pdf_file_out,'wb')
pdf_output.write(newFile)
newFile.close()
```




### Add Page number
```python
###!/usr/bin/env python3
## -*- coding:utf-8 -*-
## 本示例使用两个第三方库来实现为PDF文件添加文字水印
## 这两个库是pyPdf和reportlab
## 使用的Python版本是Python 3.7
## origing from https://www.cnblogs.com/kayb/p/10846341.html
## 作者：小磊
##链接：https://www.zhihu.com/question/19628465/answer/353504051
##来源：知乎
##著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

##!/usr/bin/env python3
## -*- coding: utf-8 -*-

helpDoc = '''
Add Page Number to PDF file with Python
Python 给 PDF 添加 页码
usage:
    python addPageNumberToPDF.py [PDF path]
require:
    pip install reportlab pypdf2
    Support both Python2/3, But more recommend Python3

tips:
    * output file will save at pdfWithNumbers/[PDF path]_page.pdf
    * only support A4 size PDF
    * tested on Python2/Python3@ubuntu
    * more large size of PDF require more RAM
    * if segmentation fault, plaese try use Python 3
    * if generate PDF document is damaged, plaese try use Python 3

Author:
    Lei Yang (ylxx@live.com)

GitHub:
    https://gist.github.com/DIYer22/b9ede6b5b96109788a47973649645c1f
'''
print(helpDoc)

import reportlab
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from PyPDF2 import PdfFileWriter, PdfFileReader

path = 'test.pdf'

def createPagePdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1,num+1):
        c.drawString((210//2)*mm, (4)*mm, str(i))
        c.showPage()
    c.save()
    return
    with open(tmp, 'rb') as f:
        pdf = PdfFileReader(f)
        layer = pdf.getPage(0)
    return layer


if __name__ == "__main__":
    pass
    import sys,os
    if len(sys.argv) == 1:
        if not os.path.isfile(path):
            sys.exit(1)
    else:
        path = sys.argv[1]
    base = os.path.basename(path)
    tmp = "__tmp.pdf"
    batch = 10
    batch = 0
    output = PdfFileWriter()
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f,strict=False)
        n = pdf.getNumPages()
        if batch == 0:
            batch = -n
        createPagePdf(n,tmp)
        if not os.path.isdir('pdfWithNumbers/'):
            os.mkdir('pdfWithNumbers/')
        with open(tmp, 'rb') as ftmp:
            numberPdf = PdfFileReader(ftmp)
            for p in range(n):
                if not p%batch and p:
                    newpath = path.replace(base, 'pdfWithNumbers/'+ base[:-4] + '_page_%d'%(p//batch) + path[-4:])
                    with open(newpath, 'wb') as f:
                        output.write(f)
                    output = PdfFileWriter()
                print('page: %d of %d'%(p, n))
                page = pdf.getPage(p)
                numberLayer = numberPdf.getPage(p)
                page.mergePage(numberLayer)
                output.addPage(page)
            if output.getNumPages():
                newpath = path.replace(base, 'pdfWithNumbers/' + base[:-4] + '_page_%d'%(p//batch + 1)  + path[-4:])
                with open(newpath, 'wb') as f:
                    output.write(f)
        os.remove(tmp)
```

### Access the size of pages

Reference: [SUN_SU3 2020](https://blog.csdn.net/u013546508/article/details/104674374)

```python
def pdf_size(path, page =0):
    pdf = PdfFileReader(open(path, 'rb'))
    page_1 = pdf.getPage(page)
    if page_1.get('/Rotate', 0) in [90, 270]:
        return page_1['/MediaBox'][2], page_1['/MediaBox'][3]
    else:
        return page_1['/MediaBox'][3], page_1['/MediaBox'][2]

height, width = pdf_size(path)
print('height: %s, width: %s'%(height, width))
```

<pre style="background-color:black; color:white">
height: 767.06, width: 575.29
</pre>

This is the size of PDF file made by **Sony DPT-1**

### Crop the pages of PDF

For doing this, you need to know the **size** of your pdf and the **width/height ratio**.

```python
File = "Improving_Reading_Skills.pdf"

height, width = pdf_size(File,20) # Function from above
C_width =  round(float(690)/(767.06/575.29),2)

with open(File, "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()
    # number
    numPages = input1.getNumPages()
    print ("document has %s pages." % numPages)
    # Start
    for i in range(10):
        page = input1.getPage(i)
        print( page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        # (x, y) from left to right, from botton to top
        #page.trimBox.lowerLeft = (400, 700)
        page.cropBox.lowerLeft = (500, 600)
        page.cropBox.upperRight = (100, 200)
        output.addPage(page)
    # End
    with open("out.pdf", "wb") as out_f:
        output.write(out_f)
```

![python pdf crop](https://z3.ax1x.com/2021/07/27/W4sAld.png)

When left and right page is different

```python
with open(File, "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()
    # number
    numPages = input1.getNumPages()
    print ("document has %s pages." % numPages)
    # Start
    for i in range(numPages):
        page = input1.getPage(i)
        print( page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        # (x, y) from left to right, from botton to top
        #page.trimBox.lowerLeft = (400, 700)
        if i%2 == 0:
          page.cropBox.lowerLeft = (540, 680)
          page.trimBox.lowerLeft = (540, 680)
          page.cropBox.upperRight = (60, 40)
          page.trimBox.upperRight = (60, 40)
        if i%2 == 1:
          page.cropBox.lowerLeft = (580, 680)
          page.trimBox.lowerLeft = (580, 680)
          page.cropBox.upperRight = (100, 40)
          page.trimBox.upperRight = (100, 40)
        output.addPage(page)
    # End
    with open("out.pdf", "wb") as out_f:
        output.write(out_f)

```

### Extract images from PDF

Reference:[Labo; 2016](https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python)
```python
from PIL import Image

from PyPDF2 import PdfReader

def extract_image(pdf_file_path):
    reader = PdfReader(pdf_file_path)
    page = reader.pages[0]
    x_object = page["/Resources"]["/XObject"].getObject()

    for obj in x_object:
        if x_object[obj]["/Subtype"] == "/Image":
            size = (x_object[obj]["/Width"], x_object[obj]["/Height"])
            data = x_object[obj].getData()
            if x_object[obj]["/ColorSpace"] == "/DeviceRGB":
                mode = "RGB"
            else:
                mode = "P"

            if x_object[obj]["/Filter"] == "/FlateDecode":
                img = Image.frombytes(mode, size, data)
                img.save(obj[1:] + ".png")
            elif x_object[obj]["/Filter"] == "/DCTDecode":
                img = open(obj[1:] + ".jpg", "wb")
                img.write(data)
                img.close()
            elif x_object[obj]["/Filter"] == "/JPXDecode":
                img = open(obj[1:] + ".jp2", "wb")
                img.write(data)
                img.close()
```

## pdfplumber

### Read

```python
import pdfplumber

path = 'MMR.pdf'
pdf =  pdfplumber.open(path)
```

Reference: [SUN_SU3 2020](https://blog.csdn.net/u013546508/article/details/104674374)

```python
import pdfplumber

path = 'MMR.pdf'

def run(path):
    with pdfplumber.open(path) as pdf:
        page_1 = pdf.pages[0]
        return page_1.height, page_1.width

height, width = run(path)
print('height: %s, width: %s'%(height, width))
```

<pre style="background-color:black; color:white">
height: 841.920, width: 595.200
</pre>


```python
import cv2
import numpy as np
from PIL import Image
from pandas import pd
import seaborn as sns
import matplotlib.pyplot as plt

img = cv2.imread('I0.jpg')
# remove usless infor
def Get_data(img):
    # Main string
    img[img[:,:,2]<250] = 0
    img[img[:,:,1]>50] = 0
    img[img[:,:,0]<60] = 0
    return img

def Get_box(img):
    # Main string
    img[np.abs(img[:,:,2]-135)>=1] = 255
    img[np.abs(img[:,:,1]-135)>=1] = 255
    img[np.abs(img[:,:,0]-135)>=1] = 255
    return img

img_show = Get_data(img)
img_show = cv2.resize(img_show, (2382,1936))
while(True):
   cv2.imshow('image',img_show)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break

img_show = cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)
colourImg = Image.fromarray(img_show)

colourPixels = colourImg.convert("RGB")
colourArray = np.array(colourPixels.getdata()).reshape(colourImg.size + (3,))
indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))


df = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])
df_lines = df[df.red!=0]
df_line_1 = df_lines[df_lines.y>=2000]
df_line_1 = df_line_1.sort_values(by=['x'])
plt.plot(df_line_1.x, df_line_1.y, 'ro')
plt.show()
```

( [])
(255,50,51)
