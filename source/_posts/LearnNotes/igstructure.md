---
toc: true
url: igstructure
covercopy: <a href="https://www.researchgate.net/publication/337733518_Quantitative_Mass_Spectrometric_Analysis_of_Autoantibodies_as_a_Paradigm_Shift_in_Autoimmune_Serology">© Adrian Y. S. Lee</a>
priority: 10000
date: 2024-01-02 10:53:01
title: "Structure of the Immunoglobulin"
ytitle: "Structure of the Immunoglobulin"
description: "Structure of the Immunoglobulin"
excerpt: "Structure of the Immunoglobulin"
tags: []
category: []
cover: "https://www.researchgate.net/publication/337733518/figure/fig2/AS:832370903097347@1575464096611/Basic-structure-of-an-IgG-antibody-The-IgG-antibody-is-made-out-of-variable-V-and.png"
thumbnail: "https://www.researchgate.net/publication/337733518/figure/fig2/AS:832370903097347@1575464096611/Basic-structure-of-an-IgG-antibody-The-IgG-antibody-is-made-out-of-variable-V-and.png"
---

## The Structure of the Immunoglobulin

|![](https://www.researchgate.net/publication/337733518/figure/fig2/AS:832370903097347@1575464096611/Basic-structure-of-an-IgG-antibody-The-IgG-antibody-is-made-out-of-variable-V-and.png)|
|:-:|
|[© Adrian Y. S. Lee](https://www.researchgate.net/publication/337733518_Quantitative_Mass_Spectrometric_Analysis_of_Autoantibodies_as_a_Paradigm_Shift_in_Autoimmune_Serology)|

Immunoglobulins, commonly known as antibodies, are crucial proteins in the immune system that recognize and bind to specific antigens, such as bacteria and viruses, to help protect the body. Their structure is both unique and complex, consisting of several key components:

1. **Basic Structure**: Immunoglobulins are Y-shaped molecules made up of four polypeptide chains - two identical heavy (H) chains and two identical light (L) chains. These chains are held together by disulfide bonds.

2. **Variable (V) and Constant (C) Regions**:
   - **Variable Regions**: The tips of the 'Y' shape consist of the variable regions of the light and heavy chains. These regions are highly diverse and are responsible for the antigen-binding specificity of the antibody.
   - **Constant Regions**: The rest of the molecule forms the constant region, which is relatively conserved across different antibodies. The constant region of the heavy chains determines the class or isotype (e.g., IgG, IgM, IgA, IgE, IgD) of the antibody and mediates effector functions.

3. **Isotypes**: Mammals have several classes of immunoglobulins (IgG, IgA, IgM, IgE, IgD), each with different roles in the immune response. These isotypes differ mainly in their heavy chain constant regions.

4. **Glycosylation**: Many antibodies are glycosylated, meaning they have carbohydrate groups attached. This glycosylation can affect the antibody's stability, distribution, and activity.

5. **Light Chain Types**: There are two types of light chains in antibodies - kappa (==κ==) and lambda (==λ==). An individual antibody will have two identical light chains of one type.

## V(D)J

|![](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5089068/bin/nihms-673138-f0001.jpg)|
|:-:|
|[© David B. Roth](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5089068/)|

V(D)J recombination is a mechanism in the immune system that generates the immense diversity of antibodies (immunoglobulins) and T cell receptors necessary for the adaptive immune response. This process is named for the three gene segments involved in the recombination: Variable (V), Diversity (D), and Joining (J). So, V(D)J is the recombination unit.

### V(D)J in 3D Structure

We take `5wl2` as example:

|![](https://cdn.rcsb.org/images/structures/5wl2_assembly-1.jpeg)|
|:-:|
|[©PDB 5wl2](https://www.rcsb.org/structure/5wl2)|



## Kabat Number

|![Kabat number](https://assets-global.website-files.com/628cfd01406f3f5bb9c8477d/63821c6283c0cdf36d5289da_Antibody-numbering-IMGT-Kabat-Chothia.png)|
|:-:|
|[© pipebio](https://pipebio.com/blog/antibody-numbering)|

How to make it in python:

```python
import pandas as pd
from abnumber import Chain

Fasta = "xxx.fa"
with open(Fasta, 'r') as F:
    Seq = F.read()

KABAT = pd.DataFrame([dict(Chain(i, scheme='kabat')) for i in  Seq.split('\n')[:-2] if ">" not in i])
```

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
