---
title: "Fasta Sequences Align| Karobben"
description: "Align fasta sequences by ClustelW and Muscle"
url: faalign
date: 2020/07/27
---

# Fasta Sequences Align

## Quick look about the data
suppose there are fasta file name as `LYSV-NCBI.fasta`

**Have a quick look**
```bash
grep  ">" LYSV-NCBI.fasta |wc
wc LYSV-NCBI.fasta
echo $(wc LYSV-NCBI.fasta| awk '{print $2}')-$(grep  ">" LYSV-NCBI.fasta |wc |awk '{print $2}')|bc
```
```
124    1114    8363
18250   19116 1282572 LYSV-NCBI.fasta
18002
```
As we can see, there are 124 sequences and **roughly** about 18002 bases

**Have a quick look about the sequences by [Seq-view](https://github.com/Karobben/Seq-view)**

```bash
Seq-view1.3 -i LYSV-NCBI.fasta
```
[![aFEKqH.png](https://s1.ax1x.com/2020/07/27/aFEKqH.png)](https://imgchr.com/i/aFEKqH)



# ClustelW2

## Install
url: [click me](http://www.clustal.org/download/current/)
```bash
wget http://www.clustal.org/download/current/clustalw-2.1.tar.gz
tar -zxvf clustalw-2.1.tar.gz
cd clustalw-2.1/
./configure
make
make install
```

```bash
clustalw2 -QUICKTREE -OUTPUT=FASTA  -INFILE=LYSV-NCBI.fasta
```
It takes less than 20 mins
![aFEQZd.gif](https://s1.ax1x.com/2020/07/27/aFEQZd.gif)

**Quick look**
```bash
Seq-view1.3  -i LYSV-NCBI.fasta -a 90
```
[![aFekIs.md.png](https://s1.ax1x.com/2020/07/27/aFekIs.md.png)](https://imgchr.com/i/aFekIs)

# Muscle

```bash
apt install muscle
time muscle -in LYSV-NCBI.fasta -out 123.fa
```
[![aFnKUJ.png](https://s1.ax1x.com/2020/07/27/aFnKUJ.png)](https://imgchr.com/i/aFnKUJ)

```
real  17m59.470s
user  17m59.034s
sys  0m0.256s
```
It takes about 18min as well as *ClustelW2*
