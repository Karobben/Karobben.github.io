---
toc: true
url: kegg_api
covercopy: © Karobben
priority: 10000
date: 2022-10-28 16:00:41
title: "KEGG API"
ytitle: "KEGG API"
description: "KEGG API"
excerpt: "Learning KEGG API is important for accessing and integrating biological pathway data, enabling researchers to analyze and visualize complex biological systems, identify new potential drug targets, and explore the relationships between genes, proteins, and metabolic pathways. <a title='ChatGPT'>Who sad this?</a>"
tags: [KEGG, Database, api, Bioinformatics]
category: [Biology, Bioinformatics,  Database]
cover: "https://s1.ax1x.com/2020/05/26/tieZcT.md.png"
thumbnail: "https://s1.ax1x.com/2020/05/26/tieZcT.md.png"
---

## KEGG API

list of all pathways:
```bash
curl https://rest.kegg.jp/list/pathway/dme
```

<pre>
path:dme00010	Glycolysis / Gluconeogenesis - Drosophila melanogaster (fruit fly)
path:dme00020	Citrate cycle (TCA cycle) - Drosophila melanogaster (fruit fly)
path:dme00030	Pentose phosphate pathway - Drosophila melanogaster (fruit fly)
</pre>



list of all organisms gene ID


```bash
curl https://rest.kegg.jp/list/dme
```
<pre>
dme:Dmel_CG40494	CDS	X:127449..140340	RhoGAP1A; Rho GTPase activating protein at 1A, isoform A
dme:Dmel_CR43552	miRNA	X:133385..133502	mir-4915-RA
dme:Dmel_CG17131	CDS	X:140318..200663	tyn; trynity, isoform A
dme:Dmel_CG17707	CDS	X:complement(142731..148426)	CG17707; uncharacterized protein, isoform B
dme:Dmel_CG3038	CDS	X:complement(243954..245856)	CG3038; uncharacterized protein, isoform C
dme:Dmel_CG2995	CDS	X:245978..254650	G9a; G9a, isoform B
dme:Dmel_CG42376	CDS	X:254876..255524	CG42376; uncharacterized protein, isoform A
</pre>



pathway information

```
curl https://rest.kegg.jp/get/dme00010
```
<pre>
ENTRY       dme00010                    Pathway
NAME        Glycolysis / Gluconeogenesis - Drosophila melanogaster (fruit fly)
DESCRIPTION Glycolysis is the process of converting glucose into pyruvate and generating small amounts of ATP (energy) and NADH (reducing power). It is a central pathway that produces important precursor metabolites: six-carbon compounds of glucose-6P and fructose-6P and three-carbon compounds of glycerone-P, glyceraldehyde-3P, glycerate-3P, phosphoenolpyruvate, and pyruvate [MD:M00001]. Acetyl-CoA, another important precursor metabolite, is produced by oxidative decarboxylation of pyruvate [MD:M00307]. When the enzyme genes of this pathway are examined in completely sequenced genomes, the reaction steps of three-carbon compounds from glycerone-P to pyruvate form a conserved core module [MD:M00002], which is found in almost all organisms and which sometimes contains operon structures in bacterial genomes. Gluconeogenesis is a synthesis pathway of glucose from noncarbohydrate precursors. It is essentially a reversal of glycolysis with minor variations of alternative paths [MD:M00003].
CLASS       Metabolism; Carbohydrate metabolism
PATHWAY_MAP dme00010  Glycolysis / Gluconeogenesis
MODULE      dme_M00001  Glycolysis (Embden-Meyerhof pathway), glucose => pyruvate [PATH:dme00010]
            dme_M00002  Glycolysis, core module involving three-carbon compounds [PATH:dme00010]
            dme_M00003  Gluconeogenesis, oxaloacetate => fructose-6P [PATH:dme00010]
            dme_M00307  Pyruvate oxidation, pyruvate => acetyl-CoA [PATH:dme00010]
DBLINKS     GO: 0006096 0006094
ORGANISM    Drosophila melanogaster (fruit fly) [GN:dme]
GENE        Dmel_CG8094  Hex-C; hexokinase C [KO:K00844] [EC:2.7.1.1]
            Dmel_CG32849  Hex-t2; Hex-t2 [KO:K00844] [EC:2.7.1.1]
            Dmel_CG3001  Hex-A; hexokinase A, isoform C [KO:K00844] [EC:2.7.1.1]
            Dmel_CG33102  Hex-t1; Hex-t1 [KO:K00844] [EC:2.7.1.1]
</pre>



KEGG modules

```bash
curl https://rest.kegg.jp/list/md
```

<pre>
md:M00951	Cremeomycin biosynthesis, aspartate/3,4-AHBA => cremeomycin
md:M00952	Benzoxazinoid biosynthesis, indoleglycerol phosphate => DIMBOA-glucoside
md:M00953	Mugineic acid biosynthesis, methionine => 3-epihydroxymugineic acid
md:M00956	Lysine degradation, bacteria, L-lysine => succinate
md:M00957	Lysine degradation, bacteria, L-lysine => glutarate => succinate/acetyl-CoA
md:M00958	Adenine ribonucleotide degradation, AMP => Urate
md:M00959	Guanine ribonucleotide degradation, GMP => Urate
md:M00960	Lysine degradation, bacteria, L-lysine => D-lysine => succinate
md:M00961	Betacyanin biosynthesis, L-tyrosine => amaranthin
md:M00962	Psilocybin biosynthesis, tryptophan => psilocybin
md:M00963	Chanoclavine aldehyde biosynthesis, tryptophan => chanoclavine-I aldehyde
md:M00964	Fumigaclavine biosynthesis, chanoclavine-I aldehyde => fumigaclavine C
md:M00965	Vindoline biosynthesis, tabersonine => vindoline
</pre>

## Another Project

```bash
curl https://rest.kegg.jp/get/hsa05130/image --output test.png
curl https://rest.kegg.jp/get/hsa05130/conf --output test
```


```html
<img src="test.png">
<button title ="123"; style="background-color: #0075eb; width: 50px;position: absolute;  left: 485px; top: 959px;">ITGB1</button>
<div class="dropdown" style="background-color: #eb0027; width: 50px;position: absolute;  left: 750px; top: 1788px;">

<button class="dropbtn" style="background-color: #eb0027">NAIP</button>
<div class="dropdown-content">
<a >Name</a>
<a >Name</a>
<a >Name</a>
</div>


<style>
    .dropbtn {
        background-color: black;
        color: white;
        padding: #px;
        font-size: #px;
        border: none;
    }

    .dropdown {
        position: relative;
        display: inline-block;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: lightgrey;
        min-width: #px;
        z-index: 1;
    }

    .dropdown-content a {
        color: black;
        padding: #px #px;
        text-decoration: none;
        display: block;
    }
    .dropdown-content a:hover {background-color: white;}
    .dropdown:hover .dropdown-content {display: block;}
    .dropdown:hover .dropbtn {background-color: grey;}
</style>
```













<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
