---
title: "Bioconda"
description: "Bioconda"
url: bioconda
date: "2020/07/28"
toc: true
excerpt: "An Integrated Package for Bisulfite DNA Methylation Data Analysis with Indel-sensitive Mapping."
tags: [R, Bioinformatics]
category: [Biology, Bioinformatics, Software, Bioconda]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Bioconda

## 1. Install
Location: [link for Miniconda](https://docs.conda.io/en/latest/miniconda.html)
```bash
# this script might not work now
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

!!! info For Zsh environment
    Conda would add code for initiate it at the end of the `.bashrc`. You may need to copy them in to the `~/.zshrc` if you are using `zsh`.


An example of codes after you run `cat ~/.bashrc`
<pre>

And then, you can start the conda by `source ~/.zshrc` or open a new terminal.

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/ken/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/ken/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/ken/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/ken/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
</pre>

## 2. Setup Channels
You may need to add the bin file in your environment
```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```


## Virtual Environment
```
## Create an environment
conda create -n Biostation python=3.7

## Check the env list
conda env list

## 激活工作环境，需要几十秒
source activate Biostation
##or
conda activate Biostation

## 关闭工作环境：不用时关闭，不然你其它程序可能会出错
source deactivate
## Or
conda deactivate
```

## Install into Non-default Location

Reference: [saturncloud](https://saturncloud.io/blog/how-to-specify-a-new-environment-location-for-conda-create-a-guide/)


```bash
# you can use --prefix or -p to replace the -n/--name
conda create --prefix /path/to/directory python=3.8 numpy

# this is how you can activate this environment
conda activate /path/to/directory
```

## Delete you Environment

```bash
conda remove --name snpeff --all
```
## Common Software for Bioinformatics

```bash
conda install fastqc
conda install fastp
conda install trimmomatic
conda install bowtie
conda install bowtie2
conda install samtools
```
## Error

<pre>
UnavailableInvalidChannel: The channel is not accessible or is invalid.
  channel name: miniconda/cloud/bioconda
  channel url: https://mirrors.bfsu.edu.cn/miniconda/cloud/bioconda
  error code: 404

You will need to adjust your conda configuration to proceed.
Use `conda config --show channels` to view your configuration's current state,
and use `conda config --show-sources` to view config file locations
</pre>

Solving his by run:
`conda config --remove-key channels`

### GLIBC_2.17

<pre>
ImportError: /lib64/libc.so.6: version 'GLIBC_2.14' not found
ImportError: /lib64/libc.so.6: version 'GLIBC_2.15' not found
ImportError: /lib64/libc.so.6: version 'GLIBC_2.17' not found
</pre>

This error is very wired. When you have sudo right, you can solve it easily. But when you don't have sudo right, I believe that the quickest way to "solve", bypass actually, this problem is down-grade your libraries. Most of time, the conflict comes from `zlib` and  `Xz`. This is not the only way to solve it in CentOS 6.

```bash
conda install Xz==5.2.3 zlib==1.2.8 #numpy==1.9.3
```


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
