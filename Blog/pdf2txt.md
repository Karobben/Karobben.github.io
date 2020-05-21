---
url: pdf2txt
---

# 如何用python提取pdf的文本內容

pdf2txt.py; extract the txt from pdf files.

github: [pdfminer](https://github.com/pdfminer/pdfminer.six)
reference: [Mr_Vague](https://blog.csdn.net/m0_37952030/article/details/85041434)
# 1.Install

```bash
git clone https://github.com/pdfminer/pdfminer.six.git
python3 setup.py install
```

**or**
you can use pip
```bash
sudo pip3.7  install -i https://pypi.tuna.tsinghua.edu.cn/simple pdfminer.six
```

# 2. Run
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

## html
output as html file:
```bash
pdf2txt.py -o test.html Papers/vilhelmsson2004.pdf
```
