---
---

# Reading ab1 file by R (sangerseqR)

Install: [Bioconductor](http://www.bioconductor.org/packages/release/bioc/html/sangerseqR.html)
ReadMe: [PDF](http://www.bioconductor.org/packages/release/bioc/vignettes/sangerseqR/inst/doc/sangerseq_walkthrough.pdf)

# Install
```r
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("sangerseqR")
```

# Quick Start
```r
library(sangerseqR)

A <- read.abif("119DOWN-ST.119DOWN-F.11731873.C04.ab1")
str(A)
```

<pre>
Formal class 'abif' [package "sangerseqR"] with 3 slots
  ..@ header   :Formal class 'abifHeader' [package "sangerseqR"] with 9 slots
  .. .. ..@ abif       : chr "ABIF"
  .. .. ..@ version    : int 101
  .. .. ..@ name       : raw [1:4] 74 64 69 72
  .. .. ..@ number     : int 1
  .. .. ..@ elementtype: int 1023
  .. .. ..@ elementsize: int 28
  .. .. ..@ numelements: int 118
  .. .. ..@ dataoffset : int 259806
  .. .. ..@ datahandle : int 0
  ..@ directory:Formal class 'abifDirectory' [package "sangerseqR"] with 7 slots
  .. .. ..@ name       : chr [1:118] "AEPt" "AEPt" "APFN" "APXV" ...
  .. .. ..@ tagnumber  : int [1:118] 1 2 2 1 1 1 1 1 1 1 ...
  .. .. ..@ elementtype: int [1:118] 4 4 18 19 19 19 2 5 4 4 ...
  .
  .
  .
</pre>

# Data
## Electronic Signal Matrix
```r
A@data$DATA.1
A@data$DATA.2
A@data$DATA.3
A@data$DATA.4
```

## Base Signal Matrix
```r
A@data$DATA.9
A@data$DATA.10
A@data$DATA.11
A@data$DATA.12
```
### Plot
```r
librar(ggplot2)

Y1 = head(hetab1@data$DATA.9,3000)
Y2 = head(hetab1@data$DATA.10,3000)
Y3 = head(hetab1@data$DATA.11,3000)
Y4 = head(hetab1@data$DATA.12,3000)

ggplot() + geom_path(aes(x=c(1:length(Y)), y= Y1),color='salmon')+
  geom_path(aes(x=c(1:length(Y2)), y= Y2),color='green')+
  geom_path(aes(x=c(1:length(Y3)), y= Y3),color='blue')+
  geom_path(aes(x=c(1:length(Y4)), y= Y4),color='black')

```


# Read by Python
Working Manual: [Biopython](https://biopython.org/wiki/ABI_traces)

```python
from Bio import SeqIO
record = SeqIO.read("55-Mn-fw-EM-28.ab1", "abi")
list(record.annotations.keys())
dict_keys(["DATA5", "DATA8", "RUNT1", "phAR1", ..., "DATA6"])
```

# Cluster

96 results are stored are `HRB-1_s7346` file
```r
library(sangerseqR)
library(reshape2)

setwd("HRB-1_s7346/")
List = dir()

All = c()
for(i in List){
  A = read.abif(i)
  tmp = data.frame(A@data$DATA.1,A@data$DATA.2,A@data$DATA.3,A@data$DATA.4)
  tmp = data.frame(melt(t(data.frame(A@data$DATA.1,A@data$DATA.2,A@data$DATA.3,A@data$DATA.4)))$value)
  colnames(tmp) = A@data$TUBE.1
  All = c(All, tmp)
}

TB = data.frame(All)
```
