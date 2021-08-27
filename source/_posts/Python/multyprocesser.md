---
title: "Multiprocessing"
description: "Multiprocessing"
url: multiprocessing
date: 2020/09/12
toc: true
excerpt: "Buildozer install and android APK packaging"
tags: [Python, Data Science, Machine Learning]
category: [Python, Scripting, Module]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Multiprocessing

## Quick Start
```python
import multiprocessing as mp
from time import sleep

def echo(i):
  '''Working Function for cycle'''
  sleep(i)
  print(i)

def multicore(Pool=10):
  pool = mp.Pool(processes=Pool)
  for i in range(10):
    # Working function "echo" and the arg 'i'
    multi_res = [pool.apply_async(echo,(i,))]
  pool.close()
  pool.join()

if __name__ == '__main__':
  multicore()
```

## With Return
Cite: [StackoverFlow](https://stackoverflow.com/a/10415215)
```python
import multiprocessing as mp

def worker(procnum, return_dict):
    '''worker function'''
    print (str(procnum) + ' represent!')
    return_dict[procnum] = procnum


if __name__ == '__main__':
    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = mp.Process(target=worker, args=(i,return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    print (return_dict.values())

for i in return_dict.values():
  print(i)
```
