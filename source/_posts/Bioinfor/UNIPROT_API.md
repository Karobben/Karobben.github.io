---
title: "UNIPROT_API"
description: "UNIPROT_API"
url: uniprot_api2
date: 2020/06/03
toc: true
excerpt: "Uniprot api for R"
tags: [Bioinformatic, Protein, R, Python, api, Database]
category: [Biology, Bioinformatics, Database]
cover: 'https://www.uniprot.org/uniprot-logo.img.0df091.svg'
thumbnail: 'https://www.uniprot.org/uniprot-logo.img.0df091.svg'
priority: 10000
covercopy: <a href="https://www.uniprot.org/">Uniprot</a>
---


## UNIPROT_API

for more information, please visit: [uniprot expample](https://www.uniprot.org/help/id_mapping)

```python
library(httr)

isJobReady <- function(jobId) {
  pollingInterval = 5
  nTries = 20
  for (i in 1:nTries) {
    url <- paste("https://rest.uniprot.org/idmapping/status/", jobId, sep = "")
    r <- GET(url = url, accept_json())
    status <- content(r, as = "parsed")
    if (!is.null(status[["results"]]) || !is.null(status[["failedIds"]])) {
      return(TRUE)
    }
    if (!is.null(status[["messages"]])) {
      print(status[["messages"]])
      return (FALSE)
    }
    Sys.sleep(pollingInterval)
  }
  return(FALSE)
}

getResultsURL <- function(redirectURL) {
  if (grepl("/idmapping/results/", redirectURL, fixed = TRUE)) {
    url <- gsub("/idmapping/results/", "/idmapping/stream/", redirectURL)
  } else {
    url <- gsub("/results/", "/results/stream/", redirectURL)
  }
}

files = list(
  ids = "P21802,P12345",
  from = "UniProtKB_AC-ID",
  to = "UniRef90"
)
r <- POST(url = "https://rest.uniprot.org/idmapping/run", body = files, encode = "multipart", accept_json())
submission <- content(r, as = "parsed")

if (isJobReady(submission[["jobId"]])) {
  url <- paste("https://rest.uniprot.org/idmapping/details/", submission[["jobId"]], sep = "")
  r <- GET(url = url, accept_json())
  details <- content(r, as = "parsed")
  url <- getResultsURL(details[["redirectURL"]])
  # Using TSV format see: https://www.uniprot.org/help/api_queries#what-formats-are-available
  url <- paste(url, "?format=tsv", sep = "")
  r <- GET(url = url, accept_json())
  resultsTable = read.table(text = content(r), sep = "\t", header=TRUE)
  print(resultsTable)
}
```
<pre>
From      Cluster.ID                                       Cluster.Name Common.taxon Size Date.of.creation
1 P21802 UniRef90_P21802       Cluster: Fibroblast growth factor receptor 2      Amniota  110       2022-04-27
2 P12345 UniRef90_P00507 Cluster: Aspartate aminotransferase, mitochondrial     Mammalia  199       2022-04-27
</pre>


Python for All infor

```python
import requests
Result = requests.post(url="https://rest.uniprot.org/uniprotkb/A6NNB3", data= {"Accept":"application/json"})
print(Result.json())
```


```python
import requests
import pandas as pd

def Domain_anno(ID, POS):
    Result = requests.post(url="https://rest.uniprot.org/uniprotkb/" + ID, data= {"Accept":"application/json"})
    Features = Result.json()['features']
    TB = pd.DataFrame()
    for Loc in POS:
        for Chat in Features:
            try:
                if Loc >= Chat['location']['start']['value'] and Loc <= Chat['location']['end']['value']:
                    print(Chat['type'])
                    TMP= pd.DataFrame([[Chat['type'], Loc, Chat['description']]], columns=["Type", "Loc", "Discrip"])
                    TB = pd.concat([TB, TMP])
            except:
                print(Chat)
    return TB
```
