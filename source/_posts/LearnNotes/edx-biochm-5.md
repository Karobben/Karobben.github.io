---
toc: true
url: edx_biochm_5
covercopy: © stoddard lab
priority: 10000
date: 2021-03-29 15:06:26
title: "Principles of Biochemistry 5 | Enzyme Catalysis| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 5 || 哈佛 edx網課"
description: "Enzyme Catalysis; Class notes for biochemistry"
excerpt: "Enzyme Catalysis; Class notes for biochemistry"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
cover: "https://research.fredhutch.org/stoddard/en/projects/protein-and-enzymeengineering/_jcr_content/par/image.img.jpg/1536688974648.jpg"
thumbnail: "https://courses.edx.org/asset-v1:harvardx+MCB63X+1T2021+type@thumbnail+block@course_image-375x200.jpg"
---

## Enzyme Catalysis

|![The free energy profile of an enzymatic reaction](https://www.creative-enzymes.com/images/1-2-Enzyme-Catalysis-1.jpg)|
|:-:|
|(c) Gerlt J A. 1994|

Though the spontaneous reaction could happen automatically, it could run very slow without the help of the catalyzes.

## Why Enzyme Can Catalysis

- Transient covalent bonds
  - Activate substrate, lower the activate-energy..
- Weak non-covalent interaction
  - binding energy: $ \Delta G_B$ (Figure: Enzymatic Reaction, D), needed energy to decrease the reaction
- Desolvation:  weak interaction between water and substrate is replaced by weak interaction between the substrate and the enzyme.

**Catalysis is driven by structure and conformational changes.**

|![Figure: Enzymatic Reaction](https://courses.edx.org/assets/courseware/v1/ff759f0869102fc7b3c44d93dd0923ca/asset-v1:harvardx+MCB63X+1T2021+type@asset+block/2.3.2_O2_Q1.png)|
|:-:|
|(c) HarvardX|
### Exp: Beta-galactosidase

$\beta-glycosidic$ bond
$\alpha-glycosidic$ bond

$\beta-galactosidase$ can only hydrolysis the $\beta-glycosidic$ bond but not
$\alpha-glycosidic$ bond though they are highly similar.



## Why enzyme

### Size of the enzyme
Compared to the small active site, the enzyme is relatively large.
Role of the outside residues:
  - position the active residues in the right position
  - optimizing catalysis by induced fit
  - enzyme regulation:
    - Methylation
    - phosphorylation: tyrosine, serine, and threonine residues.
  - enzyme complexes
  - conformation changes after binding the substrate
short peptide:
  - few conformation possibilities.


### 3-point attachment model
Phenomenon: In ethanol, two hydrogen bonds to the Carbon, and both of them are equally expected to be transferred to NADH， but only one of the hydrogen could be transferred.

In this model, the enzyme attaches 3 positions of ethanol:
 - methyl group
 - hydroxyl group
 - one specific hydrogen from the methylene group


## Protein Processing

*[Allosteric]: ~~~~~~~~~~~ 〔生〕变构；别构的
*[Duodenum]: ~~~~~~~~ 十二指肠
*[Proteolytic]: ~~~~~~~~~~ 蛋白水解的 蛋白水解酶

DNA -> mRNA -> Protein ->
Post translation modification:
  - Substrate Dependence
  - Allosteric Control
  - Covalent Modification: **Phosphorylation**
  - Proteolytic: from zymogen and proenzyme to functional protein by **proteolytic enzyme digestion**.


```graphviz
digraph F {
  rankdir ="LR"
  subgraph A {
    rank = same
    node [style=filled, color = green];
    DNA
    mRNA
    Protein
  }
  subgraph cluster_0 {
    rank = same
    node [style=filled, font=Courier, color = red, shape = box];
    sub1 [label = "Substrate Dependence"]
    sub2 [label = "Allosteric Control"]
    sub3 [label = "Covalent Modification"]
    sub4 [label = "Proteolytic", shape = "", color = green ]
    style=filled;
		color=lightgrey;
		node [style=filled,color=white];
		label = "Post Translation Modification";
  }

  DNA -> DNA [label="Replication"]
  DNA -> mRNA [label = "Transcription"]
  mRNA -> Protein [label = "Translation"]
  Protein -> sub1
  Protein -> sub2
  Protein -> sub3
  Protein -> sub4
}
```

### Proteolytic

#### The fate of the protein

The different fate of protein translation:
  - Translated freely in the cytoplasm by free ribosomes
  - Transported into organisms once been translated
  - Ribosomes were soon attached to the ER and peptides went to the Golgi transport system to Plasma membrane or lysosomes.

```graphviz
digraph F {
  rankdir ="LR"
  ribosome1 [label="Free Ribosome"]
  ribosome2 [label ="ER Ribosome"]
  PM [label = "Plasma Membrane"]
  Mitochondrial [label = "Mitochondrial"]
  subgraph A {
    rank = same
    Mitochondrial
    Preoxisome
    Nuclear
    Lysosomes
    Secretory
    PM
  }

  subgraph B {
    rank = same

  }
  ｍRNA -> ribosome1 -> Cytoplasm
  ribosome1 -> Mitochondrial
  ribosome1 -> Preoxisome
  ribosome1 -> Nuclear
  ｍRNA -> ribosome2
  ribosome2 -> ER -> Golgi -> PM
  ER -> Lysosomes
  ER -> Secretory
}
```

#### Enzyme Chymotrypsin

*[zymogen]: ~~~~~~~~~~~~~~~~~~~~~~~~~ A proenzyme, or enzyme precursor, which requires a biochemical change (i.e. hydrolysis) to become an active form of the enzyme.

Chymotrypsin:
  - a zymogen
  - a digested enzyme created by the pancreas
  - Started with an inactive form: chymotrypsinogen.
  - work in the Duodenum to digest the food.
  - 245 residues

1. chymotrypsinogen + Trypsin -> 15 residues peptide + 230 residues peptide
2. $\Pi-Chymotrypsin$:
  - [1:15] S-S [16:245] (disulfide bond)
3. Autolysis:
  - [1:13] S-S [16-146] S-S [149:245]
4. the mature form of chymotrypsin: $\alpha-Chymotrypsin$

```graphviz
digraph F {
  node [style=filled, color = green, shape = box];

  P1 [label = "1-245"
        ]


  subgraph cluster_1{
    subgraph B{
      rank = same
      P3_1 [label = "1-13"]
      P3_2 [label = "16-146"]
      P3_3 [label = "149-245"]
    }
    label = "Autolysis: alpha-Chymotrypsin"
  }

  subgraph cluster_0 {
    subgraph A{
      rank = same
      P2_1 [label = "1-15"]
      P2_2 [label = "16-245"]

    }

    P2_1
    P2_2
    label ="Trypsin: pi-Chymotrypsin"
  }
  P1 -> P2_1
  P1 -> P2_2

  P2_1 -> P3_1
  P2_2 -> P3_2
  P2_2 -> P3_3
  P2_1 -> P2_2 [label ="disulfide" arrowhead = "none", color = "red"]
  P3_1 -> P3_2 [label ="disulfide" arrowhead = "none", color = "red"]
  P3_2 -> P3_3 [label ="disulfide" arrowhead = "none", color = "red"]
}
```

Insert an model:
PDBID:

### Hormone: Insulin
Insulin:
  - secreted by the pancreas;
  - regulating the level of blood glucose;

1. Rre-pro-insulin: 110 residues
2. Pro-insulin
3. Folding: intramolecular disulfide bonds link together the N-terminal and the C-terminal
4. Golgi
5. Digested to insulin + C-peptide
6. Secreted

insulin: A (N-terminal)+ B (C-terminal)
```graphviz
digraph F{
  node [shape = box]

  Pre [label = "Pre-pro-insulin"]
  Pro [label = "Pro-insulin"]

  subgraph A{
    rank = "same"
    Pro
    ProP [label = "Pro-insulin"]
    }

  ProC [label = "C-terminal"]
  ProN [label = "N-terminal"]
  subgraph B {
    rank = "same"
  }

  Pre -> Pro [label="remove part of AAs (Signal peptide)"]
  Pro -> ProP [label="folding"]
  ProN -> ProC [ label ="disulfide", color = "red", arrowhead="none"]
  ProN->ProP->ProC [arrowhead="none"]

  subgraph cluster_0{
    CP
    insulin
    style=filled;
		color=lightgrey;
		node [style=filled,color=white];
		label = "Golgi: Final Product";
  }

  CP [label="C-protein"]
  Out [label="Out Cell"]
  ProP -> CP
  ProC -> insulin
  ProN -> insulin
  CP -> Out [label="secrete"]
  insulin -> Out
}

```

C-Protein:
  Previously Recognition: It's for structure support and inactivity by-product.
  Recent research: involved in many physiological events.  
  - opposing with insulin in red blood cells

#### Case 1: Revers Regulation

In red blood cell: PDE3 + ATP -> AMP

When PED3 is deactivated: ATP is released, enzyme ENOS is working:
- ENOS + ATP + NO(nitric oxide) -> Vasodilation

C-Protein +[binding]+ GPR146 (receptors) -> PKC -> prohibited PDE3

```graphviz
digraph F{
  rankdir = "UD"

  CP [label = "C-Protein", style = "filled", color ="green"]
  insulin [style = "filled", color ="red"]
  subgraph cluster_0{

    subgraph A {
      rank = same
      marr0001
      PDE3
    }
    "marr0001" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
    "insulinR" [label = "insulin receptor"]
    ATP -> marr0001 [dir=none,weight=1]
    marr0001 -> AMP
    PDE3 -> marr0001 [label="hydrolysis"]
    GPR146 -> PDE3  [label ="Prohibited"]
    insulinR -> PDE3 [label ="Activate" arrowhead = "tee"]

    label ="Red Blood Cell"
    color = "pink"
    style=filled;
  }

  subgraph cluster_1{
    subgraph AA{
      rank = "same"
      marr0002
      marr0003
    }
    "marr0002" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
    "marr0003" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
    ENOS
    NO -> marr0003 [dir = "none"]
    marr0003 -> Vasodilation
    label = "Endothelial Cell"
  }


  CP -> GPR146
  insulin -> insulinR

  ENOS -> marr0002 [arrowhead = "none"]
  ATP -> marr0002 [arrowhead = "none"]
  marr0002 -> marr0003
}
```


#### Case 2: Both have inhibitory effects.
WBC (White blood cell):
  release cytokines-> active adhesion molecules of the endothelial cells -> WBC attach to the endothelial cell -> extravasation  
WBC binds both C-protein and insulin: **decreases** the release of cytokines:
  Prevent tissue infiltration to reduce inflammation.

```graphviz
digraph F {
  "marr0001" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  "marr0002" [shape=diamond,style=filled,label="",height=.1,width=.1] ;
  subgraph A {
    rank = same
    insulin
    marr0001
    marr0002
  }
  subgraph B {
    rank = same
    CP
    cytokines
  }
  WB [label ="White Blood Cell", shape="circle"]
  CP [label = "C-Protein", shape = "box", style = "filled", color = "green"]
  insulin [shape = "box", style = "filled", color="deeppink1"]
  infiltration [shape ="invhouse", color = "cadetblue1", style = "filled"]
  WB -> marr0002 -> cytokines -> infiltration
  CP -> marr0001
  insulin -> marr0001
  marr0001 -> marr0002 [label="Prohibit"]
}
```

#### Case 3: C-Protein mediates the tuning of insulin signaling.
- Low insulin levels:
  - C-peptide binds to the membrane receptor
  - Activate G-protein
  - Insulin signaling enhanced
- High insulin level:
  - C-peptide binds the membrane receptor
  - Activate another G-protein
  - Insulin signaling repressed

```graphviz
digraph{
  node [shape = "box"]
  Hi [label = "High insulin level"]
  Li [label = "Low insulin level"]
  Is [label = "insulin signaling" ]

  subgraph A {
    rank = same
    CP1 [label = "C-Protine"]
    "marr0001" [shape="point",style=filled,label="",height=.1,width=.1] ;
    "marr0002" [shape=point,style=filled,label="",height=.1,width=.1] ;
  }

  Hi -> marr0001 -> Receptor2 -> GP2 [ color ="green"]
  Li -> marr0002 -> Receptor1 -> GP1 [ color ="red"]
  marr0001 -> CP1 -> marr0002 [dir=none]

  GP1 -> Is [label="active", color ="red"]
  GP2 -> Is [label="prohibit", color = "green"]
}
```

Conclusion:
Protein processing is an important way to regulate protein activity:
  - Stored as precursors to avoid toxicity
  - Quick response to acute change with active precursors.
