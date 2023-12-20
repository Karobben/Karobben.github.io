---
toc: true
url: PacBio
covercopy: © Dalle3
priority: 10000
date: 2023-10-30 16:02:46
title: "Understanding PacBio Sequencing: A Deep Dive for RNA-Seq Enthusiasts"
ytitle: "Understanding PacBio Sequencing: A Deep Dive for RNA-Seq Enthusiasts"
description: "Deep dive into PacBio sequencing, its comparison with other methods, and an in-depth look into its data analysis pipeline."
excerpt: "The blog post delves into the realm of PacBio sequencing, elucidating its significance in the world of next-generation sequencing. Contrasting PacBio with other sequencing technologies, such as Illumina's short-read and Oxford Nanopore's long-read sequencing, the article highlights the unique advantages and challenges posed by each. The comprehensive PacBio data analysis pipeline is elucidated step by step, from raw data collection to final report generation. A special section is dedicated to comparing tools used in the PacBio pipeline, offering insights into their strengths and limitations."
tags: [Bioinformatics, PacBio, NGS]
category: [Biology, Bioinformatics]
cover: "https://imgur.com/lQm0SYu.png"
thumbnail: "https://i.imgur.com/lQm0SYu.png"
---


## **Introduction**:

For the seasoned RNA-Seq explorer, diving into the intricate realms of next-generation sequencing might be routine. But have you paused to marvel at PacBio sequencing, weighing its merits against other sequencing champions? Join us as we unravel PacBio's mysteries, juxtapose it with its peers, and delve into its data analysis intricacies.



## **What is PacBio Sequencing?**

|![PacBio Sequencing](https://www.liebertpub.com/cms/10.1089/gen.36.20.03/asset/images/medium/gen.36.20.03.g001.png)|
|:-:|
|[© ](https://www.liebertpub.com/doi/10.1089/gen.36.20.03)|

Pacific Biosciences, fondly termed PacBio, is the stalwart behind the long-read sequencing revolution. Standing distinct from short-read sequencers, PacBio devices unfurl considerably elongated reads, paving the path for precise assembly and a simplified data analysis voyage.



## **PacBio vs. Other Sequencing Technologies**:

* **Short-Read Sequencing (e.g., Illumina)**:
    - *Advantages*: High-throughput capabilities, economical for grand-scale endeavors, and a rich arsenal of tried-and-tested data tools.
    - *Disadvantages*: The brevity of reads can muddle the assembly of repetitive domains and hinder the detection of structural variants.
    
* **PacBio (Long-Read Sequencing)**:
    - *Advantages*: Its prowess in reading extensive DNA fragments simplifies genome assembly and eases the identification of structural variants. A boon, particularly for genomes riddled with repetitive sequences.
    - *Disadvantages*: A compromise on throughput in comparison to short-read sequencing and a heftier price tag.

* **Nanopore Sequencing (e.g., Oxford Nanopore Technologies)**:
    - *Advantages*: Astoundingly long reads, compact devices, and real-time sequencing insights.
    - *Disadvantages*: A trade-off in accuracy vis-à-vis PacBio and an evolving, thus unpredictable, tech landscape.


## PacBio Sequencing Process


|![PacBio](https://www.researchgate.net/profile/Chloe-Baum/publication/357946568/figure/fig2/AS:1114137841143808@1642642569421/Principle-of-Single-molecule-real-time-SMRT-sequencing-from-PacBio-Goodwin-McPherson.png)|
|:-:|
|[© Chloé Baum](https://www.researchgate.net/publication/357946568_New_approaches_and_concepts_to_study_complex_microbial_communities?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6Il9kaXJlY3QiLCJwYWdlIjoicHVibGljYXRpb24iLCJwcmV2aW91c1BhZ2UiOiJfZGlyZWN0In19)|

Video Tutorial:
    - [PacBio](https://www.youtube.com/watch?v=_lD8JyAbwEo)
    - [RobEdwards; SDSU](https://www.youtube.com/watch?v=-nOr5B_bF3A)

**1. SMRTbell Template Preparation**:
- DNA is fragmented to the desired length, typically ranging from a few kilobases to over 20 kb.
- Fragmented DNA is treated to create blunt ends.
- Hairpin adaptors, called SMRTbell adaptors, are ligated to these blunt ends. This results in the formation of SMRTbell templates which are essentially circular molecules of DNA.

**2. Primer Annealing and DNA Polymerase Binding**:
- A sequencing primer is annealed to the SMRTbell template.
- High-fidelity DNA polymerase is then bound to the primer-annealed SMRTbell template.

**3. Loading onto SMRT Cells**:
- The polymerase-bound SMRTbell templates are loaded onto SMRT Cells. A SMRT Cell contains up to millions of zero-mode waveguides (ZMWs).
- Only a fraction of ZMWs capture a polymerase-bound SMRTbell, ensuring each ZMW contains a single molecule.

**4. Zero-Mode Waveguides (ZMWs)**:
- ZMWs are nanophotonic structures that allow observation of individual fluorophores attached to nucleotides.
- They work by confining the observation volume to a zeptoliter level, thereby enabling the detection of single-molecule fluorescence while excluding background fluorescence.
  
**5. Sequencing by Synthesis**:
- The sequencing reaction involves the incorporation of fluorescently labeled nucleotides by the DNA polymerase.
- Each of the four DNA bases (A, T, C, G) is attached to a distinct fluorescent dye. As the polymerase adds a nucleotide to the growing DNA strand, the attached dye briefly fluoresces.
- The order in which these dyes fluoresce, as observed in real-time from the bottom of ZMWs, corresponds to the sequence of the template.

**6. Continuous Long Reads**:
- Due to the circular nature of the SMRTbell templates, the DNA polymerase can continue to sequence in a rolling-circle manner, producing long continuous reads from the same template.
  
**7. Pulse Detection and Base Calling**:
- The raw output from the sequencing process is a series of fluorescence pulses over time.
- Sophisticated algorithms analyze these pulses to detect and differentiate the fluorescent signals from each other and from the background noise.
- These detected pulses are then converted into a sequence of nucleotide bases, resulting in raw sequence reads.

**8. Circular Consensus Sequencing (CCS)**:
- Since the polymerase can sequence the same SMRTbell template multiple times, it generates several subreads from the same molecule.
- These subreads are aligned and a consensus sequence is called, enhancing the accuracy of the read by averaging out the random errors.

## **PacBio Data Analysis Pipeline**:

From raw data collation on PacBio devices to insightful report generation, the pipeline comprises:

---

**PacBio Data Analysis Pipeline: A Detailed Overview**

1. **Raw Data Collection**: 
    - *Process*: The sequencing run on a PacBio machine produces raw data files.
    - *Output*: Files in formats like `.h5` or `.bam` which encapsulate raw sequence reads, quality scores, and other metadata.

2. **Read Filtering and Quality Control**:
    - *Process*: Before analysis, raw reads undergo filtering to remove unwanted sequences.
    - *Tools*: `pbccs` (Circular Consensus Sequencing) refines raw subreads to generate high-quality consensus sequences.
    - *Output*: Filtered and high-quality sequence reads ready for further analysis.

3. **Genome Assembly (if de novo sequencing)**:
    - *Process*: Assembling the filtered reads into contiguous sequences or "contigs".
    - *Tools*: 
        - `Canu`: Corrects, trims, and assembles in one go.
        - `Flye`: Known for speed and scalability.
        - `HGAP`: PacBio's native assembler, optimized for their data.
    - *Output*: Genome assembly in the form of contigs or scaffolds.

4. **Mapping (if resequencing)**:
    - *Process*: Aligning or "mapping" the reads to a reference genome.
    - *Tools*: 
        - `pbmm2`: Tailored for PacBio data.
        - `minimap2`: Versatile and can align both PacBio and Oxford Nanopore data.
    - *Output*: Alignment file, typically in BAM or SAM format.

5. **Variant Calling**:
    - *Process*: Post alignment, identify differences or "variants" between the sequenced data and the reference genome.
    - *Tools*: 
        - `DeepVariant`: Uses deep learning for interpretation.
        - `PBSV`: PacBio's variant caller, adept at detecting larger structural variants.
    - *Output*: List of variants, typically in VCF format.

6. **Annotation and Analysis**:
    - *Process*: Predicting genes, proteins, and other genomic elements in the assembled genome or called variants.
    - *Tools*: 
        - `Prokka` (for prokaryotes)
        - `AUGUSTUS` (for eukaryotes)
    - *Output*: Annotated genome with predicted genes, regulatory elements, and other features. 

7. **Visualization**:
    - *Process*: Visual representation of the data for easier interpretation.
    - *Tools*: 
        - `IGV` (Integrative Genomics Viewer)
        - `GenomeBrowse`
        - `Circos`
    - *Output*: Graphical representation of the data, such as genome maps, variant plots, etc.

8. **Downstream Analysis**:
    - *Process*: Additional analyses based on the research question.
        - Comparative genomics: Comparing with other genomes.
        - Transcriptomics: Gene expression analysis.
        - Metagenomics: Analyzing community composition in mixed samples.
    - *Output*: Specific insights or findings related to the research question.

9. **Report Generation**:
    - *Process*: Compiling all findings, methodologies, and conclusions into a comprehensive report.
    - *Output*: Detailed report ready for review, publication, or sharing with stakeholders.

---

This detailed pipeline provides a roadmap for PacBio data analysis, guiding researchers through each stage and ensuring that they obtain meaningful and actionable insights from their data.


## The different output formats


| **Dimension** | **.h5 Format** | **.bam Format** |
|---------------|----------------|-----------------|
| **Definition** | A hierarchical data format designed to store and organize large amounts of data. | The binary version of a Sequence Alignment/Map (SAM) format, used to store aligned sequence data. |
| **Usage in PacBio** | Earlier PacBio sequencing runs produced `.h5` files as raw output. | Used as a standard format for storing aligned PacBio reads. |
| **File Size** | Generally larger due to the comprehensive information it contains about the sequencing run, including raw pulse and signal data. | Compressed and therefore more compact than its SAM counterpart. Size depends on the depth of sequencing. |
| **Content** | Contains raw sequence data, quality metrics, and other metadata about the sequencing run. | Contains aligned sequence reads, quality scores, and alignment information against a reference genome. |
| **Advantages** | Comprehensive: Contains raw data and additional metadata which can be useful for in-depth analysis. | Standardized: Widely accepted in bioinformatics pipelines and tools. Efficient storage with indexed access to alignments. |
| **Disadvantages** | File size can be substantial. Requires specific tools to extract relevant data. | Does not contain the raw signal or pulse data, only the resultant sequence and its alignment. |
| **Associated Tools** | PacBio's SMRT Analysis software can work with `.h5` files. | Numerous tools available, e.g., `SAMtools`, `Picard`, and many bioinformatics pipelines accept `.bam` files. |
| **Interoperability** | More specific to PacBio's technology and less commonly used in generic bioinformatics pipelines. | Highly interoperable and recognized as a standard format in genomics. |


Both `.h5` and `.bam` formats have their specific utilities in the realm of PacBio sequencing. While `.h5` offers a deeper dive into the raw data and sequencing intricacies, `.bam` provides a streamlined, standardized format for aligned sequence data, making it more amenable to various bioinformatics analyses.


## **Spotlight on Tools: A Comparative Table**

| **Tool** | **Type** | **Advantages** | **Disadvantages** |
|----------|----------|----------------|-------------------|
| **Canu** | Genome Assembler | Tailored for high-noise single-molecule sequencing. All-in-one: corrects, trims, and assembles. | Resource-intensive; demands hefty computational power. |
| **Flye** | Genome Assembler | Efficient for PacBio & Oxford Nanopore. Speedy and scalable. | Might struggle with highly repetitive genomes. |
| **HGAP** | Genome Assembler | PacBio's native. Stellar for microbial genomes. | Challenges with mammoth genomes. Demands high coverage. |
| **pbmm2** | Mapping Tool | Custom-made for PacBio data. Handles long-read errors well. | PacBio-specific; lacks versatility. |
| **minimap2** | Mapping Tool | Swift and versatile. Aligns both PacBio and Oxford Nanopore data. | Optimal results might need parameter fine-tuning. |
| **DeepVariant** | Variant Caller | Harnesses deep learning for high accuracy. Adapted for long-reads. | Computationally taxing. Might be overwhelming for ML novices. |
| **PBSV** | Variant Caller | Fine-tuned for PacBio. Excels in detecting large structural variants. | Exclusively for PacBio data. |

---

## **Conclusion**:

While RNA-Seq has its allure, navigating the PacBio seas can offer refreshing insights. With its long-read capabilities, PacBio emerges as a formidable contender in the sequencing arena. As with every tech marvel, it presents both opportunities and challenges. Yet, armed with the right tools and insights, one can sail smoothly through the PacBio waters, discovering genomic treasures along the way.

To sequencing and beyond!


## More to know

### What is flank sequence

In the context of PacBio sequencing, "flanking sequences" or "flanks" often refer to the sequences on ==either side of a particular region of interest within the DNA==. These regions can be particularly important in various analyses such as structural variation detection, insertions, deletions, or when identifying the context of a specific mutation or sequence feature.

However, when referring to "flank sequences" in relation to PacBio's SMRTbell library preparation, it has a more specific meaning. For PacBio SMRT sequencing, the DNA of interest is ligated to hairpin adapters at both ends, creating a SMRTbell template. These hairpin adapters allow the DNA polymerase to read the same molecule multiple times, moving in a circular fashion. ==The sequences directly adjacent to these adapters on the SMRTbell template are often referred to as the "flanking sequences".==

These flanking sequences are typically removed during data processing to retain only the sequence of interest. In the context of the raw PacBio reads, you might sometimes see remnants of these adapter sequences or the flanking regions, especially if there was any inefficiency in the adapter trimming process.

If you're dealing with PacBio data and want to identify or remove such sequences, tools and workflows provided by PacBio, such as the SMRT Link software suite, can help in the adapter trimming and filtering process.

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
