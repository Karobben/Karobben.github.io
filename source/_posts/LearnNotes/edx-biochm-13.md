---
toc: true
url: edx_biochm_13
covercopy: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4234377/">© Baoping Zhang, et al.</a>
priority: 10000
date: 2021-04-24 15:20:24
title: "Principles of Biochemistry 13 |Glycolysis in Red Blood Cell| Class Notes |HarvardX"
ytitle: "基礎生物化學筆記 13 |红细胞的糖酵解| 哈佛 edx網課"
description: "Glycolysis in Red Blood Cell| Class Notes |HarvardX"
excerpt: "Glycolysis in Red Blood Cell; Class notes for biochemistry"
tags: [Classes, Biology, Biochemistry]
category: [Notes, Class, Biochemistry]
cover: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4234377/bin/pone.0112624.g002.jpg"
thumbnail: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4234377/bin/pone.0112624.g002.jpg"
---

## Red Blood Cell


|![Glycolysis of Red Blood Cell](https://www.researchgate.net/publication/320492390/figure/fig4/AS:551177252032512@1508422305627/Schematic-representation-of-the-Ca-2-mediated-linkage-between-activation-of-Piezo1-by.png)|
|:-:|
|[(c) Philip W Kuchel, et al.](https://www.researchgate.net/publication/320492390_Accelerating_metabolism_and_transmembrane_cation_flux_by_distorting_red_blood_cells)|


Physiological Adaptation of RBC:
  - one third of the volume is occupied by hemoglobin.
  - lack of intercellular organelles, like Mitochondrial
  - allows deformation for moving through narrow capillaries
  - lactate fermentation
  - **Cori cycle**: lactate catabolism


***Cori Cycle***

```graphviz
digraph{
  rankdir = "UD"
  node [shape = box  ]

  Lactates1 [label ="Lactate *2"]
  Lactates2 [label ="Lactate *2"]
  ATP [shape = "none"; fontcolor = "white"]
  ATP6 [label = "ATP *6"; shape = "none"; fontcolor = "white"]
  Glucose  [label = "Glucose", shape ="hexagon", height = 1]
  Glucose2 [label = "Glucose", shape ="hexagon", height = 1]

  mm1 [label = "" , shape = none, height = 0, width = 0]
  mm2 [label = "" , shape = none, height = 0, width = 0]
  mm3 [label = "" , shape = none, height = 0, width = 0]
  mm4 [label = "" , shape = none, height = 0, width = 0]

  Lactates1 -> Lactates2 [label = "transport"; style ="dashed"]
  Lactates2 -> mm2 [arrowhead = none; headport="n"]
  mm2 -> Glucose2  

  subgraph cluster_1{
    label = "Red Blood Cell"
    style =  "filled"
    color = "crimson"
    fontsize = 20

    Glucose; mm1;
    {rank=same; Glucose; Lactates1; mm1}

    Glucose->mm1 [dir = none]
    mm1 -> Lactates1
    mm1 -> ATP

  }

  subgraph cluster_2{
    label = "Liver"
    style =  "filled"
    color = "deeppink4"
    fontsize = 20

    Glucose2; Lactates2  
    ATP6 -> mm2
  }

}
```


## Rapoport-Luebering shunt
It is a pathway that converts 1, 3-bisphosphoglycerate, one intermediate of glycolysis, into its isomer, 2,3-BPG.

```graphviz
digraph{
  ATP3  [label="ATP", color="salmon", style="filled"]
  ADP3  [label="ADP"]

  BSG   [label = "1,3-\nBisphosphoglycerate", shape = underline]
  Phos  [label = "3-Phosphoglycerate", shape = underline]
  BPG   [label = "2,3 - BPG", shape = "box"]
  mm7 [label = "Phosphoglycerate\nkinase" , shape = box, color = "coral", fontcolor = "coral"]

  BSG   -> mm7    [dir = back, color = "deeppink"]
  mm7   -> Phos   [color = "deeppink"]
  BSG   -> BPG    [label ="mutase", dir=both, color = "red"]
  BPG   -> Phos   [label = "Rapoport-\nLeubering shunt", color = "red", tailport ="s"]

  {rank="same"; BSG; BPG}
  subgraph BB{
    {rank = same; ADP3; mm7}
    {rank = same; ATP3; Phos}
    ADP3 -> mm7 [arrowhead =none, headport = "s"; color = "blue"]
    mm7 -> ATP3 [tailport = "s"; color = "blue"]
  }

}
```

As a bypass pathway, the ATP generation was avoid. As a result, most cells have a very low lever of the 2,3-BPG. But it is very high in RBC since this molecule has a very important function in ==release of Oxygen==.

NADH was produced in **Glycolysis** works for maintaining the iron in Fe^2+^ state, which was used to carry the Oxygen.

##  NADH maintains reduced iron

```graphviz
digraph{
  rankdir = "LR"
  mm1 [label = "" , shape = none, height = 0, width = 0]
  mm2 [label = "" , shape = none, height = 0, width = 0]
  mm3 [label = "" , shape = none, height = 0, width = 0]

  Fe [ label = "<f1> Fe(3+)-Hb |<f2>|<f3> Fe(2+)-Hb"
              shape = "record"
              color = "white"
              ];
  cytochrome [ label = "<f1> Reduced\ncytochrome b5 |<f2>|<f3> Oxidized\ncytochrome b5"
              shape = "record"
              color = "white"
              ];

  NAD [ label = "<f1> NAD+ |<f2>|<f3> NADH"
              shape = "record"
              color = "white"
              ];

  Glu [ label = "<f1> Glyceraldehyde\n-3-P |<f2>|<f3>1,3-\nbisphosphoglycerate"
              shape = "record"
              color = "none"
              ];


  Fe:f1 -> mm1  [arrowhead = none, headport ="N", color = "red"]
  Fe:f3 -> mm1  [dir = "back", headport ="s", color = "red"]

  mm1 -> cytochrome:f1  [arrowhead = none, tailport ="N"]
  mm1 -> cytochrome:f3  [tailport ="s"]

  cytochrome:f3 -> mm2  [arrowhead = none, headport ="s", color = "red"]
  cytochrome:f1 -> mm2  [dir = "back", headport ="n", color = "red"]

  mm2 -> NAD:f1  [tailport ="n"]
  mm2 -> NAD:f3  [arrowhead = none, tailport ="s"]

  NAD:f1 -> mm3  [arrowhead = none, headport ="n", color = "red"]
  NAD:f3 -> mm3  [dir = "back", headport ="s", color = "red"]

  mm3 -> Glu:f1  [tailport ="n"]
  mm3 -> Glu:f3  [tailport ="s"]

  subgraph cluster_1{
    Glu
    label = "Glucose Glycolysis"
    style = "filled"
    color = "aquamarine2"
    fontcolor = "salmon"
    fontsize = 20
  }

}
```

## HMP shut
HMP shut could protect RBC from reactive oxygen species.
Defense against ROS

```graphviz
digraph{
  subgraph cluster_1{
    hexo2 [label = "", shape = hexagon, width = 1, height = .8]
    node [style=filled,color=white];
    label = "Glucose-6-phosphate";
    URL="https://www.bing.com";
    subgraph C{
      rank = same
      P1 -> hexo2 [dir = none, headport = "nw", arrowhead ="none"]
    }
    color = "white";
    labeljust=l
    labelloc=b
  }

  subgraph cluster_2{
    hexo3 [label = "", shape = hexagon, width = 1, height = .8]
    node [style=filled,color=white];
    label = "Fructose-6-phosphate";
    URL="https://www.bing.com";
    subgraph C{
      rank = same
      P2 -> hexo3 [dir = none, headport = "nw", arrowhead ="none"]
    }
    color = "white";
    labeljust=l
    labelloc=b
  }

  subgraph cluster_3{
    hexo4 [label = "", shape = hexagon, width = 1, height = .8]
    node [style=filled,color=white];
    label = "Fructose-1,6-phosphate";
    URL="https://www.bing.com";
    subgraph C{
      rank = same
      P3 -> hexo4 [dir = none, headport = "nw", arrowhead ="none"]
      hexo4 -> P4 [dir = none, arrowhead ="none"]
    }
    color = "white";
    labeljust=l
    labelloc=b
  }

  mm2 [label = "Phosphoglucose\nisomerase" , shape = box, color = "coral", fontcolor = "coral"]
  mm3 [label = "Phospho\nFructokinase" , shape = box, color = "coral", fontcolor = "coral"]
  mm4 [label = "Aldolase" , shape = none, color = "coral", fontcolor = "coral"]
  mm5 [label = "Triose\nphosphate\nisomerase" , shape = box, color = "coral"]
  mm6 [label = "" , shape = none, height = 0, width = 0]
  mm7 [label = "" , shape = none, height = 0, width = 0]
  P1    [label="", shape = circle, color= "cyan3", height = 0.3, width = 0.3]
  P2    [label="", shape = circle, color= "cyan3", height = 0.3, width = 0.3]
  P3    [label="", shape = circle, color= "cyan3", height = 0.3, width = 0.3]
  P4    [label="", shape = circle, color= "cyan3", height = 0.3, width = 0.3]

  hexo2 -> mm2    [dir = none , color = "deeppink"]
  mm2   -> hexo3  [  color = "deeppink"]
  hexo3 -> mm3    [dir = none , color = "deeppink"]
  mm3   -> hexo4  [ color = "deeppink"]
  hexo4 -> mm4    [dir = none , color = "deeppink"]
  mm4   -> GAP    [color = "deeppink"]
  DHAP  -> mm4    [dir = back , color = "deeppink"]
  DHAP  -> mm5    [dir = back , color = "deeppink", headport = w]
  mm5   -> GAP    [color = "deeppink", tailport = e]
  hexo2 -> mm6    [headport = "w"; dir = none]
  mm6   -> mm7    [dir = none]
  HMP   -> hexo3  [headport = "w"; color ="red"]
  HMP   -> DHAP   [headport = "w"; color ="red"]

  subgraph C{
    rank = same
    mm4
    DHAP  [label= "Dihydroxyacetone\nphosphate", shape = underline]
    GAP   [label= "Glyceraldehyde\n3-phosphate", shape = underline]
  }

  subgraph cluster_4{
    node  [shape = none]
    NADP  [label ="NADP+"]
    Red   [label = "Reduced\nglutathione"]
    Oxi   [label = "Oxidized\nglutathione"]
    DeROS [label = "Destroyed\nROS"]
    mm8 [label = "" , shape = none, height = 0, width = 0]
    mm9 [label = "" , shape = none, height = 0, width = 0]

    mm7 -> HMP
    {rank = "same";  mm6; mm7; HMP}
    NADP -> mm7  [dir = none, headport = "e"; color="red"]
    mm7 -> NADPH [tailport = "w"; color="red"]
    NADPH -> mm8 [dir = none, headport = "w"]
    mm8 -> NADP [tailport = "e", color="black"]
    {rank = "same"; NADP; NADPH}
    Oxi -> mm8 [dir = none, headport = "e"; color="red"]
    mm8 -> Red [tailport = "w"; color="red"]
    Red -> mm9 [dir = none, headport = "w"]
    mm9 -> Oxi [tailport = "e", color="black"]
    {rank = "same"; Oxi; Red}
    ROS -> mm9   [dir = none, headport = "e"; color="red"]
    mm9 -> DeROS [tailport = "w"; color="Red"]
    {rank = "same"; ROS; DeROS}

    label = "HMP shut:\ndefense\nagainst ROS"
    fontcolor = "white"
    fontsize = 20
    style = "filled"
    color = "darksalmon"
    labeljust= "l"
  }

}
```

## Oxygen Tranportaion

Conformation Chage:
  - R-State (oxygenated, high affinity)
  - T-State (non-oxygenated, low affinity)

Affinity

Cooperative binding: Dynamic Oxygen biding
  -  Releasing about 25% of oxygen
  -  When it is needed, it could releasing 75% of O~2~

$$
Hb \underset{O_ 2}{\overset{K1}{\rightleftharpoons}}
HbO_ 2 \underset{O_ 2}{\overset{K2}{\rightleftharpoons}}
Hb(O_ 2)_ 2 \underset{O_ 2}{\overset{K3}{\rightleftharpoons}}
Hb(O_ 2)_ 3  \underset{O_ 2}{\overset{K4}{\rightleftharpoons}}
Hb(O_ 2)_ 4
$$

|![Cooperative Bindg](https://z3.ax1x.com/2021/04/28/gPoaad.png)|
|:-:|
|[(c) HarvardX](https://courses.edx.org/courses/course-v1:harvardx+MCB63X+1T2021/course/#block-v1:harvardx+MCB63X+1T2021+type@sequential+block@0764db07b5c544b2ad9e7157968935d5)|

### Binding affinity change

- Leftward shift: higher affinity
- Rightward shift: lower affinity

#### PH

The PH changed, which also connected the change of concentration's level of
CO~2~:

Muscle: CO~3~, reducing the PH, which causing Rightward shift, and decreasing the affinity, increasing the releasing of the O~2~
Lungs: CO~3~ reduced, PH increased.


2,3-BPG

In the T-shape it was bond
In the R-shape, the bond was crushed and 2.3-BPG was released.
