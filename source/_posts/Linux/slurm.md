---
toc: true
url: slurm
covercopy: <a href="https://cloud.google.com/blog/topics/hpc/introducing-the-latest-slurm-on-gcp-scripts">© google</a>
priority: 10000
date: 2022-09-22 13:02:50
title: "Slurm Workload Manager"
ytitle: "Slurm 工作调度工具"
description: "slurm, sbatch"
excerpt: "slurm, sbatch"
tags: [Linux, slurm]
category: [Linux, System]
cover: "https://storage.googleapis.com/gweb-cloudblog-publish/images/slurm.max-900x900.jpg"
thumbnail: "https://storage.googleapis.com/gweb-cloudblog-publish/images/slurm.max-900x900.jpg"
---

## Introduction

> Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Slurm requires no kernel modifications for its operation and is relatively self-contained. As a cluster workload manager, Slurm has three key functions. First, it allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work. Optional plugins can be used for accounting, advanced reservation, gang scheduling (time sharing for parallel jobs), backfill scheduling, topology optimized resource selection, resource limits by user or bank account, and sophisticated multifactor job prioritization algorithms.
>From: [slurm](https://slurm.schedmd.com/overview.html)


## Sbatch

```bash
sbatch run.sh
```

## Chcek jobs

```bash
squeue -u {username}
```

## kill jobs

```bash
scancel -u {username}
```

## Check the log

```bash
sacct --format=jobid,elapsed,ncpus,ntasks,state|headsacct
```

<pre>
       JobID    Elapsed      NCPUS   NTasks      State
------------ ---------- ---------- -------- ----------
2218153        00:00:01          1              FAILED
2218153.bat+   00:00:01          1        1     FAILED
2218154        00:00:00          1              FAILED
2218154.bat+   00:00:00          1        1     FAILED
2218155        00:00:01          1              FAILED
2218155.bat+   00:00:01          1        1     FAILED
2218501        00:14:52          1           COMPLETED
2218501.bat+   00:14:52          1        1  COMPLETED
2218502        00:47:16          1             RUNNING
2218503        00:15:19          1           COMPLETED
2218503.bat+   00:15:19          1        1  COMPLETED
</pre>


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
