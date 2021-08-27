---
title: "Sanger Sequencing (abi) Plot (Biopython)"
ytitle: "用python 畫 abi文件， 測序結果"
description: "Sanger Sequencing Result Plot with python"
url: bio_ssp
date: 2020/11/29
toc: true
excerpt: "Generally, we can read abi file by Biopython and Plot result with matplotlib."
tags: [Python, Biopython, matplotlib]
category: [Python, Bio]
cover: 'https://biopython.org/assets/images/biopython_logo_white.png'
thumbnail: 'https://biopython.org/assets/images/biopython_logo_white.png'
priority: 10000
---

Sanger Sequencing Plot (Biopython + Matplotlib)

## Quick Start

```python
from Bio import SeqIO
import matplotlib.pyplot as plt
from collections import defaultdict


## Abi File
abi_file = "D10.1.F.YP13033649.D10.S7695.ab1"
record = SeqIO.read(abi_file, "abi")
channels = ["DATA1", "DATA2", "DATA3", "DATA4"]
trace = defaultdict(list)
for c in channels:
    trace[c] = record.annotations["abif_raw"][c]

plt.plot(trace["DATA2"], color="green" ,alpha=0.6, lw=0.2) # A
plt.plot(trace["DATA4"], color="blue"  ,alpha=0.6, lw=0.2) # C
plt.plot(trace["DATA1"], color="black" ,alpha=0.6, lw=0.2) # G
plt.plot(trace["DATA3"], color="red"   ,alpha=0.6, lw=0.2) # T
plt.title(record.annotations['abif_raw']['TUBE1'])
plt.show()
```

![Sanger sequencing plot](https://s3.ax1x.com/2020/11/29/DgCjyR.png)

## Script for Results of 96-wells plate
**abi_plot.py**
```python
##!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-O','--output', default="out.png")     #输入文件

##获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
#####
#####

import os
import matplotlib as mpl
import matplotlib.pyplot as plt

from Bio import SeqIO
from collections import defaultdict

def raw_plot(INPUT):
    record = SeqIO.read(INPUT, "abi")
    channels = ["DATA1", "DATA2", "DATA3", "DATA4"]
    trace = defaultdict(list)
    for c in channels:
        trace[c] = record.annotations["abif_raw"][c]
    plt.plot(trace["DATA2"], color="green" ,alpha=0.6, lw=0.2) # A
    plt.plot(trace["DATA4"], color="blue"  ,alpha=0.6, lw=0.2) # C
    plt.plot(trace["DATA1"], color="black" ,alpha=0.6, lw=0.2) # G
    plt.plot(trace["DATA3"], color="red"   ,alpha=0.6, lw=0.2) # T
    plt.title(record.annotations['abif_raw']['TUBE1'])
    #plt.show()


Cmd = "ls "+ str(INPUT)
LIST = os.popen(Cmd).read().split("\n")[:-1]
print(LIST)

plt.figure(figsize=(14*3, 8*3))
plt.ion()
for i in range(96):
    plt.subplot(8,12,i+1)
    abi = INPUT+"/"+LIST[i]
    print(abi)
    raw_plot(abi)


plt.show()
plt.savefig(OUTPUT)
```

Usage:
```bash
abi_plot.py -i 96Well_Result
```
![wmCyRJ.md.png](https://s1.ax1x.com/2020/09/06/wmCyRJ.md.png)

## Box plot
It is useful when all abi files are plasmid or long sequencing result.

Box plot
```python
def raw_box_plot(INPUT):
    record = SeqIO.read(INPUT, "abi")
    channels = ["DATA1", "DATA2", "DATA3", "DATA4"]
    trace = []
    for c in channels:
        trace  += record.annotations["abif_raw"][c][2500:15000]
    plt.boxplot(trace) # A
    plt.axis([0,2,0,600])
    plt.title(record.annotations['abif_raw']['TUBE1'])
    plt.show()
```


```python
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

from Bio import SeqIO

INPUT = "96Well_Result"
Cmd = "ls "+ str(INPUT)
LIST = os.popen(Cmd).read().split("\n")[:-1]

trace = []
for i in range(96):
  abi = INPUT+"/"+LIST[i]
  record = SeqIO.read(abi, "abi")
  channels = ["DATA1", "DATA2", "DATA3", "DATA4"]
  for c in channels:
      trace  += record.annotations["abif_raw"][c][2500:15000]

trace2 = []
for i in range(18):
  abi = INPUT+"/"+LIST[i]
  record = SeqIO.read(abi, "abi")
  channels = ["DATA1", "DATA2", "DATA3", "DATA4"]
  for c in channels:
      trace2  += record.annotations["abif_raw"][c][2500:15000]

trace3 = []
for i in range(18,96):
  abi = INPUT+"/"+LIST[i]
  record = SeqIO.read(abi, "abi")
  channels = ["DATA1", "DATA2", "DATA3", "DATA4"]
  for c in channels:
      trace3  += record.annotations["abif_raw"][c][2500:15000]

plt.boxplot([trace, trace2, trace3])
plt.axis([0,4,0,600])
```
