---
toc: true
url: edx_biochm_14
covercopy: <a href="https://www.researchgate.net/publication/331874089_Clostridium_difficile_Modulates_the_Gut_Microbiota_by_Inducing_the_Production_of_Indole_an_Interkingdom_Signaling_and_Antimicrobial_Molecule">© Charles Darkoh, et al.</a>
priority: 10000
date: 2021-04-28 15:56:45
title: "Principles of Biochemistry 14 |Glycolysis in Bacterial| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 14 |细菌的糖酵解| 哈佛 edx網課"
description: "Glycolysis in Bacterial| Class Notes |HarvardX"
excerpt: "Glycolysis in Bacteriall; Class notes for biochemistry"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
cover: "https://www.researchgate.net/publication/331874089/figure/fig5/AS:749473122766852@1555699725803/A-proposed-model-for-interaction-of-the-gut-microbiota-and-indole-production-during-C.jpg"
thumbnail: "https://www.researchgate.net/publication/331874089/figure/fig5/AS:749473122766852@1555699725803/A-proposed-model-for-interaction-of-the-gut-microbiota-and-indole-production-during-C.jpg"
---

## Aerobes Condition

Metabolic pathways in becteria that operate with Low O~2~

Exp: ***E. Coli***

Multiple fermentation product:
For example, lactate, ethanol, acetate, citrate.

|![Fermentation Pathways](https://z3.ax1x.com/2021/04/28/gPqwg1.png)|
|:-:|
|(C) HarvardX|


|![Lactate and Ethanol Fermentation](https://z3.ax1x.com/2021/04/28/gPLBGj.png)|
|:-:|
|(C) HarvardX|




## Fermentation Branches

|![E.Coli Fermentation](https://z3.ax1x.com/2021/04/28/gPL0iQ.png)
|:-:|
|(C) HarvardX|


## Anaerobic Respiration and ATP

|Respiration Type|O~2~|Electron Receptor|Product|$\Delta G (kJ/2e^ -)$|
|:-|:--:|:-|:-|:-|
|Cellular Respiration| O~2~ is sufficient| O~2~| H~2~O|-219.07|
|Fermentation|  O~2~ is not used|Varieties|Varieties|
|Anaerobic (Denitrifier))| O~2~ is not used|NO~3~^-^|N~2~|-209.46|
|Anaerobic (Metal Reducer))| O~2~ is not used|Fe^3+^|Fe^2+^|-206.12|
|Anaerobic (Sulfidogen))| O~2~ is not used|SO~4~^2-^|HS^-^|-20/24|
|Anaerobic (Mehtanogen))| O~2~ is not used|CO~2~|CH~4~|-14.58|


## Dinitrifying

```graphviz
digraph{
  rankdir = "LR"
  mm1 [label="", shape=none, width=0, height = 0]
  NO [label="<f1>NO2- + 2H+|<f2>|<f3>NO + H2O",
       shape = "record", color = "none"]
  Fe [label="<f1>Fe2+|<f2>|<f3>Fe3+",
      shape = "record", color = "none"]
  NO3 -> NO:f1
  NO:f1 -> mm1 [dir =none, headport = n]
  NO:f3 -> mm1 [dir =back, headport = s]
  mm1 -> Fe:f1 [dir =none, tailport = n]
  mm1 -> Fe:f3 [tailport = s]
}
```
Fe^2+^: Ferrous iron hemoglobin
Fe^3+^: Ferric iron methemoglobin

$2NO_ 3 ^- + 12H^ + 10 e^ - \to N_ 2 + 6 H_ 2O$
$NO_ 3 ^- \to NO_ 2 ^-$ **Nitrate** to **Nitrite**
$NO_ 2 ^- \to NO$ **Nitric oxide**
$NO\ \  \to N_ 2O$ **Nitrous oxide**
$N_ 2O\  \to N_ 2$ **Dinitrogen**

|(C) HarvardX; Dinitrifying|
|:-:|
|![Dinitrifying](https://z3.ax1x.com/2021/04/28/gi9OT1.png)|
|![Dinitrifying](https://z3.ax1x.com/2021/04/28/gi9LwR.png)|

## Bacterial and human health

The exist of  bacterial:
Colonization:
- Begins at birth
- First from mother
- Then from environment

Diversity:
- Nutrient availability
- Physical/chemical environment
- Anti-microbial defenses
- Microbe interaction and modification of the local environment

Beneficial:
  - Pathogen defence
  - Metabolic function
  - Immune system maintain
  - Energy balance

Disrabtion:
