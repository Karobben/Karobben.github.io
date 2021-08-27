---
toc: true
url: edx_biochm_23
covercopy: <a href="https://www.researchgate.net/figure/Cartoon-showing-key-features-of-glucose-metabolism-in-neurons-N-and-green-and_fig9_291388245">© Marie Elizabeth Gibbs</a>
priority: 10000
date: 2021-06-22 15:03:05
title: "Principles of Biochemistry 23 |Carbohydrate metabolism| Class Notes |HarvardX"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
ytitle: "基礎生物化學筆記 23 |糖类代谢| 哈佛 edx網課"
description: "Principles of Biochemistry 23 |Carbohydrate metabolism| Class Notes |HarvardX"
excerpt: "Carbohydrate metabolism, Edx classes, HarvardX"
cover: "https://www.researchgate.net/publication/291388245/figure/download/fig9/AS:614063138680839@1523415469695/Cartoon-showing-key-features-of-glucose-metabolism-in-neurons-N-and-green-and.png"
thumbnail: "https://www.researchgate.net/publication/291388245/figure/download/fig9/AS:614063138680839@1523415469695/Cartoon-showing-key-features-of-glucose-metabolism-in-neurons-N-and-green-and.png"
---

## Transporters

Glucose is not permeable to the cell membranes. So, the transporter is needed for cells absorbing glucose.

### Quick View: Glucose Transporters (GUL1)
- **Passive transport**: Glucose moves with the concentration gradient
- **Not a channel**: Transport is slower than diffusion

Model of **GUL1**: *Stepwise transfer*


### Monosaccharide import

Glucose, galactose, fructose use GLUT transporters.

**RBCs**: glucose and galactose but not fructose transported by ***GLUT1***
**Liver**: ***GLUT2*** transports glucose, galactose, and fructose

## Glycolysis of monosaccharide

### galactose

```graphviz
digraph{
node [shape = box]
inter1 [label="", width =0, height = 0]
inter2 [label="", width =0, height = 0]
"UDP-Glucose" [label = "UDP-Glucose", style = "filled", color = "skyblue"]
"UDP-Glucose2" [label = "UDP-Glucose", style = "filled", color = "skyblue"]

Galactose -> inter1 -> "Galactose-1-P"

"Galactose-1-P" -> inter2 -> "UDP-Galactose"  ->"UDP-Glucose" -> "Glucose-1-P" [dir = both]

ATP -> inter1 -> ADP [color = red, style = "dotted"]
"UDP-Glucose2" -> inter2 -> "Glucose-1-P" [dir = both, color = skyblue, style = "dotted"]
"UDP-Glucose2" -> "UDP-Glucose" [dir = none, style = "dotted", color = "red"]
}

```

This net gain of 2 ATP per galactose from glycolysis


### fructose

In glycolysis, hexokinase has a much higher affinity for glucose than for glucose. As a consequence, it phosphorylates the fructose only when the concentration of glucose is low. e.g.: adipocytes

$$
Fructose +ATP \overset{Fructokinase}{\longrightarrow} Fructose^ {_ -}1^ {_ -}P + ADP \overset{Aldolase}{\longrightarrow} Glyceraldehyde + DHAP + (ADP) \overset{Triose\ kinase}{\longrightarrow} Glyceraldehyde ^ {_ -} 3 ^ {_ -} P + ADP
$$
***DHAP***: Dihydroxyacetone phosphonate


### Moannose

Moannose $\to$ Glucose-6-P


## Polysaccharides

Digestion: Polysaccarides $\to$ oligosaccharides $\to$ disaccharides



## Pentose Phosphate Pathway

Oxidative

$$
Glucose^ {_ -}6^ {_ -}P + 2NADP^ + \to Ribose^ {_ -}5^ {_ -}P + 2NADPH
$$

Non-oxidative
\
$$
Ribose^ {_ -}5^ {_ -}P \overset{Transketolase}{\longrightarrow}
\ \ \overset{Transaldolase}{\longrightarrow}
Fructose^ {_ -}1,6^ {_ -} 2P
$$

NADPH = Reducing potential
- Fatty acid synthesis
- ROS neutralization

Ribose-5-P $\to$ PRPP $\to$ Nucleotide synthesis

```graphviz
digraph{
  subgraph{
    node [shape = none, weight = 0, height = 0, fontcolor="skyblue"]
    inter1 [label = "Glucose-6-P\ndehydrogenase"]
    inter2 [label = "Gluconolactonase"]
    inter3 [label = "6-Phosphogluconate\ndehydrogenase"]
    inter4 [label = "Phosphopentose\nisomerase"]
  }

  subgraph{
    node [shape = hexagon ]
    "Glucose-6-P"
    "6-Phosphoglucono-δ-lactone"
    "Ribose-5-phosphate2" [label = "Ribose-5-phosphate", shape = pentagon]
  }
  subgraph{
    node [shape = underline]
    "6-Phosphogluconate"
    "Ribulose-5-P"
    "Ribose-5-phosphate"
  }

  node [shape = line]
  "Glucose-6-P" -> inter1 -> "6-Phosphoglucono-δ-lactone" -> inter2 -> "6-Phosphogluconate" -> inter3 -> "Ribulose-5-P" -> inter4 -> "Ribose-5-phosphate" -> "Ribose-5-phosphate2" [dir = both, style="bold"]

  subgraph{
    edge [color = "red", style = "dotted"]
    "NADP⁺2" [label = "NADP⁺"]
    NADPH2   [label = "NADPH"]
    "NADP⁺" -> inter1 -> NADPH [dir = both]
    "H₂O" -> inter2 -> "H⁺" [dir = both]
    "NADP⁺2" -> inter3 -> NADPH2 [dir = both]
    inter3 -> "CO₂"
  }

}
```

|![Pentose Phosphate Pathway](https://z3.ax1x.com/2021/06/25/RlbqN6.md.png)|
|:-:|
|![Pentose Phosphate Pathway2](https://z3.ax1x.com/2021/06/25/Rlq056.md.png)|
|(c) HarvardX|

```graphviz
digraph{
  rankdir = "LR"
  node [shape=box]
  GLY [label = "Glyceraldehyde-3-P"]
  DIH [label = "Dihydroxyacetone-P"]
  FRU [label = "Fructose-1,6-P"]
  edge [dir = both, fontcolor = "skyblue"]
  subgraph{
    rank = same
    GLY ->  DIH [label = "Triose Phosphate\nisomerase"]
  }
  GLY -> FRU [label = "Aldolase"]
  DIH -> FRU [label = "Aldolase"]
  FRU -> "Fructose-6-P" [label = "Fructose-1,6-\nbisphosphate"]
}
```


## Medical Consequence

NADPH is used to turn ***oxidized Glutathione*** to ***reduced Glutathione***.

**Glutathione** could reduce the **H~2~O~2~** and **hemoglobin aggregates**.


### G6PD Deficiency

**Glucose-6-P Dehydrogenase** (***G6PD***) Deficiency

|![Glucose-6-P Dehydrogenase](https://cdn.rcsb.org/images/structures/dp/1dpg/1dpg_assembly-1.jpeg)|
|:-:|
|<a href="https://www.rcsb.org/structure/1DPG">(c) PDB:1DPG</a>|
$$
Glucose-6-P \overset{Glucose-6-P Dehydrogenase}{\longrightarrow} 6-Phosphoglucono-\delta-lactone
$$

This enzyme was made by dimer. N-terminal is the site of the NADPH interactive center. $\alpha$ and $\beta$ domains are keeping the dimer structure.

The deficiency of this enzyme

Red blood cells encounter oxidative stress - a large amount of iron & hemoglobin, highly oxygenate tissue
- lack mitochondria
- Dependent on the pentose phosphate pathway for reducing agents

Hemoglobin aggregates lead to the formation of **Heinz bodies** that affect the elastic properties of red blood cells and also contribute to hemolysis.

**Heinz bodies**:
- Heinz bodies (Heinz-Ehrlich bodies)
  - Inclusions within red blood cells composed of denaturing hemoglobin
  - The hallmark of **G6PD** deficiency

|Classes|Result|
|:-|:-|
|**I**|- Extreme deficiency - chronic haemolytic anaemia|
|**II**|- Severely deficiency (1-10% residual activity), acute haemolytic anaemia|
|**III**|- Moderately deficient(10-60%)|
|**IV**|- Normal activity (60-150%)|
|**V**|- Increased Activity(>150%)|

X chromosome linked Gene

#### Discovery

- Soldiers received Primaquine, an anti-malarial drug that adds oxidative stress to blood cells
- Some became anemic - had G6PD deficiency.
- Leading Acute hemolytic anemia (AHA)

Primaquine induces lethal oxidative damage to different strains of Plasmodium. In healthy people, the oxidative damage could be prevented by the ***reduced Glutathione***


Factors affecting the severity of ***AHA***:
- G6PD Activity
- Red Cell Aging
- Drug dose


#### Prevention
Triggering Agents
- Drug
- Ingestion of Fava Bean
- Infection
- Diseases like diabetes, myocardial infraction
- Intense physical exercise

Severe neonatal jaundice
- neurological consequences
- The peak of bilirubin in the blood due to accumulation of hemoglobin breakdown (hallmark)


Favism
- Fava beans contain high concentrations of:
  - Nonvolatile glucosides (vicine, convivine)
  - Aglycones: Produce free radicals
- Can trigger a hemolytic response in G6PD-deficient people.


Cures for G6PD Deficiency
- The most important measure is prevention - avoidance of the drugs and foods that cause hemolysis
- In severe cases of hemolysis, blood transfusions might be necessary, or even dialysis in acute renal failure.
- Some patients benefit from the removal of the spleen as red blood cells are lysed there.


The distribution of the G6PD is correlated to the distribution of malaria, which leads to a hypothesis that the G6PD is a selective advantage in parts of the world.
