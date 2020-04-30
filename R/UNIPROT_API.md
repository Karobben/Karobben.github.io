---
url: uniprot_api
---

# UNIPROT_API


```r
library(httr)
my_protein_ids <- c('Q8N4C6', 'Q9UM73')


results <- POST(url = "https://www.uniprot.org/uploadlists/",
	body = list(from = 'ID',
	to = 'GENENAME',
	format = 'tab',
	query = paste(my_protein_ids, collapse = ' ')))
print(results)
'''
# Result
From	To
Q8N4C6	NIN
Q9UM73	ALK
'''

uniprot_results <- content(results, type = 'text/tab-separated-values',
	col_names = TRUE,
	col_types = NULL,
	encoding = "UTF-8")

results <- POST(url = "https://www.uniprot.org/uploadlists/",
	body = list(from = 'GENENAME',
	to = 'ID',
	format = 'tab',
	query = paste(x, collapse = ' ')))

```


