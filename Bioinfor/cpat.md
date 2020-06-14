---
url: cpat
---

# CPAT

# Quick start
```bash
cpat.py  -g Tinity.fna -d ~/Biosoft/CPAT-1.2.4/dat/Human_logitModel.RData -x ~/Biosoft/CPAT-1.2.4/dat/Human_Hexamer.tsv -o output
```
-r 指定参考基因组  
-g 输入的转录本序列。如果是BED格式，必须-r指定参考基因组；如果是FASTA格式，不需要指定参考基因组，即使使用-r参数也会被忽略。  
-d 预制好的模型（Prebuilt training model）（CPAT自带人、鼠、果蝇、斑马鱼的模型）  
-x 预制好的六聚体频率表（Prebuilt hexamer frequency table）（CPAT自带人、鼠、果蝇、斑马鱼的六聚体频率表）  
-o 输出
---  
[Github](https://github.com/Karobben)  
[Blog](http://Karobben.github.io)  
[Bilibili](https://space.bilibili.com/393056819)  
[R 语言画图索引](https://karobben.github.io/R/R-index.html)
