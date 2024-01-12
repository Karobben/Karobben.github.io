---
title: "Compress and Decompress"
url: compress_linux
description: "How to compress and decompress files and directories in linux command lines"
date: 2020/06/26
toc: true
excerpt: "'tar' is a command-line utility in Linux used for archiving and compressing files and directories into a single file. It stands for 'tape archive' and can create files in various formats, including .tar, .tar.gz, and .tar.bz2. It can also extract files from archives and display their contents.<a title='chatgpt'> Who said this?<a>"
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, Bash, More]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## tar

##reference:[https://man.linuxde.net/tar](https://man.linuxde.net/tar)


- Compress:
  `tar -zcvf File.tar.gz File`
- Decompress:
  `tar - zxvf File.tar.gz`

|Format|Decompress|compress|
|:-|:-|:-|
|.tar|xvf|cvf|
|.tar.gz|zxvf|zcvf|
|.tar.bz2|jxvf|jcvf|
|.tar.bz|jxvf|
|.tar.Z|.tar.Z|.tar.Z|


## Tar with ssh to substitute scp

This pipe could help you upload large files much faster than `scp`. It is a very good way to substitute `scp`.

I tried to backup ***1.4 T*** files from a moveable hard drive with `scp` and it takes a half hour for ***24 KB*** files. It spends most of the time reading files.
When I switched this pipeline, ***a few decade gigabytes was uploaded within a few minutes***. ==It is crazy fast!!!!==

Cite: [roaima; 2015](https://unix.stackexchange.com/questions/238152/why-is-scp-so-slow-and-how-to-make-it-faster)
```bash
tar czf - cap_* | ssh user@host tar xvzfC - dir
tar cf - cap_* | gzip | ssh user@host 'cd dir && gzip -d | tar xvf -'
```

## cp files with tar

```bash
tar czf - cap_* | ssh user@host tar xvzfC - dir
tar cf - cap_* | gzip | ssh ken@0.0.0.0 'cd dir && gzip -d | tar xvf -'
```

### Samll size fiels:


1. `cp -r Github /media/Side/ken/Github`
    <pre>cp -r Github /media/Side/ken/Github  0.00s user 0.23s system 27% cpu 0.835 total</pre>
2. `time tar cf -Github | gzip | ssh ken@0.0.0.0 'cd /media/Side/ken && gzip -d | tar xvf -'`
    <pre>
    tar cf - Githu*  0.06s user 0.32s system 2% cpu 13.564 total
    gzip  10.70s user 0.04s system 79% cpu 13.566 total
    ssh ken@0.0.0.0 'cd /media/Side/ken && gzip -d | tar xvf -'  0.59s user 0.26s system 6% cpu 13.567 total
    </pre>

For the `Github` directory, `cp` only takes less than 1 s, but take `13.5s` for tar-pipe. So, if you have lots of small files, `cp` still are your first choose.

### Large file test

check the size of the file: `du -sh Mutation/Raw_VCF`
    <pre>23G	Mutation/Raw_VCF</pre>

1. `time cp -r Mutation/Raw_VCF /media/Side/ken/`
    <pre>cp -r Mutation/Raw_VCF /media/Side/ken/  0.53s user 59.35s system 7% cpu 12:31.78 total</pre>
2. `time tar cf - Mutation/Raw_VCF | gzip | ssh ken@0.0.0.0 'cd /media/Side/ken && gzip -d | tar xvf -'`
    <pre>
    tar cf - Mutation/Raw_VCF  3.21s user 27.98s system 4% cpu 10:36.64 total
    gzip  532.32s user 2.73s system 84% cpu 10:36.65 total
    ssh ken@0.0.0.0 'cd /media/Side/ken && gzip -d | tar xvf -'  18.95s user 7.16s system 4% cpu 10:36.65 total
    </pre>

So, in this result, `cp` takes like 12 minutes, but our tar-pipe takes 10.5 minutes

### A better way

Though the pipeline works, but the `ssh` part is wasting large of resource. The best way for this situation is:

```bash
tar cf - Mutation/Raw_VCF | (cd /media/Side/ken/; tar xvf -)
```

And it only takes roughly 2 minutes.


## gzip

- Compress:
`gzip -cr 220725_KEGG  > KEGG.gz`
- Decompress:
`gzip -d KEGG.gz`



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
