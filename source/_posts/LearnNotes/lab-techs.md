---
toc: true
url: lab_techs
covercopy: © Karobben
priority: 10000
date: 2022-11-09 13:54:20
title: "Wet Lab Techs with Brief Explained"
ytitle: "Wet Lab Techs with Brief Explained"
description: "Wet Lab Techs with Brief Explained"
excerpt: "Wet Lab Techs with Brief Explained"
tags: [Biology, Wet, Protocol]
category: [Biology, Wet Protocol]
cover: "https://s1.ax1x.com/2022/11/10/zSvqbD.png"
thumbnail: "https://s1.ax1x.com/2022/11/10/zSvqbD.png"
---

## Wet Lab Techs with Brief Explained

## Gel Shift Assays–EMSA

!!! note What is EMSA
    The interaction of proteins with DNA is central to the control of many cellular processes including DNA replication, recombination and repair, transcription, and viral assembly. One important technique for studying gene regulation and determining protein–DNA interactions is the electrophoretic mobility shift assay (EMSA). An advantage of studying protein–DNA interactions by an electrophoretic assay is the ability to resolve complexes of different stoichiometry or conformation. Another major advantage is that the source of the DNA-binding protein may be a crude nuclear or whole cell extract, in vitro transcription product or a purified preparation. EMSA can be used qualitatively to identify sequence-specific, DNA-binding proteins (such as transcription factors) in crude lysates and, in conjunction with mutagenesis, to identify the important binding sequences within the upstream regulatory region of a given gene. EMSA can also be utilized quantitatively to measure thermodynamic and kinetic parameters.
    [@ ThermoFisher 2022](https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-biology-learning-center/protein-biology-resource-library/pierce-protein-methods/gel-shift-assays-emsa.html)

Brief explained: During Gel electrophoration, if we add DNA (oligo) and protein together and the protein could interact with the DNA, the transfer speed of DNA is much slower because protein is dragging them.

One of a standard kit for EMSA:
|[LightShift™ Chemiluminescent EMSA Kit](https://www.thermofisher.com/order/catalog/product/20148) from thermofisher. ([documentation](https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets%2FLSG%2Fmanuals%2FMAN0011409_LightShift_Chemiluminescent_EMSA_UG.pdf))|![](https://www.thermofisher.com/TFS-Assets/LSG/product-images/20148-DNA-EMSA-Kit-b.jpg-650.jpg)|
| :------------- | :------------- |

|![](https://s1.ax1x.com/2022/11/10/zSvqbD.png)|
|:-:|
|[© ThermoFisher](https://www.thermofisher.com/order/catalog/product/20148)|

According its documentation, a group should have at least 3 tracks:
1. labeled DNA: which works as negative control. It shows them band when there are no protein-DNA interaction.
2. labeled DNA + protein: The main track for results. The position of DNA shifts because proteins interact with them. The movement of DNA is hindered by proteins.
3. labeled DNA + protein + overload unlabeled DNA: By competition, most proteins interact with unlabeled DNA because the quantity of them is higher them labeled. As a result, we can see a dim-shifted band or no shifted band at all. The track could eliminate false positives brought by protein-label tag binding.

Publication used:
- Shyamsunder, Pavithra, et al. "Identification of a novel enhancer of CEBPE essential for granulocytic differentiation." Blood, The Journal of the American Society of Hematology 133.23 (2019): 2507-2517.

### Eamples in paper

|![](https://s1.ax1x.com/2022/11/10/zSxCKf.png)|
|:-:|
|[© Shyamsunder, 2019](https://ashpublications.org/blood/article/133/23/2507/273839/Identification-of-a-novel-enhancer-of-CEBPE)|

In this paper, they showed the 4~th~ track, which is protein + unlabeled DNA. In the panel right, there are weak shifted bind which could be the protein.


## Luciferase Report Assay

!!! note What is a Luciferase Report Assay?
    A luciferase reporter assay is a test that investigates whether a protein can activate or repress the expression of a target gene using luciferase as a reporter protein ([Carter & Shieh, 2015](https://www.sciencedirect.com/science/article/pii/B9780128005118000150?via%3Dihub)). The synthesis of the reporter protein and the addition of a substrate results in a chemical reaction with bioluminescence (or the emission of photons) as a by-product. This bioluminescence directly corresponds with the effect of the protein on expression of the target gene.
    [© GoldBio, 2022;](https://goldbio.com/articles/article/a-deep-dive-into-the-luciferase-assay-what-it-is-how-it-works-and-more)


|![](https://www.jbc.org/cms/attachment/6d2ce07c-a367-4fc6-8d4f-c2e1efbe40b5/gr1.jpg)|
|:-:|
|[© Scholl, et al., 2014](https://www.sciencedirect.com/science/article/pii/S0021925820371155?via%3Dihub)|
|![](https://commercio.nyc3.digitaloceanspaces.com/goldbio-2018/pages/Functional%20luc.png)|
|[© GoldBio, 2022;](https://goldbio.com/articles/article/a-deep-dive-into-the-luciferase-assay-what-it-is-how-it-works-and-more)|


Scholl, Zackary & Yang, Weitao & Marszalek, Piotr. (2014). Chaperones Rescue Luciferase Folding by Separating Its Domains. The Journal of biological chemistry. 290. 10.1074/jbc.M114.582049.


After inserting the target DNA segment in the plasmid, the vector is transferred into cells. If proteins could interact with the segment, luciferase would express and cells could illuminate.

|![](https://www.researchgate.net/profile/Chrysostomos-Tornari/publication/44789832/figure/fig11/AS:906421684170753@1593119178226/pGL410luc2-vector-Schematic-diagram-of-the-pGL410luc2-luciferase-reporter-vector.jpg)|
|:-:|
|[© Chrysostomos Tornari; 2010](https://www.researchgate.net/figure/pGL410luc2-vector-Schematic-diagram-of-the-pGL410luc2-luciferase-reporter-vector_fig11_44789832)|
































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
