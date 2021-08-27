---
title: "用biopython抽取特定長度的序列"
description: "用biopython抽取特定長度的序列"
url: python_seqlen
date: 2020/12/13
toc: true
excerpt: "用biopython抽取特定長度的序列"
tags: [Python, Biopython, Bioinformatics]
category: [Python, Bio]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## 用biopython抽取特定長度的序列

## 1. fasta 讀取和長度統計

### 1.1 統計
```python
from Bio import SeqIO

Seq = '/media/ken/Data/Yan/RNA-seq/report/2.assembly/out.fa'
Seq = SeqIO.parse(Seq, "fasta")

Len_Seq = []
for seq_record in Seq:
  Num =  len(str(seq_record.seq))
  Len_Seq += [Num]
```

### 1.2 統計圖

```python
import matplotlib.pyplot as plt

plt.ion()
plt.show()

plt.figure(figsize=(7, 4))
plt.hist(Len_Seq, label=['1st', '2nd'], bins=900)
plt.grid(True)
plt.legend(loc=0)
plt.xlim(xmax=1000,xmin=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
```
![Figure_1](https://i.loli.net/2020/06/10/Rhle6H7x9rMQJWu.png)
ummm, 決定篩掉30000bp一下的reads

```python
from Bio import SeqIO

Seq = '/media/ken/Data/Yan/RNA-seq/report/2.assembly/out.fa'
Seq = SeqIO.parse(Seq, "fasta")

Num = 4000
Result = []
for seq_record in Seq:
  if len(str(seq_record.seq)) > Num:
    Result +=[">"+seq_record.id]
    Result +=[str(seq_record.seq)]

Fasta = "\n".join(Result)
F = open("out.fa",'w')
F.write(Fasta)
F.close()
```


