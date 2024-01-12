---
toc: true
url: cp
covercopy: <a href="https://www.vecteezy.com/members/supiandiyendi169870">© supiandiyendi169870</a>
priority: 10000
date: 2022-09-14 15:44:19
title: "How to copy files in linux faster than cp"
ytitle: "How to copy files in linux faster than cp"
description: "How to copy files in linux faster than cp"
excerpt: "How to copy files in linux faster than cp"
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, System]
cover: "https://static.vecteezy.com/system/resources/previews/004/871/788/non_2x/keyboard-keys-ctrl-c-and-ctrl-v-copy-and-paste-the-key-shortcuts-computer-icon-on-yellow-background-free-vector.jpg"
thumbnail: "https://static.vecteezy.com/system/resources/previews/004/871/788/non_2x/keyboard-keys-ctrl-c-and-ctrl-v-copy-and-paste-the-key-shortcuts-computer-icon-on-yellow-background-free-vector.jpg"
---


## How to copy files in linux faster than cp


### Tar pipe
1. install the pv: `sudo apt install pv`
2. `tar cf - . | (cd /dst; tar xvf -)`[^Cesar_Capillas_17]

```bash
time tar cf - Mutation/Raw_VCF | (cd /media/Side/ken/; tar xvf -)
```
<pre>
tar cf - Mutation/Raw_VCF  2.04s user 21.44s system 18% cpu 2:06.94 total
( cd /dst; tar xvf -; )  1.33s user 32.93s system 26% cpu 2:06.94 total
</pre>

It only takes 2 minutes compared 12 minutes by `cp`.

Another commands such as pv can help you too, to monitor the progress of a copy between two directories, for example:

```bash
tar cf - . | pv | (cd /dst; tar xf -)
```

### gcp

Only works for git repository.

`gcp -rv ~/Music/* /data/music/` [^Cesar_Capillas_17]










[^Cesar_Capillas_17]: [Cesar Capillas, 2017: How to copy files in linux faster and safer than cp](https://www.zylk.net/en/web-2-0/blog/-/blogs/how-to-copy-files-in-linux-faster-and-safer-than-cp)



























































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
