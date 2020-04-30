---
url: xres0q
---

# 用Python快速批量压缩图片


![](https://cdn.nlark.com/yuque/__graphviz/7876f967a606f15eb5f012c748a84d92.svg#lake_card_v2=eyJjb2RlIjoiZGlncmFwaCBGIHtcbiAgICByYW5rZGlyID0gQTtcbiAgICBlZGdlIFtzdHlsZT1zb2xpZF07XG4gICAgbm9kZSBbc3R5bGU9ZmlsbGVkLCBmb250PUNvdXJpZXJdO1xuXG4gICAgc3ViZ3JhcGggQiB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBTdGFydCBbbGFiZWwgPSBcIlB5dGhvbiByZWFkXCIsIHNoYXBlID0gYm94LCBmaWxsY29sb3IgPSBcIiNGRjAwMDBcIiBdO1xuICAgICAgICBDb24xIFtsYWJlbCA9IFwiVGFyZ2V0KHMpXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMSwgc2l6ZSA9IDNdO1xuXHRcdFx0XHRDb24yIFtsYWJlbCA9IFwiUHJpbnQgaW5mXCIsIHNoYXBlID0gZGlhbW9uZCwgY29sb3IgPSBncmVlbiwgc2l6ZSA9IDNdO1xuICAgICAgfVxuXG4gICAgc3ViZ3JhcGggQyB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBGaWxlIFtsYWJlbCA9IFwiRmlsZShzKVwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuXHRcdFx0XHRKdWRnZSBbbGFiZWwgPSBcIkZpbGUvRGlyZWN0b3JcIiwgc2hhcGUgPSBkaWFtb25kLCBjb2xvciA9IGdyZWVuXTtcbiAgICB9XG4gICAgc3ViZ3JhcGggRCB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBTX0ZpbGUgW2xhYmVsID0gXCJTaW5nbGUgRmlsZVwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuICAgICAgICBNX0ZpbGUgW2xhYmVsID0gXCJNdWx0aXBsZSBGaWxlc1wiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuICAgIH1cbiAgICBzdWJncmFwaCBFIHtcbiAgICAgICAgcmFuayA9IHNhbWU7XG4gICAgICAgIFJlc2l6ZSBbbGFiZWwgPSBcIlJlc2l6ZVwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuICAgICB9XG4gICAgc3ViZ3JhcGggRSB7XG4gICAgICAgIHJhbmsgPSBzYW1lO1xuICAgICAgICBFbmQgICBbbGFiZWwgPSBcIk91dCBwdXRcIiAgICAgICwgc2hhcGUgPSBib3gsIGNvbG9yID0gY29yYWxdO1xuICAgICB9XG5cbiAgICBTdGFydFx0LT4gQ29uMVxuXHRcdENvbjFcdC0-IENvbjJcblx0XHRDb24yXHQtPiBKdWRnZVx0W2xhYmVsID0gXCJOb25lXCJdXG4gICAgSnVkZ2VcdC0-IEZpbGVcdFtsYWJlbCA9IFwiRmlsZVwiXVxuXHRcdFxuXHRcdEZpbGVcdC0-XHRTX0ZpbGVcblx0XHRGaWxlXHQtPlx0TV9GaWxlXG5cdFx0XG5cdFx0SnVkZ2VcdC0-IFJlc2l6ZVx0W2xhYmVsID0gXCJEaXJjdG9yXCJdXG5cdFx0e1NfRmlsZSxNX0ZpbGV9XHQtPiBSZXNpemVcblx0XHRcblx0XHRDb24yXHQtPiBFbmRcdFtsYWJlbCA9IFwiUHJpbnQgb3V0XCJdXG5cdFx0UmVzaXplXHQtPlx0RW5kXG59IiwidHlwZSI6ImdyYXBodml6IiwiaWQiOiJkTktWTSIsInVybCI6Imh0dHBzOi8vY2RuLm5sYXJrLmNvbS95dXF1ZS9fX2dyYXBodml6Lzc4NzZmOTY3YTYwNmYxNWViNWYwMTJjNzQ4YTg0ZDkyLnN2ZyIsImNhcmQiOiJkaWFncmFtIn0=)
<a name="TmQUo"></a>
# Structure
<a name="4K9LJ"></a>
## 1 Arguments

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')	#输入文件
parser.add_argument('-o','-O','--output',default = "OUT")	#输出文件
parser.add_argument('-r','-R','--ratio', type = int,default = 2)	#resize ratio
parser.add_argument('-w','-W','--width',default = "NA")	#resize by width
parser.add_argument('-t','-T','--height',default = "NA")	#resize by Height

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
R_img = args.ratio
W_img = args.width
H_img = args.height
```

<a name="i7RXm"></a>
## 2 File/Director Judgement

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
## 3 Resize Determine

```python
import PIL.Image as Image

def Calc_WH(w,h,W_img,H_img,R_img):
	if W_img != "NA" and H_img == "NA":	#Resize by Width
		print('Resize by Width')
		R = w/ int(W_img)
		w=int(w/R)
		h=int(h/R)
	elif H_img != "NA" and W_img == "NA":	#Resize by Height
		print("Resize by Height")
		R = h/ int(H_img)
		w=int(w/R)
		h=int(h/R)
	elif H_img != "NA" and W_img != "NA":	#Resize by Width and Height
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
## 4 Resize function

```python
def Resize(path,W_img,H_img,R_img):
	Img=Image.open(path)
	w,h=Img.size
	w,h=Calc_WH(w,h,W_img,H_img,R_img)
	Img_out=Img.resize((w,h),Image.ANTIALIAS)
	return Img_out


```

<a name="e03og"></a>
## 5 logic

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

test result:<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580108042076-b38a3770-2605-4623-98d1-4699d31470cf.png#align=left&display=inline&height=244&name=image.png&originHeight=244&originWidth=429&size=36702&status=done&style=none&width=429)



<a name="O7xWv"></a>
# Whole Scripts:[link](https://www.yuque.com/liuwenkan/pwh0c8/pwm2gg)

<a name="klIGH"></a>
# Result
<a name="Z32ZF"></a>
# Single file
Reading img infor With package "imagemagick". If you doesn't have this lib, for debian, please execute:<br />**sudo apt install ****imagemagick

<a name="0HsKy"></a>
## Running with default argument
```bash
../test.py -i 1.png
#Outfile: Re_1.png

identify 1.png Re_1.png 

# 1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.010
# Re_1.png PNG 1333x913 1333x913+0+0 8-bit sRGB 203679B 0.000u 0:00.000

../test.py -i 1.png -o my.png
#Outfile: my.png

identify 1.png my.png 
#1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
#my.png PNG 1333x913 1333x913+0+0 8-bit sRGB 203679B 0.000u 0:00.000
```

<a name="jFLlM"></a>
## Resize by width

```bash
../test.py -i 1.png -w 300

identify 1.png Re_1.png
#1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
#Re_1.png PNG 300x205 300x205+0+0 8-bit sRGB 27338B 0.000u 0:00.000
```

<a name="Z1Pwd"></a>
## Resize by Height

```bash
../test.py -i 1.png -t 300

identify 1.png Re_1.png 
#1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
#Re_1.png PNG 437x300 437x300+0+0 8-bit sRGB 44276B 0.000u 0:00.000
```

<a name="YQmGR"></a>
## Resize by Ratio

```bash
../test.py -i 1.png -r 10

identify 1.png Re_1.png 
#1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
#Re_1.png PNG 266x182 266x182+0+0 8-bit sRGB 23398B 0.000u 0:00.000
```

<a name="3sPlw"></a>
# Resize by Height and Width

```bash
../test.py -i 1.png  -t 200 -w 10

#1.png PNG 2666x1827 2666x1827+0+0 8-bit sRGB 295921B 0.000u 0:00.000
#Re_1.png PNG 10x200 10x200+0+0 8-bit sRGB 2186B 0.000u 0:00.000
```

<a name="QHhlD"></a>
# Resize Multiple files
<a name="1TAZK"></a>
## Resize multiple file

```bash
../test.py -i "*.png"
```
All result will be printed to "OUT" director. 

```bash
../test.py -i OUT -o test -w 100
```
reading all pictures from OUT directory, and all result where out put to test file

<a name="BKexU"></a>
# update
<a name="yFwCg"></a>
## Print information
2020/2/9
> Adding arguments

```python
parser.add_argument('-inf','-INF','--infor',default = "None")    #resize by Height

INFORM = args.infor

```

<a name="g4W1b"></a>
### Def functions：
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
### Logic:
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
### Usage:

```bash
Imresize.py -i "*" -inf 1
```

> output:

![Re_DeepinScreenshot_select-area_20200209144821.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581231152106-47ad9abd-5d58-46b4-b048-f5051534eb67.png#align=left&display=inline&height=114&name=Re_DeepinScreenshot_select-area_20200209144821.png&originHeight=114&originWidth=500&size=122253&status=done&style=none&width=500)
> explain

| Name | Size | Width&height | DPI | format | mode | Bit |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| bash.jpg | 16.8KB  | size:800x450 | dpi: NA | JPEG (ISO 10918) | RGB | bit:8 |






<br />--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
