---
toc: true
url: paper_3
covercopy: © Karobben
priority: 10000
date: 2023-03-16 09:40:32
title: "paper revise3"
ytitle: "paper"
description: "paper"
excerpt: "123"
tags: ""
category: ""
cover: ""
thumbnail: ""
---

## paper revise

## Abstract

Tumors vary greatly in their characteristics and underlying mechanisms. Drosophila provides an excellent model for studying tumor similarity and mechanisms due to its well-understood background and relatively simple genome size and gene-gene interactions. In this study, we downloaded and re-processed over 500 tumor samples from the fly model and found that tumor initiation is not always associated with high proliferation and evading death. By utilizing bioinformatic methods, we identified that under excellent control of Wnt and JNK, cells may not need to show these characteristics to initiate tumors. These findings provide a new perspective on the mechanisms underlying tumor initiation in Drosophila.

## Introduction

The fruit fly has a long history as a model organism, with Thomas Hunt Morgan being one of the first scientists to make major contributions to fruit fly experiments in the 1900s and pushing this organism onto the stage of genetics. Drosophila melanogaster (Dmel), which is one of the most popular species among other fruit flies, is widely used in genetic, longevity, development, and behavior studies. The merits of Dmel are outstanding, including low cost, rapid generation, lots of offspring, well-defined phenotype corresponding genotype, a short life span, an elegant genome, and simplified but highly homologous pathways. All of these advantages have made Dmel an ideal and irreplaceable experimental organism and have also contributed to many early Nobel Prizes, including those by Thomas Hunt Morgan[^Morgan_16] and Hermann Muller[^Muller_28].

Other model organisms such as Caenorhabditis elegans also know as roundworm have also been noted for their simple genome size. However, Dmel stands out as a model organism due to its 60% homologous gene sharing with humans, with 75% of these genes being responsible for human diseases[^Ugur_B_16]. This feature makes Dmel a popular model organism for studying diseases such as Alzheimer's, non-specific immunity, muscle development diseases, and various types of cancer. In particular, research on Dmel tumors has seen an exponential increase since the 1990s[^Mirzoyan_19].

The majority of human cancers exhibit well-described hallmarks including sustaining proliferative signaling, evading growth suppressors, activating invasion and metastasis, enabling replicative immortality, inducing angiogenesis, and resisting cell death, as previously described by Hanahan and Weinberg[^Hanahan_11]. These hallmarks have also been observed in fly tumor models. Mutated clones of the scribble gene in Drosophila larvae have developed tumors on the wing disc (WD), leading to sustained proliferation and abnormal growth, ultimately resulting in larval death[^Ji_19_Disease]. Autophagy is observed in these tumors, but when the ras signaling pathway is overactivated, the tumor can evade death and continue to proliferate[^Uhlirova_06]. Salivary gland tumors induced by Notch in Drosophila also display invasive properties[^Jhappan_1992][^Yang_19]. However, Drosophila tumors cannot persist for long periods as it leads to cachexia-like wasting and early death[^Figueroa_15]. Transplanting tumor tissue into the abdomen of Drosophila and passing it on to subsequent generations demonstrates that the tumor can establish itself as an immortal cell line[^Jiang_18_NC]. These findings confirm the similarities between human and Drosophila tumors and establish Drosophila as a useful model organism for studying tumor initiation, progression, and the ultimate outcome of cachexia and host death.

The Drosophila WD is a valuable tool for investigating well-regulated differentiation and tumor initiation. Through elegantly regulated signaling pathways such as Hippo and Wnt, the WD can increase its size by a thousand-fold in just five days. The expression of dlg-IR can induce apoptosis and an invasion-like phenotype in the WD. Meanwhile, in egr^-/-^ clones, cell death in the WD is entirely blocked. Moreover, a well-established study demonstrated that lgl4 mutants can initiate tumors in the WD[^Agrawal_95]. Additionally, Sun et al. showed that Yki mutation can also lead to WD tumors[^sun_2011]. Finally, Wts mutation could also cause WD tumors[^Pascual_17].

The eye disc was initially introduced in 1976 as a model for developmental biology research[^Ready_76]. The Hedgehog (Hh) signaling pathway plays a crucial role in eye development and differentiation[^Heberlein_95], and it can regulate critical genes through the Notch signaling pathway[^Fu_03_dev]. Delta (DL), a transmembrane ligand of the Notch receptor, has downstream effects controled by the Hh signaling pathway[^Parks_95]. The conserved subunit complex CCR4-NOT plays a role as a tumor suppressor by regulating gene expression[^Collart_12]. Overexpressing DL and knocking down CCR4-NOT together can result in the development of Drosophila eye tumors[^Vicente_18]. Polycomb group (PcG) protein PRC1 (ph) is another gene that regulates gene expression[^Grossniklaus_14]. It suppresses tumor growth in Drosophila by repressing the Notch signaling pathway[^Martinez_09]. Knocking down ph can induce the development of eye disc tumors, which can survive and grow larger after transplantation into the abdomen[^Torres_18][^Loubiere_16][^Jiang_18_NC].

Ras is an enzyme that catalyzes the conversion of inosine monophosphate (IMP) to guanosine monophosphate (GMP) and thereby regulates cell growth[^Nash_94]. Scrib is a gene that encodes a protein with an essential role in cell polarity[^Bilder_00] and growth[^Albertson_03]. It can directly target the Hippo signaling pathway and modulate cell growth[^shen_21]. While overexpression of activated ras alone is not sufficient to induce tumor in the WD, mutated ras alone is adequate to initiate tumor in the Dmel eye disc[^Külshammer]. Knockdown of scrib alone could induce WD tumor[^Ji_19_Disease], but not eye disc tumor[^Atkins_16]. However, the simultaneous overexpression of activated ras and knockdown of scrib can cause more aggressive tumors in both the eye and WDs[^Atkins_16][^Külshammer][^Hodgson_16].


WNT signals are responsible for cell fate determination through the canonical pathway and control of cell movement and tissue polarity through the noncanonical pathway[^Logan_04]. The canonical pathway is activated by the Frizzled (FZD) family receptors and lipoprotein-related receptors 5 and 6 (LRP5/LRP6) coreceptor which transduces signals to the β-catenin signaling cascade[^Bhanot_96]. In the absence of WNT signals, the scaffold protein APC (adenomatous polyposis coli) forms a degradation complex with other proteins such as AXIN, CKIα (casein kinase Iα), and GSK3β (glycogen synthase kinase 3β) to promote β-catenin degradation[^Price_2006]. In the noncanonical pathway, Dishevelled, which is also required in the canonical pathway, activates the JNK signaling pathway[^Boutros_98][^Majidinia_17]. P53 is an essential oncogene that coordinates the DNA repair system and the cell cycle checkpoint[^Karimian_16], and it is crucial for cancer cell fate. On one hand, p53 mediates the degradation of β-catenin via E3 ubiquitin ligase[^Matsuzawa_01]. On the other hand, the canonical Wnt signaling pathway up-regulates the expression of the p14/p19^ARF^ (ARF)  tumor suppressor protein and directly activates p53 to trigger a p53 response[^Oren_02].

Scrib^-^ has been found to activate the Hippo Signaling pathway, leading to tumor initiation; however, the cell would simultaneously activate the JNK signaling pathway, inducing apoptosis[^Chen_12]. JNK is a well-known molecule that has been identified as both a tumor suppressor and a contributor to tumor initiation[^Tournier_13][^Kennedy_03_cc]. While some studies suggest that JNK is not essential for fibroblast tumor formation in mice[^Kennedy_03], in our case, it appears to play a critical role in tumor initiation in ras-scrib model. The ras-scrib eye disc tumor is ras^V12^/scrib^-^ extremely malignant tumor, and bsk^-^ has the potential to almost entirely rescue the tumor phenotype[^Uhlirova_05][^Brumby_03].

[^Uhlirova_05]: Uhlirova, Mirka, Heinrich Jasper, and Dirk Bohmann. "Non-cell-autonomous induction of tissue overgrowth by JNK/Ras cooperation in a Drosophila tumor model." Proceedings of the National Academy of Sciences 102.37 (2005): 13123-13128.
[^Brumby_03]: Brumby, Anthony M., and Helena E. Richardson. "scribble mutants cooperate with oncogenic Ras or Notch to cause neoplastic overgrowth in Drosophila." The EMBO journal 22.21 (2003): 5769-5779.
[^Chen_12]: Chen, Chiao-Lin, et al. "Tumor suppression by cell competition through regulation of the Hippo pathway." Proceedings of the National Academy of Sciences 109.2 (2012): 484-489.
[^Oren_02]: Oren, Moshe, et al. "Regulation of p53: intricate loops and delicate balances." Annals of the New York Academy of Sciences 973.1 (2002): 374-383.
[^Matsuzawa_01]: Matsuzawa, Shu-ichi, and John C. Reed. "Siah-1, SIP, and Ebi collaborate in a novel pathway for β-catenin degradation linked to p53 responses." Molecular cell 7.5 (2001): 915-926.
[^Karimian_16]: Karimian, Ansar, Yasin Ahmadi, and Bahman Yousefi. "Multiple functions of p21 in cell cycle, apoptosis and transcriptional regulation after DNA damage." DNA repair 42 (2016): 63-71.
[^Majidinia_17]: Majidinia, Maryam, and Bahman Yousefi. "Breast tumor stroma: A driving force in the development of resistance to therapies." Chemical biology & drug design 89.3 (2017): 309-318.
[^Boutros_98]: Boutros M, Paricio N, Strutt DI, et al. Dishevelled activates JNK and discriminates between JNK pathways in planar polarity and wingless signaling. Cell 1998;94:109–18.
[^Price_2006]: Price MA. CKI, there's more than one: casein kinase I family members in Wnt and Hedgehog signaling. Genes Dev 2006;20:399–410.
[^Bhanot_96]: Bhanot P, Brink M, Samos CH, et al. A new member of the frizzled family from Drosophila functions as a Wingless receptor. Nature 1996;382:225–30.
[^Logan_04]: Logan, Catriona Y., and Roel Nusse. "The Wnt signaling pathway in development and disease." Annu. Rev. Cell Dev. Biol. 20 (2004): 781-810.

[^shen_21]: Shen, Hengyang, et al. "SCRIB promotes proliferation and metastasis by targeting Hippo/YAP signalling in colorectal cancer." Frontiers in cell and developmental biology 9 (2021): 656359.
[^Hodgson_16]: Hodgson, Joseph A., et al. "Drosophila larval models of invasive tumorigenesis for in vivo studies on tumour/peripheral host tissue interactions during cancer cachexia." International Journal of Molecular Sciences 22.15 (2021): 8317.
[^Atkins_16]: Atkins, Mardelle, et al. "An ectopic network of transcription factors regulated by hippo signaling drives growth and invasion of a malignant tumor model." Current Biology 26.16 (2016): 2101-2113.
[^Külshammer]: Külshammer, Eva, et al. "Interplay among Drosophila transcription factors Ets21c, Fos and Ftz-F1 drives JNK-mediated tumor malignancy." Disease models & mechanisms 8.10 (2015): 1279-1293.
[^Albertson_03]: Albertson, Roger, and Chris Q. Doe. "Dlg, Scrib and Lgl regulate neuroblast cell size and mitotic spindle asymmetry." Nature cell biology 5.2 (2003): 166-170.
[^Bilder_00]: Bilder, David, Min Li, and Norbert Perrimon. "Cooperative regulation of cell polarity and growth by Drosophila tumor suppressors." Science 289.5476 (2000): 113-116.
[^Nash_94]: Nash, D., et al. "The raspberry locus of Drosophila melanogaster includes an inosine monophosphate dehydrogenase like coding sequence." Genome 37.2 (1994): 333-344.
[^Loubiere_16]: Loubiere, Vincent, et al. "Coordinate redeployment of PRC1 proteins suppresses tumor formation during Drosophila development." Nature genetics 48.11 (2016): 1436-1442.
[^Torres_18]: Torres, Joana, et al. "A switch in transcription and cell fate governs the onset of an epigenetically-deregulated tumor in Drosophila." Elife 7 (2018): e32697.
[^Martinez_09]: Martinez, Anne-Marie, et al. "Polyhomeotic has a tumor suppressor activity mediated by repression of Notch signaling." Nature genetics 41.10 (2009): 1076-1082.
[^Grossniklaus_14]: Grossniklaus, Ueli, and Renato Paro. "Transcriptional silencing by polycomb-group proteins." Cold Spring Harbor perspectives in biology 6.11 (2014): a019331.
[^Collart_12]: Collart, Martine A., and Olesya O. Panasenko. "The Ccr4–not complex." Gene 492.1 (2012): 42-53.
[^Vicente_18]: Vicente, Carmen, et al. "The CCR4-NOT complex is a tumor suppressor in Drosophila melanogaster eye cancer models." Journal of Hematology & Oncology 11.1 (2018): 1-16.
[^Parks_95]: Parks, Annette L., F. Rudolf Turner, and Marc AT Muskavitch. "Relationships between complex Delta expression and the specification of retinal cell fates during Drosophila eye development." Mechanisms of development 50.2-3 (1995): 201-216.
[^Fu_03_dev]: Fu, Weimin, and Nicholas E. Baker. "Deciphering synergistic and redundant roles of Hedgehog, Decapentaplegic and Delta that drive the wave of differentiation in Drosophila eye development." (2003): 5229-5239.
[^Heberlein_95]: Heberlein, Ulrike, and Kevin Mosest. "Mechanisms of Drosophila retinal morphogenesis: the virtues of being progressive." Cell 81.7 (1995): 987-990.
[^Ready_76]: Ready, Donald F., Thomas E. Hanson, and Seymour Benzer. "Development of the Drosophila retina, a neurocrystalline lattice." Developmental biology 53.2 (1976): 217-240.
[^Pascual_17]: Pascual, Justine, et al. "Hippo reprograms the transcriptional response to Ras signaling." Developmental cell 42.6 (2017): 667-680.
[^sun_2011]: Sun, Gongping, and Kenneth D. Irvine. "Regulation of Hippo signaling by Jun kinase signaling during compensatory cell proliferation and regeneration, and in neoplastic tumors." Developmental biology 350.1 (2011): 139-151.
[^Agrawal_95]: Agrawal, Namita, et al. "Neoplastic Transformation and Aberrant Cell–Cell Interactions in Genetic Mosaics oflethal (2) giant larvae (lgl), a Tumor Suppressor Gene ofDrosophila." Developmental biology 172.1 (1995): 218-229.
[^Cordero_10]: Cordero, Julia B., et al. "Oncogenic Ras diverts a host TNF tumor suppressor activity into tumor promoter." Developmental cell 18.6 (2010): 999-1011.
[^LeGoff_13]: LeGoff, Loïc, Hervé Rouault, and Thomas Lecuit. "A global pattern of mechanical stress polarizes cell divisions and cell shape in the growing Drosophila wing disc." Development 140.19 (2013): 4051-4059.
[^Jiang_18_NC]: Jiang, Yanrui, et al. "An intrinsic tumour eviction mechanism in Drosophila mediated by steroid hormone signalling." Nature communications 9.1 (2018): 3293.
[^Figueroa_15]: Figueroa-Clarevega, Alejandra, and David Bilder. "Malignant Drosophila tumors interrupt insulin signaling to induce cachexia-like wasting." Developmental cell 33.1 (2015): 47-55.
[^Uhlirova_06]: Uhlirova, Mirka, and Dirk Bohmann. "JNK‐and Fos‐regulated Mmp1 expression cooperates with Ras to induce invasive tumors in Drosophila." The EMBO journal 25.22 (2006): 5294-5304.
[^Yang_19]: Yang, Sheng-An, et al. "Oncogenic notch triggers neoplastic tumorigenesis in a transition-zone-like tissue microenvironment." Developmental cell 49.3 (2019): 461-472.
[^Jhappan_1992]: Jhappan, Chamelli, et al. "Expression of an activated Notch-related int-3 transgene interferes with cell differentiation and induces neoplastic transformation in mammary and salivary glands." Genes & development 6.3 (1992): 345-355.
[^Ji_19_Disease]: Ji, Tiantian, et al. "Dynamic MAPK signaling activity underlies a transition from growth arrest to proliferation in Drosophila scribble mutant tumors." Disease Models & Mechanisms 12.8 (2019): dmm040147.
[^Hanahan_11]: Hanahan, Douglas, and Robert A. Weinberg. "Hallmarks of cancer: the next generation." cell 144.5 (2011): 646-674.
[^Mirzoyan_19]: Mirzoyan Z, Sollazzo M, Allocca M, Valenza AM, Grifoni D, Bellosta P. Drosophila melanogaster: A Model Organism to Study Cancer. Front Genet. 2019 Mar 1;10:51. doi: 10.3389/fgene.2019.00051. PMID: 30881374; PMCID: PMC6405444.
[^Ugur_B_16]: Ugur B., Chen K., Bellen H. J. (2016). Drosophila tools and assays for the study of human diseases. Dis. Model. Mech. 9, 235–244. 10.1242/dmm.023762
[^Morgan_16]: Morgan T.H., Bridges C.B. Sex-Linked Inheritance in Drosophila. Carnegie Institution of Washington; Washington, DC, USA: 1916
[^Muller_28]: Muller H.J. The production of mutations by X-rays. Proc. Natl. Acad. Sci. USA. 1928;14:714–726. doi: 10.1073/pnas.14.9.714

## Martial and Method

### RNA-Seq general processing

As of the conclusion of 2022, we have discovered approximately 30 projects and obtained a total of 32 tumor models, comprising several tumor types within certain projects, as well as 215 biological groups and 517 samples from the National Center for Biotechnology Information (NCBI). We obtained all data from NCBI using sra-tools, excluding DNA-Seq, CHIP-Seq, and single-cell RNA-Seq data, which downloaded all data as fastq.gz files. We then employed our unpublished RNA-Seq data for standard processing. For raw reads quality control, we utilized fastp 0.22.0[^fastp]. Adaptors, low-quality bases from the ends of reads, or low-quality reads were automatically trimmed by fastp using default parameters. Quality before and after auto-trimming was estimated by statistics from samtools. Following quality control, we mapped the reads to the genome dme6 using bowtie2[^bowtie2], following the guidelines of Trinity-RNAseq[^trinity]. Some samples consisted of multiple fastq files, which were mapped together to output a single bam file after short-read alignment. Additionally, we utilized RSEM 1.2.31[^rsem] to count the reads to generate raw expected counts, transcripts per million (TPM), and fragments per kilobase of transcript per million mapped reads (FPKM) of each gene. We then used the abundance_estimates_to_matrix.pl script to combine the counts matrix, TPM matrix, and cross-library normalized trimmed mean of M values (TMM) matrix. Finally, we used edgeR 3.36.0[^edgeR] to calculate differentially expressed genes (DEGs) using the count matrix for pairwise comparisons within a project’s samples. We applied a threshold of P ≤ 0.001 and a log~2~ fold change (log~2~FC) of 2 to filter significant DEGs. Mean while counts per million reads mapped (CPM) of a gene less than 1 are excluded. The heatmap-related plots use the normalized TMM matrix.

Following the estimation of expression changes using edgeR, we conducted gene set enrichment analysis (GSEA) utilizing pairwise comparison fold change results. The GSEA was executed utilizing clusterProfiler 4.2[^clusterprofiler]. In line with the recommended protocol, all genes listed in the fold change list were included without imposing a P-value cutoff to ensure comprehensive results. Normalized enrichment score (NES) was applied as the metric for downstream comparison. Subsequently, we focused on the comparisons of tumor/rescued tumor samples with their respective controls to create an NES matrix, which was used to compare and contrast differences and similarities between tumors and samples.

### Sample comparison and pathway correlation

After generating the expression matrix, we employed the TMM method to normalize the data across all libraries, and performed association analysis on the normalized expression matrix. To address the influence of tissue-specific expression genes, we implemented a filter that only retained genes with a TMM value greater than or equal to 10 in all samples. We then utilized hierarchical clustering to group the samples based on the filtered expression matrix, and performed principal component analysis (PCA) using the prcomp function from stats package in R to estimate the similarity among all samples.

For pathway correlation analysis, we selected two pathways from the NES matrix and applied a statistical filter with a significance threshold of less than 0.05. We then employed the cor function in R to calculate the Pearson correlation coefficient and used the lm function to perform linear regression and obtain the R-squared value.

### GESA clustering

Upon completion of the NES calculation using both Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway gene sets and Gene Ontology (GO) term gene sets (KGOSs), we compiled the results and created a sample-KGOSs matrix. In the event of missing values, we ensured that they were filled with 0 to enable successful hierarchy cluster and Weighted Correlation Network Analysis (WGCNA)[^WGCNA] by chosen softthreshold as 9. WGCNA was chosen to cluster the KGOSs because it not only groups KGOSs with similar changing patterns but also groups reversed KGOSs into one module, a feature that hierarchical clustering may not be aware of the reversed patterns. We then manually selected the module with DNA replication, which had more than 755 KGOSs in total. We then verified the p-value of the KGOSs for each sample and filtered out the samples with insignificant adjusted p-values for most KGOSs (>=10%), and KGOSs missing in most Samples (>=25%). Otherwise, to check the distribution of the p-value, dengsity plot is generated to illustrate the distribution characteristic of up-regulation and down-regulation than 0.05. Overlap arear of the two groups is estimated by 'overlapping' package from R.

[^WGCNA]: Langfelder, Peter, and Steve Horvath. "WGCNA: an R package for weighted correlation network analysis." BMC bioinformatics 9.1 (2008): 1-13.

### Network analysis

We obtained physical connections from the Search Tool for the Retrieval of Interacting Genes/Proteins (STRING) database[^string] and discarded any connections with a total score below 150. Protein IDs were then converted to gene IDs using online tools from FlyBase. From this, we selected genes that were exclusively part of the KGOSs module as the main network and calculated the mean FC value. Genes with an absolute FC below 1.5 were filtered out, and those with a node degree less than 1 were also removed to isolate key genes. This led to the retention of 1250 genes and 29174 connections, and we used qgraph[^qgraph] to create the Fruchterman Reingold layout[^layout] for each node (gene). Based on the log~2~FC distribution, we grouped the genes into two sets, with mainly up-regulated genes on the right and down-regulated genes on the left. We identified the boundary by using Gaussian smoothing from Python SciPy[^scipy] to smooth the log~2~FC value, and a value of 0 was used to demarcate the boundary between the two groups. We identified potential hub genes from each group based on their degree rank, and cross-talking genes were manually determined based on their reversed group connection preference: genes that were connected to fewer genes from their own group than from the other group.

### DNA repair-related genes and autophagy/apoptosis related genes selection and visualization

In this part, we carefully selected the samples to be analyzed, including all WD scrib tumor samples, one WD ras-scrib sample, all eye disc ras-scrib tumor samples, and bsk^DN^ rescued eye disc samples, for comparison. We excluded one WD ras-scrib tumor as it was found to be a significant outlier through hierarchical clustering. To identify genes related to autophagy/apoptosis and DNA repair, we searched for keywords such as "auto," "apop," "lyso," "repair," "Fanconi," and "DNA damage" in KEGG pathway names and GO terms. The genes and samples log~2~FC matrix was generated and the mean of the absolute log~2~FC value for each gene was calculated, with FC values less than 0.3 excluded to remove non-changing genes. Finally, the log~2~FC matrix was scaled by z-score and hierarchical clustering was performed on both samples and genes.

### Wnt-JNK interaction

To investigate the potential effects of the interaction between the Wnt signaling pathway and JNK activity on autophagy, we employed a two-way Analysis of Variance (ANOVA) analysis in R. To further explore the association between this interaction, we first created a two-dimensional matrix of Wnt NES and Mmp1 log~2~FC, and then we projected the matrix onto a one-dimensional line with an intersection of 0 and a slope of -1. We made the assumption that the interaction was reversed and then projected the matrix onto this line accordingly using the specific function below. The function under consideration involves the coordinates of a projected point denoted by (X, Y) and a raw point represented by (x, y). Here, 's' denotes the slope of the line on which the projected point lies, while 'b' represents the intersection of the same line. This projection allowed us to obtain new coordinates $(\frac{y-x}{-2}, \frac{y-x}{2})$ that could be used to illustrate the linear relationship between the interaction of Wnt and JNK on autophagy activity. Specifically, we then used the projected x-axis as our new x-axis and the NES of autophagy as our y-axis to visualize the linear relationship between these variables. 

$$
X = (y - b + s×x)/(-s^2 - 1) 
$$
$$
Y = s × X + b 
$$


[^scipy]: SciPy 1.0: fundamental algorithms for scientific computing in Python
[^layout]: Fruchterman, Thomas MJ, and Edward M. Reingold. “Graph drawing by force‐directed placement.” Software: Practice and experience 21.11 (1991): 1129-1164.
[^string]: Szklarczyk, Damian, et al. "The STRING database in 2023: protein–protein association networks and functional enrichment analyses for any sequenced genome of interest." Nucleic Acids Research 51.D1 (2023): D638-D646.
[^qgraph]: Epskamp, Sacha, et al. "qgraph: Network visualizations of relationships in psychometric data." Journal of statistical software 48 (2012): 1-18.
[^bowtie2]: Langmead, Ben, and Steven L. Salzberg. "Fast gapped-read alignment with Bowtie 2." Nature methods 9.4 (2012): 357-359.

[^clusterprofiler]: Yu, Guangchuang, et al. "clusterProfiler: an R package for comparing biological themes among gene clusters." Omics: a journal of integrative biology 16.5 (2012): 284-287.

[^edgeR]: Robinson, Mark D., Davis J. McCarthy, and Gordon K. Smyth. "edgeR: a Bioconductor package for differential expression analysis of digital gene expression data." bioinformatics 26.1 (2010): 139-140.

[^pathview]: Luo, Weijun, and Cory Brouwer. "Pathview: an R/Bioconductor package for pathway-based data integration and visualization." Bioinformatics 29.14 (2013): 1830-1831.

[^fastp]: Chen, Shifu, et al. "fastp: an ultra-fast all-in-one FASTQ preprocessor." Bioinformatics 34.17 (2018): i884-i890.

[^rsem]: Li, Bo, and Colin N. Dewey. "RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome." BMC bioinformatics 12 (2011): 1-16.

[^trinity]: Haas, Brian J., et al. "De novo transcript sequence reconstruction from RNA-seq using the Trinity platform for reference generation and analysis." Nature protocols 8.8 (2013): 1494-1512.

## Result

### Data quality and consistency

The majority of the samples possess sufficient quality to be utilized in our study. After processing all data according to Fig. 1, we initially assessed quality control and consistency with previously published works. To present the quality before and after auto-trimming, we utilized a density plot. The scores before and after were found to be similar for over 90% of the samples (Fig. 2A). However, a high quality of raw reads does not necessarily ensure an appropriate library. We observed that certain libraries, such as salivary gland G17F and G17M, exhibited a very high ratio of unmapped reads, indicating that most of the reads from these samples were incorrect. This could be due to erroneous operations during sequencing, as all other libraries from the same batch were deemed satisfactory (Fig. 2B). It may be reasonable for some gut samples to have approximately 50% of unmapped reads due to potential contamination from probiotics. We also noticed a relatively high mismatch rate in wing disk and eye disk samples. This could be caused by *de novo* mutations, but may also be attributed to complicated cross-background factors.

Making sure that our data is consistent is really important for re-analyzing it. We checked if our results could be reproduced and trusted by comparing important genes like ImpL2 (Ecdysone-inducible gene L2) and NUCB1 (Nucleobindin 1) from the original research paper to our own analysis. We also conducted PCA to double-check that our findings were accurate. Our results show that, like the original research in eye yki-drived tumor model[^Atkins_16], genes such as ImpL2 and NUCB1 were up-regulated in the tumor group, while genes like sNPF and NPF were down-regulated (Fig. 2C).Another research paper about WD yki-driven tumors showed the number of genes that were either up-regulated or down-regulated[^Nagarkar_20] with Venn diagrams (Fig. 2 D^I^). Because we are using entirely different protocols from short reads alignment to counts estimation and differential expression comparison, the numbers of genes in up-regulated and down-regulated group are not exactly the same (Fig. 2D^II^). And during the processing, the low expression counts read are also been filtered from our results and which makes the results not exactly the same. But in general, our results agree with their findings (Fig. 2D).  Two other studies about Deml tumor models also had PCA plots[^Ji_19_Disease], and we found that our findings agreed with their overall trends (Fig. 2E & F). 

[^Kowalczyk_22]: Kowalczyk, W., et al. "Hippo signaling instructs ectopic but not normal organ growth." Science 378.6621 (2022): eabg3679.
[^Atkins_16]: Atkins, Mardelle, et al. "An ectopic network of transcription factors regulated by hippo signaling drives growth and invasion of a malignant tumor model." Current Biology 26.16 (2016): 2101-2113.
[^Nagarkar_20]: Nagarkar, Sanket, et al. "Promoter proximal pausing limits tumorous growth induced by the yki transcription factor in drosophila." Genetics 216.1 (2020): 67-77.

> Figure 2. Figure A shows the density plot for the change in library quality reads. Figure B displays a partial heatmap of five categories of reads quality that exhibits abnormal values. Figure C shows the relative gene expression changes between the tumor and control groups, presented in the form of five bar charts from the original paper (above) and five bar charts from our re-processed data (below), with the difference being illustrated by TMM. Figure D presents the Venn diagram that displays the intersection of genes from different treatments, with D^I^ showing the intersection from the original paper and D^II^ displaying the intersection from our results. Finally, figures E and F show the PCA plots, with the left panel for each group showing our re-processed results and the right panel showing the results from the original paper.

### Two main different types of tumors

Describing the whole gene expression profile from various samples is a complex task. Consequently, different types of tumors are challenging to classify and describe based on their gene expression profiles. As a result, clustering information is difficult to interpret regarding tumor/none tumor, different tissues, and mutation drivers, as shown in Fig. 3A. Despite sharing similar tumor hallmarks, the driving factors behind tumor development are often diverse and intricate. Single-gene-level analysis may introduce considerable noise in the data, which makes it challenging to draw meaningful conclusions. To mitigate this issue, we attempted to cluster samples based on the GSEA results (Fig. 3B), as it reduces the noise significantly at the gene set level. Our findings indicate that tumor samples can be effectively classified based on their tissue origin using the PCA results obtained from the NES matrix (Fig. 3C).

The hallmark of over-proliferation is a primary feature of tumors, and it is commonly assumed that all tumors exhibit high levels of proliferation. However, the results of GSEA indicate that not all tumors in flies show significant up-regulation of this process. Utilizing a hierarchical clustering approach, we grouped the KGOSs into 500 clusters based on the NES matrix. We extracted the cluster associated with DNA replication to highlight proliferation activities (Fig. 3B). Additionally, we excluded overgrowth and rescued tumors to isolate malignant tumors. Consequently, a NES matrix was generated comprising 30 KGOSs and 80 samples (Fig. 3D). Our analysis revealed that salivary Notch tumors, head brat tumors, and neuroblast Syp tumors exhibited a significant increase in DNA replication and repair-related KGOSs. However, in WD scrib/ras-scrib and ovary tumors, we observed a negative NES. Initially, we speculated that this may be due to tissue-specific effects. However, we subsequently observed that WD wts tumors and WD Yki tumors were grouped in the first cluster. Furthermore, we noted that eye disc ras-scrib tumors and leg disc ras-scrib tumors were grouped in cluster 3, despite the GSEA result not being significant. Therefore, we concluded that this phenomenon is not tissue-specific but rather a difference driven by scrib/ras-scrib-driven tumors because they have a relatively low level of DNA replication.

> Figure 3. Figure A displays a heatmap of the gene expression profile obtained from more than 543 samples with 1185 selected genes. The phenotype is indicated by specific markers, where "?" denotes an unknown sample type, "Control" represents the control group used in each paper, "Growth" indicates samples with mutation-caused overgrowth but not tumors, "Non-Tumor" represents samples with mutations that neither initiate tumor nor cause overgrowth, "Tumor^-^" represents tumor rescued by mutation, and "Tumor^+^" indicates malignant tumor types compared to "Tumor". Figures B and D present a NES heatmap, with Figure B showing 110 selected mutation samples against their respective controls along with 4312 KGOSs, while Figure D displays only 80 tumor and malignant tumor samples against their controls in the cluster which has 30 KGOSs and belonging to DNA replication and repair. Figure C showcases PCA diagrams based on the NES matrix from Figure B, with C^I^ grouped by phenotype and C^II^ grouped by tissue type.

### DNA replication is positively correlated to DNA repair

The DNA replication and DNA repair pathways have been observed to have a high correlation with each other, which could be attributed to the presence of numerous shared genes between the two pathways. To mitigate the effects of shared genes, we performed correlation analysis between the DNA replication pathway and the Fanconi anemia pathway, which is responsible for DNA damage sensing and signal transduction. Using the Pearson correlation coefficient (R), we obtained a value of 0.94, suggesting a strong correlation between DNA replication and damage (Fanconi anemia pathway) (Fig. 4A). Our analysis revealed that only a few tumor samples such as WD scrib^-^ tumor, exhibited negative NES scores in both the Fanconi anemia and DNA replication pathways, as illustrated in the diagram. Overall, our results suggest that DNA damage repair and DNA replication are closely intertwined and support the idea that the Fanconi pathway is involved in DNA replication and DNA repair.

### DNA replication and autophagy are negatively correlated with each other

To establish the similarities in KGOSs changing patterns among tumor samples, we utilized the WGCNA algorithm to cluster the NES matrix. Despite the availability of another clustering algorithm, CLEAN, designed for clustering NES matrix, it has a limitation of grouping only positively related clusters and lacks negative correlation awareness[^CLEAN]. With the parameters applied to run 4039 KGOSs (Fig. 4B), we detected a certain number of modules, focusing on the module containing DNA replication (Fig. 4C). Further hierarchical clustering grouped the samples based on these modules into three categories: group 3 had mostly positive NES, group 1 had an almost reversed pattern from group 3, and group 2 had a more random distribution and most NES showed a non-significant q-value. Comparing groups 1 and 3 revealed a reversed pattern between the two sets, where the set with the most positive NES is related to DNA replication, repair, and damage sensing, while the set with the most negative NESs is related to metabolism, lysosome, and autophagy. It indicates a connection between DNA replication/damage and lysosome/autophagy, warranting further investigation into the genes.

To acquire more reliable data from reliable sources, we checked the relationship between q-value and NES. The majority of KGOSs q-values from the samples are not significant, thus we filtered the data to avoid the negative effects of non-significant NESs of KGOSs and samples. We finally selected 320 KGOSs and 34 samples based on the criteria mentioned in the material and methods (Fig. 4D). Interestingly, all remaining samples belong to group 1, which can be explained by the fact that among the significant q-value group, positive NES are greater than negative NES (Fig. 4E). We listed the genes from all 320 KGOSs and calculated the mean value of log~2~FC among the 34 samples, all belonging to group 1. We obtained 4155 genes in the list and further reduced redundant genes by deleting low expression changing genes with a FC smaller than 1.5, resulting in a final list of 1250 genes.

[^CLEAN]: Freudenberg, Johannes M., et al. "Clean: Clustering enrichment analysis." BMC bioinformatics 10 (2009): 1-15.

> Figure 4. Figure A is a scatter plot that displays the linear relationship between the NES of Fanconi and DNA Replication (n = 110). The grey dots represent samples with a p-value less than 0.05, salmon dots indicate the WD-scrib tumor, and blue dots represent samples where both two KEGG pathways GSEA results are significant. The salmon line on the graph depicts the regression line for only the blue dots. Figure B illustrates the clustering result of the Weighted Gene Co-expression Network Analysis (WGCNA). Each small rectangle in the heatmap corresponds to a gene. The brighter colors indicate a higher correlation to genes on the other axis. The color bar on the edge of the heatmap shows the WGCNA detected modules, and the dendrogram represents the hierarchical clustering of those genes. Figure C displays all the KEGG Orthology Groups (KOGs) from the module that contains DNA replication. The x-axis represents the samples, and the y-axis represents the KOGs. There are 759 KGOSs in total, and group A has 565 sets, and group B has 194 sets. In the sample columns, group 1 has 35 samples, group 2 has 36 samples, and group 3 has 39 samples. Figure D shows the selected samples and sets based on the q-value. After filtering, we have 320 sets and 34 samples left. Figure E is the q-value distribution along with NES. All 437120 NES are applied to this plot.


### Protein networks are consistent with the inner connections between the DNA replication and autophagy reversed pattern 

Next, in order to further expand our understanding and present the inner connections among those 4155 genes, we applied graphical network analysis. The network data utilized in this study were based on the STRING database, specifically the physical interaction Drosophila data of version v11.5. We extracted the genes from the list and filtered those with a total score below 150. Prior to gene filtering, we observed 182,458 connections among 4155 genes. After filtering based on both log~2~FC and degree number (less than 2), we obtained 29174 connections and 1250 genes. Using qgraph, we calculated the Fruchterman Reingold layout based on the smallest entropy of an electron-spring model system. This layout algorithm groups frequently connected genes and separates non-connected genes. The resulting distribution showed 3 to 4 groups based on the density of the special distribution and two groups based on the log~2~FC distribution. Most of the nodes on the left side were down-regulated while the right side was up-regulated (Fig. 5A). Based on the KGOSs NES results, we propose that the genes on the down-regulated side are associated with lysosomes/autophagy, while the genes on the up-regulated side are linked to DNA damage. To validate this idea, we separated the genes into two groups, and the edge genes in the center with the largest changes were used for grouping. For avoiding human bias, we employed Gaussian smoothing to smooth the log~2~FC values to detect the center of each side and the result shows in Fig. 5B^I^. Based on this 3-dimensional (3D) plot result, we set the threshold as 0 to detect the edge of two groups and the edge is shown in at the center of the Fig. 5B^II^. Finally, we identified the group based on the spatial distribution and the result shows in the Fig. 5B^III^.

### Ppn (Papilin) and tou (toutatis) as the two genes with highest degree for the 2 respective groups

Upon dividing them into two groups, genes were ranked based on their degrees. Among the down-regulated group, we found many NADH dehydrogenase proteins, Cytochrome c oxidase family proteins, and Serpin family proteins that are correlated with proteolysis, lysosome, oxidative, and autophagy-related functions/pathways. In this network, we observed that Ppn has the highest degree, connecting many proteolysis-related genes (Spn family) and oxidative-related genes (ND, COX families) (Fig. 5C). Ppn is a crucial extracellular matrix (ECM) protein that affects cell rearrangements and is abundant in the nerve cord, gut, and trachea where apoptosis frequently occurs[^Kramerova_00]. Ppn deposition is reduced when apoptosis is blocked[^Ambrosini_17], indicating that Ppn could serve as a marker for apoptosis and oxidative activity changes.

In contrast, the up-regulated group contains many cell cycle, chromosome, and DNA regulation-related genes, such as Cdk1, Blm, PCNA, and Mi-2, indicating that the up-regulated group is associated with cell proliferation and DNA repair pathways. In this network, we identified tou as having the highest degree and being a hub for many genes (Fig. 5D). Tou is a transcription factor responsible for chromatin remodeling and nervous system development[^Ito_99][^Strohner_01]. Tou can also affect other transcription factors such as Pnr to alter and determine cell fate[^Vanolst_05], establishing its hub gene status among the up-regulated group. Other genes, such as brahma (brm), a transcriptional regulator[^Tamkun_92], and polo, which has significant effects on cell cycle[^Llamazares_91][^Savoian_14], also have high degrees among the up-regulated group.

[^Savoian_14]: Savoian, Matthew S., and David M. Glover. "Differing requirements for Augmin in male meiotic and mitotic spindle formation in Drosophila." Open biology 4.5 (2014): 140047.
[^Llamazares_91]: Llamazares, S., et al. "polo encodes a protein kinase homolog required for mitosis in Drosophila." Genes & development 5.12a (1991): 2153-2165.
[^Tamkun_92]: Tamkun, John W., et al. "brahma: A regulator of Drosophila homeotic genes structurally related to the yeast transcriptional activator SNF2SWI2." Cell 68.3 (1992): 561-572.
[^Vanolst_05]: Vanolst, Luc, Catherine Fromental-Ramain, and Philippe Ramain. "Toutatis, a TIP5-related protein, positively regulates Pannier function during Drosophila neural development." (2005): 4327-4338.
[^Strohner_01]: Strohner, Ralf, et al. "NoRC—a novel member of mammalian ISWI-containing chromatin remodeling machines." The EMBO journal 20.17 (2001): 4892-4900.
[^Ito_99]: Ito, Takashi, et al. "ACF consists of two subunits, Acf1 and ISWI, that function cooperatively in the ATP-dependent catalysis of chromatin assembly." Genes & development 13.12 (1999): 1529-1539.
[^Ambrosini_17]: Ambrosini, Arnaud, et al. "Apoptotic forces in tissue morphogenesis." Mechanisms of development 144 (2017): 33-42.
[^Kramerova_00]: Kramerova, Irina A., et al. "Papilin in development; a pericellular protein with a homology to the ADAMTS metalloproteinases." Development 127.24 (2000): 5475-5485.

### Grouping Cross-talking gene indicates Wnt signaling pathway is important

We identified hub genes from each group based on node of degrees, and importantly, we identified cross-talking nodes (Fig. 5E). Among the cross-talking nodes, Sec22 has the highest degree which is important to Wnt portein secretion[^Hausmann_07]. On the other hand, wg had the highest mean log~2~FC value. Furthermore, genes Dally, CanB2, and norpA were associated with the Wnt signaling pathway, while l(2)gl was involved in the Hippo signaling pathway, which is upstream of the Wnt signaling pathway. These findings suggest that the Wnt signaling pathway may contribute to the observed pattern, which is high in DNA replication and damage repair and low in lysosome and autophagy activities.

[^Hausmann_07]: Hausmann, George, Carla Bänziger, and Konrad Basler. "Helping Wingless take flight: how WNT proteins are secreted." Nature reviews Molecular cell biology 8.4 (2007): 331-336.

### Scrib tumor is a good model to show DNA replication and autophagy reversed pattern

We then carefully selected a total of 115 DNA-repair related genes and 146 autophagy/apoptosis related genes from KGOSs. We analyzed the relative expression changes of these genes in the log~2~FC matrix and compared them among the scrib, ras-scrib, and rescued ras-scrib-bsk tumor models. Our results showed that despite the inclusion of both WD and eye disc ras-scrib tumor models, the tumor groups were well-clustered according to their genotypes. Even the tumors that were largely rescued by bsk^DN^ still exhibited ras-scrib-like behavior rather than scrib. Furthermore, we were able to divide these genes into three distinct groups based on their hierarchical clustering patterns (Fig. 5F). The first group consisted mostly of autophagy/apoptosis related genes such as Atg18b, Sid, Tsp42Ej, which were highly expressed in scrib tumor but low in ras-scrib tumor. Conversely, the second group consisted mostly of DNA repair-related genes such as P53, CycE, PCAN, Fancl, which showed a reversed pattern compared to the first group. The third group consisted mostly of autophagy/apoptosis related genes, and the reversed pattern between scrib tumor and ras-scrib tumor was less prominent compared to the other two groups. These results provide confirmation of the reversed pattern between DNA repair and autophagy/apoptosis, and suggest that the scrib and ras-scrib tumor models are suitable for studying this pattern. The identification of these gene groups and their expression patterns could provide insights into the underlying mechanisms of tumor progression and may have implications for the development of targeted therapies.

> Fig.5. Figure A displays network plots generated from the STRING database data. Figure B shows the Gaussian smoothed log~2~FC distribution of the nodes from graph A. Figure C presents a portion of the identified hub genes from the down-regulated group, and Figure D displays the hub genes from the up-regulated group. Figure E illustrates the identified cross-talking genes between the two groups. The legends for Figures A, C, D, and E are the same. Lastly, Figure F exhibits genes involved in DNA repair, autophagy, and apoptosis from WD-scrib, WD ras-scrib, and other eye disc ras-scrib related tumor samples.

### JNK signaling pathway activation and apoptosis activities

The activation markers of the JNK signaling pathway, Mmp1[^Uhlirova_06][^Igaki_06] and puc, are significantly up-regulated in the scrib^-^ WD, while the apoptosis marker Dcp-1[^Song_Z_97] is down-regulated, which is reversed to the autophagy marker Atg8[^Nezis_10] (Fig. 6B). This observation may explain why the overexpression of p35 could not rescue the cell cycle arrest of the WD-scrib tumor in the early stage[^Ji_19_Disease], as apoptosis is already suppressed and the degradation of cells in the scrib^-^ WD is mainly through autophagy, as suggested by the GSEA analysis (Fig. 6G).

[^Igaki_06]: Igaki, T., Pagliarini, R. A. and Xu, T. (2006). Loss of cell polarity drives tumor growth and invasion through JNK activation in Drosophila. Curr. Biol. 16, 1139-1146.
[^Song_Z_97]: Song, Z., McCall, K. & Steller, H. DCP-1, a Drosophila cell death protease essential for development. Science 275, 536–540 (1997).
[^Nezis_10]: Nezis, I. P. et al. Autophagic degradation of dBruce controls DNA fragmentation in nurse cells during late Drosophila melanogaster oogenesis. J. Cell Biol. 190, 523–531 (2010).

### JNK is the key for these all abnormalities in tumor

The induction of ras^V12^ does not alter the activity of JNK signaling pathway (Fig. 6B). The Wnt signaling pathway is more intricate than the JNK pathway, as the Wnt family comprises many members. Among both early scrib and ras-scrib tumors, Wnt2 is broadly down-regulated. Conversely, some Wnt signals, such as Wnt4 and Wnt10, are up-regulated in scrib tumors at 10 days, 12 days, and 14 days respectively. However, all Wnt families are down-regulated in the Eye ras-scrib tumor, and the NES is significantly negative (Fig. 6A), indicating that the Wnt signaling pathway is significantly suppressed in the Eye ras-scrib tumor, but not significantly suppressed in the Wnt disk ras^V12^/scrib^-^ tumor.

[^Kennedy_03_cc]: Kennedy, Norman J., and Roger J. Davis. "Role of JNK in tumor development." Cell cycle (Georgetown, Tex.) 2.3 (2003): 199-201.
[^Tournier_13]: Tournier, Cathy. "The 2 faces of JNK signaling in cancer." Genes & cancer 4.9-10 (2013): 397-400.
[^Kennedy_03]: Kennedy, Norman J., et al. "Suppression of Ras-stimulated transformation by the JNK signal transduction pathway." Genes & development 17.5 (2003): 629-637.

### JNK plays an important role in the ras-scrib tumor

Within the WD model, we observed a greater predilection for the scrib tumor model to exhibit positive scores in relation to Wnt, lysosome, and autophagy, while displaying significantly high scores in the latter and markedly low scores in relation to DNA repair and replication (Fig. 6A). These findings are consistent with the observed phenotype, which shows cell cycle arrest in the early stages, as well as autophagic activity in abnormal areas[^Ji_19_Disease]. However, when scrib and ras are mutated in unison, this pattern is reversed, as NES scores for DNA replication and repair are up-regulated, while those for wnt, lysosome, and autophagy are down-regulated. This implies that ras^V12^ is capable of suppressing autophagy in the WD, thereby promoting its growth, as has been expounded upon in established research.

JNK signaling pathway also plays a crucial role in this context. In a cohort of eye disc ras-scrib tumors, bsk dominant-negative clones were utilized to block the JNK signaling pathway and rescue the tumor phenotype. The resultant DNA replication/repair vs lysosome and autophagy pattern was also reversed. The GSEA analysis demonstrated that the Wnt signaling pathway was significantly up-regulated after the knockdown of the JNK signaling pathway, while the DNA replication pathway was significantly down-regulated (Fig. 6A). Furthermore, by comparing these results with those of the control group, it was found that cell death-related pathways such as apoptosis and mitophagy were significantly up-regulated only in the Eye ras-scrib bsk clone, and mismatch repair and Fanconi anemia pathways were significantly up-regulated in Eye ras-scrib only. These findings further confirmed the reversed pattern.

Next, we aimed to investigate the association between JNK activity and cell death in scrib^1^ and ras^V12^-scrib tumor models. We observed that JNK activity was up-regulated in both tumor models, but cell death was suppressed only in the ras^V12^-scrib tumor. Previous studies have suggested that ras could suppress apoptosis activity induced by JNK, but the underlying mechanism remains unclear. Our study reveals that Wnt-JNK activity is associated with autophagy activity, and the two pathways act together to regulate cell death.

###  Wnt crosstalk with JNK

In order to investigate the interaction between Wnt and JNK and their impact on autophagy, we employed a two-way ANOVA. Our analysis revealed a significant interaction effect between Wnt and JNK on autophagy, with a p value of 0.01169 (Fig. 6C^I^). This suggests that the combined activity of Wnt and JNK has a significant influence on the regulation of autophagy. We then explored whether this activity association is based on cooperation or reversed competition. Based on the NES matrix, we observed that the ras-scrib tumor had a significantly negative Wnt NES and relatively low autophagy, while the scrib tumor alone had a relatively high level of both Wnt and autophagy. The JNK activity was high in both tumor models.

To obtain a better understanding of the linear relationship, we projected the Wnt NES and Mmp1 log~2~FC into one dimension and assumed that they are negatively related. Using the projected new x, we plotted Autophagy NES as y to illustrate the linear relationship. Our results suggest that in the ras-scrib system, high Wnt and high JNK activity are associated with high autophagy, while low Wnt and high JNK activity are associated with low autophagy. But noticeably, the result is not linear since the R^2^ equals 0.05243 which is far less than 1 (Fig. 6C^II^). It suggests that the interaction between Wnt and JNK is more complicated and probably in multiple dimensions including time and space. In general, our findings provide new insights into the mechanism by which JNK activity is regulated in different tumor models and how it affects cell death.

> Fig6. Figure A is a heatmap of NES for KEGG pathway. The center with a grey rectangle means the pathway in this sample is not significant. Figure B is the expression of genes from the ras-scrib-related tumor samples. Figure C is the association plot between Wnt NES, Mmp1 log~2~FC, and autophagy NES. Figure C^I^ is the Autophagy NES related to Wnt and Mmp1. Figure C^II^ is the Autophagy related to the projected Mmp1/Wnt axis. P value in the middle is ANOVA's result.

## Discussion

<!--1. scrib^-^ → hippo & Wnt-->

The scrib tumor has the capability to activate the Hippo signaling pathway, which can result in the direct alteration of the expression levels of wg and dally in Drosophila. Other experiments involving scrib paralogs have confirmed its negative regulatory role in the Wnt signaling pathway[^Almeida_18]. Additionally, evidence suggests that the PDZ domains of scrib can repress the Wnt signaling pathway by associating with β-catenin, which is modulated by Wnt3a[^Daulat_19]. In the scrib tumor model, we can find that most of the samples significantly up-regulate the Hippo signaling pathways activities and partially up-regulate Wnt. As a result, scrib nock down could up-regulate the Hippo and Wnt signaling pathways. 

<!-- 2. Ras → suppress the Wnt -->

In the canonical Wnt signaling pathway, the activated form of the Wnt receptor recruits the degradation complex in the presence of Wnt signaling, thereby releasing β-catenin. The β-catenin can then enter the nucleus and activate the translation of target genes. On the other hand, the degradation complex phosphorylates β-catenin and promotes its degradation. Once the position of the degradation complex is released, it can recruit other proteins, such as ras, and promote the degradation of both ras and β-catenin[^Jeong_18][^Lee_18]. As a result, ras over-activation could suppress the Wnt signaling pathway which could provide an explanation for the ras^V12^-scrib model having a significant negtive NES.


[^Lee_18]: Lee, Sang‐Kyu, et al. "β‐Catenin‐RAS interaction serves as a molecular switch for RAS degradation via GSK 3β." EMBO reports 19.12 (2018): e46060.
[^Jeong_18]: Jeong, Woo-Jeong, Eun Ji Ro, and Kang-Yell Choi. "Interaction between Wnt/β-catenin and RAS-ERK pathways and an anti-cancer strategy via degradations of β-catenin and RAS by targeting the Wnt/β-catenin pathway." NPJ Precision oncology 2.1 (2018): 5.
[^Almeida_18]: Almeida, Leonor Lopez, et al. "The SCRIB paralog LANO/LRRC1 regulates breast cancer stem cell fate through WNT/β-catenin signaling." Stem cell reports 11.5 (2018): 1040-1050.
[^Daulat_19]: Daulat, Avais M., et al. "The tumor suppressor SCRIB is a negative modulator of the Wnt/β‐Catenin signaling pathway." Proteomics 19.21-22 (2019): 1800487.

<!-- 3. scrib → Wnt3a → JNK -->

Previous research has shown that scrib can suppress the JNK signaling pathway[^Uhlirova_06][^Ji_19_Disease]. Additionally, the non-canonical Wnt signaling pathway can also regulate the JNK signaling pathway. However, there are few published articles that have studied the relationship between scrib, Wnt, and JNK. Previous research has verified that Wnt3a can regulate JNK in a chronic kidney disease model[^Oh_20]. Furthermore, the activity of Wnt3a can be affected by scrib[^Daulat_19]. Therefore, we have reason to believe that scrib can regulate JNK through the Wnt signaling pathway. In our reprocessed data, we have found that most scrib knockdown wing and eye disc tumors show activation of the Wnt signaling pathway. Moreover, the up-regulation of JNK pathway activity has been verified by data source articles[^Ji_19_Disease]. Another piece of evidence comes from the Eye ras-scrib tumor, in which the Wnt signaling pathway is significantly up-regulated after bsk knockdown in two independent studies, which could lead to compensatory effects.


<!-- 4. Wnt → Nkd → JNK.
JNK → App and DNA replication hold -->

JNK can interact with Wnt through the non-canonical signaling pathway. Nkd inhibits the Wnt/β-catenin signaling and promotes the JNK signaling pathway[^Rousset_01], leading to both β-catenin and ras degradation. As a result, the proliferation information is disrupted, and the cell cycle loses control both in Drosophila WD and human keloid fibroblasts[^Cai_17]. Cells from the WD begin overproliferation, which is accompanied by autophagy. Under these circumstances, overexpression of the activated form of ras (ras^V12^) could rescue the ras degradation and compensate for the β-catenin degradation by competitively binding to the degradation complex. Additionally, the downstream gene of the Wnt signaling pathway, c-myc, is up-regulated. Meanwhile, ras can activate the mTor signaling pathway to further promote proliferation and induce a malignant tumor.

[^Rousset_01]: Rousset, Raphaël, et al. "Naked cuticle targets dishevelled to antagonize Wnt signal transduction." Genes & development 15.6 (2001): 658-671.
[^Cai_17]: Cai, Yumei, et al. "down-regulation of β-catenin blocks fibrosis via Wnt2 signaling in human keloid fibroblasts." Tumor Biology 39.6 (2017): 1010428317707423.
[^Oh_20]: Oh, Yun Jung, et al. "Reduction of secreted frizzled-related protein 5 drives vascular calcification through Wnt3a-mediated Rho/ROCK/JNK signaling in chronic kidney disease." International Journal of Molecular Sciences 21.10 (2020): 3539.


<!-- 5. Wnt-JNK → Autophage -->
Based on RNA-seq data, we observed a strong association between the Wnt and JNK signaling pathways in regulating autophagic activity in ras-scrib tumor. Previous studies have shown that ras^V12^ can suppress apoptosis and autophagy mediated by JNK, but the underlying mechanisms remain unclear. To investigate this further, we conducted a two-way ANOVA analysis to examine the interaction between Wnt and JNK pathways in affecting autophagy. Our results revealed a significant association between Wnt and JNK pathways (Fig. 7), which may involve crosstalking via Nkd or β-catenin, leading to the development of a more malignant tumor phenotype.



## Table

LABEL|Tumor Model|Number of SRA|Reference
:-|:-|:-|:-
PRJNA222987|Head-brat|6|Jüschke C et al.[^Jüschke_13]
PRJNA273558|Eye-Ras_scrib|20|Külshammer E et al.[^Külshammer]
PRJNA291028|Eye-Ras_scrib-3|8|Atkins M et al.[^Atkins_16]
PRJNA291196|WD-wts|18|Atkins M et al.[^Atkins_16]
PRJNA298922|Eye-ph3|14|Loubière V et al.[^Loubiere_16]
PRJNA321171|Eye-Ras_scrib-2|12|Landskron L et al.[^Landskron_18]
PRJNA321171|Leg-Ras_scrib-2|11|Landskron L et al.[^Landskron_18]
PRJNA321171|WD-Ras_scrib-2|4|Landskron L et al.[^Landskron_18]
PRJNA343471|Brain-Brt|6|Landskron L et al.[^Landskron_18]
PRJNA358401|Gut-Rab|6|Nie Y et al.[^Nie_19]
PRJNA379962|WD-wts|36|Pascual J et al.[^Pascual_17]
PRJNA394257|Eye-ph|12|Jiang Y et al.[^Jiang_18_NC]
PRJNA394512|Eye-ph-2|22|Torres J et al.[^Torres_18]
PRJNA407359|Eye-DI|18|Vicente C et al.[^Vicente_18]
PRJNA471745|NB-Syp|6|Genovese S et al.[^Genovese_19]
PRJNA534434|WD-scrib|34|Ji T et al.[^Ji_19_Disease]
PRJNA555314|Gut-RAF|30|Pfefferkorn et al.[^Pfefferkorn_2023]
PRJNA587732|Eye-Ras_Src|8|Newton H et al.[^Newton_20]
PRJNA631772|Gut-Shn|7|Zhou J et al.[^Zhou_J_21]
PRJNA631773|Gut-Shn|9|Zhou J et al.[^Zhou_J_21]
PRJNA637769|WD-Yki|10|Nagarkar S et al.[^Nagarkar_20]
PRJNA646198|Eye-Yki|4|Yeom E et al.[^Yeom_21]
PRJNA732365|Salivary-N|18|Wang XF et al.[^Wang_XF_21]
PRJNA738503|WD-Ras_scrib1|65|Hodgson JA et al.[^Hodgson_16]
PRJNA807663|Ovary|134|Chatterjee D et al.[^Chatterjee_2023]
PRJNA870447|Eye-Yki2|33|Kowalczyk W et al.[^Kowalczyk_22]
/	|SG-N|	81|	/
/	|SG-N-Yki|	48|	/






[^Jüschke_13]: Jüschke C et al., "Transcriptome and proteome quantification of a tumor model provides novel insights into post-transcriptional gene regulation.", Genome Biol, 2013 Nov 30;14(11):r133
[^Landskron_18]: Landskron, Lisa, et al. "The asymmetrically segregating lncRNA cherub is required for transforming stem cells into malignant cells." Elife 7 (2018): e31347.
[^Nie_19]: Nie Y et al., "Oncogenic Pathways and Loss of the Rab11 GTPase Synergize To Alter Metabolism in Drosophila.", Genetics, 2019 Aug;212(4):1227-1239
[^Genovese_19]: Genovese S et al., "Coopted temporal patterning governs cellular hierarchy, heterogeneity and metabolism in Drosophila neuroblast tumors.", Elife, 2019 Sep 30;8
[^Pfefferkorn_2023]: Pfefferkorn, Roxana M., et al. "Recurrent phases of strict protein limitation inhibit tumor growth and restore lifespan in a Drosophila intestinal cancer model." bioRxiv (2023): 2023-01.
[^Newton_20]: Newton H et al., "Systemic muscle wasting and coordinated tumour response drive tumourigenesis.", Nat Commun, 2020 Sep 16;11(1):4653
[^Zhou_J_21]: Zhou J et al., "Microenvironmental innate immune signaling and cell mechanical responses promote tumor growth.", Dev Cell, 2021 Jul 12;56(13):1884-1899.e5
[^Yeom_21]: Yeom E et al., "Tumour-derived Dilp8/INSL3 induces cancer anorexia by regulating feeding neuropeptides via Lgr3/8 in the brain.", Nat Cell Biol, 2021 Feb;23(2):172-183
[^Wang_XF_21]: Wang XF et al., "Polyploid mitosis and depolyploidization promote chromosomal instability and tumor progression in a Notch-induced tumor model.", Dev Cell, 2021 Jul 12;56(13):1976-1988.e4
[^Chatterjee_2023]: Chatterjee D et al., "Cell polarity opposes Jak/STAT-mediated Escargot activation that drives intratumor heterogeneity in a Drosophila tumor model.", Cell Rep, 2023 Jan 28;42(2):112061










<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
