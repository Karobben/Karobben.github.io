---
url: biostrings2
---

# Biostrings

source("[http://bioconductor.org/biocLite.R](http://bioconductor.org/biocLite.R)")<br />
```r
# Install
BiocManager::install('Biostrings')
```

[test.txt](https://www.yuque.com/attachments/yuque/0/2020/txt/691897/1579800839293-b28e0f1a-1088-4c56-ba2a-1a910f827db0.txt?_lake_card=%7B%22uid%22%3A%221579800839229-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Ftxt%2F691897%2F1579800839293-b28e0f1a-1088-4c56-ba2a-1a910f827db0.txt%22%2C%22name%22%3A%22test.txt%22%2C%22size%22%3A6581%2C%22type%22%3A%22text%2Fplain%22%2C%22ext%22%3A%22txt%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22umG5T%22%2C%22card%22%3A%22file%22%7D)
```r
library(Biostrings)
s = readDNAStringSet("test.txt")

length(s) #No. of seq
nchar(s)	#length of each seq
reverse(s)
translate(s)
dna2rna(s)
cDNA(dna2rna(s))
tolower(s)	# = = I don't know
letterFrequency(s, DNA_BASES)	# Frq with A,T,G,C
letterFrequency(s, DNA_ALPHABET)	# Frq with A, C, G, T, M, R, W, S, Y, K, V, H, D, B, N, -, +, .
letterFrequency(s, DNA_BASES, as.prob = TRUE) # Frq with A T G C
letterFrequency(s, "GC", as.prob = TRUE) # Frq with GC
```
---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
