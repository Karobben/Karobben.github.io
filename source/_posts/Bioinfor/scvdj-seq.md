---
toc: true
url: scvdj-seq
covercopy: <a href="https://www.10xgenomics.com/cn/support/software/cell-ranger/algorithms-overview/cr-5p-vdj-algorithm">© 10X Genomics</a>
priority: 10000
date: 2023-12-21 14:52:46
title: "scVDJ-Seq Pipeline (CellRanger)"
ytitle: "scVDJ-Seq Pipeline (CellRanger)"
description: "scVDJ-Seq Pipeline"
excerpt: "The cellranger vdj pipeline can be used to analyze sequencing data produced from Chromium Next GEM Single Cell 5' V(D)J libraries. It takes FASTQ files for V(D)J libraries and performs sequence assembly and paired clonotype calling. The pipeline uses the Chromium Cell Barcodes (also called 10x Barcodes) and UMIs to assemble V(D)J transcripts per cell. Clonotypes and CDR3 sequences are output as a .vloupe file which can be loaded into Loupe V(D)J Browser. Visit the What is Cell Ranger page to learn more about Cell Ranger for Immune Profiling. (10X Genomics)"
tags: [Bioinformatics, RNA-Seq, NGS, scRNA-Seq]
category: [Biology, Bioinformatics, Single Cell]
cover: "https://cdn.10xgenomics.com/image/upload/v1654273213/software-support/vdj/algorithms/algorithm-workflow.png"
thumbnail: "https://cdn.10xgenomics.com/image/upload/v1654273213/software-support/vdj/algorithms/algorithm-workflow.png"
---

## scVDJ-Seq


|![scVDJ-Seq](https://imgur.com/PxRTphj.png)|
|:-:|
|V(D)J Library Construction|

1. <font style="background-color: red">V</font> (Variable): These are gene segments that code for the variable region of an antibody or T-cell receptor. The variable region is responsible for binding to antigens.

2. <font style="background-color: gold">D</font> (Diversity): These segments are found in some classes of antibodies and in T-cell receptors. They provide an additional level of diversity to the antigen-binding region.

3. <font style="background-color: green">J</font> (Joining): These gene segments join with the V (and D, where present) segments to complete the variable region of the receptor.

4. <font style="background-color: royalblue">C</font> (Constant): The constant region of the antibody or T-cell receptor is encoded by these segments. This region does not vary much between different antibodies and is responsible for the effector functions of the antibody, such as recruiting other parts of the immune system.


## Pipeline

|![Cell Ranger's V(D)J Algorithm](https://cdn.10xgenomics.com/image/upload/v1654273213/software-support/vdj/algorithms/algorithm-workflow.png)|
|:-:|
|[© 10X Genomics](https://www.10xgenomics.com/cn/support/software/cell-ranger/algorithms-overview/cr-5p-vdj-algorithm)|

## Install CellRanger

Click the [Link](https://www.10xgenomics.com/support/software/cell-ranger/downloads) and fill out the information and you could get the download page

```bash
# download the software (expired)
curl -o cellranger-7.2.0.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-7.2.0.tar.gz?Expires=1703232056&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA&Signature=hm5oQoPrhuNznBtqCREVSaH34WF-Fute6XHYRDUIvIsajK~sFKYuonBEUQsxRJ1oKmxuuAhmtJg3N-mEQU2dr223oXTTr9e70gFlx9-3qgR7cvAhbZXMMGPMhOVVixoEF2GaE1~x0LA4KLXG3xu4mDGsBn4u870Ql~~OfhYBF5bHcqV6hf8X-YPXNG8TbRZMe-dqcogRTPYpeOpfKBtvPs63CDJ3YgC2Bahci4jYuo2v7MZDTR018C~X-3qwgRMIPKCMZFInEjpkfds34TJ0yP3uwAprvpR~S3WCngKKzSmAQszkDMqSB2eXZw6~FF~6oFIIYV~-DmPV~a7DO416nQ__"

# decompress and install
tar -zxvf cellranger-7.2.0.tar.gz

# add this directory in your path
export PATH=$(pwd):$PATH
# You may wish to add this command to your ~/.bashrc or ~/.zshrc for convenience.
# for get the full command, you can run `echo export PATH=$(pwd):\$PATH` and add the print out result at the end of the ~/.bashrc or ~/.zshrc
```

!!! note Reference
    ```bash
    # Download the reference
    ## Human reference (GRCh38) - 2020-A
    curl -O "https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz"
    ## Mouse reference (mm10) - 2020-A
    curl -O "https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-mm10-2020-A.tar.gz"
    ## Human (GRCh38) and mouse (mm10) reference - 2020-A
    curl -O "https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-and-mm10-2020-A.tar.gz"

    ## Human V(D)J reference (GRCh38)
    curl -O "https://cf.10xgenomics.com/supp/cell-vdj/refdata-cellranger-vdj-GRCh38-alts-ensembl-7.1.0.tar.gz"
    ## Mouse V(D)J reference (GRCm38)
    curl -O "https://cf.10xgenomics.com/supp/cell-vdj/refdata-cellranger-vdj-GRCm38-alts-ensembl-7.0.0.tar.gz"
    ```

### Run

Documentation: [10X Genomics](https://www.10xgenomics.com/cn/support/software/cell-ranger/algorithms-overview/cr-5p-vdj-algorithm)

```bash
cellranger vdj --id=sample345 \
         --reference=/opt/refdata-cellranger-vdj-GRCh38-alts-ensembl-7.1.0 \
         --fastqs=/home/jdoe/runs/HAWT7ADXX/outs/fastq_path \
         --sample=mysample \
         --localcores=8 \
         --localmem=64
```


- **Command and Arguments**:
<pre>
cellranger vdj:     This is the main command being run. `cellranger` is the software package, and `vdj` specifies that you are running the V(D)J analysis pipeline, which is used for assembling and annotating V(D)J sequences from single-cell RNA-Seq data.
--id=sample345:     This sets the unique identifier for the run. Here, the identifier is `sample345`. This ID is used to name the output directory.
--reference=...:    This specifies the reference dataset to be used for the analysis. The provided path (`/opt/refdata-cellranger-vdj-GRCh38-alts-ensembl-7.1.0`) points to a reference dataset for human V(D)J sequences.
--fastqs=...:       This indicates the directory where the FASTQ files are located. FASTQ files are the input files for the Cell Ranger software, containing the sequenced reads.
--sample=mysample:  This specifies the name of the sample to be analyzed. It should match the sample name in the FASTQ files.
--localcores=8:     This parameter tells Cell Ranger to use 8 CPU cores for the computation. This setting helps to optimize the use of available computational resources.
--localmem=64:      This allocates 64 GB of memory (RAM) for the run. This parameter is crucial for ensuring the software has enough memory to process the data without crashing.
</pre>


## When the Job is Done

A successful `cellranger vdj` run should conclude with a message similar to this:
<pre>
Outputs:
- Run summary HTML:                                 /home/jdoe/runs/sample345/outs/web_summary.html
- Run summary CSV:                                  /home/jdoe/runs/sample345/outs/metrics_summary.csv
- Clonotype info:                                   /home/jdoe/runs/sample345/outs/clonotypes.csv
- Filtered contig sequences FASTA:                  /home/jdoe/runs/sample345/outs/filtered_contig.fasta
- Filtered contig sequences FASTQ:                  /home/jdoe/runs/sample345/outs/filtered_contig.fastq
- Filtered contigs (CSV):                           /home/jdoe/runs/sample345/outs/filtered_contig_annotations.csv
- All-contig FASTA:                                 /home/jdoe/runs/sample345/outs/all_contig.fasta
- All-contig FASTA index:                           /home/jdoe/runs/sample345/outs/all_contig.fasta.fai
- All-contig FASTQ:                                 /home/jdoe/runs/sample345/outs/all_contig.fastq
- Read-contig alignments:                           /home/jdoe/runs/sample345/outs/all_contig.bam
- Read-contig alignment index:                      /home/jdoe/runs/sample345/outs/all_contig.bam.bai
- All contig annotations (JSON):                    /home/jdoe/runs/sample345/outs/all_contig_annotations.json
- All contig annotations (BED):                     /home/jdoe/runs/sample345/outs/all_contig_annotations.bed
- All contig annotations (CSV):                     /home/jdoe/runs/sample345/outs/all_contig_annotations.csv
- Barcodes that are declared to be targetted cells: /home/jdoe/runs/sample345/outs/cell_barcodes.json
- Clonotype consensus FASTA:                        /home/jdoe/runs/sample345/outs/consensus.fasta
- Clonotype consensus FASTA index:                  /home/jdoe/runs/sample345/outs/consensus.fasta.fai
- Contig-consensus alignments:                      /home/jdoe/runs/sample345/outs/consensus.bam
- Contig-consensus alignment index:                 /home/jdoe/runs/sample345/outs/consensus.bam.bai
- Clonotype consensus annotations (CSV):            /home/jdoe/runs/sample345/outs/consensus_annotations.csv
- Concatenated reference sequences:                 /home/jdoe/runs/sample345/outs/concat_ref.fasta
- Concatenated reference index:                     /home/jdoe/runs/sample345/outs/concat_ref.fasta.fai
- Contig-reference alignments:                      /home/jdoe/runs/sample345/outs/concat_ref.bam
- Contig-reference alignment index:                 /home/jdoe/runs/sample345/outs/concat_ref.bam.bai
- Loupe V(D)J Browser file:                         /home/jdoe/runs/sample345/outs/vloupe.vloupe
- V(D)J reference:
fasta:
regions:       /home/jdoe/runs/sample345/outs/vdj_reference/fasta/regions.fa
donor_regions: /home/jdoe/runs/sample345/outs/vdj_reference/fasta/donor_regions.fa
reference: /home/jdoe/runs/sample345/outs/vdj_reference/reference.json
- AIRR Rearrangement TSV:                           /home/jdoe/runs/sample345/outs/airr_rearrangement.tsv
- All contig info (ProtoBuf format):                /home/jdoe/runs/sample345/outs/vdj_contig_info.pb
Waiting 6 seconds for UI to do final refresh.
Pipestance completed successfully!
</pre>


Once `cellranger vdj` has successfully completed, you can browse the resulting summary HTML file in any supported web browser, open the `.vloupe` file in Loupe V(D)J Browser, or refer to the Understanding Output section to explore the data by hand.


## Trouble Shoot

### Too Low to Meet the Required Threshold

<pre>
[error] Pipestance failed. Error log at:
MockC_cs/SC_VDJ_ASSEMBLER_CS/SC_MULTI_CORE/MULTI_CHEMISTRY_DETECTOR/VDJ_CHEMISTRY_DETECTOR/DETECT_VDJ_RECEPTOR/fork0/chnk0-u22ea849f77/_errors

Log message:
V(D)J Chain detection failed for Sample VDJ-B-293-redo-1 in "/raid/home/wenkanl2/MokC_sc/1_primary_seq".

Total Reads          = 1000000
Reads mapped to TR   = 30
Reads mapped to IG   = 28665

In order to distinguish between the TR and the IG chain the following conditions need to be satisfied:
- A minimum of 10000 total reads
- A minimum of 5.0% of the total reads needs to map to TR or IG
- The number of reads mapped to TR should be at least 3.0x compared to the number of reads mapped to IG or vice versa
Please check the input data and/or specify the chain via the --chain argument.
</pre>

The problem here is with the proportion of reads mapping to TR and IG. Even though you have a significant number of reads mapped to IG, the number of reads mapped to TR is ==too low to meet the required thresholds==.


!!! note Resolution:
    The message suggests checking the input data or specifying the chain via the --chain argument. Explicitly specify whether you are analyzing T-cell receptors (TR) or Immunoglobulins (IG) by using the --chain flag in your Cell Ranger command.
    For example, assume that it is B cell data, we could add `--chain IG` to solve this problem




<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
