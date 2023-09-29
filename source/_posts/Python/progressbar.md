---
toc: true
url: progressbar
covercopy: © Karobben
priority: 10000
date: 2023-07-10 18:38:28
title: "Progress Bar in Python"
ytitle: "Progress Bar in Python"
description: "Progress Bar in Python"
excerpt: "Progress Bar in Python"
tags: [Python, Script]
category: [Python, Scripting, Module]
cover: "https://s1.ax1x.com/2023/07/11/pCRji28.png"
thumbnail: "https://s1.ax1x.com/2023/07/11/pCRji28.png"
---

## tqdm

The tqdm package in Python provides a fast, extensible progress bar for loops and other iterable objects. It was used in pip intall. Here's a simple example:

```python
from tqdm import tqdm
import time

# Create a list of numbers
numbers = range(100)

# Wrap your iterable with tqdm()
for i in tqdm(numbers):
    # Simulate some work
    time.sleep(0.01)
```

![Progress bar, tqdm](https://s1.ax1x.com/2023/07/11/pCRXjDH.png)


## rich

```python
from rich.progress import track
import time

# Create a list of numbers
numbers = range(100)

# Wrap your iterable with track()
for i in track(numbers, description="Processing..."):
    # Simulate some work
    time.sleep(0.01)
```

`track()` works similarly to tqdm's wrapper. It takes an iterable and a description for the task, and returns an iterator that produces the same values as the original, but also updates a progress bar in the console as it iterates over the items.

The `description` parameter allows you to set a text description for the task that is displayed next to the progress bar.

Like tqdm, rich offers a variety of options to customize the appearance and behavior of the progress bar. You can find more details in the rich documentation.
![Progress bar, rich](https://s1.ax1x.com/2023/07/11/pCRXvbd.png)

## progressbar

cite: [sanjaydokula](https://www.geeksforgeeks.org/progress-bars-in-python/)
```python
import time
import progressbar
 
widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
 
bar = progressbar.ProgressBar(max_value=200,
                              widgets=widgets).start()
 
for i in range(200):
    time.sleep(0.1)
    bar.update(i)
```

![Progress bar, progressbar](https://s1.ax1x.com/2023/07/11/pCRXzVA.png)


## light-progress

cite: [@itkr](https://qiita.com/itkr/items/fab6a5e492b28bb07fab)


```python
from time import sleep
from light_progress.commandline import ProgressBar

n = 42
progress_bar = ProgressBar(n)
progress_bar.start()

for item in range(n):
    sleep(0.01)
    progress_bar.forward()

progress_bar.finish()
```

![Progress bar, light-progress](https://s1.ax1x.com/2023/07/11/pCRjp5t.png)



```python

from time import sleep
from light_progress.commandline import ProgressBar

n = 42
progress_bar = ProgressBar(n)
progress_bar.start()

for item in range(n):
    sleep(0.01)
    progress_bar.forward()

progress_bar.finish()
import time
import progressbar
 
widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
 
bar = progressbar.ProgressBar(max_value=20,
                              widgets=widgets).start()
 
for i in range(20):
    time.sleep(0.1)
    bar.update(i)
from rich.progress import track
import time

# Create a list of numbers
numbers = range(100)

# Wrap your iterable with track()
for i in track(numbers, description="Processing..."):
    # Simulate some work
    time.sleep(0.01)
from tqdm import tqdm
import time

# Create a list of numbers
numbers = range(100)

# Wrap your iterable with tqdm()
for i in tqdm(numbers):
    # Simulate some work
    time.sleep(0.01)
```



<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
