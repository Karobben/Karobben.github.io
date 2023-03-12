---
title: "用Python快速批量压缩图片"
description: "用Python快速批量压缩图片"
url: xres0q
date: 2020/10/25
toc: true
excerpt: "用Python快速批量压缩图片"
tags: [Python, Image]
category: [Python, Scripting, Practice]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## 用Python快速批量压缩图片

```flow
st=>start: Python read
op1=>operation: Target(s)
c1=>condition: Print inf
c2=>condition: File/Directory
c3=>condition: Single File
op2=>operation: File
op3=>operation: Files
op4=>operation: Risze
op5=>operation: 添加代码
op5=>operation: 初始化评论
e=>end: 完成!! Enjoy！

st->op1
op1->c1
c1(yes,right)->c2
c1(no)->e
c2(yes,right)->c3
c3(yes)->op2
c3(no)->op3
op2(left)->op4
op3->op4
c2(no)->op4
op4(left)->e
```
<a name="TmQUo"></a>
## Structure
<a name="4K9LJ"></a>
### 1 Arguments

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')  #输入文件
parser.add_argument('-o','-O','--output',default = "OUT")  #输出文件
parser.add_argument('-r','-R','--ratio', type = int,default = 2)  #resize ratio
parser.add_argument('-w','-W','--width',default = "NA")  #resize by width
parser.add_argument('-t','-T','--height',default = "NA")  #resize by Height

##获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
R_img = args.ratio
W_img = args.width
H_img = args.height
```

<a name="i7RXm"></a>
### 2 File/Director Judgement

```python
import os

def FD_judge(path):
  result = ""
  if "*" in path:
    result = "Files"
  elif os.path.isdir(path):
    result = "Directory"
  elif os.path.isfile(path):
    result = "File"
  else:
    result = "path is incorrect"
  return result


print(FD_judge(INPUT))
Typ_in = FD_judge(INPUT)
```

<a name="E5sLS"></a>
### 3 Resize Determine

```python
import PIL.Image as Image

def Calc_WH(w,h,W_img,H_img,R_img):
  if W_img != "NA" and H_img == "NA":  #Resize by Width
    print('Resize by Width')
    R = w/ int(W_img)
    w=int(w/R)
    h=int(h/R)
  elif H_img != "NA" and W_img == "NA":  #Resize by Height
    print("Resize by Height")
    R = h/ int(H_img)
    w=int(w/R)
    h=int(h/R)
  elif H_img != "NA" and W_img != "NA":  #Resize by Width and Height
    print('Resize by Width and Height')
    w=int(W_img)
    h=int(H_img)
  else:
    print("Resize by ratio, R="+str(R_img))
    w=int(w/R_img)
    h=int(h/R_img)
  return w,h
```

<a name="8huLH"></a>
### 4 Resize function

```python
def Resize(path,W_img,H_img,R_img):
  Img=Image.open(path)
  w,h=Img.size
  w,h=Calc_WH(w,h,W_img,H_img,R_img)
  Img_out=Img.resize((w,h),Image.ANTIALIAS)
  return Img_out


```

<a name="e03og"></a>
### 5 logic

```python
if Typ_in=="File" and OUTPUT == "OUT":
  OUTPUT = "Re_" + INPUT
elif Typ_in=="File" and OUTPUT != "OUT":
  OUTPUT = OUTPUT
else:
  if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)
  OUTPUT = OUTPUT +"/"
```

test result:<br />
![Ns99MR.png](https://s1.ax1x.com/2020/06/26/Ns99MR.png)


<a name="O7xWv"></a>
## Whole Scripts:[link](https://www.yuque.com/liuwenkan/pwh0c8/pwm2gg)

<a name="klIGH"></a>
## Result
<a name="Z32ZF"></a>
## Single file
Reading img infor With package "imagemagick". If you doesn't have this lib, for debian, please execute:<br />**sudo apt install ****imagemagick

<a name="0HsKy"></a>
### Running with default argument
```bash
../test.py -i 1.png
##Outfile: Re_1.png

identify 1.png Re_1.png

## 1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.010
## Re_1.png PNG 1333x913 1333x913+0+0 8-bit sRGB 203679B 0.000u 0:00.000

../test.py -i 1.png -o my.png
##Outfile: my.png

identify 1.png my.png
##1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
##my.png PNG 1333x913 1333x913+0+0 8-bit sRGB 203679B 0.000u 0:00.000
```

<a name="jFLlM"></a>
### Resize by width

```bash
../test.py -i 1.png -w 300

identify 1.png Re_1.png
##1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
##Re_1.png PNG 300x205 300x205+0+0 8-bit sRGB 27338B 0.000u 0:00.000
```

<a name="Z1Pwd"></a>
### Resize by Height

```bash
../test.py -i 1.png -t 300

identify 1.png Re_1.png
##1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
##Re_1.png PNG 437x300 437x300+0+0 8-bit sRGB 44276B 0.000u 0:00.000
```

<a name="YQmGR"></a>
### Resize by Ratio

```bash
../test.py -i 1.png -r 10

identify 1.png Re_1.png
##1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
##Re_1.png PNG 266x182 266x182+0+0 8-bit sRGB 23398B 0.000u 0:00.000
```

<a name="3sPlw"></a>
## Resize by Height and Width

```bash
../test.py -i 1.png  -t 200 -w 10

##1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
##Re_1.png PNG 10x200 10x200+0+0 8-bit sRGB 2186B 0.000u 0:00.000
```

<a name="QHhlD"></a>
## Resize Multiple files
<a name="1TAZK"></a>
### Resize multiple file

```bash
../test.py -i "*.png"
```
All result will be printed to "OUT" director. 

```bash
../test.py -i OUT -o test -w 100
```
reading all pictures from OUT directory, and all result where out put to test file

<a name="BKexU"></a>
## update
<a name="yFwCg"></a>
### Print information
2020/2/9
Adding arguments

```python
parser.add_argument('-inf','-INF','--infor',default = "None")    #resize by Height

INFORM = args.infor

```

<a name="g4W1b"></a>
#### Def functions：
```python
def Resize_loop():
    if Typ_in == "File":
        Result = Resize(INPUT,W_img,H_img,R_img)
        Result.save(OUTPUT, quality=Quality)
    elif Typ_in == "Files":
        List = os.popen("ls "+INPUT).read().split('\n')[:-1]
        for i in List:
            Result = Resize(i,W_img,H_img,R_img)
            Result.save(OUTPUT + i.split('/')[-1], quality=Quality)
    elif Typ_in == "Directory":
        List = os.popen("ls "+INPUT+"/*").read().split('\n')[:-1]
        for i in List:
            Result = Resize(i,W_img,H_img,R_img)
            Result.save(OUTPUT+i.split('/')[-1], quality=Quality)

def IMG_inf(INPUT):
    Space = size_format(getsize(INPUT))
    Img = Image.open(INPUT)
    Name    = Img.filename
    Format  = Img.format_description
    Mode    = Img.mode

    try:
        Bit     = "bit:" + str(Img.bits)
    except:
        Bit     = "bit:NA"
    try:
        Dpi     = "dpi:" + 'x'.join([str(x) for x in Img.info['dpi']])
    except:
        Dpi     = "dpi: NA"
    Size    = "size:" + 'x'.join([str(x) for x in Img.size])
    Result = Name +"\t"+"    ".join([Space, Size, Dpi, Format,Mode,Bit])
    return Result
```

<a name="DUklk"></a>
#### Logic:
```python
if INFORM == "None": # Resize
    Typ_in = FD_judge(INPUT)
    print(Typ_in)
    OUTPUT = OUT_fig(INPUT,OUTPUT)
    Resize_loop()
else:  # img information
    Typ_in = FD_judge(INPUT)
    if Typ_in == "File":
        print(IMG_inf(INPUT))
    elif Typ_in == "Files":
        #List = os.popen("ls "+INPUT).read().split('\n')[:-1]
        List = os.popen("ls "+INPUT).read().split('\n\n')[0].split('\n')[:-1]
        for i in List:
            print(IMG_inf(i))
    elif Typ_in == "Directory":
        List = os.popen("ls "+INPUT+"/*").read().split('\n\n')[0].split('\n')[:-1]
        for i in List:
            print(IMG_inf(i))
```

<a name="JZkRM"></a>
#### Usage:

```bash
Imresize.py -i "*" -inf 1
```

output:
![NspOaT.png](https://s1.ax1x.com/2020/06/26/NspOaT.png)

**Details**:

| Name | Size | Width&height | DPI | format | mode | Bit |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| bash.jpg | 16.8KB  | size:800x450 | dpi: NA | JPEG (ISO 10918) | RGB | bit:8 |







