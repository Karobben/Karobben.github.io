---
toc: true
url: immun
covercopy: © Karobben
priority: 10000
date: 2023-10-31 13:45:08
title: "Understanding Antibodies and Phage Display: A Deep Dive"
ytitle: "Understanding Antibodies and Phage Display: A Deep Dive"
description: "Understanding Antibodies and Phage Display: A Deep Dive"
excerpt: "In the evolving realm of biotechnology, antibodies and phage display stand as two pillars of immense significance. This article delves into the structural intricacies of antibodies, emphasizing their heavy and light chains, along with the pivotal Complementarity-Determining Regions (CDRs). Furthermore, the article illuminates the concept of phage display, a groundbreaking technique that bridges genotypic information with phenotypic expression, offering a high-throughput approach to study protein interactions. Illustrated with detailed visuals, the piece offers readers an in-depth understanding of these subjects, underscoring their paramount importance in modern medicine and research."
tags: [Biology, Immunology, Antibody]
category: [Notes, Biology, Immunity]
cover: "https://imgur.com/ZPxhVgf.png"
thumbnail: "https://imgur.com/ZPxhVgf.png"
---



## **The Magnificent World of Antibodies**

Antibodies, also known as immunoglobulins, are Y-shaped proteins produced by the immune system to neutralize foreign substances like bacteria and viruses. Let's break down the components:

### **Heavy Chain & Light Chain**

The basic structure of an antibody is composed of two identical heavy chains and two identical light chains. Each chain is a sequence of amino acids, which fold into a specific three-dimensional shape.

- **Heavy Chain (H)**: The heavy chains are the larger of the two, and they form the base of the Y-shape. They play a pivotal role in determining the class of an antibody (like IgG, IgM, IgA, etc.).

- **Light Chain (L)**: The light chains pair with the heavy chains to form the arms of the Y-shaped antibody. Each antibody has one of two types of light chains - either kappa (κ) or lambda (λ).

### **Complementarity-Determining Regions (CDR)**

|![CDR](https://www.rapidnovor.com/wp-content/uploads/2022/04/Antibody-CDR-600x273.png)|
|:-:|
|[Yuning Wang, PhD](https://www.rapidnovor.com/identifying-cdrs-antibody-sequencing/)|

The tips of the "Y" arms contain a special region known as the CDR. This region is responsible for recognizing and binding to specific parts of foreign invaders, called antigens. Each antibody has six CDRs (three from the light chain and three from the heavy chain), which collectively determine its specificity. It's like the "lock and key" model; the CDR is the lock, and the antigen is the key.

## **The Magic of Phage Display**

Phage display is a high-throughput technology used to study protein-protein, protein-peptide, and protein-DNA interactions. It's like a library, but instead of books, we have bacteriophages - viruses that infect bacteria.

### **Basics of Phage Display**

|![Different types of phage](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656071/bin/hvi-8-1817-g1.jpg)|
|:-:|
|[© Justyna Bazan](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656071/)|

In phage display, a gene encoding a protein or peptide of interest is fused to a coat protein gene of a bacteriophage, causing the displayed protein to be expressed on the outside of the phage particle. This allows the protein to be physically linked to the genetic information that encodes it.

### **Display of antibody fragments**

Typically, antibodies comprise two heavy chains and a pair of light chains interconnected through noncovalent bonds and disulfide bridges. However, unique antibodies without light chains, found in Camelidae serum, bind antigens using a specific V~H~H fragment. This fragment can recognize distinctive conformational epitopes due to its extended complementary-determining region 3 (CDR3). 

Antibody fragments' expression in E. coli necessitates in vivo refolding to maintain their activity and function. A method for soluble recombinant protein expression in the cytoplasm of the Origami DE3 E. coli strain has been introduced. This method enhances the folding of heterologous proteins dependent on disulfide bonds. Intriguingly, scFv expressed in the bacterial cytoplasm displayed superior binding characteristics compared to periplasmic expression. While periplasmic expression offers suitable conditions for V~H~ and V~L~ pairing, co-expression of periplasmic chaperones has shown to significantly impact soluble scFv productivity.

Various antibody fragments, including Fab, Fv, scFv, and their modifications, are employed in phage display technology. These fragments, particularly scFv, have been expressed on the phage surface without compromising antibody affinity. The CRAbs construct, comprising two scFv fragments targeting adjacent epitopes, is one notable example.


|![Schematic presentation of antibody fragments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656071/bin/hvi-8-1817-g2.jpg)|
|:-:|
|[© Justyna Bazan](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3656071/); Fab (the antigen-binding fragment), scFab (the single chain antigen-binding fragment), scFabΔC (the scFab variant without cysteins), scFv (the single chain fragment variable), Fv (the fragment variable), VHdAb (the antibody with one variable heavy chain domain), CRAb (the construct specific to adjacent epitopes on the antigen)|

| Antibody Fragment | Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
| **Fab**           | VH-CH and VL-CL segments linked by disulfide bonds. Used in tumor imaging.                       |
| **Fv**            | Comprises only the VL and VH regions.                                                            |
| **scFv**          | A commonly used antibody fragment consisting of VL and VH regions stabilized by (Gly4Ser)3 linker.|
| **VHH**           | Unique fragment found in Camelidae serum antibodies, targeting unique conformational epitopes.    |
| **CRAbs**         | Construct with two scFv fragments specific to adjacent epitopes of the same antigen.             |
| **Diabodies**     | Formed by dimerization of molecules and connection of antibody fragments.                        |


### **Technical Details of Phage Display**

#### **1. Phage Biology Basics:**
- **Bacteriophages**, or phages, are viruses that infect bacteria. They are composed of a protein coat that encases their genetic material, which can be either DNA or RNA.
- The life cycle of a phage includes attaching to a bacterial cell, injecting its genetic material, and then using the host's machinery to replicate and produce new phage particles.

#### **2. Fusion Proteins in Phage Display:**
- The principle behind phage display is the creation of **fusion proteins**. A gene of interest (encoding the protein or peptide to be displayed) is inserted into a phage coat protein gene, leading to the expression of a fusion protein on the phage surface.
- Commonly used coat proteins for display include **pIII** and **pVIII** of the M13 filamentous phage.

#### **3. Constructing the Library:**
- A diverse collection of DNA sequences is cloned into phage vectors to produce a **library**. This library represents a vast array of different peptides or proteins displayed on the phage surface.
- The library's diversity can range from millions to billions of unique sequences, making it a powerful tool for screening.

#### **4. Biopanning and Selection:**
- **Biopanning** is the iterative process of enriching phages that bind to a specific target from a diverse library.
- The process involves incubating the phage library with a target (e.g., a protein, cell, or tissue), washing away non-binding phages, and then amplifying the bound phages by infecting bacteria. This cycle is typically repeated several times to enrich for high-affinity binders.

#### **5. Elution and Analysis:**
- After the final round of biopanning, bound phages are eluted, often by changing pH or adding a competitive ligand.
- The DNA from these phages is then sequenced to identify the displayed peptides or proteins. Modern techniques like **next-generation sequencing** can be used to analyze vast numbers of sequences simultaneously.

#### **6. Applications in Drug Discovery:**
- Phage display is instrumental in **antibody engineering**. Therapeutic antibodies like adalimumab (Humira) were discovered using phage display.
- It's also used to discover peptide ligands for various targets, which can lead to the development of new drugs or diagnostic tools.

#### **7. Challenges and Considerations:**
- While phage display is a powerful tool, it's essential to consider factors like the library's quality and diversity, the stringency of washing steps during biopanning, and potential biases introduced during phage amplification.
- Some proteins or peptides may not be displayed well on the phage surface due to folding issues or interference with phage assembly.


### **Advanced Insights**

- **Library Creation**: Scientists can create vast libraries of phages displaying a diverse array of peptides or proteins. When looking for a needle in a haystack (like a specific antibody for a new disease), this library becomes invaluable.

- **Biopanning**: This is the process of selecting phages that bind to a specific target. The library is exposed to a target (like a protein receptor), and non-binding phages are washed away. Those that bind are amplified, creating a pool of potential candidates.

- **Applications**: Phage display has revolutionized medicine, especially in the field of drug discovery. It's instrumental in identifying therapeutic antibodies, understanding disease mechanisms, and even vaccine development.


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
