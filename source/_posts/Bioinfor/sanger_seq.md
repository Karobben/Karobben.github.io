---
title: "abi processing"
description: "Processing Sanger Sequencing file (abi) wiht Python or R"
date: 2020/09/05
url: ab1
toc: true
excerpt: "abi"
tags: [Software, Bioinformatics, Sanger Sequencing, R]
category: [Biology, Bioinformatics, others]
cover: 'https://s1.ax1x.com/2020/06/26/Nro4d1.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/Nro4d1.png'
priority: 10000
---

## Processing Sanger Sequencing file (abi) wiht Python or R


In R, you can using `sangerseqR` to reading *ab1* file.
An example can see: [Karobben 2020](https://karobben.github.io/2020/09/20/R/r_ab1/)

## Python

### Biopython
```python
from Bio import SeqIO
handle = open("test.ab1", "rb")
for record in SeqIO.parse(handle, "abi"):
    print(record)
```

#### Trace plot
Biopython: [Click hear](https://biopython.org/wiki/ABI_traces)
### Package sanger-sequencing
[Link](https://pypi.org/project/sanger-sequencing/)
Can't find any examples...

## Perl
[ABIF](http://search.cpan.org/~vita/Bio-Trace-ABIF-1.05/lib/Bio/Trace/ABIF.pm)

## Convert abi to Scf
reference: [stock overflow](https://www.biostars.org/p/622/)
```bash
convert_trace -out_format scf < trace.ab1 > trace.scf
```

## Convert ab1 to excel
Working Manual: [ab1_organizer](https://pypi.org/project/ab1-organizer/)
```bash
pip install ab1_organizer

ab1_organizer.py -f ./path/to/zip/file -t ./path/to/order/table.xlsx
```

## <span style="background:salmon;font-size:50px">Base Calling</span>
[GitHub: tracy](https://github.com/gear-genomics/tracy)
[Documentation](https://www.gear-genomics.com/docs/tracy/installation/#installation-from-source)
[Paper](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-020-6635-8#author-information)

(PS: It seems like we need to download some files from google. So, as you can see, it's not easy for the people in China mainland to install it.)
It is a great app for basecalling, alignment, assembly and deconvolution of sequencing chromatogram files.

### Installation
```bash
apt install \
    build-essential g++ \
    cmake \
    git-all \
    liblzma-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libboost-date-time-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    libboost-iostreams-dev

git clone --recursive https://github.com/gear-genomics/tracy.git
cd tracy/
make all
make install
./bin/tracy -h
```
