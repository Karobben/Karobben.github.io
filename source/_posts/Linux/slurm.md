---
toc: true
url: slurm
covercopy: <a href="https://cloud.google.com/blog/topics/hpc/introducing-the-latest-slurm-on-gcp-scripts">© google</a>
priority: 10000
date: 2022-09-22 13:02:50
title: "Slurm Workload Manager"
ytitle: "Slurm 工作调度工具"
description: "slurm, sbatch"
excerpt: "SLURM (Simple Linux Utility for Resource Management) is an open-source, highly scalable, and highly customizable cluster management and job scheduling system. It is widely used for managing high-performance computing (HPC) systems, allowing users to efficiently allocate resources, manage workloads, and monitor job progress. SLURM provides a simple and flexible interface for submitting, scheduling, and managing large-scale computing jobs, making it a popular choice for researchers, engineers, and other HPC users. <a title='ChatGPT'>Who sad this?</a>"
tags: [Linux, System, Scripting, bash, CLI Tools]
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

## Tricks

### Hold the job submit when the waiting list is too long

Sometimes, we need to upload a large number of jobs using a for loop. However, there is a limit to the number of jobs that can be submitted by each user. In such cases, we prefer to hold off on job submission and wait until some of the previously submitted jobs are completed. To achieve this, the easiest way is to use a while loop before submitting the jobs.

```bash
for i in {1..3000}; do
  while [ $(squeue -u user| wc -l) -gt 900 ] ;do
      echo $(squeue -u user| wc -l) too many jobs;
      sleep 10;
  done
  sbatch job.sh
done
```

In this while loop, we utilize the command squeue -u user | wc -l to determine the number of jobs in the user's list. When it exceeds 900, we enter a while loop that will pause the submission process until some jobs have completed.



This is a bash script that will submit a batch job (`job.sh`) 3000 times. However, it will check if there are already 900 or more jobs running under the user account "user" using the `squeue` command. If there are, it will wait for 10 seconds and check again. This loop will continue until there are fewer than 900 jobs running, at which point it will submit the next batch job using the `sbatch` command.

Here is a breakdown of the code:

- `for i in {1..3000}; do` starts a loop that will run 3000 times. This is just a counter and is not used in the loop.
- `while [ $(squeue -u user| wc -l) -gt 900 ] ;do` starts a while loop that will continue as long as there are 900 or more jobs running under the user account "user".
- `echo $(squeue -u user| wc -l) too many jobs;` prints a message to the console indicating how many jobs are currently running.
- `sleep 10;` pauses the script for 10 seconds before checking again.
- `sbatch job.sh` submits the batch job job.sh to the queue for processing.


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
