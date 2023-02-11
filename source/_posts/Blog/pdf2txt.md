---
title: "pdf to txt| txt to pdf"
description: "Converting your pdf to text file or text files to pdf"
url: pdf2txt
date: 2020/10/25
toc: true
excerpt: "Converting your pdf to text file or text files to pdf"
tags: [Python, Tools]
category: [Python]
cover: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
thumbnail: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
priority: 10000
---

## 如何用python提取pdf的文本內容

`pdf2txt.py`; extract the txt from pdf files.

github: [pdfminer](https://github.com/pdfminer/pdfminer.six)
reference: [Mr_Vague](https://blog.csdn.net/m0_37952030/article/details/85041434)

## PDF to text
### 1.Install

```bash
git clone https://github.com/pdfminer/pdfminer.six.git
python3 setup.py install
```

**or**
you can use pip
```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple pdfminer.six
```

### 2. Run
```bash
pdf2txt.py Papers/vilhelmsson2004.pdf| tail
```
<span style="background:salmon">**backs to**</span>:
```bash
ken@ken-PC:~/Desktop$ pdf2txt.py Papers/vilhelmsson2004.pdf| tail -n 20
Fotsis T & Mann M (1996) Femtomole sequencing of proteins
from polyacrylamide gels by nano-electrospray mass spec-
trometry. Nature 379, 466– 469.

Wilson RP & Cowey CB (1985) Amino acid composition of
whole-body tissue of rainbow trout and Atlantic salmon. Aqua-
culture 48, 373– 376.

Wing SS, Haas AL & Goldberg AL (1995) Increase in ubiquitin –
protein conjugates concomitant with the increase in proteolysis
in rat skeletal muscle during starvation and atrophy denerva-
tion. Biochem J 307, 639–645.

Yamamoto T, Shima T, Furuita H & Suzuki N (2002) Inﬂuence of
feeding diets with and without ﬁsh meal by hand and by self-
feeders on feed intake, growth and nutrient utilization of juven-
ile rainbow trout (Oncorhynchus mykiss). Aquaculture 214,
289– 305.
...
```
Compare to raw file:
![YLZMxf.png](https://s1.ax1x.com/2020/05/22/YLZMxf.png)
© vilhelmsson 2004

### PDF to html
output as html file:
```bash
pdf2txt.py -o test.html Papers/vilhelmsson2004.pdf
```

## Text to PDF
Profile: [mkumarchaudhary06](https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/)
### Install
```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple fpdf
```

### Quick Start

```python
from fpdf import FPDF

pdf = FPDF()   # save FPDF() class into a variable pdf
pdf.add_page() # Add a page

pdf.set_font("Arial", size = 15) # set style and size of font that you want in the pdf

pdf.cell(200, 10, txt = "GeeksforGeeks",  
         ln = 1, align = 'C') # create a cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C') # add another cell

pdf.output("GFG.pdf")         # save the pdf with name .pdf
```
**Output**:
![GFG.pdf](https://media.geeksforgeeks.org/wp-content/uploads/20200108153749/GFG201.jpg)

It works, but you need to slicing the sentences before running this codes or the contents will **run out of the page**.

By solving this problem, there is a script in github: [baruchel
](https://github.com/baruchel/txt2pdf). It's not perfect but it works.

```bash
git clone https://github.com/baruchel/txt2pdf.git
txt2pdf -s 12 -o document.pdf document.txt
```
