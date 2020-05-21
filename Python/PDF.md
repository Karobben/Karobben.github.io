---
url: pdf2
---

# PDF


<a name="kyqqW"></a>
# 1. Read & Write

```python
from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = 'read.pdf'
writeFile = 'write.pdf'

pdfReader = PdfFileReader(open(readFile, 'rb'))
pdfWriter.write(open(writeFile, 'wb'))
```


<a name="m4WEP"></a>
# 2. Pick First two Page

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


<a name="uLu8m"></a>
## 2.1 Double the Pages

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
<a name="pr7No"></a>
##  
![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1581773048819-52b7a636-1021-498a-ad6d-2f44c198c4d1.jpeg#align=left&display=inline&height=173&name=123.jpg&originHeight=138&originWidth=400&size=15804&status=done&style=none&width=500)<br />
<br />

<a name="B7oXn"></a>
# 3. Water Mark
<a name="pAwMC"></a>
## 3.1 Make a Water Mark

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

![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1581774737413-64483457-ac2f-4ee1-964d-c396015c1cb6.jpeg#align=left&display=inline&height=400&name=123.jpg&originHeight=400&originWidth=400&size=17973&status=done&style=none&width=400)<br />

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
#encoding=utf-8
#author: walker
#date: 2014-03-18
#function:给pdf添加水印
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
#所有路径为绝对路径


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




<a name="LcBYr"></a>
# Add Page number
```python
##!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 本示例使用两个第三方库来实现为PDF文件添加文字水印
# 这两个库是pyPdf和reportlab
# 使用的Python版本是Python 3.7
# origing from https://www.cnblogs.com/kayb/p/10846341.html
# 作者：小磊
#链接：https://www.zhihu.com/question/19628465/answer/353504051
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](https://karobben.github.io/) <br />R 语言画图索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)<br />
