---
toc: true
url: igblast
covercopy: © Karobben
priority: 10000
date: 2023-12-21 20:21:23
title: "Immunoglobulin BLAST (Igblast), a Blast Tool Specific for Antibodies"
ytitle: "Immunoglobulin BLAST (Igblast), a Blast Tool Specific for Antibodies"
description: "Igblast, a Blast Tool Specific for Antibodies"
excerpt: " IgBLAST is a tool commonly used in bioinformatics. IgBLAST (Immunoglobulin BLAST) is designed for the analysis of immunoglobulin (IG) and T cell receptor (TCR) sequences. It's part of the suite of tools offered by the National Center for Biotechnology Information (NCBI)."
tags: [Software, Database, Align]
category: [Biology, Bioinformatics, Software, Align]
cover: "https://imgur.com/vyMdRiw.png"
thumbnail: "https://imgur.com/vyMdRiw.png"
---

## Key Features of IgBLAST 

1. **Identification of V(D)J segments**: IgBLAST can identify variable (V), diversity (D), and joining (J) gene segments in IG or TCR sequences.

2. **Clonotype Analysis**: It helps in determining clonotypes based on V(D)J segment usage, providing insights into the diversity and clonality of IG or TCR repertoires.

3. **Somatic Hypermutation Analysis**: It identifies somatic hypermutations in IG sequences and can compare these to germline sequences, which is critical in understanding adaptive immune responses.

4. **Flexible Input Options**: IgBLAST can process both nucleotide and protein sequences, and it supports various input formats.

5. **Detailed Alignment Information**: It provides detailed alignment results that include information about gene segments, framework regions, complementarity-determining regions (CDRs), and mutations.

6. **Integration with Other Databases**: The results can be linked to other NCBI databases for additional information and analysis.

IgBLAST is widely used in immunology and related fields for studying B cell and T cell receptor repertoire, which is crucial for understanding immune responses, vaccine development, and in the study of autoimmune diseases and cancer.


## Local Set Up

- Basically, you can use the online service: [NCBI igblast](https://www.ncbi.nlm.nih.gov/igblast/)
- Set up by following the official documentation: [NCBI igblast set up](https://ncbi.github.io/igblast/cook/How-to-set-up.html)

Here is an example of set up by using conda from [nicwulab/SARS-CoV-2_Abs](https://github.com/nicwulab/SARS-CoV-2_Abs#local-igblast-setup)

```bash
conda create -n Abs -c bioconda \
  python=3.9 \
  igblast

conda activate Abs
# install pyir and use it to set up the blast database
pip3 install crowelab_pyir
pyir setup
```

In the `pyir`, it is using 'http' and download the data failed. By following the error code, we could find the script and alter the 'http' to 'https'. It should solving the problem. 

An example of running the program:

1. prepare the DataBase


2. run the blast
```bash
igblastn -query result/test.fasta \
  -germline_db_V imgt_database/human_nuc/IGV.fasta \
  -germline_db_J imgt_database/human_nuc/IGJ.fasta \
  -germline_db_D imgt_database/human_nuc/IGD.fasta \
  -organism human -domain_system kabat \
  -auxiliary_data imgt_database/optional_file/human_gl.aux \
  -out result/igblast_output
```

<pre>
-germline_db_V <String> Germline database name
-organism <String> The organism for your query sequence. Supported organisms include human, mouse, rat, rabbit and rhesus_monkey for Ig and human and mouse for TCR. Custom organism is also supported but you need to supply your own germline annotations (see IgBLAST web site for details) Default = `human'
</pre>


## pyir

If you installed pyir, we could use the [pyir](https://github.com/crowelab/PyIR) to do the igblast with less parameters.

```bash
pyir -m 60  result/clean_split.fa --outfmt tsv -o result/clean
```

Key parameters:

<pre>
--sequence_type {nucl,prot}     default: nucl
-m MULTI, --multi MULTI         Number of threads
-o,  --out                      default: inputfile.json.gz
--outfmt {tsv,lsjson,dict,json} suggest: tsv
--igdata IGDATA                 Path to your IGDATA directory.
-r, --receptor {Ig,TCR}         The receptor you are analyzing, immunoglobulin or t cell receptor
-s, --species {human,mouse...}  The Species you are analyzing {human,mouse,rabbit,rat,rhesus_monkey}
</pre>


## Q&A

!!! question Can I annotate the light chain and heavy chain simultaneously?
    IgBLAST is designed to analyze immunoglobulin (IG) sequences, including both heavy and light chains. However, it typically processes and analyzes these chains separately. When you input a sequence that contains both heavy and light chains, IgBLAST might only process the first recognizable sequence, which in your case appears to be the heavy chain.

    To analyze both heavy and light chains using IgBLAST, you generally need to input them as separate sequences. This means splitting your combined sequence into two parts - one for the heavy chain and the other for the light chain - and then running IgBLAST for each part individually.

    There isn't a parameter in IgBLAST that allows for the simultaneous analysis of both heavy and light chains when they are combined into a single sequence. The tool's algorithm is designed to identify and annotate the V(D)J segments of a single chain at a time, as the structure and sequence features of heavy and light chains are distinct.

    If you are consistently working with sequences that contain both chains, you may need to develop a preprocessing step in your workflow to separate these chains before analysis. Alternatively, if such a tool is essential for your work, you might need to look into other bioinformatics tools or custom scripting to first identify and separate the heavy and light chain sequences before feeding them into IgBLAST.

















<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
