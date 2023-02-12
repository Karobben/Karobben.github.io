---
toc: true
url: flybase_api
covercopy: <a href="https://flybase.org/">© flybase</a>
priority: 10000
date: 2022-12-05 14:49:59
title: "flybase api"
ytitle: "flybase api"
description: "flybase api"
excerpt: "Learning the API from FlyBase is important for accessing and integrating fly genetic and genomic data. It provides programmatic access to a variety of data, such as gene sequences, expression patterns, and genetic variants, allowing researchers to easily extract and analyze large datasets. This can facilitate the discovery of new insights and hypotheses in biological research. <a title='ChatGPT'>Who sad this?</a>"
tags: [flybase, Bioinformatics, api]
category: [Biology, Bioinformatics, Database]
cover: 'https://www.researchgate.net/profile/Dr-Jean-Paul-Kamdem/publication/259184998/figure/fig3/AS:297072130576395@1447838923298/FlyBase-Home-Page-wwwflybaseorg.png'
thumbnail: 'https://www.researchgate.net/profile/Dr-Jean-Paul-Kamdem/publication/259184998/figure/fig3/AS:297072130576395@1447838923298/FlyBase-Home-Page-wwwflybaseorg.png'
---

## Flybase api

[API documentation](https://flybase.github.io/api/swagger-ui/#/Chado/getChadoXmlById)



```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

ID = "FBgn0051624"
url = "https://api.flybase.org/api/v1.0/chadoxml/" + ID
html = urlopen(url)
soup = BeautifulSoup(html, features='xml')

Orth_all = [i for i in  soup.find_all("feature_relationship") if i.find('name').get_text() == 'orthologous_to']
Orth_Homo = [i  for i in Orth_all if i.find('genus').get_text() == 'Homo']
Gene_Syambol = [i.find_all('name')[2].get_text().split('\\')[1] for i in Orth_Homo]
Gene_Ensembl = [[i.find('accession').get_text() for i in ii.find_all("dbxref_id") if i.find('name').get_text() == "Ensembl_Homo_sapiens"][0]  for ii in Orth_Homo]
```
<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
