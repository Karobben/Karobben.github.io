---
title: "Fasta Sequences Align| Karobben"
description: "Align fasta sequences by ClustelW and Muscle"
url: faalign
date: 2020/07/27
toc: true
excerpt: "Entrez Direct: E-utilities on the UNIX Command Line"
tags: [Software, Bioinformatics, Align]
category: [Biology, Bioinformatics, Protocol, Align]
cover: 'https://s1.ax1x.com/2020/07/27/aFEKqH.png'
thumbnail: 'https://s1.ax1x.com/2020/07/27/aFEKqH.png'
priority: 10000
---

## Fasta Sequences Align

### Quick look about the data
Suppose there is a `fasta` file name as `LYSV-NCBI.fasta`

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
As you can see, there are 124 sequences and **roughly** about 18002 bases

**Let's have a quick look at the sequences by [Seq-view](https://github.com/Karobben/Seq-view)**

```bash
Seq-view1.3 -i LYSV-NCBI.fasta
```
![aFEKqH.png](https://s1.ax1x.com/2020/07/27/aFEKqH.png)



## ClustalW2

### Install
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
![aFekIs.md.png](https://s1.ax1x.com/2020/07/27/aFekIs.md.png)

### ALign prarmeters

UPGAM Tree
```bash
clustalw2 -QUICKTREE -OUTPUT=FASTA  -INFILE=LYSV-NCBI.fasta -CLUSTERING=UPGMA -BOOTSTRAP=1000

clustalw2 -QUICKTREE -OUTPUT=FASTA  -INFILE=LYSV-NCBI.fasta -CLUSTERING=NJ -BOOTSTRAP=1000
```

==PS:==
ClustalW well not change the " ' " from the name of the sequence which may cause trouble in the tree file.


## Muscle

```bash
apt install muscle
time muscle -in LYSV-NCBI.fasta -out 123.fa
```
![aFnKUJ.png](https://s1.ax1x.com/2020/07/27/aFnKUJ.png)

```
real  17m59.470s
user  17m59.034s
sys  0m0.256s
```
It takes about 18min as well as *ClustelW2*

## Tcoffee

Source: [:house: T-Coffee](https://tcoffee.readthedocs.io/en/latest/tcoffee_quickstart.html)

### Protein sequences

```bash
# Default
t_coffee sample_seq1.fasta

# Quick
t_coffee sample_seq1.fasta -mode quickaln

# Consistent (M-Coffee combines the most common MSA packages)
t_coffee sample_seq1.fasta -mode mcoffee

# Structure (Expresso finds structures homologous to your sequences)
t_coffee sample_seq1.fasta -mode expresso

# Homology (PSI-Coffee enriches your dataset with homologous sequences)
t_coffee sample_seq1.fasta -mode psicoffee

# Accurate (combines Structures and Homology)
t_coffee sample_seq1.fasta -mode accurate
```


### DNA sequences

```bash
# Default
t_coffee sample_dnaseq1.fasta

# Functional (Pro-Coffee increases accuracy of functional DNA regions )
t_coffee sample_dnaseq1.fasta -mode procoffee
```

### RNA sequences

```bash
# Default
t_coffee sample_rnaseq1.fasta

# Structure 2D (R-Coffee uses predicted secondary structures)
t_coffee sample_rnaseq1.fasta -mode rcoffee

# Structure 3D (R-Coffee combined with Consan structural alignments)
t_coffee sample_rnaseq1.fasta -mode rcoffee_consan

# Accurate (RM-Coffee use M-Coffee and secondary structure predictions)
t_coffee sample_rnaseq1.fasta -mode rmcoffee
```


Full Tutorial: [:house::house::house:](http://www.tcoffee.org/Projects/tcoffee/workshops/tcoffeetutorials/index.html)
