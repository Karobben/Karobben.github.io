---
title: "Change the Citation Format by Python"
ytitle: "Change the Citation Format by Python"
description: "Pyhton"
url: citation_format
date: 2021/01/22
toc: true
excerpt: "Chage the formate of citation with python"
tags: [Python]
category: [Python]
cover: 'https://biopython.org/assets/images/biopython_logo_white.png'
thumbnail: 'https://biopython.org/assets/images/biopython_logo_white.png'
priority: 10000
---


```python
import json

def BibTeX_Dic(X):
	X = X.replace("@article", "")
	Cite_id = X[:X.find(",")].replace("{","")
	X = X.replace(Cite_id+", ","")
	X = X.replace("={",'":"').replace("}, ", '", "')[:-2]
	X = '{"' + X[1:-1] + '"}'
	Cite_P = json.loads(X)
	Cite_P['author'] = Cite_P['author'].split(" and ")
	Cite_P['pages'] = Cite_P['pages'].split("--")
	return Cite_P

X = "@article{sun1960analysis, title={Analysis of joint action of insecticides against house flies}, author={Sun, Yun-Pei and Johnson, EoRo}, journal={Journal of economic entomology}, volume={53}, number={5}, pages={887--892}, year={1960}, publisher={Oxford University Press Oxford, UK} }"

Cite_P = BibTeX_Dic(X)

Format = "MLA"
if Format == "MLA":
    Author = ", and ".join([i for i in Cite_P['author']])
    Result = [Author + '. "' +
        Cite_P['title'] +'." ' +
        Cite_P['journal'] + " " +
        Cite_P['volume'] +"."+
        Cite_P['number'] + " ("+
        Cite_P['year']+"): "+
        Cite_P['pages'][0] +"-"+ Cite_P['pages'][1]
    ]
print(Result[0])

Format = "APA"
if Format == "APA":
    Author = []
    for i in Cite_P['author']:
        # chinese name with "-":
        N_fam = i.split(", ")[0]
        N_giv = i.split(", ")[1]
        if "-" in i:
            N_giv = " ".join([i[0]+"." for i in N_giv.split("-")])
            Author += [N_fam +", "+N_giv]

        elif " " not in N_giv:
            Author += [N_fam +", "+N_giv[0]+"."]
        Result = [", & ".join(Author) + " (" +
                  Cite_P['year'] + '). "'+
                  Cite_P['title'] + '." ' +
                  Cite_P['journal'] + ", "+
                  Cite_P['volume'] +"("+
                  Cite_P['number'] + "), "+
                  Cite_P['pages'][0] +"-"+ Cite_P['pages'][1]
                 ]
print(Result[0])
```
