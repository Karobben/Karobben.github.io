---
title: "TransDecoder"
description: "TransDecoder"
copyright: <a href="https://bengreenfieldlife.com/podcast/self-quantification-podcasts/how-to-decode-your-genome/">Affiliate Disclosure</a>
url: transdecoder
date: 2020/07/28
toc: true
excerpt: "transdecoder for translate your mRNA to protein"
tags: [Software, Bioinformatics, RNA-Seq, Translation]
category: [Biology, Bioinformatics, Software, Trans]
cover: 'https://bengreenfieldlife.com/wp-content/uploads/2017/05/How-To-Decode-Your-Genome-Unlock-The-Nitty-Gritty-Details-Behind-Your-DNA-Discover-Your-Good-Genes-Your-Bad-Genes.png'
thumbnail: 'https://bengreenfieldlife.com/wp-content/uploads/2017/05/How-To-Decode-Your-Genome-Unlock-The-Nitty-Gritty-Details-Behind-Your-DNA-Discover-Your-Good-Genes-Your-Bad-Genes.png'
priority: 10000
---

## TransDecoder

[github](https://github.com/TransDecoder/TransDecoder)  
[latest release](https://github.com/TransDecoder/TransDecoder/releases)

## Install

### By Bioconda

```bash
conda install -c bioconda transdecoder 
```

### Build from Source

Downloading the file and make a test (16M)
```bash
wget -c https://github.com/TransDecoder/TransDecoder/archive/TransDecoder-v5.5.0.tar.gz
tar -zxvf TransDecoder-v5.5.0.tar.gz
cd TransDecoder-TransDecoder-v5.5.0/
make test
```
You are supposed to see the code below after execute `make test`
```bash
-Fasta_retriever:: begin initializing for supertranscripts.fasta
-Fasta_retriever:: done initializing for supertranscripts.fasta

+ echo Done
Done
make[2]: Leaving directory '/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0/sample_data/supertranscripts_example'
make[1]: Leaving directory '/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0/sample_data'
```
<span style="color:salmon;"><b>If it comes with any `Error` during the `make test`,<br>
please see the 'Debug' at the end.</b></span>


Now, add the current directory to your `$PATH`:
```bash
echo -e "\n#TransDecoder\n export PATH=\$PATH:$(pwd)" >> ~/.bashrc
source  ~/.bashrc
```
So, it will add the line below to the end of the `~/.bashrc` file.
```bash

##TransDecoder
 export PATH=$PATH:/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0
```
Now, you can ENJOY the TransDecoder.

## Running TransDecoder

Preparing a fasta file as `HitMe.fa`

### Extract the long open reading frames

```bash
TransDecoder.LongOrfs -t HitMe.fa
```

The result should be the `longest_orfs.pep`


## Debug  
### E1; makeblastdb: command not found

#### code
```bash
./runMe.sh: line 49: makeblastdb: command not found
make[2]: *** [Makefile:2: test] Error 127
make[2]: Leaving directory '/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0/sample_data/cufflinks_example'
make[1]: *** [Makefile:5: test] Error 2
make[1]: Leaving directory '/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0/sample_data'
make: *** [Makefile:10: test] Error 2
```
`./runMe.sh: line 49: makeblastdb: command not found
`
#### Why&How
Lake of blast+
```bash
sudo apt-get install ncbi-blast+
```

### E2; hmmpress: command not found

#### code
```bash
./runMe.sh: line 56: hmmpress: command not found
make[2]: *** [Makefile:2: test] Error 127
make[2]: Leaving directory '/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0/sample_data/cufflinks_example'
make[1]: *** [Makefile:5: test] Error 2
make[1]: Leaving directory '/home/ken/Bio/TransDecoder-TransDecoder-v5.5.0/sample_data'
make: *** [Makefile:10: test] Error 2
```
#### Why&How
Lake of hammper2
```bash
sudo apt-get install hmmer
```
