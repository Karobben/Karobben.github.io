---
title: "UNIPROT_API"
description: "UNIPROT_API"
url: uniprot_api2
---

# UNIPROT_API

for more information, please visit: [uniprot expample](https://www.uniprot.org/help/api_idmapping)

```R
library(httr)
my_protein_ids = c("A5WWC6.1","P16152.3","Q15125.3","Q6P5L8.1","Q6PUF3.1","Q8MI29.1","Q9EQC1.1","Q9MYP6.1")

results <- POST(url = "https://www.uniprot.org/uploadlists/",
	body = list(from = 'ID',
	to = 'GENENAME',
	format = 'tab',
	query = paste(my_protein_ids, collapse = ' ')))
print(results)
```
<span style="Background:salmon">backs to</span>
```bash
From	To
A5WWC6	hsdl1
P16152	CBR1
Q15125	EBP
Q6P5L8	hsdl2
Q6PUF3	hsd11b1l
Q8MI29	CBR1
Q9EQC1	Hsd3b7
Q9MYP6	HSD17B14
```
|ID|GENENAME|CRC64|
|----|----|----|
|A5WWC6|	hsdl1|8C21E1A95DEB67B3|
|P16152|	CBR1|8C21E1A95DEB67B3|
|Q15125|	EBP|3931A9DE3DBAFA04|
|Q6P5L8|	hsdl2|B8BAC424D4E7CC61|

```R
uniprot_results <- content(results, type = 'text/tab-separated-values',
	col_names = TRUE,
	col_types = NULL,
	encoding = "UTF-8")

results <- POST(url = "https://www.uniprot.org/uploadlists/",
	body = list(from = 'GENENAME',
	to = 'ID',
	format = 'tab',
	query = paste(my_protein_ids, collapse = ' ')))
```

# more

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
