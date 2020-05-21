---
url: bioconda
---

# Bioconda

# 1. Install
Location: [link](https://bioconda.github.io/user/install.html)
```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

# 2. Setup Channels
You may need to add the bin file in your environment
```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```


# Virtual Environment
```
# Create an environment
conda create -n Biostation python=3.7

# Check the env list
conda env list

# 激活工作环境，需要几十秒
source activate Biostation
#or
conda activate Biostation

# 关闭工作环境：不用时关闭，不然你其它程序可能会出错
source deactivate
# Or
conda deactivate
```
