---
toc: true
url: edx_biochm_22
covercopy: <a href="https://www.researchgate.net/figure/Xeno-Nucleic-Acids-XNAs-and-their-structures_fig3_281743623">© Stella Diafa</a>
priority: 10000
date: 2021-06-18 16:21:23
title: "Principles of Biochemistry 22 |Nucleic acids| Class Notes |HarvardX"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
ytitle: "基礎生物化學筆記 22 |核酸的代谢| 哈佛 edx網課"
description: "Principles of Biochemistry 22 |Nucleic acids| Class Notes |HarvardX"
excerpt: "Nucleic acids, Edx classes, HarvardX"
cover: "https://www.researchgate.net/profile/Marcel-Hollenstein/publication/281743623/figure/fig3/AS:669166759591936@1536553196049/Xeno-Nucleic-Acids-XNAs-and-their-structures.png"
thumbnail: "https://www.researchgate.net/profile/Marcel-Hollenstein/publication/281743623/figure/fig3/AS:669166759591936@1536553196049/Xeno-Nucleic-Acids-XNAs-and-their-structures.png"
---

## Quick review

- Building blocks of nucleic acids
- Energy currency in cells (ATP)
- Precursors of universal electron acceptors
- Signaling molecules

RAN: Ribose; DNA: Deoxyribose
Purines: **A** (Adenine), **G** (Guanine)
pyrimidine: **T** (Thymine), **C** (Cytosine),  **U** (Uracil)


Nucleosides:
  - pentos + purine/pyrimidine
  - nucleic acid without a phosphate group
  e.g. Adenosine

Nucleotides:
  - petos + purine/pyrimidine + one or more phosphates
  - Nucleic acid with three phosphates group
  e.g. ATP

DNA/RNA:
  - polymerized Nucleotides are linked by a **phosphodiester linkage**
  - Ribonucleotide: RNA
  - Dexoyribonucleotide: DNA

### Nucleotides Biosynthesis
PRPP: phosphoribosyl pyrophosphate
PRPP + base $\to$ NMP + PP~i~

novo pathway:
PRPP + amino acids + HCO~3~^-^ + folate + ... $\to$ nucleotide

Glucose-6-P $\overset{Pentose\ phosphate\ pathway}{\to}$ Ribose-5-P $\to$ PRPP


**Another contribution of nucleotides**
Coenzyme A; cAMP

## Novo nucleotide biosynthesis
![purine synthesis](https://www.kegg.jp/tmp/search_pathway_text//map01065_org_2021061818222598425.png)

Inositol monophosphate (IMP) $\to$ AMP/GMP
PRPP $\to$ IMP has 11 steps

1. carbonyl activation
$Glycine + ATP \to Glycine-P + ADP $
The carbonyl oxygen of glycine is activated by phosphorylation.

2. Displacement by amine
$Glycine-P + NH_ 2 -R \to Glycine-NH-R$ R is nucleotide
...

Purine Biosynthesis:
- [By Biochemistry Den](https://biochemden.com/purine-synthesis/) (Recommended)
- [By Hidaya Aliouche, B.Sc.](https://www.news-medical.net/life-sciences/Purine-Biosynthesis.aspx)
- [by Sagar Aryal](https://microbenotes.com/purine-synthesis/)


### IMP to AMP/GMP

```graphviz
digraph F {
    rankdir = LR;

    "node1" [ label = "<f1>  |<f2> IMP|<f3> "
              shape = "record"
              color = white
              fontcolor = "red"
              fontsize = 20
              ];
    "node2" [ label = "<f1> Adenylosuccinate| <f2>|<f3> XMP"
              shape = "record"
              color = white
              fontcolor = "red"
              fontsize = 20
              ];
    "node3" [ label = "<f1> AMP| <f2>|<f3> GMP"
              shape = "record"
              color = white
              fontcolor = "red"
              fontsize = 20
              ];
    node1:f2 -> node2:f1 -> node3:f1 [ style = "bold"]
    node1:f2 -> node2:f3 -> node3:f3 [ style = "bold"]

    Asp -> node2:f1  [color = "red"]
    node3:f1 -> Fumarate [color = "red"]
    GTP -> node2:f1 -> "GDP+Pᵢ" [color = "green"]
    "H₂O" -> node2:f3
    "NAD⁺" -> node2:f3
    Gln -> node3:f3 -> Glu [color = "red"]
    ATP -> node3:f3 -> "AMP + PPᵢ" [color = "green"]

}
```


### Regulation of the synthesis

```graphviz
digraph {
  node [shape = none]
  inter1 [ label = "", width=0, height =0]
  En1 [label = "PRPP\nsynthase", fontcolor="cyan"]
  En2 [label = "Gln-PRPP\namidotransferase", fontcolor="cyan"]
  En3 [label = "Adenylosuccinate\nsynthase", fontcolor="cyan"]
  En4 [label = "IMP\ndehydrogenase", fontcolor="cyan"]
  En5 [label = "XMP-glutamine\namidotransferase", fontcolor="cyan"]
  subgraph{
    node [fontcolor = "crimson"]
    AGI [label ="AMP\nGMP\nIMP" ]
    AMP2 [label = "AMP"]
    GMP2 [label = "GMP"]
  }
  subgraph{
    node [fontcolor = "green"]
    ATP; GTP
  }


  "Ribose-5-P" -> En1 -> PRPP -> En2 -> "5-P-ribosylamine" -> IMP -> En3 -> Adenylosuccinate -> inter1 -> AMP
  IMP -> En4 -> XMP -> En5 -> GMP

  AGI -> En1 [arrowhead = "tee", color = "crimson"]
  AGI -> En2 [arrowhead = "tee", color = "crimson"]
  AMP2 -> En3 [arrowhead = "tee", color = "crimson"]
  GMP2 -> En4 [arrowhead = "tee", color = "crimson"]
  GTP -> En3 [color = "green"]
  ATP -> En5 [color = "green"]
}
```


## Biosynthesis of pyrimidine

$UMP \to UTP \to CTP$

Formation of the pyrimidine-ring:
- $Carbamoyl-P + Aspartate \overset{ATCase}{\longrightarrow} Carbamoyl aspartate$
- $Carbamoyl aspartate  \overset{Dihydroorotase}{\longrightarrow} Dihydroorotate$
- $Dihydroorotate  + NAD^ +\overset{Dihydroorotate\ Dihydroorotase}{\longrightarrow} Orotate + NADH + H^ +$

Pyrimidine assemble
- $Orotate + PRPP \to UMP + PP_ i + CO_ 2$
- $UMP + 2ATP \to UTP + 2ADP$
- $UTP + ATP + Gln \to CTP + ADP + P_ i + Glu$
## NDP to dNDP
![NDP to dNDP](https://z3.ax1x.com/2021/06/18/RpORdf.md.png)

## Cancer Treatment

The cancer cell is more sensitive than normal cells to inhibitors  of nucleotide biosynthesis

- $dUMP \overset{Thymidylate\ synthase}{\longrightarrow} dTMP$

### Folate cycle

```graphviz
digraph{
  subgraph{
    node [shape = ellipse, fontcolor ="brown", color = grey, style = "filled"]
    TS  [label = "thymidylate\nsynthase"]
    DR  [label = "dihydrofolate\nreductase"]
    SHT [label = "serine\nhydroxymethyl-\ntransferase"]
  }
  subgraph main{
    node [shape = none]
    "N5,N10-Methylene\nTHF" -> TS -> "7,8-dihydrofolate" -> DR -> THF -> SHT ->  "N5,N10-Methylene\nTHF" [style = "bold"]

  }
  NADPH -> DR -> "NADP+" [color = red]
  serine -> SHT -> Glycine [color = red]

  subgraph cluster_0{
    label = "Cancer Drag"
    node [shape=box, color = red, style = "filled"]
    edge [arrowhead="tee", color = red]
    FD [label = "FdUMP"]
    ME [label = "Methotrexate"]
  }
  FD -> TS [arrowhead="tee", color = red]
  ME -> DR [arrowhead="tee", color = red]
}
```


## Catabolism

### Pyrimidine catabolism
$Uridine + Pi \underset{phophorylase}{\overset{Pyrimidine-}{\longleftrightarrow}} Ribose-1-phosphate + Uracil$
$Uracil + NADPH \to Dihydrouracil + NADP^ +$
$Dihydrouracil \overset{Ring cleavage}{\longrightarrow} \beta-alanine + CO_ 2 + NH_ 4^ +$

### Adenosine degradation
$Adenosine \ monophosphate (AMP) + H_ 2O \to P_ i + Adenosine$
$Adenosine + H_ 2O \to Inosine + NH_ 3$
$Inosine + H_ 2O \to Ribose + Hypoxanthine$
$Hypoxanthine + O_ 2 + H_ 2O \to  Xanthine+ H_ 2O_ 2$

### Guanosine degradation
$GMP + P_ i \to Guanosine + H_ 2O$
$Guanosine + H_ 2O \to Ribose + Guanine$
$Guanine + H_ 2O \to Xanthine + NH_ 3$
$Xanthine \overset{Xanthine \ oxidase}{\longrightarrow} Uric \ acid$

Accumulation of Uric acid in blood could cause gout.


## treatment

- Reduce the formation of uric acid
Hypoxanthine and Allopurinal could serve as potent xanthine oxidase inhibitors. By restricted the production of the uric acid, the xanthine remained. But it is more soluble and easy to be cleaned.
- Uric acid degradation
$Uric acid \overset{Urate oxidase}{\longrightarrow} Allantoin$

## Pyrimidine/Purine salvage
### Pyrimidine
$Uracil \longleftrightarrow Ribose-1-P$
$Ribose-1-P \overset{Pyrimidine \ phosphorylase}{\longleftrightarrow} Uridine + P_ i$

### Purine
$Adenine + PRPP \overset{APRT}{\longrightarrow} Adenosine \ monophosphate$
APRT: adenine phosphoribosyltransferase.
$Guanine + PRPP \overset{HPRT}{\longrightarrow} Guanine \ monophosphate$
HPRT: hypoxanthine guanine phosphoribosyltransferase.


## Lesch-Nyhan disease
Genetic deficiency in HPRT

X-linked (Uncommon in females)

It causes Hyperuricemia, Severn neurological symptoms
Allopurinol treats hyperuricemia, but no neurological symptoms.
