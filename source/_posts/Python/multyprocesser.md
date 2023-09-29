---
title: "Multiprocessing"
description: "Multiprocessing"
url: multiprocessing
date: 2020/09/12
toc: true
excerpt: "Multiprocessing in Python is a way to run multiple processes simultaneously using multiple CPUs or cores. It allows for faster processing of data by dividing the task into smaller sub-tasks that can be executed in parallel. Python's multiprocessing module provides easy-to-use APIs for implementing multiprocessing in Python. <a title='GhatGPT'>Who said this?</a>"
tags: [Python, Script]
category: [Python, Scripting, Module]
cover: 'https://files.realpython.com/media/An-Overview-of-Concurrency-in-Python_Watermarked.c54c399ccb32.jpg'
covercopy: '<a href="https://realpython.com/python-concurrency/">© realpython.com</a>'
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


## why pool.join() is taking a long time

 If `pool.join()` takes a long time, it typically indicates that there are still ongoing tasks in the pool. The duration is largely determined by the longest task in the pool. Issues such as inter-process communication, waiting for shared resources, and insufficient CPU cores can also cause slowdowns.


## startmap()


Generally, `startmap` could work faster than `map`.

```python
import multiprocessing as mp

def calculate_overlap(i, Ther):
    row = TB_NST_FP.iloc[i]
    TB_TMP = TB_NST[TB_NST.Frame == row['Frame']]
    over_N = TB_TMP.apply(lambda x: overlap_area(row, x, Ther), axis=1).sum()
    return (i, over_N)

# Assuming you have a list/array of i and Ther values
i_values = range(len(TB_NST_FP))  # Replace this with your actual i values
Ther_values = [0.5] * len(TB_NST_FP)  # Replace this with your actual Ther values

# Pair up i_values and Ther_values
args = list(zip(i_values, Ther_values))
# Create a Pool of subprocesses
with mp.Pool() as p:
    results = p.starmap(calculate_overlap, args)
```

In this code, it only consume 6.3s.

```python
def calculate_overlap(args):
    i, Ther = args
    row = TB_NST_FP.iloc[i]
    TB_TMP = TB_NST[TB_NST.Frame == row['Frame']]
    over_N = TB_TMP.apply(lambda x: overlap_area(row, x, Ther), axis=1).sum()
    return (i, over_N)
# Create a pool of processes

Ther = 0.5
with Pool(cpu_count()) as p:
    # Map calculate_overlap function to each index in TB_NST_FP
    results = p.map(calculate_overlap, [(i, Ther) for i in range(len(TB_NST_FP))])
# Filter results to only include indices where over_N < 1
FP_lst = [i for i in results if i[1] < 1]
```

In this code, it cost 8.9s
